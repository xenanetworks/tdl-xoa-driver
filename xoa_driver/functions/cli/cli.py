import asyncio
from xoa_driver import testers, modules, ports
from ._cli_manager import XOACLIManager
from typing import Optional, Callable, Union, List, Dict, Any

async def save_port_config(tester: testers.L23Tester, port: ports.GenericL23Port, path: str) -> str:
    """Save port configuration to the specifiied filepath

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param port: Port object to save configuration from
    :type port: ports.GenericL23Port
    :param save_path: File path to save the port configuration
    :type save_path: str
    :return: Port configuration string
    :rtype: str
    """
    
    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password
    port_index = f"{port.kind.module_id}/{port.kind.port_id}"
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=False, halt_on_error=False)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    # Get full port configuration
    resp = xm.get_port_full_config(port_index)

    # Save configuration to file
    with open(path, 'w+', newline='') as xpcfile:
        xpcfile.write(resp)

    return resp

async def load_port_config(tester: testers.L23Tester, port: ports.GenericL23Port, path: str) -> None:
    """Load port configuration from the specifiied filepath

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param port: Port object to load configuration to
    :type port: ports.GenericL23Port
    :param load_path: File path to load the port configuration from
    :type load_path: str
    """
    
    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password
    port_index = f"{port.kind.module_id}/{port.kind.port_id}"
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=False, halt_on_error=False)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    # Reserve the port before applying configuration
    xm.reserve_port(port_index)

    # Read configuration from file
    with open(path, 'r', newline='') as xpcfile:
        config_data = xpcfile.read()
    
    for line in config_data.splitlines():
        if line.startswith(';'):
            # Remove the line from the config data
            config_data = config_data.replace(line + '\n', '')

    # Split the config data into individual commands
    commands = config_data.strip().split('\n')
    
    # Send each command to the tester
    for command in commands:
        if command.strip():  # Ensure the command is not empty
            xm.send(cmd=command, sync_on=False)

async def port_config_from_file(tester: testers.L23Tester, port: ports.GenericL23Port, path: str) -> None:
    """Load port configuration from the specifiied filepath. This function is a wrapper around load_port_config to provide backward compatibility.

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param port: Port object to load configuration to
    :type port: ports.GenericL23Port
    :param load_path: File path to load the port configuration from
    :type load_path: str
    """
    await load_port_config(tester, port, path)


__all__ = (
    "save_port_config",
    "load_port_config",
    "port_config_from_file",
)