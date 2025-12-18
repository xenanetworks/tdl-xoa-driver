from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .layer1.prbs import Prbs
from .layer1.pcs_fec import PcsLayer
from .layer1.impair import Impair
from .layer1.medium import BasicMedium
from .layer1.eye_diagram import EyeDiagram
from .layer1.rs_fault import RsFault
from .tvcr.transceiver import Transceiver
from .tvcr.cmis import Cmis
from xoa_driver import enums

from xoa_driver.internals.commands import (
    PP_PRBSTYPE,
)

class SerDesThor:
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

class Layer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.serdes: Tuple[SerDesThor, ...] = tuple(
                SerDesThor(conn, *port.kind, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        
        self.impairment = Impair(conn, port)
        """Impairment functions"""

        self.rs_fault = RsFault(conn, *port.kind)
        """RS Fault Management"""

        self.pcs_fec = PcsLayer(conn, port)
        """PCS/FEC layer"""

        self.prbs_config = PP_PRBSTYPE(conn, *port.kind)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """
        
        self.transceiver = Transceiver(conn, *port.kind)
        """Thor Transceiver configuration and status
        """