from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_ITB_CNT,
    PL1AD_TX_ITB,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class InvalidTranscodeBlock:
    """Invalid Transcode Block (ITB) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_count = PL1AD_RX_ITB_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Invalid 256b/257b Transcode Blocks since last query.
        
        :type: PL1AD_RX_ITB_CNT
        """

        self.tx_inject = PL1AD_TX_ITB(conn, module_id, port_id)
        """Sends an Invalid 256b/257b Transcode Block from the Tx port immediately when called.
        
        :type: PL1AD_TX_ITB
        """
