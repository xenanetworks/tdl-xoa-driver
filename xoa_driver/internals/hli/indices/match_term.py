from typing import (
    List,
    Type,
    TypeVar,
    TYPE_CHECKING,
)
from xoa_driver.internals.commands import (
    PM_INDICES,
    PM_CREATE,
    PM_DELETE,
    PM_PROTOCOL,
    PM_POSITION,
    PM_MATCH,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
from xoa_driver.internals.utils.indices import observer as idx_obs
from .base_index import BaseIndex

MT = TypeVar("MT")


class MatchTermIdx(BaseIndex):
    """L23 Match Term Index Manager"""
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> None:
        super().__init__(conn, kind, observer)

        self.protocol = PM_PROTOCOL(conn, *kind)
        """The protocol segments assumed on the packets received on the port.

        :type: PM_PROTOCOL
        """

        self.position = PM_POSITION(conn, *kind)
        """The position within each received packet where content matching begins for the port.

        :type: PM_POSITION
        """

        self.match = PM_MATCH(conn, *kind)
        """The value that must be found at the match term position for packets received on the port.

        :type: PM_MATCH
        """

    async def delete(self):
        await PM_DELETE(self._conn, *self.kind).set()
        """Delete the match term.
        
        :type: PM_DELETE
        """

        self._observer.notify(idx_obs.IndexEvents.DEL, self)

    @classmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        resp = await PM_INDICES(conn, module_id, port_id).get()
        return list(resp.match_term_xindices)

    @classmethod
    async def _new(cls: Type[MT], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "idx_obs.IndicesObserver") -> MT:
        await PM_CREATE(conn, *kind).set()
        return cls(conn, kind, observer)
