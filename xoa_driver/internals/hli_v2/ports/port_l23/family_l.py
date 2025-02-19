import functools
from typing import TYPE_CHECKING
from typing_extensions import Self
from xoa_driver.internals.commands import (
    # P_FAULTSIGNALING,
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine
from .fault_jkl import Fault
from .pcs_pma_ijkl_chimera import PcsPma as PcsPma1
from .pcs_pma_ghijkl import (
    PcsPma as PcsPma2,
    SerDes,
)
from .pcs_pma_l import PcsPma as PcsPma3


class PcsPma(PcsPma1, PcsPma2, PcsPma3):
    def __init__(self, conn: "itf.IConnection", port) -> None:
        PcsPma1.__init__(self, conn, port)
        PcsPma2.__init__(self, conn, port)
        PcsPma3.__init__(self, conn, port)


class FamilyL(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        Representation of P_DYNAMIC
        """

        self.fault = Fault(conn, module_id, port_id)

    async def _setup(self) -> Self:
        await super()._setup()
        self.pcs_pma = PcsPma(self._conn, self)
        self.serdes = tuple(
            SerDes(self._conn, *self.kind, serdes_xindex=serdes_xindex)
            for serdes_xindex in range(self.info.capabilities.serdes_count)
        )
        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PThor400G7S1P_b(FamilyL):
    """L23 port on Thor-400G-7S-1P[b] module.
    """
    ...


class PThor400G7S1P_c(FamilyL):
    """L23 port on Thor-400G-7S-1P[c] module.
    """
    ...


class PThor400G7S1P_d(FamilyL):
    """L23 port on Thor-400G-7S-1P[d] module.
    """
    ...
