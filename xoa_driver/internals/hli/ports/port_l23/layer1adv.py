from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya
    from xoa_driver.internals.hli.ports.port_l23.family_edun import FamilyEdun
    
from xoa_driver.internals.commands import (
    PL1_CLEAR,
    PL1_CDRLOL_STATUS,
    PL1_RX_FREQ,
    PL1_TX_FREQ,
    PL1_RX_DATARATE,
    PL1_TX_DATARATE,
    PL1_RX_PPM,
    PL1_TX_PPM,
)

from .layer1_adv.pcs import PcsLayerAdv

class SerdesAdv:
    """Serdes Advanced Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_idx: int) -> None:

        self.rx_cdr_lol = PL1_CDRLOL_STATUS(conn, module_id, port_id, serdes_idx)
        """Returns the current and the latched CDR Loss of Lock (LOL) status of the specified Serdes.

        :type: PL1_CDRLOL_STATUS
        """
        
        self.rx_freq = PL1_RX_FREQ(conn, module_id, port_id, serdes_idx)
        """Return the current, minimum and maximum port Rx frequency in Hz of the specified SerDes.
        
        :type: PL1_RX_FREQ
        """

        self.rx_ppm = PL1_RX_PPM(conn, module_id, port_id, serdes_idx)
        """Return the current, minimum and maximum port Rx frequency offset in parts per million (ppm) of the specified SerDes.

        :type: PL1_RX_PPM
        """

        self.rx_datarate = PL1_RX_DATARATE(conn, module_id, port_id, serdes_idx)
        """Return the current, minimum and maximum port Rx datarate in bits per second (bps) of the specified SerDes.

        :type: PL1_RX_DATARATE
        """


class Layer1Adv:
    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya | FamilyEdun") -> None:
        module_id, port_id = port.kind

        self.serdes: Tuple["SerdesAdv", ...] = tuple(
            SerdesAdv(conn, module_id, port_id, serdes_idx=idx)
            for idx in range(port.info.capabilities.serdes_count)
        ) 
        """SerDes Lane
        
        :type: Tuple[SerdesAdv, ...]
        """

        self.tx_freq = PL1_TX_FREQ(conn, module_id, port_id)
        """Return the current, minimum and maximum port Tx frequency in Hz.

        :type: PL1_TX_FREQ
        """

        self.tx_ppm = PL1_TX_PPM(conn, module_id, port_id)
        """Return the current, minimum and maximum port Tx frequency offset in parts per million (ppm).

        :type: PL1_TX_PPM
        """

        self.tx_datarate = PL1_TX_DATARATE(conn, module_id, port_id)
        """Return the current, minimum and maximum port Tx datarate in bits per second (bps).

        :type: PL1_TX_DATARATE
        """

        self.pcs = PcsLayerAdv(conn, port)
        """PCS configuration and status

        :type: PcsLayerAdv
        """

        self.clear = PL1_CLEAR(conn, module_id, port_id)
        """Clear Layer 1 advanced statistics counters on the port.

        :type: PL1_CLEAR
        """


        