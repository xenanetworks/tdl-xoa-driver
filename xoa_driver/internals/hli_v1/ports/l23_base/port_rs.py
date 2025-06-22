from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums


class Fault:
    """L23 port fault settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.signaling = P_FAULTSIGNALING(conn, module_id, port_id)
        """L23 port fault signaling.
        
        :type: P_FAULTSIGNALING
        """

        self.status = P_FAULTSTATUS(conn, module_id, port_id)
        """L23 port fault status.
        
        :type: P_FAULTSTATUS
        """