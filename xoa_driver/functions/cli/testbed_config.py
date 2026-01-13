import asyncio
from xoa_driver import testers, modules, ports
from ._cli_manager import XOACLIManager
from typing import List, Tuple
from ..mgmt import *
from ._config_block import *

async def save_testbed_config(tester: testers.L23Tester, ports: List[ports.GenericL23Port], path: str, testbed_name: str = "<testbed>", with_module_config: bool = True, debug=False, halt_on_error=False) -> str:
    """Save testbed configuration to the specifiied filepath

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param ports: List of port objects to save configuration from
    :type ports: typing.List[ports.GenericL23Port]
    :param path: File path to save the test case configuration
    :type path: str
    :param testbed_name: Name of the testbed
    :type testbed_name: str
    :param with_module_config: Whether to include module configuration in the saved test case configuration
    :type with_module_config: bool
    :return: Test case configuration string
    :rtype: str
    """

    # Get a list of modules from the ports
    modules_list: List[modules.GenericL23Module] = []
    if with_module_config:
        for port in ports:
            module = tester.modules.obtain(port.kind.module_id)
            if module not in modules_list:
                if not isinstance(module, modules.ModuleChimera):
                    modules_list.append(module)
    
    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=debug, halt_on_error=halt_on_error)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    # Save configuration to file
    result = ""
    # Create testbed metadata block
    testcase_metadata_block = ConfigBlock()
    testcase_metadata_block.type = ConfigMetadataType.TESTCASE
    testcase_metadata_block.testbed_name = testbed_name
    result += testcase_metadata_block.config_block_str

    for module in modules_list:
        module_index = f"{module.module_id}"
        raw_resp = xm.get_module_full_config_raw(module_index)

        # Create config block
        module_config_block = ConfigBlock()
        # Fill in metadata
        module_config_block.type = ConfigMetadataType.MODULE
        module_config_block.chassis_name = tester.info.name
        module_config_block.chassis_sn = str(tester.info.serial_number)
        module_config_block.chassis_version_str = tester.info.version_string
        module_config_block.module_name = module.info.model_name
        module_config_block.module_model = module.info.model
        module_config_block.module_sn = module.info.serial_number
        module_config_block.module_version_str = module.info.version_string
        module_config_block.module_revision = module.info.revision
        module_config_block.module_id = module_index
        module_config_block.commands = raw_resp[0]
        result += "\n" + ";\n" + module_config_block.config_block_str

    for port in ports:
        port_index = f"{port.kind.module_id}/{port.kind.port_id}"
        module = tester.modules.obtain(port.kind.module_id)
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
        result += "\n" + ";\n" + port_config_block.config_block_str
        
    with open(path, 'w+') as xtcfile:
        xtcfile.write(result)
    
    return result

async def load_testbed_config(tester: testers.L23Tester, path: str, mode: str = "default", delay_after_module_config: int = 5, debug=False, halt_on_error=False) -> List[Tuple[str, str]]:
    """Load testbed configuration from the specifiied filepath

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param path: File path to load the module configuration from
    :type path: str
    :param mode: Load mode, "default | port | module". "default" loads both module and port configurations, "port" loads only port configurations, "module" loads only module configurations.
    :type mode: str
    :param delay_after_module_config: Delay in seconds after configuring each module to ensure proper configuration
    :type delay_after_module_config: int
    :return: List of tuples containing response and the corresponding command sent
    :rtype: List[Tuple[str, str]]
    """

    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password

    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=debug, halt_on_error=halt_on_error)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    result: List[Tuple[str, str]] = []

    # Read configuration from file
    with open(path, 'r') as xpcfile:
        config_data = xpcfile.read()

    # Parse the config data to configure modules and ports block by block
    config_datas = config_data.split(f";\n")
    for block in config_datas:
        if config_block_type(config_block_str=block) == ConfigMetadataType.MODULE and mode in ["default", "module"]:
            module_block = ConfigBlock()
            module_block.config_block_str = block
            module_index = module_block.module_id

            # Free the module before applying configuration
            module = tester.modules.obtain(int(module_index))
            await release_modules([module], should_release_ports=True)
            # Reserve the module before applying configuration
            xm.reserve_module(module_index)

            # Send each command to the tester
            for cmd in module_block.commands:
                if cmd.strip():  # Ensure the command is not empty
                    # print(f"Applying command: {module_index} {cmd}")
                    resp = xm.send(cmd=f"{module_index} {cmd}", sync_on=False)
                    result.append((resp, f"{module_index} {cmd}"))
            # Free the module after applying configuration
            xm.free_module(module_index)
            await asyncio.sleep(delay_after_module_config)  # Small delay to ensure proper module configuration

        elif config_block_type(config_block_str=block) == ConfigMetadataType.PORT and mode in ["default", "port"]:
            port_block = ConfigBlock()
            port_block.config_block_str = block
            port_index = port_block.port_id

            # Reserve the port before applying configuration
            xm.reserve_port(port_index)

            # Send each command to the tester
            for cmd in port_block.commands:
                if cmd.strip():  # Ensure the command is not empty
                    # print(f"Applying command: {port_index} {cmd}")
                    resp = xm.send(cmd=f"{port_index} {cmd}", sync_on=False)
                    result.append((resp, f"{port_index} {cmd}"))
            # Free the port after applying configuration
            xm.free_port(port_index)
    return result

async def module_config_from_file(tester: testers.L23Tester, path: str, debug=False, halt_on_error=False) -> List[Tuple[str, str]]:
    """Load module configuration from the specifiied filepath. This function is a wrapper around load_module_config to provide backward compatibility.

    :param tester: Chassis object
    :type tester: testers.L23Tester
    :param path: File path to load the module configuration from
    :type path: str
    """
    return await load_testbed_config(tester, path, mode="module", debug=debug, halt_on_error=halt_on_error)