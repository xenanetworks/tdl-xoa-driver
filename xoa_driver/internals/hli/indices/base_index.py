import abc
from typing import (
    List,
    TypeVar,
    Type,
    TYPE_CHECKING,
)
import warnings
from xoa_driver.internals.warn import XoaDeprecationWarning

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer


CT = TypeVar("CT")


class BaseIndex(abc.ABC):
    def __init__(self, conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> None:
        self._observer = observer
        self._conn = conn
        
        self.identity = kind
        """Index identity (module ID, port ID, and index ID).

        :type: kind.IndicesKind
        """
    
    @property
    def kind(self) -> "kind.IndicesKind":
        """Deprecated. Use 'identity' instead.
        """
        
        warnings.warn(
            "BaseIndex.kind is deprecated; use BaseIndex.identity instead.",
            XoaDeprecationWarning,
            stacklevel=2,
        )
        return self.identity
    
    @kind.setter
    def kind(self, value: "kind.IndicesKind") -> None:
        """Deprecated. Use 'identity' instead.
        """
        
        warnings.warn(
            "BaseIndex.kind is deprecated; use BaseIndex.identity instead.",
            XoaDeprecationWarning,
            stacklevel=2,
        )
        self.identity = value

    @property
    def idx(self) -> int:
        """Short for 'identity.index_id'."""
        return self.identity.index_id

    @abc.abstractmethod
    async def delete(self) -> None:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    async def _fetch(cls, conn: "itf.IConnection", module_id: int, port_id: int) -> List[int]:
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    async def _new(cls: Type[CT], conn: "itf.IConnection", kind: "kind.IndicesKind", observer: "observer.IndicesObserver") -> CT:
        raise NotImplementedError()
