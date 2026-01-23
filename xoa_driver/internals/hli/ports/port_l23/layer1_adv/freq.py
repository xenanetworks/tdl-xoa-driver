from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_FREQ_CURR,
    PL1AD_RX_FREQ_MAX,
    PL1AD_RX_FREQ_MIN,
    PL1AD_TX_FREQ_CURR,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class FrequencyAdv:
    """Frequency Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_curr = PL1AD_RX_FREQ_CURR(conn, module_id, port_id)
        """Returns the current receive frequency.
        
        :type: PL1AD_RX_FREQ_CURR
        """

        self.rx_max = PL1AD_RX_FREQ_MAX(conn, module_id, port_id)
        """Returns the maximum receive frequency.
        
        :type: PL1AD_RX_FREQ_MAX
        """

        self.rx_min = PL1AD_RX_FREQ_MIN(conn, module_id, port_id)
        """Returns the minimum receive frequency.

        :type: PL1AD_RX_FREQ_MIN
        """

        self.tx_curr = PL1AD_TX_FREQ_CURR(conn, module_id, port_id)
        """Returns the current transmit frequency.

        :type: PL1AD_TX_FREQ_CURR
        """
