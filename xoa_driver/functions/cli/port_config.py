import asyncio
from xoa_driver import testers, ports
from typing import List, Tuple
from ._cli_manager import XOACLIManager
from ._config_block import *

async def save_port_config(tester: testers.L23Tester, port: ports.GenericL23Port, path: str, debug=False, halt_on_error=False) -> str:
    """Save port config to the specified filepath

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
    module = tester.modules.obtain(port.kind.module_id)
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=debug, halt_on_error=halt_on_error)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    # Get full port configuration
    raw_resp = xm.get_port_full_config_raw(port_index)

    # Create config block
    port_config_block = ConfigBlock()
    # Fill in metadata
    port_config_block.type = ConfigMetadataType.PORT
    port_config_block.chassis_name = tester.info.name
    port_config_block.chassis_sn = str(tester.info.serial_number)
    port_config_block.chassis_version_str = tester.info.version_string
    port_config_block.module_name = module.info.model_name
    port_config_block.module_model = module.info.model
    port_config_block.module_sn = module.info.serial_number
    port_config_block.module_version_str = module.info.version_string
    port_config_block.module_revision = module.info.revision
    port_config_block.port_id = port_index
    port_config_block.commands = raw_resp[0]

    # Save configuration to file
    result = port_config_block.config_block_str
    with open(path, 'w+') as xpcfile:
        xpcfile.write(result)
    return result

async def load_port_config(tester: testers.L23Tester, port: ports.GenericL23Port, path: str, debug=False, halt_on_error=False) -> List[Tuple[str, str]]:
    """Load port config from the specified filepath

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param port: Port object to load configuration to
    :type port: ports.GenericL23Port
    :param load_path: File path to load the port configuration from
    :type load_path: str
    :return: List of tuples containing response and the corresponding command sent
    :rtype: List[Tuple[str, str]]
    """
    
    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password
    port_index = f"{port.kind.module_id}/{port.kind.port_id}"
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=debug, halt_on_error=halt_on_error)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    # Reserve the port before applying configuration
    xm.reserve_port(port_index)

    result: List[Tuple[str, str]] = []

    # Read configuration from file
    with open(path, 'r', encoding='utf-8') as xpcfile:
        config_data = xpcfile.read()

    # Deserialize config block and send CLI commands
    config_block = ConfigBlock()
    config_block.config_block_str = config_data
    cli_cmds = config_block.commands
    for cmd in cli_cmds:
        if cmd.strip():  # Ensure the command is not empty
            resp = xm.send(cmd=f"{port_index} {cmd}", sync_on=False)
            result.append((resp, f"{port_index} {cmd}"))

    # Free the port after applying configuration
    xm.free_port(port_index)
    return result

async def port_config_from_file(tester: testers.L23Tester, port: ports.GenericL23Port, path: str, debug=False, halt_on_error=False) -> List[Tuple[str, str]]:
    """Load port configuration from the specifiied filepath. This function is a wrapper around load_port_config to provide backward compatibility.

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param port: Port object to load configuration to
    :type port: ports.GenericL23Port
    :param load_path: File path to load the port configuration from
    :type load_path: str
    :return: List of tuples containing response and command sent
    :rtype: List[Tuple[str, str]]
    """
    return await load_port_config(tester, port, path, debug=debug, halt_on_error=halt_on_error)


