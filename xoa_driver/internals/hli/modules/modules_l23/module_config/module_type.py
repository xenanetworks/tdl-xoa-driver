from __future__ import annotations
import asyncio
import functools
import typing
from typing import Self
from xoa_driver.internals.commands import (
    M_MEDIA,
    M_STATUS,
    M_UPGRADE,
    M_UPGRADEPROGRESS,
    M_TIMESYNC,
    M_CFPTYPE,
    M_CFPCONFIGEXT,
    M_COMMENT,
    # M_TIMEADJUSTMENT,
    M_CAPABILITIES,
    M_MEDIASUPPORT,
    M_FPGAREIMAGE,
    M_MULTIUSER,
    M_CLOCKPPB,
    M_SMAINPUT,
    M_SMAOUTPUT,
    M_SMASTATUS,
    M_NAME,
    M_REVISION,
    M_CLOCKSYNCSTATUS,
    M_TXCLOCKSOURCE_NEW,
    M_TXCLOCKSTATUS_NEW,
    M_TXCLOCKFILTER_NEW,
    M_UPGRADEPAR,
    M_VERSIONSTR,
    M_RECONFIG_STATUS,
)

from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.state_storage import modules_state
from xoa_driver.enums import MediaConfigurationType
from xoa_driver.internals.core.token import Token
from ... import base_module as bm
from ... import __interfaces as m_itf

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ...module_chimera import ModuleChimera
    from ..bases.module_l23 import ModuleL23
    

class ExtendedToken:
    def __init__(
        self, token: Token, module: typing.Union["ModuleL23", "ModuleChimera"]
    ) -> None:
        self.__token = token
        self.__module = module

    def __await__(self):
        return self.__ask_then().__await__()

    async def __ask_then(self):
        r = await self.__token
        p_counts = (await self.__module.port_count.get()).port_count
        if self.__module.ports is not None:
            changed = self.__module.ports.reinit(p_counts)
            if changed:
                await self.__module.ports.fill()
        return r

class MediaModule:
    def __init__(self, conn: "itf.IConnection", module: typing.Union["ModuleL23", "ModuleChimera"]) -> None:
        self.__media = M_MEDIA(conn, module.module_id)
        self.__module = module

    def get(self) -> Token:
        return self.__media.get()

    def set(self, media_config: MediaConfigurationType) -> ExtendedToken:
        return ExtendedToken(self.__media.set(media_config), self.__module)
    

class CfpModule:
    def __init__(self, conn: "itf.IConnection", module: typing.Union["ModuleL23", "ModuleChimera"]) -> None:
        self.__cfpconfigext = M_CFPCONFIGEXT(conn, module.module_id)
        self.__module = module
    
    def get(self) -> Token:
        return self.__cfpconfigext.get()

    def set(self, portspeed_list: typing.List[int]) -> ExtendedToken:
        return ExtendedToken(self.__cfpconfigext.set(portspeed_list), self.__module)


class CFP:
    """Test module CFP"""

    def __init__(self, conn: "itf.IConnection", module: typing.Union["ModuleL23", "ModuleChimera"]) -> None:
        self.type = M_CFPTYPE(conn, module.module_id)
        """The transceiver's CFP type currently inserted.

        :type: M_CFPTYPE
        """


class ModuleConfig:
    """Test module CFP"""

    def __init__(self, conn: "itf.IConnection", module: typing.Union["ModuleL23", "ModuleChimera"]) -> None:
        self.media = MediaModule(conn, module)
        """Test module's media type configuration."""

        self.port_speed = CfpModule(conn, module)
        """Test module's port speed configuration."""

        self.status = M_RECONFIG_STATUS(conn, module.module_id)
        """Test module's configuration status."""