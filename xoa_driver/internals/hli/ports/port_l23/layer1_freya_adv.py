from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya
    
from xoa_driver.internals.commands import (
    PL1AD_RX_LOL,
)

from .layer1_adv.freq import FrequencyAdv
from .layer1_adv.pcs_fec import PcsLayerAdv
from .layer1_adv.rs_fault import *

class SerdesAdv:
    """Serdes Advanced Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_idx: int) -> None:

        self.rx_cdr_lol_since_last = PL1AD_RX_LOL(conn, module_id, port_id, serdes_idx)
        """Returns the current and the latched CDR Loss of Lock (LOL) status of the specified Serdes.

        :type: PL1AD_RX_LOL
        """


class Layer1Adv:
    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        module_id, port_id = port.kind

        self.serdes: Tuple["SerdesAdv", ...] = tuple(
            SerdesAdv(conn, module_id, port_id, serdes_idx=idx)
            for idx in range(port.info.capabilities.serdes_count)
        ) 
        """SerDes Lane
        
        :type: Tuple[SerdesAdv, ...]
        """

        self.freq = FrequencyAdv(conn, module_id, port_id)
        """Frequency Management

        :type: FrequencyAdv
        """

        self.rs_fault = RsFault(conn, module_id, port_id)
        """RS Fault Management

        :type: RsFault
        """

        self.pcs = PcsLayerAdv(conn, port)
        """PCS configuration and status
        """

        


        