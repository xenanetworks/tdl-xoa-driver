from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .ctlos import UecCtlOs
from .linkneg import LinkNeg
from .llr import UecLlr

class UltraEthernet:
    """Ultra Ethernet of the port"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.ctlos = UecCtlOs(conn, module_id, port_id)
        """UE CtlOS (Control and Observation System) of the port.

        :type: UecCtlOs
        """

        self.linkneg = LinkNeg(conn, module_id, port_id)
        """UE Link Negotiation of the port.

        :type: LinkNeg
        """

        self.llr = UecLlr(conn, module_id, port_id)
        """UE LLR (Link Layer Retry) of the port.

        :type: UecLlr
        """