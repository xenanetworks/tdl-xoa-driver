from typing import (
    TYPE_CHECKING,
    Tuple,
)

from xoa_driver.internals.commands import (
    PL1_PCS_VARIANT,
    PP_PRBSTYPE,
    PP_LINKTRAINSTATUS,
)
from .prbs import Prbs
from .impair import Impair
from .pcs import PcsLayer, FecCodewordErrorInject
from ..tcvr.transceiver import Transceiver
from .rs_fault import RsFault
from .medium import FreyaMedium
from .siv import FreyaSIV
from .pma import FreyaPMA
from .anlt import AnltAdvanced, LinkTrainingAdvanced, AnltBasic

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ..family_freya import FamilyFreya

class SerDesFreya:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: Prbs
        """
        
        self.pma = FreyaPMA(conn, module_id, port_id, serdes_xindex)
        """PMA

        :type: FreyaPMA
        """

        self.medium = FreyaMedium(conn, module_id, port_id, serdes_xindex)
        """Medium

        :type: FreyaMedium
        """

        self.lt = LinkTrainingAdvanced(conn, module_id, port_id, serdes_xindex)
        """Advanced ANLT - Link Training on serdes level

        Same as lt_adv, for backward compatibility.

        :type: LinkTrainingAdvanced
        """

        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Signal Integrity

        :type: FreyaSIV
        """


        self.lt_adv = LinkTrainingAdvanced(conn, module_id, port_id, serdes_xindex)
        """Advanced ANLT - Link Training on serdes level

        :type: LinkTrainingAdvanced
        """

        self.lt_status = PP_LINKTRAINSTATUS(conn, module_id, port_id, serdes_xindex)
        """Basic ANLT - Link Training status on serdes level

        :type: PP_LINKTRAINSTATUS
        """
        
class FreyaPcsLayer(PcsLayer):
    """Freya PCS and FEC configuration and status
    """

    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        module_id, port_id = port.kind
        PcsLayer.__init__(self, conn, port)
    
        self.variant = PL1_PCS_VARIANT(conn, module_id, port_id)
        """PCS variant configuration

        :type: PL1_PCS_VARIANT
        """

        self.fec_error_inject = FecCodewordErrorInject(conn, module_id, port_id)
        """FEC codeword error injection

        :type: FreyaFecCodewordErrorInject
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

        :type: Impair
        """
        
        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault configuration and status

        :type: RsFault
        """

        self.pcs = FreyaPcsLayer(conn, port)
        """Freya PCS and FEC configuration and status

        :type: FreyaPcsLayer
        """

        self.prbs_config = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).

        :type: PP_PRBSTYPE
        """

        self.anlt = AnltAdvanced(conn, module_id, port_id)
        """Advanced ANLT. For per-serdes configuration and status, use serdes[x]

        Same as anlt_adv, for backward compatibility.

        :type: AnltAdvanced
        """
        
        self.transceiver = Transceiver(conn, module_id, port_id)
        """Freya Transceiver configuration and status.

        :type: Transceiver
        """

        self.anlt_basic = AnltBasic(conn, module_id, port_id)
        """Basic ANLT. For per-serdes configuration and status, use serdes[x].

        :type: AnltBasic
        """

        self.anlt_adv = AnltAdvanced(conn, module_id, port_id)
        """Advanced ANLT. For per-serdes configuration and status, use serdes[x].

        :type: AnltAdvanced
        """

        