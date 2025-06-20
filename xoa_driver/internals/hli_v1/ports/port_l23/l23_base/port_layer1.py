from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums

from .port_pcs_fec import *
from .port_prbs import *
from .port_rs import *
from .port_serdes import *
from .port_anlt import *
from .port_pma import *
from .port_rs import *
from .port_transceiver import *



class PhysicalCodingSublayer:
    """L23 high-speed port PCS/PMA"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port

        self.alarms = PCSErrorAlarm(conn, *port.kind)
        """PCS/PMA alarms

        :type: PcsPmaAlarms
        """

        self.fec_rx_stats = FECStatistics(conn, *port.kind)
        """PCS/PMA RX

        :type: PcsPmaRx
        """

        self.fec_error_inject = FreyaFecCodewordErrorInject(conn, *port.kind)
        """FEC codeword error injection

        :type: FreyaFecCodewordErrorInject
        """

        self.variant = PL1_PCS_VARIANT(conn, *port.kind)
        """PCS variant configuration
        
        :type: PL1_PCS_VARIANT
        """

        self.clear = PP_RXCLEAR(conn, *port.kind)
        """Clear all the PCS/PMA receiver statistics.

        :type: PP_RXCLEAR
        """
        
class PsedoRandomBitSequence:
    """L23 high-speed port PRBS"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port

        self.error_gen = PRBSErrorGen(conn, *port.kind)
        """PCS/PMA error generation

        :type: PcsPmaTxErrorGeneration
        """

        self.config = PP_PRBSTYPE(conn, *port.kind)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        
        :type: PP_PRBSTYPE
        """

        self.clear = PP_RXCLEAR(conn, *port.kind)
        """Clear all the PCS/PMA receiver statistics.

        :type: PP_RXCLEAR
        """


class ReconciliationSublayer:
    """L23 high-speed port RS"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port

        self.fault = Fault(conn, *port.kind)
        """RS fault status.

        :type: Fault
        """

class PhysicalMediumAttachment:
    """L23 high-speed port PMA"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self._conn = conn
        self.__port = port

        self.link_flap = LinkFlap(conn, *port.kind)
        """Link flap settings.
        
        :type: LinkFlap
        """

        self.error_inject = PMAErrorInject(conn, *port.kind)
        """PMA pulse error injection settings.

        :type: PMAErrorInject
        """

class PortLayer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:

        self.lanes: Tuple["PCSLane", ...] = tuple(
            PCSLane(conn, *port.kind, lane_xindex=idx)
            for idx in range(port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because lanes are created before awaiting the port


        self.serdes: Tuple[SerdesLane, ...] = tuple(
            SerdesLane(conn, *port.kind, serdes_xindex=idx)
            for idx in range(port.info.capabilities.serdes_count)
            )
        
        self.pcs = PhysicalCodingSublayer(conn, port)
        """PCS/PMA configuration and status.
        """

        self.prbs = PsedoRandomBitSequence(conn, port)
        """PRBS configuration and status.
        """

        self.rs = ReconciliationSublayer(conn, port)
        """RS configuration and status.
        """

        self.pma = PhysicalMediumAttachment(conn, port)
        """PMA configuration and status.
        """


        self.anlt = FreyaANLT(conn, *port.kind)
        """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
        """

        self.anlt_thor = ThorANLT(conn, *port.kind)
        """Thor port-level anlt. For per-serdes configuration and status, use serdes[x]
        """
        
        self.transceiver = PortTransceiver(conn, *port.kind)
        """L23 port transceiver configuration.

        :type: PortTransceiver
        """