from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_ERR_CW_CNT,
    PL1AD_TX_ERR_CW,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class ErrorCodeword:
    """Erroneous Codeword (CW) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_count = PL1AD_RX_ERR_CW_CNT(conn, module_id, port_id)
        """Returns the number of cumulative erroneous 64b/66b codewords since last query.
        
        :type: PL1AD_RX_ERR_CW_CNT
        """

        self.tx_inject = PL1AD_TX_ERR_CW(conn, module_id, port_id)
        """Sends an error 64b/66b codeword from the Tx port immediately when called.
        
        :type: PL1AD_TX_ERR_CW
        """
