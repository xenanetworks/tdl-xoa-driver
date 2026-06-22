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

from ..health.health import MHealth
from ..timing_clock.ppm_sweep import MClockSweep
from ..timing_clock.timing import (
    MTiming,
    AdvancedTiming,
)
from ..module_config.module_type import (
    ExtendedToken,
    CFP,
    ModuleConfig,
)
from ..upgrade.upgrade import MUpgrade


if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ...module_chimera import ModuleChimera


class ModuleL23(bm.BaseModule["modules_state.ModuleL23LocalState"]):
    """
    This is a conceptual class of L23 test module on a Valkyrie tester.

    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self._local_states = modules_state.ModuleL23LocalState()

        self.name = M_NAME(conn, self.module_id)
        """Test module's name.

        :type: M_NAME
        """

        self.comment = M_COMMENT(conn, self.module_id)
        """Test module's description.

        :type: M_COMMENT
        """

        self.status = M_STATUS(conn, self.module_id)
        """Test module's status.

        :type: M_STATUS
        """

        self.supported_configs = M_MEDIASUPPORT(conn, self.module_id)
        """Test module's available speeds.

        :type: M_MEDIASUPPORT
        """

        self.revision = M_REVISION(conn, self.module_id)
        """Test module's model P/N name.

        :type: M_REVISION
        """

        self.version_str = M_VERSIONSTR(conn, self.module_id)
        """Module version number in the new format

        :type: M_VERSIONSTR
        """

        self.multiuser = M_MULTIUSER(conn, self.module_id)
        """If multiple users are allowed to control the same test module.

        :type: M_MULTIUSER
        """

        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        """Test module's capabilities.

        :type: M_CAPABILITIES
        """

        self.timing = MTiming(conn, self.module_id)
        """Test module's timing configuration.

        :type: MTiming
        """

        self.advanced_timing = AdvancedTiming(conn, self.module_id)
        """Test module's advanced timing configuration.

        :type: AdvancedTiming
        """

        self.cfp = CFP(conn, self)
        """Test module's CFP configuration.

        :type: CFP
        """

        self.config = ModuleConfig(conn, self)
        """Test module's configuration."""

        self.upgrade = MUpgrade(conn, self.module_id)
        """Test module's upgrade settings.

        :type: MUpgrade
        """

        self.ports: typing.Optional[pm.PortsManager] = None
        """L23 Port Index Manager of the test module.

        :type: PortsManager
        """

    @property
    def info(self) -> modules_state.ModuleL23LocalState:
        """Return the module's local state

        :return: the module's local state
        :rtype: ModuleL23LocalState
        """
        return self._local_states

    async def _setup(self) -> Self:
        if self.ports is None:
            raise NotImplementedError("Ports manager type are not defined.")  # Maybe can be better solution then this...
        await asyncio.gather(
            self._local_states.initiate(self),
            self.ports.fill()
        )
        self._local_states.register_subscriptions(self)
        return self

    on_cfp_type_change = functools.partialmethod(utils.on_event, M_CFPTYPE)
    """Register a callback to the event that the module's CFP type (:class:`M_CFPTYPE`) changes."""

    on_cfp_config_change = functools.partialmethod(utils.on_event, M_CFPCONFIGEXT)
    """Register a callback to the event that the module's CFP configuration changes."""

    on_status_change = functools.partialmethod(utils.on_event, M_STATUS)
    """Register a callback to the event that the module's status changes."""

    on_revision_change = functools.partialmethod(utils.on_event, M_REVISION)
    """Register a callback to the event that the module's model type changes."""

    on_name_change = functools.partialmethod(utils.on_event, M_NAME)
    """Register a callback to the event that the module's name changes."""

    on_adv_timing_clock_tx_status_change = functools.partialmethod(utils.on_event, M_TXCLOCKSTATUS_NEW)
    """Register a callback to the event that the module's TX clock status changes."""

    on_adv_timing_clock_tx_source_change = functools.partialmethod(utils.on_event, M_TXCLOCKSOURCE_NEW)
    """Register a callback to the event that the module's clock that drives the port TX rates changes."""

    on_adv_timing_clock_tx_filter_change = functools.partialmethod(utils.on_event, M_TXCLOCKFILTER_NEW)
    """Register a callback to the event that the module's loop bandwidth on the TX clock filter changes."""

    on_adv_timing_sma_status_change = functools.partialmethod(utils.on_event, M_SMASTATUS)
    """Register a callback to the event that the module's SMA status changes."""

    on_adv_timing_sma_input_change = functools.partialmethod(utils.on_event, M_SMAINPUT)
    """Register a callback to the event that the module's SMA input function changes."""

    on_adv_timing_sma_output_change = functools.partialmethod(utils.on_event, M_SMAOUTPUT)
    """Register a callback to the event that the module's SMA output function changes."""

    on_media_support_change = functools.partialmethod(utils.on_event, M_MEDIASUPPORT)
    """Register a callback to the event that the module's supported media changes."""

    on_media_change = functools.partialmethod(utils.on_event, M_MEDIA)
    """Register a callback to the event that the module's media and available speeds change."""

    on_comment_change = functools.partialmethod(utils.on_event, M_COMMENT)
    """Register a callback to the event that the module's description changes."""

    on_timing_source_change = functools.partialmethod(utils.on_event, M_TIMESYNC)
    """Register a callback to the event that the module's timesync mode changes."""

    on_timing_clock_local_adjust_change = functools.partialmethod(utils.on_event, M_CLOCKPPB)
    """Register a callback to the event that the module's clock adjustment ppb changes."""
