from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums

#region Port-level
class PCSErrorAlarm:
    """L23 high-speed port PCS/PMA alarms"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.errors = PP_ALARMS_ERRORS(conn, module_id, port_id)
        """Error count of each alarm on a L23 high-speed port.

        :type: PP_ALARMS_ERRORS
        """

class FECStatistics:
    """L23 high-speed port PCS/PMA RX"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.total = PP_RXTOTALSTATS(conn, module_id, port_id)
        """RX FEC total counters.

        :type: PP_RXTOTALSTATS
        """

        self.sym_err_dist = PP_RXFECSTATS(conn, module_id, port_id)
        """RX FEC symbol error distribution.

        :type: PP_RXFECSTATS
        """

        


class FreyaFecCodewordErrorInject:
    """Freya FEC Codeword Error Injection
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.cycle = PL1_CWE_CYCLE(conn, module_id, port_id)
        """FEC codeword error injection cycle.
        """
        self.err_symbols = PL1_CWE_ERR_SYM_INDICES(conn, module_id, port_id)
        """The positions of the errored symbols in errored codewords.
        """
        self.bit_err_mask = PL1_CWE_BIT_ERR_MASK(conn, module_id, port_id)
        """The bit error mask for the errored symbols.
        """
        self.engine = PL1_CWE_FEC_ENGINE(conn, module_id, port_id)
        """The FEC engines to use.
        """
        self.statistics = PL1_CWE_FEC_STATS(conn, module_id, port_id)
        """FEC error injection statistics
        """
        self.clear_stats = PL1_CWE_FEC_STATS_CLEAR(conn, module_id, port_id)
        """Clear FEC codeword injection stats
        """
        self.control = PL1_CWE_CONTROL(conn, module_id, port_id)
        """Control the FEC codeword error injection
        """

#endregion

#region Lane-level
class PCSLaneStatus:
    """L23 high-speed port PCS/PMA lane status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.errors = PP_RXLANEERRORS(conn, module_id, port_id, lane_idx)
        """RX lane error statistics.

        :type: PP_RXLANEERRORS
        """

        self.lock = PP_RXLANELOCK(conn, module_id, port_id, lane_idx)
        """RX lane lock.

        :type: PP_RXLANELOCK
        """

        self.status = PP_RXLANESTATUS(conn, module_id, port_id, lane_idx)
        """RX lane status

        :type: PP_RXLANESTATUS
        """

class PCSLane:
    """L23 high-speed port lane configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_xindex: int) -> None:
        self.rx_status = PCSLaneStatus(conn, module_id, port_id, lane_xindex)
        """PCS/PMA RX lane status.
        """

        self.tx_error_inject = PP_TXLANEINJECT(conn, module_id, port_id, lane_xindex)
        """Inject CAUI error into a TX lane.

        :type: PP_TXLANEINJECT
        """

        self.tx_config = PP_TXLANECONFIG(conn, module_id, port_id, lane_xindex)
        """TX lane configuration.

        :type: PP_TXLANECONFIG
        """
#endregion



