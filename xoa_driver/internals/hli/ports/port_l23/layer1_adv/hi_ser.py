from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_HIBER,
    PL1AD_RX_HISER,
    PL1AD_RX_HISER_ALARM,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class HighSer:
    """High Symbol Error Rate (SER)"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1AD_RX_HISER(conn, module_id, port_id)
        """Returns the current and the latched High SER status of the port.
        
        :type: PL1AD_RX_HISER
        """

        self.alarm = PL1AD_RX_HISER_ALARM(conn, module_id, port_id)
        """Configures the High SER Alarm.

        :type: PL1AD_RX_HISER_ALARM
        """
