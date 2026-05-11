from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_UE_CTLOS_CLEAR,
    P_UE_CTLOS_RX_STATS,
    P_UE_CTLOS_TX_STATS,
)

class UecCtlOsStats:
    """UE CtlOS statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.rx = P_UE_CTLOS_RX_STATS(conn, module_id, port_id)
        """UE CtlOS Rx statistics.

        :type: P_UE_CTLOS_RX_STATS
        """

        self.tx = P_UE_CTLOS_TX_STATS(conn, module_id, port_id)
        """UE CtlOS Tx statistics.

        :type: P_UE_CTLOS_TX_STATS
        """

        self.clear = P_UE_CTLOS_CLEAR(conn, module_id, port_id)
        """Clear UE CtlOS counters in the specified direction(s).

        :type: P_UE_CTLOS_CLEAR
        """


class UecCtlOs:

    """UE CtlOS (Control Plane Oversubscription) related features of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.stats = UecCtlOsStats(conn, module_id, port_id)
        """UE CtlOS statistics.

        :type: UecCtlOsStats
        """
