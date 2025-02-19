from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PR_FLOWTOTAL,
    PR_FLOWCLEAR,
)


class ReceptionStatistics:
    """Chimera RX statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.total = PR_FLOWTOTAL(conn, module_id, port_id, flow_index)
        """RX statistics of a flow.
        Representation of PR_FLOWTOTAL
        """

        self.clear = PR_FLOWCLEAR(conn, module_id, port_id, flow_index)
        """Clear RX statistics of a flow.
        Representation of PR_FLOWCLEAR
        """
