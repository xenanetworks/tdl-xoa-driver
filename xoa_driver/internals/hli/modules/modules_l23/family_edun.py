import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

from .bases.module_l23 import ModuleL23
from xoa_driver.internals.commands import (
    M_CLOCKPPBSWEEP,
    M_CLOCKSWEEPSTATUS,
    M_HEALTH,
    M_SOLUTION_TRACK,
    M_SOLUTION_TRACK_INDICES,
    M_SOLUTION_TRACK_DEMO_EXP,
    M_SOLUTION_TRACK_ENABLE,
)
from .solution_track.solution_track import MSolutionTrack
from .health.health import MHealth
from .timing_clock.ppm_sweep import MClockSweep

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

#region - Module Family Edun
class ModuleFamilyEdun(ModuleL23):
    """Test module Edun family"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.clock_sweep = MClockSweep(conn, self.module_id)
        """Clock ppm sweep control"""

        self.health = MHealth(conn, self.module_id)
        """Module health information"""
        
        self.solution_track = MSolutionTrack(conn, self.module_id)
        """Module solution track control"""

#endregion
        

#region - Edun-800G-3S-1P-SMPX
@typing.final
@revisions.register_valkyrie_module(rev="Edun-800G-3S-1P-SMPX[a]")
class MEdun800G3S1PSMPX_a(ModuleFamilyEdun):
    """Test module Edun-800G-3S-1P-SMPX[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun800G3S1PSMPX_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun800G3S1PSMPX_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-800G-3S-1P-SMPX[a]"""

#endregion


#region - Edun-1600G-4S-1P-OSFP (OSFP-IHS)
@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP[a]")
class MEdun1600G4S1POSFP_a(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP[a]
    
    Supports transceiver cage form factor OSFP (OSFP-IHS).
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP[a]"""
        

@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP[c]")
class MEdun1600G4S1POSFP_c(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP[c]
    
    Supports transceiver cage form factor OSFP (OSFP-IHS).
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP[c]"""
        
#endregion


#region - Edun-1600G-4S-1P-OSFP-RHS        
@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-RHS[a]")
class MEdun1600G4S1POSFP_RHS_a(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-RHS[a]
    
    Supports transceiver cage form factor OSFP-RHS.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_RHS_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_RHS_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP-RHS[a]"""
        

@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-RHS[c]")
class MEdun1600G4S1POSFP_RHS_c(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-RHS[c]
    
    Supports transceiver cage form factor OSFP-RHS.
    """
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_RHS_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_RHS_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP-RHS[c]"""
        
#endregion