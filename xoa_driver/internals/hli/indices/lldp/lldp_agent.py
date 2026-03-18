from typing import (
    TYPE_CHECKING,
    List,
    TypeVar,
    Type,
)
from xoa_driver.internals.commands import (
    P_LLDP_CONFIG,
    P_LLDP_CREATE,
    P_LLDP_DATA,
    P_LLDP_DELETE,
    P_LLDP_HEADER,
    P_LLDP_INDICES,
    P_LLDP_OPMODE,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer as idx_obs
from ..base_index import BaseIndex


LA = TypeVar("LA")


class LLDPAgentIdx(BaseIndex):
    """LLDP Agent Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)
        
        self.config = P_LLDP_CONFIG(conn, *kind)
        """Configures LLDP agent
        
        :type: P_LLDP_CONFIG
        """

        self.lldpdu = P_LLDP_DATA(conn, *kind)
        """Configure LLDPDU of the LLDP agent.
        
        :type: P_LLDP_DATA
        """

        self.header = P_LLDP_HEADER(conn, *kind)
        """Condfigure LLDP header information of the LLDP agent.
        
        :type: P_LLDP_HEADER
        """

        self.opmode = P_LLDP_OPMODE(conn, *kind)
        """Configures the operation mode of the LLDP agent.
        
        :type: P_LLDP_OPMODE
        """

    async def delete(self) -> None:
        """Delete the LLDP agent.
        """

        await P_LLDP_DELETE(self._conn, *self.kind).set()

        self._observer.notify(idx_obs.IndexEvents.DEL, self)

    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await P_LLDP_INDICES(conn, module_id, port_id).get()
        return list(resp.lldp_agent_indices)

    @classmethod
    async def _new(cls: Type[LA], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> LA:
        await P_LLDP_CREATE(conn, *kind).set()
        return cls(conn, kind, observer) # type: ignore
