import functools
import typing
from xoa_driver.internals.commands import (
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils

from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1.layer1_thor import Layer1

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

__all__ = (
    "PThor100G5S4P",
    "PThor400G7S1P",
    "PThor400G7S1PLE",
    "PThor400G7S1P_b",
    "PThor400G7S1P_c",
    "PThor400G7S1P_d",
)


class FamilyThor(BasePortL23Genuine):
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
class PThor100G5S4P(FamilyThor):
    """L23 port on Thor-100G-5S-4P module.
    """
    ...

@typing.final
class PThor400G7S1P(FamilyThor):
    """L23 port on Thor-400G-7S-1P module.
    """
    ...

@typing.final
class PThor400G7S1PLE(FamilyThor):
    """L23 port on Thor-400G-7S-1P LE module.
    """
    ...

@typing.final
class PThor400G7S1P_b(FamilyThor):
    """L23 port on Thor-400G-7S-1P[b] module.
    """
    ...


@typing.final
class PThor400G7S1P_c(FamilyThor):
    """L23 port on Thor-400G-7S-1P[c] module.
    """
    ...


@typing.final
class PThor400G7S1P_d(FamilyThor):
    """L23 port on Thor-400G-7S-1P[d] module.
    """
    ...