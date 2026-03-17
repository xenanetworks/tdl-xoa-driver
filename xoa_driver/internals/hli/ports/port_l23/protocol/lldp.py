from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_LLDP_CLEAR,
    P_LLDP_NEIGHBORS,
    P_LLDP_STATS,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.hli.indices.lldp.lldp_agent import LLDPAgentIdx
LLDPAgentIndices = idx_mgr.IndexManager[LLDPAgentIdx]


class LLDP:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.agents: LLDPAgentIndices = idx_mgr.IndexManager(conn, LLDPAgentIdx, module_id, port_id)

        self.clear = P_LLDP_CLEAR(conn, module_id, port_id)
        """Clears LLDP data on a L23 port.
        
        :type: P_LLDP_CLEAR
        """

        self.neighbors = P_LLDP_NEIGHBORS(conn, module_id, port_id)
        """Get LLDP neighbors discovered by the port.
        
        :type: P_LLDP_NEIGHBORS
        """

        self.statistics = P_LLDP_STATS(conn, module_id, port_id)
        """Get LLDP Tx and Rx statistics by the port.
        
        :type: P_LLDP_STATS
        """