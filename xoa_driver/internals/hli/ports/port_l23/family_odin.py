import functools
from typing import (
    TYPE_CHECKING,
)
from xoa_driver.internals.commands import (
    P_MDIXMODE,
    P_AUTONEGSELECTION,
    P_DYNAMIC,
)
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from .bases.port_l23_genuine import BasePortL23Genuine
from .layer1.lower_power import LowPowerMode
from .trafficgen.runt import Runt
from .layer1.preamble import Preamble
from .layer1.brr import BroadrReach

class FamilyOdin(BasePortL23Genuine):
    """Base class for Odin-1G port"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """Auto-negotiation selection.
        
        :type: P_AUTONEGSELECTION
        """

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""

        
        

class POdin1G3S6P(FamilyOdin):
    """L23 port on Odin-1G-3S-6P module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        """MDI/MDIX mode.
        
        :type: P_MDIXMODE
        """


class POdin1G3S6P_b(POdin1G3S6P):
    """L23 port on Odin-1G-3S-6P[b] module.
    """
    ...


class POdin1G3S6PE(POdin1G3S6P):
    """L23 port on Odin-1G-3S-6P-E module.
    """
    ...


class POdin1G3S2PT(POdin1G3S6P):
    """L23 port on Odin-1G-3S-2P-T module.
    """
    ...


class POdin1G4S4PCombi(FamilyOdin):
    """L23 port on Odin-1G-4S-2P-Combi module.
    """
    ...


class POdin1G4S4PCombi_b(FamilyOdin):
    """L23 port on Odin-1G-4S-2P-Combi_b module.
    """
    ...



class POdin10G4S2PCombi(FamilyOdin):
    """L23 port on Odin-10G-4S-2P-Combi module.
    """
    ...


class POdin10G4S2PCombi_b(FamilyOdin):
    """L23 port on Odin-10G-4S-2P-Combi_b module.
    """
    ...

class POdin10G1S2P(FamilyOdin):
    """L23 port on Odin-10G-1S-2P module.
    """
    ...


class POdin10G1S2P_b(POdin10G1S2P):
    """L23 port on Odin-10G-1S-2P[b] module.
    """
    ...


class POdin10G1S2P_c(POdin10G1S2P):
    """L23 port on Odin-10G-1S-2P[c] module.
    """
    ...


class POdin10G1S6P(FamilyOdin):
    """L23 port on Odin-10G-1S-6P module.
    """
    ...

class POdin10G1S6P_b(POdin10G1S6P):
    """L23 port on Odin-10G-1S-6P[b] module.
    """
    ...


class POdin5G4S6PCU(FamilyOdin):
    """L23 port on Odin-5G-4S-6P-CU module.
    """
    ...


class POdin10G5S6PCU(FamilyOdin):
    """L23 port on Odin-10G-5S-6P-CU module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self.eee = LowPowerMode(conn, module_id, port_id)
        """L23 port Low Power mode settings.
        
        :type: LowPowerMode
        """


class POdin10G5S6PCU_b(POdin10G5S6PCU):
    """L23 port on Odin-10G-5S-6P-CU[b] module.
    """
    ...


class POdin10G3S6PCU(FamilyOdin):
    """L23 port on Odin-10G-3S-6P-CU module.
    """
    ...


class POdin10G3S2PCU(FamilyOdin):
    """L23 port on Odin-10G-3S-2P-CU module.
    """
    ...


class POdin10G6S6P_a(FamilyOdin):
    """L23 port on Odin-10G-6S-6P[a] module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        
        self.runt = Runt(conn, module_id, port_id)
        """Runt settings.
        
        :type: Runt
        """

        self.preamble = Preamble(conn, module_id, port_id)
        """Preamble settings.
        
        :type: Preamble
        """


class POdin10G1S2PT(FamilyOdin):
    """L23 port on Odin-10G-1S-2P-T module.
    """
    ...


class POdin10G1S2P_d(FamilyOdin):
    """L23 port on Odin-10G-1S-2P[d] module.
    """
    ...


class POdin10G1S12P(FamilyOdin):
    """L23 port on Odin-10G-1S-12P module.
    """
    ...


class POdin40G2S2P(FamilyOdin):
    """L23 port on Odin-40G-2S-2P module.
    """
    ...
    


class POdin40G2S2PB(POdin40G2S2P):
    """L23 port on Odin-40G-2S-2P-B module.
    """
    ...


class POdin1G3S6PT1RJ45(FamilyOdin):
    """L23 port on Odin-1G-3S-6P-T1-RJ45 module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.brr = BroadrReach(conn, module_id, port_id)
        """BroadR-Reach settings.
        """

class POdin100G3S1P(FamilyOdin):
    """L23 port on Odin-100G-3S-1P module.
    """
    ...