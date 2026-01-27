"""
The resource management high-level function module, 
including testers, modules, ports, and streams.
"""

from __future__ import annotations
import asyncio
from typing import (
    TYPE_CHECKING,
    Any,
    Union,
    List,
    Tuple,
)
from xoa_driver import enums, ports
from xoa_driver.utils import apply
if TYPE_CHECKING:
    from xoa_driver.ports import GenericL23Port, Z800FreyaPort, Z1600EdunPort, GenericAnyPort, E100ChimeraPort
    from xoa_driver.modules import GenericAnyModule, GenericL23Module, Z800FreyaModule, Z1600EdunModule, E100ChimeraModule
    from xoa_driver.testers import L23Tester
    FreyaEdunModule = Union[Z800FreyaModule, Z1600EdunModule]
    FreyaEdunPort = Union[Z800FreyaPort, Z1600EdunPort]
    from xoa_driver.internals.commands.enums import MediaConfigurationType
from .exceptions import (
    NotSupportMedia,
    NotSupportPortSpeed,
    NotSupportMediaPortSpeed,
)
from .tools import MODULE_EOL_INFO
from itertools import chain  # type: ignore[Pylance false warning]
from datetime import datetime
import json


# region Testers
async def reserve_tester(tester: L23Tester, force: bool = True) -> None:
    """
    Reserve a tester regardless whether it is owned by others or not.

    :param tester: The tester to reserve
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param force: Should force reserve the tester
    :type force: boolean
    :return:
    :rtype: None
    """

    await release_tester(tester, force)
    await tester.reservation.set_reserve()


async def release_tester(
        tester: L23Tester, 
        should_release_modules_ports: bool = False,
        ) -> None:
    """
    Free a tester. If the tester is reserved by you, release the tester. If the tester is reserved by others, relinquish the tester. The tester should have no owner afterwards.

    :param tester: The tester to free
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param should_release_modules_ports: should modules and ports also be freed, defaults to False
    :type should_release_modules_ports: bool, optional
    :return:
    :rtype: None
    """
    r = await tester.reservation.get()
    if r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
        await tester.reservation.set_relinquish()
    elif r.operation == enums.ReservedStatus.RESERVED_BY_YOU:
        await tester.reservation.set_release()
    if should_release_modules_ports:
        await asyncio.gather(*(release_modules(list(tester.modules), True)))


async def get_chassis_sys_uptime(tester: L23Tester) -> int:
    """
    Get chassis system uptime in seconds

    :param tester: The tester to free
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :return: Chassis system uptime in seconds
    :rtype: int
    """
    resp = await tester.health.uptime.get()
    info_js = resp.info
    info_dict = json.loads(info_js)
    result = info_dict['1']['data']['uptime_secs']
    return result


# endregion


# region Modules


async def obtain_modules_by_ids(tester: L23Tester, module_ids: List[str], reserve: bool = False) -> Tuple[GenericL23Module | E100ChimeraModule, ...]:
    """
    Get the module objects of the tester specified by module index ids

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param module_ids: the index ids of the modules.

    Use "*" to get all modules.
    
    If the list is empty, return all modules of the tester

    :type module_ids: List[str]
    :param reserve: should reserve the modules, defaults to False
    :type reserve: bool, optional
    :raises NoSuchModuleError: No such a module index on the tester
    :return: module objects
    :rtype: List[:class:`~xoa_driver.modules.GenericL23Module` | :class:`~xoa_driver.modules.E100ChimeraModule`]
    """

    if len(module_ids) == 0 or "*" in module_ids:
        module_list = [m for m in tuple(tester.modules)]
        if reserve:
            await reserve_modules(modules=module_list, force=reserve)
        return tuple(tester.modules)
    else:
        module_list = [tester.modules.obtain(int(module_id)) for module_id in module_ids]
        if reserve:
            await reserve_modules(modules=module_list, force=reserve)
        return tuple(tester.modules.obtain(int(module_id)) for module_id in module_ids)
    

async def obtain_module_by_id(tester: L23Tester, module_id: str, reserve: bool = False) -> Union[GenericL23Module, E100ChimeraModule]:
    """
    Get the module object of the tester specified by module index id

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param module_id: the index id of the module.

    :type module_id: str
    :param reserve: should reserve the module, defaults to False
    :type reserve: bool, optional
    :raises NoSuchModuleError: No such a module index on the tester
    :return: module object
    :rtype: Union[:class:`~xoa_driver.modules.GenericL23Module`, :class:`~xoa_driver.modules.E100ChimeraModule`]
    """
    if reserve:
        await reserve_modules([tester.modules.obtain(int(module_id))], force=reserve)
    return tester.modules.obtain(int(module_id))


async def obtain_module_by_port_id(tester: L23Tester, port_id: str, separator: str = "/", reserve: bool = False) -> Union[GenericL23Module, E100ChimeraModule]:
    """
    Get the module object of the tester specified by the port index id

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param port_id: the index id of the port.

    :type port_id: str
    :param separator: The separator between module index and port index in port id, defaults to "/"
    :type separator: str, optional
    :param reserve: should reserve the module, defaults to False
    :type reserve: bool, optional
    :raises NoSuchModuleError: No such a module index on the tester
    :return: module object
    :rtype: Union[:class:`~xoa_driver.modules.GenericL23Module`, :class:`~xoa_driver.modules.E100ChimeraModule`]
    """
    if separator not in port_id:
        raise ValueError(f"Invalid port_id format: {port_id}. Expected format 'm{separator}p'.")
    module_id = port_id.split(separator)[0]
    if reserve:
        await reserve_modules([tester.modules.obtain(int(module_id))], force=reserve)
    return tester.modules.obtain(int(module_id))


async def reserve_modules(modules: List[GenericL23Module | E100ChimeraModule], force: bool = True) -> None:
    """
    Reserve modules regardless whether they are owned by others or not.

    :param modules: The modules to reserve
    :type modules: List[Union[:class:`~xoa_driver.modules.GenericL23Module`, :class:`~xoa_driver.modules.E100ChimeraModule`]]
    :param force: Should force reserve the module, defaults to True
    :type force: boolean
    :return:
    :rtype: None
    """

    await release_modules(modules, force)
    await asyncio.gather(*(module.reservation.set_reserve() for module in modules))


async def release_modules(
    modules: List[GenericL23Module | E100ChimeraModule], should_release_ports: bool = False
) -> None:
    """
    Free modules. If a module is reserved by you, release the module. If a module is reserved by others, relinquish the module. The modules should have no owner afterwards.
    :param module: The module to free
    :type module: Union[:class:`~xoa_driver.modules.GenericL23Module`, :class:`~xoa_driver.modules.E100ChimeraModule`]
    :param should_release_ports: should ports also be freed, defaults to False
    :type should_release_ports: bool, optional
    :return:
    :rtype: None
    """

    for module in modules:
        r = await module.reservation.get()
        if r.operation == enums.ReservedStatus.RESERVED_BY_OTHER:
            await module.reservation.set_relinquish()
        elif r.operation == enums.ReservedStatus.RESERVED_BY_YOU:
            await module.reservation.set_release()
        if should_release_ports:
            await release_ports(list(module.ports))


def get_module_supported_configs(
    module: Union[GenericL23Module, E100ChimeraModule],
) -> List[Tuple[MediaConfigurationType, int, int]]:
    """
    Get the module's supported configurations in a list. 

    :param module: The module object
    :type module: Union[GenericL23Module, E100ChimeraModule]
    :return: List of tuple(supported media, port count, port speed) (The port speed in Mbps, e.g. 40000 for 40G)
    :rtype: List[Tuple[MediaConfigurationType, int, int]]
    """
    supported_media_list = []
    for media_item in module.info.media_info_list: # type: ignore
        for port_speed_config in media_item.supported_configs:
            supported_media_list.append((media_item.cage_type, port_speed_config.port_count, port_speed_config.port_speed))

    return supported_media_list


async def set_module_config(
    module: Union[GenericL23Module, E100ChimeraModule],
    media: enums.MediaConfigurationType,
    port_count: int,
    port_speed: int,
    force: bool = True,
) -> None:
    """Change the module configuration to the target media, port count and port speed.

    :param module: the module object
    :type module: Union[GenericL23Module, E100ChimeraModule]
    :param media: the target media for the module
    :type media: enums.MediaConfigurationType
    :param port_count: the target port count
    :type port_count: int
    :param port_speed: the target port speed in Mbps, e.g. 40000 for 40G
    :type port_speed: int
    :param force: should forcibly reserve the module, defaults to True
    :type force: bool, optional
    :raises NotSupportMediaPortSpeed: the provided media, port count and port speed configuration is not supported by the module
    """

    await set_module_configs([(module, media, port_count, port_speed)], force)


async def set_module_configs(module_configs: List[Tuple[Union[GenericL23Module, E100ChimeraModule], enums.MediaConfigurationType, int, int]], force: bool = True) -> None:

    """Configure multiple modules with specified media, port count and port speed.

    :param module_configs: List of module configuration tuples. 
    
    Each tuple contains (module object, target media, target port count, target port speed in Mbps, should forcibly reserve the module)

    :type module_configs: List[Tuple[Union[GenericL23Module, E100ChimeraModule], enums.MediaConfigurationType, int, int, bool]]

    :param force: should forcibly reserve the modules, defaults to True
    :type force: bool, optional

    :raises NotSupportMediaPortSpeed: one of the provided media, port count and port speed configuration is not supported by the corresponding module.
    """
    # reserve the modules
    await reserve_modules([module for (module, _, _, _) in module_configs], force)

    for module_config in module_configs:
        module, media, port_count, port_speed = module_config
        
        # get the supported media
        supported_media_list = get_module_supported_configs(module)

        # set the module media if the target media is found in supported media
        for item in supported_media_list:
            if all(
                (
                    item[0] == media,
                    item[1] == port_count,
                    item[2] == port_speed,
                )
            ):
                portspeed_list = [port_count] + port_count * [port_speed]
                await module.config.media.set(media_config=media)
                await module.config.port_speed.set(portspeed_list=portspeed_list)
                return None
        raise NotSupportMediaPortSpeed(module)
    
    # release the modules
    await release_modules([module for (module, _, _, _) in module_configs], False)
        

async def get_module_eol_date(module: Union[GenericL23Module, E100ChimeraModule]) -> str:
    """
    Get module's End-of-Life date

    :param module: The module object
    :type module: Union[GenericL23Module, E100ChimeraModule]
    :return: Module's EOL date
    :rtype: str
    """
    resp = await module.serial_number.get()
    module_key = str(resp.serial_number)[-2:]
    return MODULE_EOL_INFO.get(module_key, "2999-01-01")


async def get_module_eol_days(module: Union[GenericL23Module, E100ChimeraModule]) -> int:
    """
    Get days until module's End-of-Life date

    :param module: The module object
    :type module: Union[GenericL23Module, E100ChimeraModule]
    :return: days until module's End-of-Life date
    :rtype: int
    """
    eol_string = await get_module_eol_date(module)
    date1 = datetime.now()
    date2 = datetime.strptime(eol_string, "%Y-%M-%d")
    timedelta = date2 - date1
    return timedelta.days


async def get_cage_insertions(module: Union[Z800FreyaModule, Z1600EdunModule]) -> Tuple[int, ...]:
    """
    Get module cage insertion count of each cage

    :param module: The Z800 Freya/Z1600 Edun module object
    :type module: Union[Z800FreyaModule, Z1600EdunModule]
    :return: Insertion count of each cage
    :rtype: Tuple[int, ...]
    """
    resp = await module.health.cage_insertion.get()
    info_js = resp.info
    info_dict = json.loads(info_js)
    result = tuple(cage['insert_count'] for cage in info_dict['1']['data'])
    return result


async def get_cage_count(module: Union[Z800FreyaModule, Z1600EdunModule]) -> int:
    """
    Get module cage count

    :param module: The Z800 Freya/Z1600 Edun module object
    :type module: Union[Z800FreyaModule, Z1600EdunModule]
    :return: The number of cages in the module
    :rtype: int
    """
    resp = await module.health.cage_insertion.get()
    info_js = resp.info
    info_dict = json.loads(info_js)
    result = len(info_dict['1']['data'])
    return result


# endregion


# region Ports


async def obtain_ports_by_ids(tester: L23Tester, port_ids: List[str], separator: str = "/", reserve: bool = False) -> tuple[Union[GenericL23Port, E100ChimeraPort], ...]:
    """
    Get ports of the tester specified by port ids

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param port_ids: The port ids.
    
        The port index with format ``m/p``, m is module index, p is port index, e.g. ["1/3", "2/4"]. 

        Use ``1/*`` to get all ports of module 1.

        Use ``*/1`` to get port 1 of all modules.

        Use ``*``, or ``*/*`` to get all ports of all modules.
    
        Use an empty list to get all ports of all modules.

    :type port_ids: List[str]
    :param separator: The separator between module index and port index in port id, defaults to `/`
    :type separator: str, optional
    :param reserve: should reserve the ports, defaults to False
    :type reserve: bool, optional
    :return: List of port objects
    :rtype: tuple[Union[GenericL23Port, E100ChimeraPort]]
    """

    returned_ports = []
    if len(port_ids) == 0 or f"*{separator}*" in port_ids or f"*" in port_ids: # [] or ["*/*"] or ["*"]
        all_ports_ = (m.ports for m in tester.modules)
        if reserve:
            await reserve_ports(list(chain.from_iterable(all_ports_)), force=reserve)
        return tuple(chain.from_iterable(all_ports_))
    else:
        for port_id in port_ids:
            if separator not in port_id:
                continue
            mid = port_id.split(separator)[0]
            if mid != "*":
                module = tester.modules.obtain(int(mid))
                pid = port_id.split(separator)[1]
                if pid == "*": # ["1/*"]
                    returned_ports.extend(list(module.ports))
                else: # ["1/3"]
                    returned_ports.append(module.ports.obtain(int(pid)))
            else: # ["*/1"]
                pid = port_id.split(separator)[1]
                for module in tester.modules:
                    returned_ports.append(module.ports.obtain(int(pid)))
        if reserve:
            await reserve_ports(returned_ports, force=reserve)
        return tuple(returned_ports)


async def obtain_port_by_id(tester: L23Tester, port_id: str, separator: str = "/", reserve: bool = False) -> Union[GenericL23Port, E100ChimeraPort]:
    """
    Get a port of the module

    :param tester: The tester object
    :type tester: :class:`~xoa_driver.testers.L23Tester`
    :param port_id: The port index with format "m/p", m is module index, p is port index, e.g. "1/3". Wildcard "*" is not allowed.
    :type port_id: str
    :param separator: The separator between module index and port index in port id, defaults to "/"
    :type separator: str, optional
    :param reserve: should reserve the port, defaults to False
    :type reserve: bool, optional
    :raises NoSuchPortError: No port found with the index
    :return: The port object
    :rtype: Union[GenericL23Port, E100ChimeraPort]
    """
    if "*" in port_id:
        raise ValueError("Wildcard '*' is not allowed in port_id for obtain_port_by_id function.")
    if separator not in port_id:
        raise ValueError(f"Invalid port_id format: {port_id}. Expected format 'm{separator}p'.")
    port_obj = (await obtain_ports_by_ids(tester, [port_id], separator=separator, reserve=reserve))[0]
    return port_obj


async def reserve_ports(ports: list[Union[GenericL23Port, E100ChimeraPort]], force: bool = True, reset: bool = False) -> None:
    """
    Reserve a port regardless whether it is owned by others or not.

    :param ports: The ports to reserve
    :type ports: list[Union[GenericL23Port, E100ChimeraPort]]
    :param force: Should force reserve the ports, defaults to True
    :type force: boolean, optional
    :param reset: Should reset the ports after reserving, defaults to False
    :type reset: boolean, optional
    :return:
    :rtype: None
    """
    for port in ports:
        r = await port.reservation.get()
        if force and r.status == enums.ReservedStatus.RESERVED_BY_OTHER:
            await apply(
                port.reservation.set_relinquish(),
                port.reservation.set_reserve(),
            )
        elif r.status == enums.ReservedStatus.RELEASED:
            await port.reservation.set_reserve()
        if reset:
            await port.reset.set()


async def release_ports(ports: List[Union[GenericL23Port, E100ChimeraPort]]) -> None:
    """
    Free a port. If the port is reserved by you, release the port. If the port is reserved by others, relinquish the port. The port should have no owner afterwards.

    :param port: The port to free
    :type port: Union[GenericL23Port, E100ChimeraPort]
    :return:
    :rtype: None
    """
    for port in ports:
        r = await port.reservation.get()
        if r.status == enums.ReservedStatus.RESERVED_BY_OTHER:
            await port.reservation.set_relinquish()
        elif r.status == enums.ReservedStatus.RESERVED_BY_YOU:
            await port.reservation.set_release()


async def reset_ports(ports: List[Union[GenericL23Port, E100ChimeraPort]]) -> None:
    """
    Reset a list of ports.

    :param ports: The ports to reset
    :type ports: List[Union[GenericL23Port, E100ChimeraPort]]
    :return:
    :rtype: None
    """
    await asyncio.gather(*(port.reset.set() for port in ports))

# endregion


# region Streams
async def remove_streams(port: GenericL23Port) -> None:
    """
    Remove all streams on a port witout resetting the port.

    :param port: The port object
    :type port: GenericL23Port
    """
    await port.streams.server_sync()
    await asyncio.gather(*(s.delete() for s in port.streams))


# endregion

__all__ = (
    "reserve_tester",
    "release_tester",
    "get_chassis_sys_uptime",
    "obtain_modules_by_ids",
    "obtain_module_by_id",
    "obtain_module_by_port_id",
    "reserve_modules",
    "release_modules",
    "get_module_supported_configs",
    "set_module_configs",
    "set_module_config",
    "get_module_eol_date",
    "get_module_eol_days",
    "get_cage_insertions",
    "get_cage_count",
    "obtain_ports_by_ids",
    "obtain_port_by_id",
    "reserve_ports",
    "release_ports",
    "reset_ports",
    "remove_streams",
)
