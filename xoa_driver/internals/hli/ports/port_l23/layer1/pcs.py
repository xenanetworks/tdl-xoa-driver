from typing import (
    TYPE_CHECKING,
    Tuple,
    Union,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_edun import FamilyEdun
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya
    from xoa_driver.internals.hli.ports.port_l23.family_loki import FamilyLoki
    from xoa_driver.internals.hli.ports.port_l23.family_thor import FamilyThor
from xoa_driver.internals.commands import (
    PP_ALARMS_ERRORS,
    PP_TXLANECONFIG,
    PP_TXLANEINJECT,
    PP_TXERRORRATE,
    PP_TXINJECTONE,
    PP_RXTOTALSTATS,
    PP_RXFECSTATS,
    PP_RXLANELOCK,
    PP_RXLANESTATUS,
    PP_RXLANEERRORS,
    PP_RXCLEAR,
    PP_FECMODE,
    PL1_CWE_CYCLE,
    PL1_CWE_ERR_SYM_INDICES,
    PL1_CWE_BIT_ERR_MASK,
    PL1_CWE_FEC_ENGINE,
    PL1_CWE_FEC_STATS,
    PL1_CWE_CONTROL,
    PL1_CWE_FEC_STATS_CLEAR,
)
from xoa_driver import enums


class PcsAlarms:
    """L23 high-speed port PCS/PMA alarms"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.errors = PP_ALARMS_ERRORS(conn, module_id, port_id)
        """Error count of each alarm on a L23 high-speed port.

        :type: PP_ALARMS_ERRORS
        """


class PcsFecLaneStatus:
    """PCS/FEC lane status"""

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


class PcsErrorGeneration:
    """PCS/FEC TX error generation."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.error_rate = PP_TXERRORRATE(conn, module_id, port_id)
        """The rate of continuous bit-level error injection.

        :type: PP_TXERRORRATE
        """

        self.inject_one = PP_TXINJECTONE(conn, module_id, port_id)
        """Inject a single bit-level error.

        :type: PP_TXINJECTONE
        """


class PcsFecSymbolStatus:
    """PCS/FEC RX symbol status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.total_status = PP_RXTOTALSTATS(conn, module_id, port_id)
        """RX FEC total counters.

        :type: PP_RXTOTALSTATS
        """

        self.fec_status = PP_RXFECSTATS(conn, module_id, port_id)
        """RX FEC statistics.

        :type: PP_RXFECSTATS
        """


# class PcsPmaPhy:
#     """L23 high-speed port PCS/PMA PHY settings."""

#     def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
#         self.auto_neg = PP_PHYAUTONEG(conn, module_id, port_id)
#         """ Auto-negotiation settings of the PHY.

#         :type: PP_PHYAUTONEG
#         """

#         self.signal_status = PP_PHYSIGNALSTATUS(conn, module_id, port_id)
#         """The PHY signal status.

#         :type: PP_PHYSIGNALSTATUS
#         """

#         self.settings = PP_PHYSETTINGS(conn, module_id, port_id)
#         """Low-level PHY settings

#         :type: PP_PHYSETTINGS
#         """


class PcsLane:
    """PCS lane configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, lane_idx: int) -> None:
        self.rx_status = PcsFecLaneStatus(conn, module_id, port_id, lane_idx)
        """PCS/PMA RX lane status.
        """

        self.tx_error_inject = PP_TXLANEINJECT(conn, module_id, port_id, lane_idx)
        """Inject CAUI error into a TX lane.

        :type: PP_TXLANEINJECT
        """

        self.tx_config = PP_TXLANECONFIG(conn, module_id, port_id, lane_idx)
        """TX lane configuration.

        :type: PP_TXLANECONFIG
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

class PcsLayer:
    """PCS/FEC layer configuration and status."""

    def __init__(self, conn: "itf.IConnection", port: "Union[FamilyLoki, FamilyThor, FamilyFreya, FamilyEdun]") -> None:
        self._conn = conn
        self.__port = port
        module_id, port_id = port.kind

        self.alarms = PcsAlarms(conn, module_id, port_id)
        """PCS alarms

        :type: PcsAlarms
        """

        self.error_gen = PcsErrorGeneration(conn, module_id, port_id)
        """Error generation

        :type: PcsPmaTxErrorGeneration
        """

        self.fec_symbol_status = PcsFecSymbolStatus(conn, module_id, port_id)
        """Rx FEC symbol status

        :type: FecSymbolStatus
        """

        self.clear = PP_RXCLEAR(conn, module_id, port_id)
        """Clear all the PCS receiver statistics.

        :type: PP_RXCLEAR
        """

        self.fec_mode = PP_FECMODE(conn, module_id, port_id)
        """FEC mode configuration.

        :type: PP_FECMODE
        """

        self.lane: Tuple["PcsLane", ...] = tuple(
            PcsLane(self._conn, module_id, port_id, lane_idx=idx)
            for idx in range(self.__port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because lanes are created before awaiting the port
        """PCS Lane
        
        :type: Tuple[PcsLane, ...]
        """
