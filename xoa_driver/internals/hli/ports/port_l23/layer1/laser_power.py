from typing import (
    TYPE_CHECKING,
    Tuple,
)
from typing import Self
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_RXLASERPOWER,
    PP_TXLASERPOWER,
)
from xoa_driver import enums

class LaserPower:
    """Laser power status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_laser_power = PP_TXLASERPOWER(conn, module_id, port_id)
        """Power of TX laser.

        :type: PP_TXLASERPOWER
        """

        self.rx_laser_power = PP_RXLASERPOWER(conn, module_id, port_id)
        """Power of RX laser.

        :type: PP_RXLASERPOWER
        """