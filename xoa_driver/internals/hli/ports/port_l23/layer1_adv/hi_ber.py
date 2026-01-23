from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PL1AD_RX_HIBER,
    PL1AD_RX_HISER,
    PL1AD_RX_HISER_ALARM,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class HighBer:
    """High Bit Error Rate (BER)"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1AD_RX_HIBER(conn, module_id, port_id)
        """Returns the current and the latched High BER status of the port.
        
        :type: PL1AD_RX_HIBER
        """
