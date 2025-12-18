from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PL1_PCS_VARIANT,
    PP_PRBSTYPE,
)
from .layer1.prbs import Prbs
from .layer1.impair import Impair
from .layer1.pcs_fec import PcsLayer, FreyaFecCodewordErrorInject
from .tvcr.transceiver import Transceiver
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
        