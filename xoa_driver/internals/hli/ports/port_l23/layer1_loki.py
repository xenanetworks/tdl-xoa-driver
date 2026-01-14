from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_loki import FamilyLoki
from xoa_driver.internals.commands import (
    PP_PRBSTYPE,
)
from .layer1.prbs import Prbs
from .layer1.pcs_fec import PcsLayer
from .layer1.impair import Impair
from .layer1.medium import BasicMedium
from .layer1.eye_diagram import EyeDiagram
from .layer1.rs_fault import RsFault
from .tcvr.transceiver import Transceiver

class SerDesLoki:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS

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
        """Impairment functions"""

        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault Management"""

        self.pcs = PcsLayer(conn, port)
        """PCS/FEC layer"""

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """
        
        self.transceiver = Transceiver(conn, module_id, port_id)
        """Loki Transceiver configuration and status
        """