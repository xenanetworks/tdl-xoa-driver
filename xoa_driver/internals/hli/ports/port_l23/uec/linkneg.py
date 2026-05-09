from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_UE_LINKNEG_OPTIONS,
    P_UE_LINKNEG_OPTIONS_STATUS,
)

class LinkNeg:
    """UE Link Negotiation of the port"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.link_options = LinkNegLinkOptions(conn, module_id, port_id)
        """UE Link Negotiation link options of the port.

        :type: LinkNegLinkOptions
        """

class LinkNegLinkOptions:
    """UE Link Negotiation link options"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.config = P_UE_LINKNEG_OPTIONS(conn, module_id, port_id)
        """UE Link Negotiation link options.

        :type: P_UE_LINKNEG_OPTIONS
        """

        self.status = P_UE_LINKNEG_OPTIONS_STATUS(conn, module_id, port_id)
        """UE Link Negotiation link options status.

        :type: P_UE_LINKNEG_OPTIONS_STATUS
        """