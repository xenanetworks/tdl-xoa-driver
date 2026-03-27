from typing import (
    TYPE_CHECKING,
    Tuple,
    Union,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya
    from xoa_driver.internals.hli.ports.port_l23.family_edun import FamilyEdun

from xoa_driver.internals.commands import (
    PP_RXLANESTATUS,
    PL1_LOA_STATUS,
    PL1_HIBER_STATUS,
    PL1_HISER_STATUS,
    PL1_HISER_ALARM,
    PL1_DEGSER_STATUS,
    PL1_DEGSER_THRESH,
    PL1_LINKDOWN_STATUS,
    PL1_RX_CNT,
    PL1_INJECT_ERR,
    PL1_INJECT_ERR_CNT,
)


class PcsLaneAdv:
    """PCS Lane Advanced Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:

        self.pcsl_skew = PP_RXLANESTATUS(conn, module_id, port_id, lane_idx)
        """Returns the PCSL and current Rx relative skew of the PCS lane measured in bits.

        :type: PP_RXLANESTATUS
        """


class HighBer:
    """High Bit Error Rate (BER) Alarm"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1_HIBER_STATUS(conn, module_id, port_id)
        """Returns the current and the latched High BER status of the port.
        
        :type: PL1_HIBER_STATUS
        """


class HighSer:
    """High Symbol Error Rate (SER) Alarm"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1_HISER_STATUS(conn, module_id, port_id)
        """Returns the current and the latched High SER status of the port.
        
        :type: PL1_HISER_STATUS
        """

        self.alarm = PL1_HISER_ALARM(conn, module_id, port_id)
        """High SER Alarm management.

        :type: PL1_HISER_ALARM
        """

        
class DegradedSer:
    """Degraded Symbol Error Rate (SER) Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.threshold = PL1_DEGSER_THRESH(conn, module_id, port_id)
        """Configures the thresholds for the Degraded SER Alarm.
        
        :type: PL1_DEGSER_THRESH
        """

        self.status = PL1_DEGSER_STATUS(conn, module_id, port_id)
        """The current and latched Degraded SER status of the port.
        
        :type: PL1_DEGSER_STATUS
        """

class LossOfAlignment:
    """Loss of Alignment (LOA) Status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1_LOA_STATUS(conn, module_id, port_id)
        """Returns the current and the latched Loss of Alignment (LOA) status of the port.
        
        :type: PL1_LOA_STATUS
        """


class LinkDown:
    """Link Down Status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.status = PL1_LINKDOWN_STATUS(conn, module_id, port_id)
        """Returns the current and the latched Link Down status of the port.
        
        :type: PL1_LINKDOWN_STATUS
        """


class ErrorInjection:
    """Error Injection Management"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.inject = PL1_INJECT_ERR(conn, module_id, port_id)
        """Error Injection management

        :type: PL1_INJECT_ERR
        """

        self.tx_cnt = PL1_INJECT_ERR_CNT(conn, module_id, port_id)
        """Returns the count of injected errors.

        :type: PL1_INJECT_ERR_CNT
        """

        self.rx_cnt = PL1_RX_CNT(conn, module_id, port_id)
        """Returns the count of received errors.

        :type: PL1_RX_CNT
        """

class PcsLayerAdv:
    """Adv. Layer-1 - PCS layer configuration and status."""

    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya | FamilyEdun") -> None:
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

        # self.rx_stats = PL1_RX_CNT(conn, module_id, port_id)
        # """Returns the Rx statistics counters of the port.

        # :type: PL1_RX_CNT
        # """

        self.deg_ser = DegradedSer(conn, module_id, port_id)
        """Degraded Symbol Error Rate (SER) Management

        :type: DegradedSer
        """

        self.hi_ber = HighBer(conn, module_id, port_id)
        """High Bit Error Rate (BER)

        :type: HighBer
        """

        self.hi_ser = HighSer(conn, module_id, port_id)
        """High Symbol Error Rate (SER)

        :type: HighSer
        """

        # self.tx_err_inject = PL1_INJECT_ERR(conn, module_id, port_id)
        # """Error Injection management

        # :type: PL1_INJECT_ERR
        # """ 

        self.link_down = LinkDown(conn, module_id, port_id)
        """Link Down Status

        :type: LinkDown
        """

        self.err_inject = ErrorInjection(conn, module_id, port_id)
        """Error Injection management

        :type: ErrorInjection
        """
