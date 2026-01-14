from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_edun import FamilyEdun
from xoa_driver.internals.commands import (
    PL1_PCS_VARIANT,
    PP_PRBSTYPE,
    PP_LINKTRAINSTATUS,
)
from .layer1.pcs_fec import PcsLayer, FreyaFecCodewordErrorInject
from .layer1.impair import Impair
from .layer1.prbs import Prbs
from .layer1.pma import FreyaPMA
from .layer1.medium import EdunMedium
from .layer1.rs_fault import RsFault
from .tcvr.transceiver import Transceiver
from .layer1.anlt import AnltBasic
from .layer1.siv import FreyaSIV



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
        """LT status for Edun
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

        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, module_id, port_id)
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
        """Impairment functions"""

        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault configuration and status
        """

        self.pcs = EdunPcsLayer(conn, port)
        """Edun PCS and FEC configuration and status
        """

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """

        self.anlt = AnltBasic(conn, module_id, port_id)
        """Edun ANLT settings
        """

        self.transceiver = Transceiver(conn, module_id, port_id)
        """Edun Transceiver configuration and status
        """
        
        
