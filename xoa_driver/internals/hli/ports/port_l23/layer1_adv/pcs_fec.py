from typing import (
    TYPE_CHECKING,
    Tuple,
    Union,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya

from xoa_driver.internals.commands import (
    PL1AD_RX_HIBER,
    PL1AD_RX_HISER,
    PL1AD_RX_HISER_ALARM,
    PL1AD_RX_ITB_CNT,
    PL1AD_TX_ITB,
    PL1AD_RX_DEG_SER,
    PL1AD_RX_DEG_SER_THRESH,
    PL1AD_RX_ERR_CW_CNT,
    PL1AD_TX_ERR_CW,
    PL1AD_RX_SKEW,
    PL1AD_RX_LOA_CNT,
    PL1AD_RX_LOSYNC_CNT,
)


class PcsLaneAdv:
    """PCS Lane Advanced Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:

        self.rx_skew = PL1AD_RX_SKEW(conn, module_id, port_id, lane_idx)
        """Returns the current Rx relative skew of the PCS lane measured in bits.

        :type: PL1AD_RX_SKEW
        """

        # self.tx_skew = PL1AD_TX_SKEW(conn, module_id, port_id, lane_idx)
        # """Returns the current Tx relative skew of the PCS lane measured in bits.

        # :type: PL1AD_TX_SKEW
        # """


        # self.rx_loa_since_last = PL1AD_RX_LOA_CNT(conn, module_id, port_id, lane_idx)
        # """Returns the number of cumulated Loss of Alignment conditions on the PCS lane since last query

        # :type: PL1AD_RX_LOA_CNT
        # """

        # self.tx_loa = PL1AD_TX_LOA(conn, module_id, port_id, lane_idx)
        # """Sends a Loss of Alignment from the Tx lane immediately when called.
        
        # :type: PL1AD_TX_LOA
        # """



class HighBer:
    """High Bit Error Rate (BER) Alarm"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1AD_RX_HIBER(conn, module_id, port_id)
        """Returns the current and the latched High BER status of the port.
        
        :type: PL1AD_RX_HIBER
        """


class HighSer:
    """High Symbol Error Rate (SER) Alarm"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1AD_RX_HISER(conn, module_id, port_id)
        """Returns the current and the latched High SER status of the port.
        
        :type: PL1AD_RX_HISER
        """

        self.alarm = PL1AD_RX_HISER_ALARM(conn, module_id, port_id)
        """High SER Alarm management.

        :type: PL1AD_RX_HISER_ALARM
        """

        # self.tx_hi_ser = PL1AD_TX_HISER(conn, module_id, port_id)
        # """Sends a High SER condition from the Tx port immediately when called.
        
        # :type: PL1AD_TX_HISER
        # """

        # self.state = PL1AD_RX_HISER_CTRL(conn, module_id, port_id)
        # """Enable or disable High SER detection.
        
        # :type: PL1AD_RX_HISER_CTRL
        # """

class InvalidTranscodeBlock:
    """Invalid Transcode Block (ITB) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_itb_since_last = PL1AD_RX_ITB_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Invalid 256b/257b Transcode Blocks since last query.
        
        :type: PL1AD_RX_ITB_CNT
        """

        self.tx_itb = PL1AD_TX_ITB(conn, module_id, port_id)
        """Sends an Invalid 256b/257b Transcode Block from the Tx port immediately when called.
        
        :type: PL1AD_TX_ITB
        """
        


class DegradedSer:
    """Degraded Symbol Error Rate (SER) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.threshold = PL1AD_RX_DEG_SER_THRESH(conn, module_id, port_id)
        """Configures the thresholds for the Degraded SER Alarm.
        
        :type: PL1AD_RX_DEG_SER_THRESH
        """

        self.status = PL1AD_RX_DEG_SER(conn, module_id, port_id)
        """The current and latched Degraded SER status of the port.
        
        :type: PL1AD_RX_DEG_SER
        """

        # self.state = PL1AD_RX_DEG_SER_STATE(conn, module_id, port_id)
        # """Enable or disable Degraded SER detection.
        
        # :type: PL1AD_RX_DEG_SER_STATE
        # """


class ErrorCodeword:
    """Erroneous Codeword (CW) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx_err_cw_since_last = PL1AD_RX_ERR_CW_CNT(conn, module_id, port_id)
        """Returns the number of cumulative erroneous 64b/66b codewords since last query.
        
        :type: PL1AD_RX_ERR_CW_CNT
        """

        self.tx_err_cw = PL1AD_TX_ERR_CW(conn, module_id, port_id)
        """Sends an error 64b/66b codeword from the Tx port immediately when called.
        
        :type: PL1AD_TX_ERR_CW
        """


class PcsLayerAdv:
    """Adv. Layer-1 - PCS layer configuration and status."""

    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        self._conn = conn
        self.__port = port
        module_id, port_id = port.kind

        self.lane: Tuple["PcsLaneAdv", ...] = tuple(
            PcsLaneAdv(self._conn, module_id, port_id, lane_idx=idx)
            for idx in range(self.__port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because lanes are created before awaiting the port
        """PCS Lane
        
        :type: Tuple[PcsLaneAdv, ...]
        """

        self.deg_ser = DegradedSer(conn, module_id, port_id)
        """Degraded Symbol Error Rate (SER) Management

        :type: DegradedSer
        """

        self.err_cw = ErrorCodeword(conn, module_id, port_id)
        """Erroneous Codeword (CW) Management

        :type: ErrorCodeword
        """

        self.hi_ber = HighBer(conn, module_id, port_id)
        """High Bit Error Rate (BER)

        :type: HighBer
        """

        self.hi_ser = HighSer(conn, module_id, port_id)
        """High Symbol Error Rate (SER)

        :type: HighSer
        """

        self.itb = InvalidTranscodeBlock(conn, module_id, port_id)
        """Invalid Transcode Block (ITB) Management

        :type: InvalidTranscodeBlock
        """

        self.rx_total_loa_since_last = PL1AD_RX_LOA_CNT(conn, module_id, port_id) # TODO: Suggestion for R106 GA: The name of the XMP command is preferred to be changed to PL1AD_RX_LOA_TOTAL_CNT 
        """Returns the number of cumulated Loss of Alignment conditions since last query of the port.

        :type: PL1AD_RX_LOA_CNT
        """

        self.rx_link_sync_loss_since_last = PL1AD_RX_LOSYNC_CNT(conn, module_id, port_id)
        """Returns the number of cumulated Loss of Sync conditions since last query.

        :type: PL1AD_RX_LOSYNC_CNT
        """

