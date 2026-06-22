import functools
import typing
from xoa_driver.internals.commands import (
    P_DYNAMIC,
    P_TPLDOFFSET,
)
from xoa_driver.internals.utils import attributes as utils

from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1.layer1_thor2 import Layer1

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

__all__ = (
    "PThor400G7S2P_a",
    "PThor400G7S2P_c",
)


class FamilyThor2(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """
        
        self.tpld_offset = P_TPLDOFFSET(conn, module_id, port_id)
        """L23 port test payload offset configuration.

        :type: P_TPLDOFFSET
        """

    async def _setup(self) -> typing.Self:
        await super()._setup()

        self.layer1 = Layer1(self._conn, self)
        """Layer 1
        
        :type: Layer1
        """
        
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


@typing.final
class PThor400G7S2P_a(FamilyThor2):
    """L23 port on Thor-400G-7S-2P[a] module.
    """
    ...

@typing.final
class PThor400G7S2P_c(FamilyThor2):
    """L23 port on Thor-400G-7S-2P[c] module.
    """
    ...