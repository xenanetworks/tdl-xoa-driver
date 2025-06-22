import asyncio
import functools
from typing import TYPE_CHECKING

from xoa_driver.internals.commands import (
    P_CAPABILITIES,
    P_INTERFACE,
    P_STATUS,
    P_TXENABLE,
    P_LOADMODE,
    P_EMULATE,
    P_CAPABILITIES_EXT,
    PP_LINKFLAP_PARAMS,
    PP_LINKFLAP_ENABLE,
    PP_PMAERRPUL_PARAMS,
    PP_PMAERRPUL_ENABLE,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.hli.ports import base_port
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.state_storage import ports_state
from .pe_custom_distribution import CustomDistributions
from .port_emulation import ChimeraPE


class LinkFlap:
    """L23 high-speed port link flap."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_LINKFLAP_PARAMS(conn, module_id, port_id)
        """Link flap parameters.
        
        :type: PP_LINKFLAP_PARAMS
        """

        self.enable = PP_LINKFLAP_ENABLE(conn, module_id, port_id)
        """Link flap control.
        
        :type: PP_LINKFLAP_ENABLE
        """


class PMAErrorInject:
    """L23 high-speed port PMA pulse error injection."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.params = PP_PMAERRPUL_PARAMS(conn, module_id, port_id)
        """PMA pulse error injection parameters.
        
        :type: PP_PMAERRPUL_PARAMS
        """

        self.enable = PP_PMAERRPUL_ENABLE(conn, module_id, port_id)
        """PMA pulse error injection control.
        
        :type: PP_PMAERRPUL_ENABLE
        """


class PortNEBase(base_port.BasePort[ports_state.PortChimeraLocalState]):
    """Chimera port for traffic impairment."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """Chimera port capabilities.

        :type: P_CAPABILITIES
        """

        self.capabilities_ext = P_CAPABILITIES_EXT(conn, module_id, port_id)
        """Chimera port capabilities ext.

        :type: P_CAPABILITIES_EXT
        """

        self.interface = P_INTERFACE(conn, module_id, port_id)
        """Physical interface type of the Chimera port.

        :type: P_INTERFACE
        """

        self.status = P_STATUS(conn, module_id, port_id)
        """Chimera port's received optical signal level'.

        :type: P_STATUS
        """

        self.tx_enable = P_TXENABLE(conn, module_id, port_id)
        """Enabling Chimera port TX.

        :type: P_TXENABLE
        """

        self.load_mode = P_LOADMODE(conn, module_id, port_id)
        """Load mode of the Chimera port.

        :type: P_LOADMODE
        """

        self.impairment = ChimeraPE(self._conn, *self.kind)
        """Port-level network emulation settings
        
        :type: ChimeraPE
        """

        self.emulate = P_EMULATE(conn, module_id, port_id)
        """Chimera emulation control.

        :type: P_EMULATE
        """


        self.custom_distributions = CustomDistributions(conn, module_id, port_id)
        """Custom distributions."""

        self.link_flap = LinkFlap(conn, module_id, port_id)
        """Link flap settings.
        
        :type: LinkFlap
        """

        self.pma_error_inject = PMAErrorInject(conn, module_id, port_id)
        """PMA pulse error injection settings.

        :type: PMAErrorInject
        """

        self._local_states = ports_state.PortChimeraLocalState()
        """Local states of the Chimera port."""

    @property
    def info(self) -> ports_state.PortChimeraLocalState:
        return self._local_states

    async def _setup(self):
        await asyncio.gather(
            self._local_states.initiate(self),
            self.custom_distributions.server_sync(),
            self.impairment
        )
        self._local_states.register_subscriptions(self)
        return self

    on_interface_change = functools.partialmethod(utils.on_event, P_INTERFACE)
    """Register a callback to the event that the port's interface type changes."""

    on_emulate_change = functools.partialmethod(utils.on_event, P_EMULATE)
    """Register a callback to the event that the port's emulation state changes."""
