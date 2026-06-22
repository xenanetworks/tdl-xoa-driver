from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)

from xoa_driver.internals.commands import (
    PP_PRBSTYPE,
    PP_LINKTRAINSTATUS,
    PL1_PCS_VARIANT,
)
from .prbs import Prbs
from .pcs import PcsLayer, FecCodewordErrorInject
from .impair import Impair
from .medium import BasicMedium
from .rs_fault import RsFault
from .anlt import AnltBasic
from ..tcvr.transceiver import Transceiver

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ..family_thor2 import FamilyThor2
    
class SerDesThor:
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

        self.lt_status = PP_LINKTRAINSTATUS(conn, module_id, port_id, serdes_xindex)
        """Link Training status on serdes level (Basic ANLT)

        :type: PP_LINKTRAINSTATUS
        """

class Thor2PcsLayer(PcsLayer):
    """Thor2 PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port: "FamilyThor2") -> None:
        module_id, port_id = port.kind
        PcsLayer.__init__(self, conn, port)
    
        self.variant = PL1_PCS_VARIANT(conn, module_id, port_id)
        """PCS variant configuration
        """

        self.fec_error_inject = FecCodewordErrorInject(conn, module_id, port_id)
        """FEC codeword error injection
        """
        

class Layer1:
    def __init__(self, conn: "itf.IConnection", port: "FamilyThor2") -> None:
        module_id, port_id = port.kind
        self.serdes: Tuple[SerDesThor, ...] = tuple(
                SerDesThor(conn, module_id, port_id, serdes_xindex=idx)
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

        self.pcs = Thor2PcsLayer(conn, port)
        """PCS/FEC layer
        
        :type: Thor2PcsLayer
        """

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).

        :type: PP_PRBSTYPE
        """
        
        self.anlt = AnltBasic(conn, module_id, port_id)
        """Basic ANLT. For per-serdes configuration and status, use serdes[x].

        Same as anlt_basic. For backward compatibility.

        :type: AnltBasic
        """
        
        self.transceiver = Transceiver(conn, module_id, port_id)
        """Thor Transceiver configuration and status

        :type: Transceiver
        """

        self.anlt_basic = AnltBasic(conn, module_id, port_id)
        """Basic ANLT. For per-serdes configuration and status, use serdes[x].

        :type: AnltBasic
        """