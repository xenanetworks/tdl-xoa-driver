from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PRECODING,
    PP_GRAYCODING,
    PL1_AUTONEGINFO,
    PL1_LINKTRAININFO,
    PL1_LOG,
    PL1_CFG_TMP,
    PL1_LINKTRAIN_CMD,
    PL1_CTRL,
    PL1_GET_DATA,
    PL1_PHYTXEQ_LEVEL,
    PL1_PHYTXEQ_COEFF,
    PL1_AUTONEG_STATUS,
    PL1_AUTONEG_ABILITIES,
    PL1_PCS_VARIANT,
    PL1_AUTONEG_CONFIG,
    PL1_ANLT,
    PL1_PHYTXEQ,
    PL1_LINKTRAIN_CONFIG,
    PL1_LINKTRAIN_STATUS,
    PP_PHYRXEQ_EXT,
    PP_PHYRXEQSTATUS_EXT,
    PL1_CWE_CYCLE,
    PL1_CWE_ERR_SYM_INDICES,
    PL1_CWE_BIT_ERR_MASK,
    PL1_CWE_FEC_ENGINE,
    PL1_CWE_FEC_STATS,
    PL1_CWE_CONTROL,
    PL1_CWE_FEC_STATS_CLEAR,
    PL1_LT_PHYTXEQ_RANGE,
    PL1_LT_PHYTXEQ_RANGE_COEFF,
    PL1_PRESET_CONFIG,
    PL1_PRESET_CONFIG_COEFF,
    PL1_PRESET_CONFIG_LEVEL,
    PL1_PRESET_RESET,
    PP_PRBSTYPE,
    PL1_PNSWAP_RX,
    PL1_PNSWAP_TX,
)
from xoa_driver import enums

from .layer1.prbs import Prbs
from .layer1.impair import Impair
from .layer1.pcs_fec import PcsLayer, FreyaFecCodewordErrorInject
from .tvcr.transceiver import Transceiver
from .tvcr.cmis import Cmis
from .layer1.rs_fault import RsFault
from .layer1.medium import FreyaMedium
from .layer1.siv import FreyaSIV
from .layer1.pma import FreyaPMA
from .layer1.anlt import FreyaAnlt, FreyaLinkTraining


class SerDesFreya:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: Prbs
        """
        
        self.pma = FreyaPMA(conn, module_id, port_id, serdes_xindex)
        """Freya PMA

        :type: FreyaPMA
        """

        self.medium = FreyaMedium(conn, module_id, port_id, serdes_xindex)
        """Freya medium

        :type: FreyaMedium
        """

        self.lt = FreyaLinkTraining(conn, module_id, port_id, serdes_xindex)
        """Freya Link Training on serdes level

        :type: FreyaLinkTraining
        """

        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Freya Signal Integrity
        """

        
class FreyaPcsLayer(PcsLayer):
    """Freya PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port) -> None:
        PcsLayer.__init__(self, conn, port)
    
        self.pcs_variant = PL1_PCS_VARIANT(conn, *port.kind)
        """PCS variant configuration
        """

        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, *port.kind)
        """FEC codeword error injection
        """
    
class Layer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.serdes: Tuple[SerDesFreya, ...] = tuple(
                SerDesFreya(conn, *port.kind, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        
        self.impairment = Impair(conn, *port.kind)
        """Impairment functions
        """
        
        self.rs_fault = RsFault(conn, *port.kind)
        """RS Fault configuration and status
        """

        self.pcs_fec = FreyaPcsLayer(conn, port)
        """Freya PCS and FEC configuration and status
        """

        self.prbs_config = PP_PRBSTYPE(conn, *port.kind)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """

        self.anlt = FreyaAnlt(conn, *port.kind)
        """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
        """
        
        self.transceiver = Transceiver(conn, *port.kind)
        """Freya Transceiver configuration and status
        """
        