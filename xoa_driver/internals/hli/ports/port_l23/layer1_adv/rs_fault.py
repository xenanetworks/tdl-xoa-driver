from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_LF_CNT,
    PL1AD_RX_RF_CNT,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class RsFault:
    """RS Fault Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_local_fault_since_last = PL1AD_RX_LF_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Local Fault conditions since last query.
        
        :type: PL1AD_RX_LF_CNT
        """

        self.rx_remote_fault_since_last = PL1AD_RX_RF_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Remote Fault conditions since last query.
        
        :type: PL1AD_RX_RF_CNT
        """