from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums

#region Serdes-level

class PMASerdes:
    """Freya PMA"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.precoding = PP_PRECODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Pre-Coding Configurations. (only for Freya)

        :type: PP_PRECODING
        """

        self.graycoding = PP_GRAYCODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Gray-Coding Configurations. (only for Freya)

        :type: PP_GRAYCODING
        """

        self.pn_swap_rx = PL1_PNSWAP_RX(conn, module_id, port_id, serdes_xindex)
        """GET/SET PN-Swap RX Configurations. (only for Freya)

        :type: PL1_PNSWAP_RX
        """

        self.pn_swap_tx = PL1_PNSWAP_TX(conn, module_id, port_id, serdes_xindex)
        """GET/SET PN-Swap TX Configurations. (only for Freya)
        
        :type: PL1_PNSWAP_TX
        """


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

#endregion