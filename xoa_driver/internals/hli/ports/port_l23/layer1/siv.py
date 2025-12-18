from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PL1_CTRL,
    PL1_GET_DATA,
)
from xoa_driver import enums

class FreyaSIV:
    """Freya Signal Integrity View"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.control = PL1_CTRL(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Control SIV scan. (only for Freya)

        :type: PL1_CTRL
        """

        self.data = PL1_GET_DATA(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Get SIV scan data. (only for Freya)

        :type: PL1_GET_DATA
        """
