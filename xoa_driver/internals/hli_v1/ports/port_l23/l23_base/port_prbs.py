from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums

#region Port-level

class PRBSErrorGen:
    """L23 high-speed port PCS/PMA TX error generation."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.error_rate = PP_TXERRORRATE(conn, module_id, port_id)
        """The rate of continuous bit-level error injection.

        :type: PP_TXERRORRATE
        """

        self.inject_one = PP_TXINJECTONE(conn, module_id, port_id)
        """Inject a single bit-level error.

        :type: PP_TXINJECTONE
        """
#endregion


#region Serdes-level

class PRBSSerdes:
    """L23 high-speed port SerDes PRBS control and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.control = PP_TXPRBSCONFIG(conn, module_id, port_id, serdes_xindex)
        """TX PRBS configuration of a SerDes.

        :type: PP_TXPRBSCONFIG
        """

        self.status = PP_RXPRBSSTATUS(conn, module_id, port_id, serdes_xindex)
        """RX PRBS status on a SerDes

        :type: PP_RXPRBSSTATUS
        """

#endregion