from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_thor import FamilyThor
from xoa_driver.internals.commands import (
    PP_PRBSTYPE,
    PP_LINKTRAINSTATUS,
)
from .layer1.prbs import Prbs
from .layer1.pcs import PcsLayer
from .layer1.impair import Impair
from .layer1.medium import BasicMedium
from .layer1.rs_fault import RsFault
from .layer1.anlt import AnltBasic
from .tcvr.transceiver import Transceiver

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

class Layer1:
    def __init__(self, conn: "itf.IConnection", port: "FamilyThor") -> None:
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

        self.pcs = PcsLayer(conn, port)
        """PCS/FEC layer
        
        :type: PcsLayer
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