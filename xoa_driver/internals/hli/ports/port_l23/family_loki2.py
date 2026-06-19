import functools
from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
from xoa_driver.internals.commands import (
    P_DYNAMIC,
    P_TPLDOFFSET,
)
from xoa_driver.internals.utils import attributes as utils

from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1.layer1_loki2 import Layer1
from .sec.macsec import MacSec

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class FamilyLoki2(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """
        
        self.macsec = MacSec(conn, module_id, port_id)
        """MACSec configuration and status.
        
        :type: MacSec
        """
        
        self.tpld_offset = P_TPLDOFFSET(conn, module_id, port_id)
        """L23 port test payload offset configuration.

        :type: P_TPLDOFFSET
        """
        

    async def _setup(self) -> Self:
        await super()._setup()
        self.layer1 = Layer1(self._conn, self)
        """Layer 1"""
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PLoki100G5S4P_a(FamilyLoki2):
    """L23 port on Loki-100G-5S-4P[a] module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        