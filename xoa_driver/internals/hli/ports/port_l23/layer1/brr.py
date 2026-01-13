from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_BRRMODE,
    P_BRRSTATUS,
)
from xoa_driver import enums

class BroadrReach:
    """BroadR Reach configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_BRRMODE(conn, module_id, port_id)
        """BRR mode.
        
        :type: P_BRRMODE
        """
        self.status = P_BRRSTATUS(conn, module_id, port_id)
        """Actual BRR status.
        
        :type: P_BRRSTATUS
        """
