from typing import (
    Protocol,
    List,
    TypeVar,
    Self,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import kind as kind_module
    from . import observer as idx_obs


class IIndexType(Protocol):
    def __init__(self, conn: "itf.IConnection", kind: "kind_module.IndicesKind", observer: "idx_obs.IndicesObserver") -> None: ...  # noqa: E704

    async def delete(self) -> None: ...  # noqa: E704

    @property
    def idx(self) -> int: ...  # noqa: E704

    @classmethod
    async def _fetch(
        cls, 
        conn: "itf.IConnection", 
        module_id: int, 
        port_id: int) -> List[int]: ...  # noqa: E704

    @classmethod
    async def _new(
        cls, 
        conn: "itf.IConnection", 
        kind: "kind_module.IndicesKind", 
        observer: "idx_obs.IndicesObserver"
        ) -> Self: ...  # noqa: E704
    
IT = TypeVar("IT", bound=IIndexType)
