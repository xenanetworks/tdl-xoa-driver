from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_FAULTSIGNALING,
    P_FAULTSTATUS,
    P_FAULTCNT,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class RsFault:
    """RS Fault Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.signaling = P_FAULTSIGNALING(conn, module_id, port_id)
        """L23 port fault signaling.
        
        :type: P_FAULTSIGNALING
        """

        self.status = P_FAULTSTATUS(conn, module_id, port_id)
        """L23 port fault status.
        
        :type: P_FAULTSTATUS
        """

        self.stats = P_FAULTCNT(conn, module_id, port_id)
        """L23 port fault counters.
        
        :type: P_FAULTCNT
        """
