from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PRECODING,
    PP_GRAYCODING,
    PL1_PNSWAP_RX,
    PL1_PNSWAP_TX,
)

from xoa_driver import enums


class FreyaPMA:
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