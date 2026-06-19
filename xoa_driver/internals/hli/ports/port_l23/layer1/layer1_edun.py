from typing import (
    TYPE_CHECKING,
    Tuple,
)

from xoa_driver.internals.commands import (
    PL1_PCS_VARIANT,
    PP_PRBSTYPE,
    PP_LINKTRAINSTATUS,
)
from .pcs import PcsLayer, FecCodewordErrorInject
from .impair import Impair
from .prbs import Prbs
from .pma import FreyaPMA
from .medium import EdunMedium
from .rs_fault import RsFault
from ..tcvr.transceiver import Transceiver
from .anlt import AnltBasic
from .siv import FreyaSIV

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ..family_edun import FamilyEdun


class SerDesEdun:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: Prbs
        """
        
        self.pma = FreyaPMA(conn, module_id, port_id, serdes_xindex)
        """Edun PMA

        :type: FreyaPMA
        """

        self.medium = EdunMedium(conn, module_id, port_id, serdes_xindex)
        """Edun medium

        :type: EdunMedium
        """

        self.lt_status = PP_LINKTRAINSTATUS(conn, module_id, port_id, serdes_xindex)
        """Basic ANLT - Link Training status on serdes level

        :type: PP_LINKTRAINSTATUS
        """

        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Signal Integrity
        """

class EdunPcsLayer(PcsLayer):
    """Edun PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port: "FamilyEdun") -> None:
        module_id, port_id = port.kind
        PcsLayer.__init__(self, conn, port)
    
        self.variant = PL1_PCS_VARIANT(conn, module_id, port_id)
        """PCS variant configuration
        """

        self.fec_error_inject = FecCodewordErrorInject(conn, module_id, port_id)
        """FEC codeword error injection
        """

class Layer1:
    def __init__(self, conn: "itf.IConnection", port: "FamilyEdun") -> None:
        module_id, port_id = port.kind
        self.serdes: Tuple[SerDesEdun, ...] = tuple(
                SerDesEdun(conn, module_id, port_id, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        
        self.impairment = Impair(conn, module_id, port_id)
        """Impairment functions
        
        :type: Impair
        """

        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault configuration and status

        :type: RsFault
        """

        self.pcs = EdunPcsLayer(conn, port)
        """Edun PCS and FEC configuration and status

        :type: EdunPcsLayer
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
        """Edun Transceiver configuration and status

        :type: Transceiver
        """

        self.anlt_basic = AnltBasic(conn, module_id, port_id)
        """Basic ANLT. For per-serdes configuration and status, use serdes[x].

        :type: AnltBasic
        """
        
        
