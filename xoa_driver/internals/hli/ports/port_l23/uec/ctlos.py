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
    P_UE_CTLOS_SPACING,
    P_UE_CTLOS_TX_INTERVAL,
    P_UE_CTLOS_RX_INTERVAL,
    P_UE_CTLOS_RX_ERRORS,
)

class UecCtlOsConfig:
    """UE CtlOS configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.spacing = P_UE_CTLOS_SPACING(conn, module_id, port_id)
        """UE CtlOS spacing configuration.

        :type: P_UE_CTLOS_SPACING
        """
        
class UecCtlOsStats:
    """UE CtlOS counters and values statistics"""

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
        
        self.rx_interval = P_UE_CTLOS_RX_INTERVAL(conn, module_id, port_id)
        """UE CtlOS Rx interval statistics.

        :type: P_UE_CTLOS_RX_INTERVAL
        """

        self.tx_interval = P_UE_CTLOS_TX_INTERVAL(conn, module_id, port_id)
        """UE CtlOS Tx interval statistics.

        :type: P_UE_CTLOS_TX_INTERVAL
        """
        
        self.rx_errors = P_UE_CTLOS_RX_ERRORS(conn, module_id, port_id)
        """The number of CtlOS received with Rx errors, including CRC error, invalid length error, and other errors.
        
        :type: P_UE_CTLOS_RX_ERRORS 
        """
        
class UecCtlOs:

    """UE CtlOS (Control Plane Oversubscription) related features of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.statistics = UecCtlOsStats(conn, module_id, port_id)
        """UE CtlOS statistics.

        :type: UecCtlOsStats
        """
        
        self.configuration = UecCtlOsConfig(conn, module_id, port_id)
        """UE CtlOS configuration.
        
        :type: UecCtlOsConfig
        """
        
        
