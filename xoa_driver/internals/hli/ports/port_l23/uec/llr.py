from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_UE_LLR_MODE,
    P_UE_LLR_RX_STATS,
    P_UE_LLR_TX_STATS,
    PR_CLEAR,
    PT_CLEAR,
)

class UecLlr:
    """UE LLR Link Layer Retry"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.mode = P_UE_LLR_MODE(conn, module_id, port_id)
        """Get or set the LLR mode of the port.

        :type: P_UE_LLR_MODE
        """

        self.stats = UecLlrStats(conn, module_id, port_id)
        """UE LLR statistics.

        :type: UecLlrStats
        """

class UecLlrStats:
    """UE LLR (Link Layer Retry) statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.rx = P_UE_LLR_RX_STATS(conn, module_id, port_id)
        """UE LLR Rx statistics.

        :type: P_UE_LLR_RX_STATS
        """

        self.tx = P_UE_LLR_TX_STATS(conn, module_id, port_id)
        """UE LLR Tx statistics.

        :type: P_UE_LLR_TX_STATS
        """

        self.clear_tx = PT_CLEAR(conn, module_id, port_id)
        """Clear UE LLR Tx counters in the specified direction(s).
        
        This command also clears L2/L3 Tx traffic statistics of the port.

        :type: PT_CLEAR
        """

        self.clear_rx = PR_CLEAR(conn, module_id, port_id)
        """Clear UE LLR Rx counters in the specified direction(s).

        This command also clears L2/L3 Rx traffic statistics of the port.

        :type: PR_CLEAR
        """