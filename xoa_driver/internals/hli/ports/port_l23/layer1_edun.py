from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PRECODING,
    PP_GRAYCODING,
    PL1_PHYTXEQ_LEVEL,
    PL1_PHYTXEQ_COEFF,
    PL1_PCS_VARIANT,
    PL1_PHYTXEQ,
    PL1_CWE_CYCLE,
    PL1_CWE_ERR_SYM_INDICES,
    PL1_CWE_BIT_ERR_MASK,
    PL1_CWE_FEC_ENGINE,
    PL1_CWE_FEC_STATS,
    PL1_CWE_CONTROL,
    PL1_CWE_FEC_STATS_CLEAR,
    PP_PRBSTYPE,
    PL1_PNSWAP_RX,
    PL1_PNSWAP_TX,
    PP_AUTONEG,
    PP_AUTONEGSTATUS,
    PP_LINKTRAIN,
    PP_LINKTRAINSTATUS,
)
from xoa_driver import enums
from .layer1.pcs_fec import PcsLayer, FreyaFecCodewordErrorInject
from .layer1.prbs import Prbs
from .layer1.pma import FreyaPMA
from .layer1.medium import EdunMedium
from .layer1.rs_fault import RsFault
from .tvcr.transceiver import Transceiver
from .tvcr.cmis import Cmis
from .layer1.anlt import AnltBasic



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

class EdunPcsLayer(PcsLayer):
    """Edun PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port) -> None:
        PcsLayer.__init__(self, conn, port)
    
        self.pcs_variant = PL1_PCS_VARIANT(conn, *port.kind)
        """PCS variant configuration
        """

        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, *port.kind)
        """FEC codeword error injection
        """

class EdunTransceiver(Transceiver):
    """Edun Transceiver configuration and status
    """

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int,) -> None:
        Transceiver.__init__(self, conn, module_id, port_id)

        self.cmis = Cmis(conn, module_id, port_id)
        """CMIS transceiver configuration and status
        """

class Layer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.serdes: Tuple[SerDesEdun, ...] = tuple(
                SerDesEdun(conn, *port.kind, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        
        self.rs_fault = RsFault(conn, *port.kind)
        """RS Fault configuration and status
        """

        self.pcs_fec = EdunPcsLayer(conn, port)
        """Edun PCS and FEC configuration and status
        """

        self.prbs_config = PP_PRBSTYPE(conn, *port.kind)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """

        self.anlt = AnltBasic(conn, *port.kind)
        """Edun ANLT settings
        """

        self.transceiver = EdunTransceiver(conn, *port.kind)
        """Edun Transceiver configuration and status
        """
        
        
