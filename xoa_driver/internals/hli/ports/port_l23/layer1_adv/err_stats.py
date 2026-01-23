from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_LF_CNT,
    PL1AD_RX_RF_CNT,
    PL1AD_RX_LOA_CNT,
    PL1AD_RX_LOSYNC_CNT,
    PL1AD_RX_LOL,
    PL1AD_RX_SKEW,

)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class ErrStats:
    """Port PCS Error Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.rx_lf_count = PL1AD_RX_LF_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Local Fault conditions since last query.
        
        :type: PL1AD_RX_LF_CNT
        """

        self.rx_rf_count = PL1AD_RX_RF_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Remote Fault conditions since last query.
        
        :type: PL1AD_RX_RF_CNT
        """

        self.rx_loa_count = PL1AD_RX_LOA_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Loss of Alignment conditions since last query.

        :type: PL1AD_RX_LOA_CNT
        """

        self.rx_losync_count = PL1AD_RX_LOSYNC_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Loss of Sync conditions since last query.

        :type: PL1AD_RX_LOSYNC_CNT
        """

class PcsLaneAdv:
    """PCS Lane Advanced Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:

        self.rx_lol = PL1AD_RX_LOL(conn, module_id, port_id, lane_idx)
        """Returns the current and the latched CDR Loss of Lock (LOL) status of the specified PCS lane.

        :type: PL1AD_RX_LOL
        """

        self.rx_skew = PL1AD_RX_SKEW(conn, module_id, port_id, lane_idx)
        """Returns the relative skew of the PCS lane measured in bits.

        :type: PL1AD_RX_SKEW
        """