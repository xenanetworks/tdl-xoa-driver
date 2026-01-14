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
from .layer1_loki import Layer1
from .sec.macsec import MacSec


class FamilyLoki(BasePortL23Genuine):
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


class PLoki100G3S1P(FamilyLoki):
    """L23 port on Loki-100G-3S-1P module.
    """
    ...


class PLoki100G3S1P_b(FamilyLoki):
    """L23 port on Loki-100G-3S-1P[b] module.
    """
    ...


class PLoki100G3S1PSE(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-SE module.
    """
    ...

class PLoki100G3S1PB(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-B module.
    """
    ...

class PLoki100G3S1PB_b(FamilyLoki):
    """L23 port on Loki-100G-3S-1P-B[b] module.
    """
    ...

class PLoki100G5S1P(FamilyLoki):
    """L23 port on Loki-100G-5S-1P module.
    """
    ...

class PLoki100G5S2P(FamilyLoki):
    """L23 port on Loki-100G-5S-2P module.
    """
    ...


class PLoki100G5S4P_a(FamilyLoki):
    """L23 port on Loki-100G-5S-4P[a] module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self.macsec = MacSec(conn, module_id, port_id)
        """MACSec configuration and status."""