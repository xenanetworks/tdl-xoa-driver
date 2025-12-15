import os
import sys
import time
import threading
import inspect
import logging
from typing import Optional, Callable, Union, List, Dict, Any
from ._socket_driver import SimpleSocket
LOGFILE = "XENALOG"


def _redact_sensitive(cmd: str) -> str:
    """Redact password or sensitive data from CLI command strings."""
    # Redact values in commands likely to contain passwords (e.g., C_LOGON, or generically matching quoted args to C_LOGON)
    import re
    # Redact anything in C_LOGON "..."
    cmd = re.sub(r'(C_LOGON\s*")([^"]+)(")', r'\1***REDACTED***\3', cmd)
    # (Optional) Redact anything that looks like password="..."
    cmd = re.sub(r'(password\s*=\s*")([^"]+)(")', r'\1***REDACTED***\3', cmd, flags=re.IGNORECASE)
    # (Optional) Redact any --password=... arguments
    cmd = re.sub(r'(--password=)(\S+)', r'\1***REDACTED***', cmd, flags=re.IGNORECASE)
    return cmd

def errexit(msg):
    logging.error(f"Error: { msg }, exiting...")
    sys.exit(1)

# Keepalive thread to ensure TCP connection is kept open
# Do not edit this 
class KeepAliveThread(threading.Thread):
    message = ''
    def __init__(self, connection: "XenaSocketDriver", interval: int = 10):
        threading.Thread.__init__(self)
        self.connection = connection
        self.interval = interval
        self.finished = threading.Event()
        self.daemon = True
        logging.info('[KeepAliveThread] Thread initiated, interval %d seconds' % (self.interval))

    def stop(self):
        self.finished.set()
        self.join()

    def run(self):
        while not self.finished.is_set():
            self.finished.wait(self.interval)
            self.connection.send_and_response(self.message)


# Low level driver for TCP/IP based query
# Do not edit this
class XenaSocketDriver(SimpleSocket):
    def __init__(self, hostname: str, tcp_port: int = 22611):
        super(XenaSocketDriver, self).__init__(hostname=hostname, port=tcp_port)
        self.set_keepalives()
        self.access_semaphore = threading.Semaphore(1)

    def send_only(self, cmd: str):
        with self.access_semaphore:
            super().send_only(cmd)

    def send_and_response(self, cmd: str, sync_on: bool = False) -> str:
        with self.access_semaphore:
            reply = super().send_and_response(cmd, sync_on=sync_on).strip('\n')
        return reply

    def send_and_response_multiple(self, cmd: str, num: int):
        with self.access_semaphore:
            reply = super().send_and_response_multiple(cmd, num)
        return reply


# Xena supplied class example for Scripting via Python3
# Feel free to add functions below
class XOACLIManager:

    CHASSIS_RESERVATION      = lambda self: f"C_RESERVATION ?"
    CHASSIS_RELEASE          = lambda self: f"C_RESERVATION RELEASE"
    CHASSIS_RELINQUISH       = lambda self: f"C_RESERVATION RELINQUISH"
    CHASSIS_RESERVE          = lambda self: f"C_RESERVATION RESERVE"

    MODULE_RESERVATION      = lambda self, mod: f"{ mod } M_RESERVATION ?"
    MODULE_RELEASE          = lambda self, mod: f"{ mod } M_RESERVATION RELEASE"
    MODULE_RELINQUISH       = lambda self, mod: f"{ mod } M_RESERVATION RELINQUISH"
    MODULE_RESERVE          = lambda self, mod: f"{ mod } M_RESERVATION RESERVE"

    PORT_RESET              = lambda self, port: f"{ port } P_RESET"
    PORT_RESERVATION        = lambda self, port: f"{ port } P_RESERVATION ?"
    PORT_RESERVE            = lambda self, port: f"{ port } P_RESERVATION RESERVE"
    PORT_RELINQUISH         = lambda self, port: f"{ port } P_RESERVATION RELINQUISH"
    PORT_RELEASE            = lambda self, port: f"{ port } P_RESERVATION RELEASE"
    PORT_SPEEDSELECTION     = lambda self, port, speed: f"{ port } P_SPEEDSELECTION {speed}"

    PORT_TRAFFIC_ON            	= lambda self, port: f"{ port } P_TRAFFIC ON"
    PORT_TRAFFIC_OFF            = lambda self, port: f"{ port } P_TRAFFIC OFF"

    def __init__(self, host: str, debug: bool = False, halt_on_error: bool = False) -> None:
        self.host    = host
        self.debug_enabled = debug
        self.halt_on_error_enabled  = halt_on_error
        self.is_log_cmd_empty   = False
        self.cmd_trace_list  = []
        self.logfile_path  = os.environ.get(LOGFILE)
        if self.logfile_path != None:
            self.is_log_cmd_empty = True

        self.driver = XenaSocketDriver(self.host)
        # self.keepalive_thread = KeepAliveThread(self.driver)
        # self.keepalive_thread.start()

    def __del__(self):
        if self.is_log_cmd_empty:
            if self.logfile_path:
                with open(self.logfile_path, 'w') as log_file:
                    for cmd in self.cmd_trace_list:
                        log_file.write(f"{ cmd }\n")
        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.driver.close()
        # self.keepalive_thread.stop()

    ## Enable debug - prints commands and errors
    def logging_on(self) -> None:
        """Enable debug output on terminal
        """
        self.debug_enabled = True
        logging.basicConfig(level=logging.INFO, format='%(asctime)s.%(msecs)03d %(message)s', datefmt='%m/%d/%Y %I:%M:%S')
        return

    ## Disable debug (default) - no printed output
    def logging_off(self) -> None:
        """Disable debug output on terminal
        """
        self.debug_enabled = False
        # Reset logging configuration by removing all handlers
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(level=logging.NOTSET, force=True)
        return

    def debug_message(self, msg: str) -> None:
        """Print debug message if debug is enabled"""
        if self.debug_enabled == True:
            # If the message contains a sensitive command, do NOT log it
            import re
            # Check for C_LOGON or password in string, as a safeguard
            if re.search(r'C_LOGON\s*".*"', msg) or re.search(r'password\s*=\s*".*"', msg, flags=re.IGNORECASE) or re.search(r'--password=\S+', msg, flags=re.IGNORECASE):
                logging.info(f"{time.time()} [Sensitive command redacted]")
                # print(f"{time.time()} [Sensitive command redacted]")
                return
            # Redact as an additional precaution
            safe_msg = _redact_sensitive(msg)
            logging.info(f"{time.time()} {safe_msg}")
            # print(f"{time.time()} {safe_msg}")
    def log_command(self, cmd:str) -> None:
        """Place the command in the log cmd list for later logging

        :param cmd: CLI command string
        :type cmd: str
        """
        if self.is_log_cmd_empty == True:
            self.cmd_trace_list.append(_redact_sensitive(cmd))
    
    ## Enable halt on error - calls sys.exit(1) upon error
    def enable_halt_on_error(self) -> None:
        """Enable halt on error: calls sys.exit(1) upon error."""
        self.halt_on_error_enabled = True

    ## Disable halt on error (default)
    def disable_halt_on_error(self) -> None:
        """Disable halt on error: does not call sys.exit(1) upon error."""
        self.halt_on_error_enabled = False

    ## Print diagnostics msg and halt
    def errexit(self, msg:str):
        """Print error message and exit program if halt on error is enabled"""
        # self.keepalive_thread.stop()
        if self.halt_on_error_enabled == 1:
            logging.error(f"\nError: { msg }, exiting...\n")
            sys.exit(1)
        else:
            raise Exception(f"\nError: { msg }, exiting...\n")
        

#####################################################################
#																	#
#						Send and Expect wrappers					#
#																	#
#####################################################################

    ## Send command and return response
    def send(self, cmd:str, sync_on: bool = False) -> str:
        """Send command and return response"""
        if self.driver.is_connected == False:
            self.driver = XenaSocketDriver(self.host)
        res = self.driver.send_and_response(cmd, sync_on=sync_on)
        self.debug_message(f"send()         : { cmd }")
        self.debug_message(f"send() received: { res }")
        self.log_command(cmd)
        return res
    
    ## Send one command and expect to receive a specified response
    def send_expect(self, cmd:str, resp:str) -> bool:
        """Send command and expect response (typically <OK>)"""

        self.debug_message(f"send_expect({ resp }): {_redact_sensitive(cmd)}")
        self.log_command(cmd)
        try:
            if self.driver.is_connected == False:
                self.driver = XenaSocketDriver(self.host)
            res = self.driver.send_and_response(cmd)
            if res.rstrip('\n') == resp:
                return True
            else:
                self.debug_message("send_expect() failed")
                self.debug_message(f"   Expected: { resp }")
                self.debug_message(f"   Received: { res }")
                # self.errexit(f"Halting in line {inspect.currentframe().f_back.f_lineno}")
                return False
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1] if exc_tb else "Unknown"
            if exc_tb is not None:
                logging.error(exc_type, fname, exc_tb.tb_lineno)
            else:
                logging.error(exc_type)
            return False

    ## Send one command and expect to receive <OK> as a response
    def send_expect_ok(self, cmd:str) -> bool:
        """Send commands and expect <OK>"""

        if isinstance(cmd, str):
            return self.send_expect(cmd, "<OK>")
        else:
            return False

    ## Send command and match response with specified string
    def send_and_match(self, cmd:str, match_resp:str) -> bool:
        """ Send command and match response with specified string"""
        self.debug_message(f"send_and_match() : { cmd }")
        self.log_command(cmd)

        if self.driver.is_connected == False:
            self.driver = XenaSocketDriver(self.host)
        res = self.driver.send_and_response(cmd)
        if match_resp in res:
            return True
        else:
            self.debug_message("send_and_match() failed")
            self.debug_message(f"   Expected: { match_resp }")
            self.debug_message(f"   Got     : { res }")
            frame = inspect.currentframe()
            if frame and frame.f_back:
                self.errexit(f"Halting in line { frame.f_back.f_lineno }")
            else:
                self.errexit("Halting due to an unknown error")
            return False

    ## Send multiple commands in batch and return all responses
    def send_multi_commands(self, cmdlist: list, batch = True) -> list:
        """Send multiple commands in batch and return all responses"""
        if not isinstance(cmdlist, list):
            raise ValueError('\'cmdlist\' - must be a instance of list')
        cmd = ''
        num = len(cmdlist)
        self.debug_message(f"{num} commands to send to xenaserver")

        if batch == True:
            for command in cmdlist:
                cmd = cmd + command + '\n'

            self.debug_message(f"send()         : { cmd }")
            if self.driver.is_connected == False:
                self.driver = XenaSocketDriver(self.host)
            res = self.driver.send_and_response_multiple(cmd, num)
            def mapper(v): return f"{ v[0] }: { v[1] }"
            mes = "\n".join( list( map(mapper, list( zip(cmdlist, res.split('\n')) ) ) ) )
            self.debug_message(f"send() received: { mes }")

            return res.splitlines()
        else:
            results = []
            for command in cmdlist:
                cmd = command
                self.debug_message(f"send()         : { cmd }")
                if self.driver.is_connected == False:
                    self.driver = XenaSocketDriver(self.host)
                res = self.driver.send_and_response(cmd)
                self.debug_message(f"send() received: { res }")
                self.log_command(cmd)
                results.append(res)
            return results



#####################################################################
#																	#
#				Xena Scripting API specific commands				#
#																	#
#####################################################################

    #############################################################
    # 						Chassis Commands 					#
    #############################################################

    # Logon
    def log_on(self, pwd: str) -> bool:
        return self.send_expect_ok(f"C_LOGON \"{ pwd }\"")

    # Logoff
    def log_off(self) -> None:
        self.send("C_LOGOFF")


    ## Logon and set owner
    def logon_set_owner(self, pwd: str, owner: str = "XOACLI") -> bool:
        if self.log_on(pwd):
            return self.send_expect_ok(f"C_OWNER \"{ owner }\"")
        return False

    ## Logon to chassis, set user name and password, then reserve ports
    def logon_reserve_ports(self, ports: Union[List[str], str], pwd: str, owner: str = "XOACLI") -> None:
        if isinstance(ports, str): ports = [ports]
        assert self.logon_set_owner(pwd, owner)
        self.reserve_port(ports)

    # Reserve chassis if it is not mine, else do nothing.
    def reserve_chassis(self):
        res = self.send( self.CHASSIS_RESERVATION() ).split()[1]

        if "RESERVED_BY_OTHER" in res:
            self.debug_message("Chassis is reserved by other - relinquish")
            self.send_expect_ok( self.CHASSIS_RELINQUISH() )
            self.send_expect_ok( self.CHASSIS_RESERVE() )

        elif "RELEASED" in res:
            self.send_expect_ok( self.CHASSIS_RESERVE() )

    # Reserve chassis, release or relinquish first if necessary
    def free_chassis(self):
        res = self.send( self.CHASSIS_RESERVATION() ).split()[1]

        if "RESERVED_BY_YOU" in res:
            self.debug_message("Chassis is reserved by me - release")
            self.send_expect_ok( self.CHASSIS_RELEASE() )

        elif "RESERVED_BY_OTHER" in res:
            self.debug_message("Chassis is reserved by other - relinquish")
            self.send_expect_ok( self.CHASSIS_RELINQUISH() )

        elif "RELEASED" in res:
            self.debug_message("Chassis is released - do nothing")
        else:
            frame = inspect.currentframe()
            if frame and frame.f_back:
                self.errexit(f"Halting in line { frame.f_back.f_lineno }")
            else:
                self.errexit("Halting due to an unknown error")

    # Start traffic on ports simultaneously
    def start_chassis_traffic(self, ports: Union[List[str], str]):
        if isinstance(ports, str): ports = ports.split()
        param = []
        for port in ports:
            param += port.split("/")

        param = ' '.join([str(elem) for elem in param])
        self.send_expect_ok( f"C_TRAFFIC ON {param}")

    # Start traffic on ports simultaneously
    def stop_chassis_traffic(self, ports: Union[List[str], str]):
        if isinstance(ports, str): ports = ports.split()
        param = []
        for port in ports:
            param += port.split("/")

        param = ' '.join([str(elem) for elem in param])
        self.send_expect_ok( f"C_TRAFFIC OFF {param}")


    #############################################################
    # 						Module Commands 															#
    #############################################################

    # Release module from me or relinquish module from others
    def free_module(self, module_id: str):
        res = self.send(self.MODULE_RESERVATION(module_id)).split()[2]

        if "RESERVED_BY_YOU" in res:
            self.debug_message("Module is reserved by me - release")
            self.send_expect_ok(self.MODULE_RELEASE(module_id))

        elif "RESERVED_BY_OTHER" in res:
            self.debug_message("Module is reserved by other - relinquish")
            self.send_expect_ok(self.MODULE_RELINQUISH(module_id))

        elif "RELEASED" in res:
            self.debug_message("Module is released - do nothing")

        else:
            frame = inspect.currentframe()
            if frame and frame.f_back:
                self.errexit(f"Halting in line { frame.f_back.f_lineno }")
            else:
                self.errexit("Halting due to an unknown error")


    def reserve_module(self, module_id: str):
        """
        Reserve the module if it is not mine, else do nothing
        """
        res = self.send(self.MODULE_RESERVATION(module_id)).split()[2]

        if "RESERVED_BY_OTHER" in res:
            self.debug_message("Module is reserved by other - relinquish")
            self.send_expect_ok(self.MODULE_RELINQUISH(module_id))
            self.send_expect_ok( self.MODULE_RESERVE(module_id) )

        elif "RELEASED" in res:
            self.send_expect_ok( self.MODULE_RESERVE(module_id) )


    #############################################################
    # 						Port Commands 																#
    #############################################################

    # Wait for port to be 'released' - with timeout of 1 minute
    def wait_port_to_release(self, port_ids: Union[List[str], str], timeout_s: int = 63):
        if isinstance(port_ids, str): port_ids = port_ids.split()
        for port in port_ids:
            timeout = time.time() + timeout_s # 60sec + total 3sec of slipping time by 1s
            while True:
                res = self.send( self.PORT_RESERVATION(port) )
                if 'RELEASED' in res:
                    break
                elif time.time() > timeout:
                    raise TimeoutError('port_wait_release: Waiting for changing of port reservation interval is terminated!')
                else:
                    time.sleep(0.1)

    # Reserve a port - if port is reserved, release or relinquish, then reserve
    def reserve_port(self, port_ids: Union[List[str], str]) -> None:
        if isinstance(port_ids, str): port_ids = port_ids.split()
        for port in port_ids:
            res = self.send( self.PORT_RESERVATION(port) )
            if 'RESERVED_BY_OTHER' in res:
                self.debug_message(f"Port { port } is reserved by other - relinquish")
                self.send_expect_ok( self.PORT_RELINQUISH(port) )
                self.wait_port_to_release(port)
                self.send_expect_ok( self.PORT_RESERVE(port) )
            elif 'RELEASED' in res:
                self.send_expect_ok( self.PORT_RESERVE(port) )

    # Set a port/ports free.
    def free_port(self, port_ids: Union[List[str], str]) -> None:
        if isinstance(port_ids, str): port_ids = port_ids.split()
        for port in port_ids:
            res = self.send( self.PORT_RESERVATION(port) )
            if "RESERVED_BY_OTHER" in res:
                self.send_expect_ok( self.PORT_RELINQUISH(port) )
            if "RESERVED_BY_YOU" in res:
                self.send_expect_ok( self.PORT_RELEASE(port) )

    # Reset a port/ports
    def reset_port(self, port_ids: Union[List[str], str], wait_after_reset_s: int) -> None:
        if isinstance(port_ids, str): port_ids = port_ids.split()
        self.reserve_port(port_ids)
        for port in port_ids:
            res = self.send_expect_ok( self.PORT_RESET(port) )
            
        time.sleep(wait_after_reset_s)

    ## Start traffic on ports 
    def start_port_traffic(self, port_ids: Union[List[str], str]) -> None:
        if isinstance(port_ids, str): port_list: List[str] = port_ids.split()
        else: port_list = port_ids
        for port in port_list:
            res = self.send_expect_ok(self.PORT_TRAFFIC_ON(port) )

    ## Stop traffic on ports 
    def stop_port_traffic(self, port_ids: Union[List[str], str]) -> None:
        if isinstance(port_ids, str): port_list: List[str] = port_ids.split()
        else: port_list = port_ids
        for port in port_list:
            res = self.send_expect_ok(self.PORT_TRAFFIC_OFF(port) )

    ## Port speed selection
    def select_port_speed_mode(self, port_ids: Union[List[str], str], speed_mode: str = "AUTO") -> None:
        if isinstance(port_ids, str): port_list: List[str] = port_ids.split()
        else: port_list = port_ids
        for port in port_list:
            res = self.send_expect_ok(self.PORT_SPEEDSELECTION(port, speed_mode) )

    ## Get port configuration
    def get_port_full_config_raw(self, port_ids: Union[List[str], str]) -> List[str]:
        """Get full config data of one or multiple ports

        :param port_ids: list of port ids in format "module_id/port_id"
        :type port_ids: Union[List[str], str]
        :return: list of port full config strs
        :rtype: List[str]
        """
        self.send(cmd = f"SYNC ON")
        result = []
        if isinstance(port_ids, str): port_id_list: List[str] = port_ids.split()
        else: port_id_list = port_ids
        for port_id in port_id_list:
            resp = ''
            # Send P_FULLCONFIG ? command and get response
            # It includes port configuration and stream configurations
            resp = self.send(cmd = f"{port_id} P_FULLCONFIG ?", sync_on=True)
            result.append(resp)
        self.send(cmd = f"SYNC OFF")
        return result
    
    
    ## Get module configuration
    def get_module_full_config_raw(self, module_ids: Union[List[str], str]) -> List[str]:
        """Get full config data of one or multile modules

        :param module_ids: list of module ids
        :type module_ids: Union[List[str], str]
        :return: list of module full config strs
        :rtype: List[str]
        """
        self.send(cmd = f"SYNC ON")
        result = []
        if isinstance(module_ids, str): module_id_list: List[str] = module_ids.split()
        else: module_id_list = module_ids
        for module_id in module_id_list:
            resp = ''
            resp = self.send(cmd = f"{module_id} M_CONFIG ?", sync_on=True)
            result.append(resp)
        self.send(cmd = f"SYNC OFF")
        return result

