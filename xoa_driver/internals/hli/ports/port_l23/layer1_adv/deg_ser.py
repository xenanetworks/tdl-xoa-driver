from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_DEG_SER,
    PL1AD_RX_DEG_SER_THRESH,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class DegradedSer:
    """Degraded Symbol Error Rate (SER) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.threshold = PL1AD_RX_DEG_SER_THRESH(conn, module_id, port_id)
        """Configures the thresholds for the Degraded SER Alarm.
        
        :type: PL1AD_RX_DEG_SER_THRESH
        """

        self.status = PL1AD_RX_DEG_SER(conn, module_id, port_id)
        """The current and latched Degraded SER status of the port.
        
        :type: PL1AD_RX_DEG_SER
        """
