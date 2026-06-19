from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)

from xoa_driver.internals.commands import (
    PP_PRBSTYPE,
)
from .prbs import Prbs
from .pcs import PcsLayer
from .impair import Impair
from .medium import BasicMedium
from .eye_diagram import EyeDiagram
from .rs_fault import RsFault
from ..tcvr.transceiver import Transceiver

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ..family_loki import FamilyLoki
    
class SerDesLoki:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS on SerDes level

        :type: Prbs
        """

        self.medium = BasicMedium(conn, module_id, port_id, serdes_xindex)
        """Basic medium

        :type: BasicMedium
        """

        self.eye_diagram = EyeDiagram(conn, module_id, port_id, serdes_xindex)
        """Eye diagram

        :type: EyeDiagram
        """
    
    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> Self:
        await self.eye_diagram
        return self


class Layer1:
    def __init__(self, conn: "itf.IConnection", port: "FamilyLoki") -> None:
        module_id, port_id = port.kind
        self.serdes: Tuple[SerDesLoki, ...] = tuple(
                SerDesLoki(conn, module_id, port_id, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        
        self.impairment = Impair(conn, module_id, port_id)
        """Impairment functions
        
        :type: Impair
        """

        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault Management
        
        :type: RsFault
        """

        self.pcs = PcsLayer(conn, port)
        """PCS/FEC layer
        
        :type: PcsLayer
        """

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        
        :type: PP_PRBSTYPE
        """
        
        self.transceiver = Transceiver(conn, module_id, port_id)
        """Loki Transceiver configuration and status

        :type: Transceiver
        """