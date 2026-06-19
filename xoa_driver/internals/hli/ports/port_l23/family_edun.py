
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
from .layer1.layer1_edun import Layer1
from .layer1_adv.layer1 import Layer1Adv
from .protocol.lldp import LLDP
from .uec.ue import UltraEthernet

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class FamilyEdun(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

        self.lldp = LLDP(conn, module_id, port_id)
        """LLDP protocol support for the port.
        
        :type: LLDP
        """
        
        self.uec = UltraEthernet(conn, module_id, port_id)
        """Ultra Ethernet of the port.

        :type: UltraEthernet
        """
        
        self.tpld_offset = P_TPLDOFFSET(conn, module_id, port_id)
        """L23 port test payload offset configuration.

        :type: P_TPLDOFFSET
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


class PEdun800G3S1PSMPX_a(FamilyEdun):
    """L23 port on Edun-800G-3S-1P-SMPX[a] module.
    """
    ...

class PEdun1600G4S1POSFP_a(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP[a] module.
    """
    ...
    
class PEdun1600G4S1POSFP_c(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP[c] module.
    """
    ...
    
class PEdun1600G4S1POSFP_IHS_a(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP-IHS[a] module.
    """
    ...
    
class PEdun1600G4S1POSFP_RHS_a(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP-RHS[a] module.
    """
    ...
    
class PEdun1600G4S1POSFP_IHS_c(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP-IHS[c] module.
    """
    ...
    
class PEdun1600G4S1POSFP_RHS_c(FamilyEdun):
    """L23 port on Edun-1600G-4S-1P-OSFP-RHS[c] module.
    """
    ...