from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya
from xoa_driver.internals.commands import (
    PL1_PCS_VARIANT,
    PP_PRBSTYPE,
)
from .layer1.prbs import Prbs
from .layer1.impair import Impair
from .layer1.pcs_fec import PcsLayer, FreyaFecCodewordErrorInject
from .tcvr.transceiver import Transceiver
from .layer1.rs_fault import RsFault
from .layer1.medium import FreyaMedium
from .layer1.siv import FreyaSIV
from .layer1.pma import FreyaPMA
from .layer1.anlt import AnltAdvanced, LinkTrainingAdvanced


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

        self.lt = LinkTrainingAdvanced(conn, module_id, port_id, serdes_xindex)
        """Freya Link Training on serdes level

        :type: FreyaLinkTraining
        """

        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Freya Signal Integrity
        """

        
class FreyaPcsLayer(PcsLayer):
    """Freya PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        module_id, port_id = port.kind
        PcsLayer.__init__(self, conn, port)
    
        self.variant = PL1_PCS_VARIANT(conn, module_id, port_id)
        """PCS variant configuration
        """

        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, module_id, port_id)
        """FEC codeword error injection
        """
    
class Layer1:
    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        module_id, port_id = port.kind

        self.serdes: Tuple[SerDesFreya, ...] = tuple(
                SerDesFreya(conn, module_id, port_id, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        """SerDes Lane
        
        :type: Tuple[SerDesFreya, ...]
        """
        
        self.impairment = Impair(conn, module_id, port_id)
        """Impairment functions
        """
        
        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault configuration and status
        """

        self.pcs = FreyaPcsLayer(conn, port)
        """Freya PCS and FEC configuration and status
        """

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """

        self.anlt = AnltAdvanced(conn, module_id, port_id)
        """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
        """
        
        self.transceiver = Transceiver(conn, module_id, port_id)
        """Freya Transceiver configuration and status
        """
        