import functools
from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
from xoa_driver.internals.commands import (
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1_freya import Layer1


class FamilyThorNg(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

    async def _setup(self) -> Self:
        await super()._setup()
        self.layer1 = Layer1(self._conn, self)
        """Layer 1"""
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PThor400G7S2P_a(FamilyThorNg):
    """L23 port on Thor-400G-7S-2P[a] module.
    """
    ...