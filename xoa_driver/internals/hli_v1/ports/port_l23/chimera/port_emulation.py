from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from xoa_driver.internals.commands import (
    PE_FCSDROP,
    PE_TPLDMODE,
    PE_COMMENT,
    PE_INDICES,
    PE_LATENCYRANGE,
    PE_CORRUPT,
    PE_MISORDER,
    PE_BANDPOLICER,
    PE_BANDSHAPER,
    PE_DROPTOTAL,
    PE_LATENCYTOTAL,
    PE_DUPTOTAL,
    PE_MISTOTAL,
    PE_CORTOTAL,
    PE_JITTERTOTAL,
    PE_CLEAR,
    PE_FLOWDROPTOTAL,
    PE_FLOWLATENCYTOTAL,
    PE_FLOWDUPTOTAL,
    PE_FLOWMISTOTAL,
    PE_FLOWCORTOTAL,
    PE_FLOWJITTERTOTAL,
    PE_FLOWCLEAR,
)

from .reception_statistics import ReceptionStatistics
from .transmission_statistics import TransmissionStatistics
from .pe_distribution import ImpairmentTypeDistribution
from .filter_definition import (
    shadow,
    working,
)


class CTotalFlow:
    """Total flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.drop_packets = PE_FLOWDROPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets dropped in a flow.

        :type: PE_FLOWDROPTOTAL
        """

        self.latency_packets = PE_FLOWLATENCYTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets delayed in a flow.

        :type: PE_FLOWLATENCYTOTAL
        """

        self.duplicated_packets = PE_FLOWDUPTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets duplicate in a flow.

        :type: PE_FLOWDUPTOTAL
        """

        self.mis_ordered_packets = PE_FLOWMISTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets misordered in a flow.

        :type: PE_FLOWMISTOTAL
        """

        self.corrupted_packets = PE_FLOWCORTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets corrupted in a flow.

        :type: PE_FLOWCORTOTAL
        """

        self.jittered_packets = PE_FLOWJITTERTOTAL(conn, module_id, port_id, flow_index)
        """Statistics of all packets jittered in a flow.

        :type: PE_FLOWJITTERTOTAL
        """


class StatisticsTotals:
    """Total port statistics."""

    def __init__(self, conn, module_id, port_id) -> None:
        self.drop = PE_DROPTOTAL(conn, module_id, port_id)
        """Statistics of all packets dropped on the port.

        :type: PE_DROPTOTAL
        """

        self.latency = PE_LATENCYTOTAL(conn, module_id, port_id)
        """Statistics of all packets delayed on the port.

        :type: PE_LATENCYTOTAL
        """

        self.duplicated = PE_DUPTOTAL(conn, module_id, port_id)
        """Statistics of all packets duplicated on the port.

        :type: PE_DUPTOTAL
        """

        self.mis_ordered = PE_MISTOTAL(conn, module_id, port_id)
        """Statistics of all packets mirordered on the port.

        :type: PE_MISTOTAL
        """

        self.corrupted = PE_CORTOTAL(conn, module_id, port_id)
        """Statistics of all packets corrupted on the port.

        :type: PE_CORTOTAL
        """

        self.jittered = PE_JITTERTOTAL(conn, module_id, port_id)
        """Statistics of all packets jittered on the port.

        :type: PE_JITTERTOTAL
        """


class CFlowStatistics:
    """Per flow statistics."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.rx = ReceptionStatistics(conn, module_id, port_id, flow_index)
        """RX statistics."""

        self.tx = TransmissionStatistics(conn, module_id, port_id, flow_index)
        """TX statistics."""

        self.total = CTotalFlow(conn, module_id, port_id, flow_index)
        """Total flow statistics."""

        self.clear = PE_FLOWCLEAR(conn, module_id, port_id, flow_index)
        """Clear the impairment statistics on a flow.

        :type: PE_FLOWCLEAR
        """


class CBandwidth:
    """Bandwidth configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.policer = PE_BANDPOLICER(conn, module_id, port_id, flow_index)
        """Bandwidth policer configuration.

        :type: PE_BANDPOLICER
        """

        self.shaper = PE_BANDSHAPER(conn, module_id, port_id, flow_index)
        """Bandwidth shaper configuration.

        :type: PE_BANDSHAPER
        """


class CFlow:
    """Flow settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, flow_index: int) -> None:
        self.comment = PE_COMMENT(conn, module_id, port_id, flow_index)
        """Flow description.

        :type: PE_COMMENT
        """

        self.latency_range = PE_LATENCYRANGE(conn, module_id, port_id, flow_index)
        """Flow latency range.

        :type: PE_LATENCYRANGE
        """

        self.corruption = PE_CORRUPT(conn, module_id, port_id, flow_index)
        """Corruption type.

        :type: PE_CORRUPT
        """

        self.misordering = PE_MISORDER(conn, module_id, port_id, flow_index)
        """Misordering depth

        :type: PE_MISORDER
        """

        self.bandwidth_control = CBandwidth(conn, module_id, port_id, flow_index)
        """Bandwidth configuration."""

        self.statistics = CFlowStatistics(conn, module_id, port_id, flow_index)
        """Flow statistics."""

        self.impairment_distribution = ImpairmentTypeDistribution(conn, module_id, port_id, flow_index)
        """Impairment type's distribution."""

        self.shadow_filter = shadow.FilterDefinitionShadow(conn, module_id, port_id, flow_index)
        """Shadow copy."""

        self.working_filter = working.FilterDefinitionWorking(conn, module_id, port_id, flow_index)
        """Working copy."""


class ChimeraPE:
    """Port Emulation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self.module_id = module_id
        self.port_id = port_id
        self.drop_fcs_errors = PE_FCSDROP(conn, module_id, port_id)
        """Action on FCS errors.

        :type: PE_FCSDROP
        """

        self.clear = PE_CLEAR(conn, module_id, port_id)
        """Clear impairment statistics.

        :type: PE_CLEAR
        """

        self.statistics = StatisticsTotals(conn, module_id, port_id)
        """Total port statistics."""

        self.tpld_mode = PE_TPLDMODE(conn, module_id, port_id)
        """TPLD mode.

        :type: PE_TPLDMODE
        """

        self.flows: Tuple["CFlow", ...] = tuple()

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> None:
        indices = await PE_INDICES(self._conn, self.module_id, self.port_id).get()
        self.flows = tuple(
            CFlow(self._conn, self.module_id, self.port_id, idx)
            for idx in indices.to_tuple()
        )
