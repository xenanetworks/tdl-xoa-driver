
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
from .layer1_freya_adv import Layer1Adv


class FamilyFreya(BasePortL23Genuine):
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

        self.layer1_adv = Layer1Adv(self._conn, self)
        """Layer 1 Advanced"""

        return self

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class PFreya800G1S1P_a(FamilyFreya):
    """L23 port on Freya-800G-1S-1P[a] module.
    """
    ...


class PFreya800G1S1P_b(FamilyFreya):
    """L23 port on Freya-800G-1S-1P[b] module.
    """
    ...


class PFreya800G1S1POSFP_a(FamilyFreya):
    """L23 port on Freya-800G-1S-1P-OSFP[a] module.
    """
    ...

class PFreya800G1S1POSFP_b(FamilyFreya):
    """L23 port on Freya-800G-1S-1P-OSFP[b] module.
    """
    ...


class PFreya800G4S1P_a(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[a] module.
    """
    ...


class PFreya800G4S1P_b(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[b] module.
    """
    ...


class PFreya800G4S1P_c(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[c] module.
    """
    ...


class PFreya800G4S1P_d(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[d] module.
    """
    ...


class PFreya800G4S1P_e(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[e] module.
    """
    ...


class PFreya800G4S1P_f(FamilyFreya):
    """L23 port on Freya-800G-4S-1P[f] module.
    """
    ...


class PFreya800G4S2P_a(FamilyFreya):
    """L23 port on Freya-800G-4S-2P[a] module.
    """
    ...


class PFreya800G4S1POSFP_a(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[a] module.
    """
    ...


class PFreya800G4S1POSFP_b(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[b] module.
    """
    ...


class PFreya800G4S1POSFP_c(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[c] module.
    """
    ...


class PFreya800G4S1POSFP_d(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[d] module.
    """
    ...


class PFreya800G4S1POSFP_e(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[e] module.
    """
    ...


class PFreya800G4S1POSFP_f(FamilyFreya):
    """L23 port on Freya-800G-4S-1P-OSFP[f] module.
    """
    ...