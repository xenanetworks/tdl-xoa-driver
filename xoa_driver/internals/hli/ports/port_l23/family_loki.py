import functools
import typing
from xoa_driver.internals.commands import (
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1.layer1_loki import Layer1

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

__all__ = (
    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G3S1PB",
    "PLoki100G3S1PB_b",
    "PLoki100G5S1P",
    "PLoki100G5S2P",
)


class FamilyLoki(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

    async def _setup(self) -> typing.Self:
        await super()._setup()
        self.layer1 = Layer1(self._conn, self)
        """Layer 1"""
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


@typing.final
class PLoki100G3S1P(FamilyLoki):
    """L23 port on Loki-100G-3S-1P module.
    """
    ...


@typing.final
class PLoki100G3S1P_b(FamilyLoki):
    """L23 port on Loki-100G-3S-1P[b] module.
    """
    ...


@typing.final
class PLoki100G3S1PSE(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-SE module.
    """
    ...

@typing.final
class PLoki100G3S1PB(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-B module.
    """
    ...

@typing.final
class PLoki100G3S1PB_b(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-B[b] module.
    """
    ...

@typing.final
class PLoki100G5S1P(FamilyLoki):
    """L23 port on Loki-100G-5S-1P module.
    """
    ...

@typing.final
class PLoki100G5S2P(FamilyLoki):
    """L23 port on Loki-100G-5S-2P module.
    """
    ...
