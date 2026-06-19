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

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

class MClockSweep:
    """Test module local clock sweep"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.config = M_CLOCKPPBSWEEP(conn, module_id)
        """Configure and control the module local clock sweep.
        
        :type: M_CLOCKPPBSWEEP
        """

        self.status = M_CLOCKSWEEPSTATUS(conn, module_id)
        """Status of the module local clock sweep.
        
        :type: M_CLOCKSWEEPSTATUS
        """

class MHealth:
    """Test module health"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.all = M_HEALTH(conn, module_id, [])
        """All module health information
        
        :type: M_HEALTH
        """
        
        self.info = M_HEALTH(conn, module_id, [0])
        """Module identification information
        
        :type: M_HEALTH
        """
        
        self.cage_insertion = M_HEALTH(conn, module_id, [1])
        """Module cage insertion counter
        
        :type: M_HEALTH
        """
        
        
class MSolutionTrack:
    """Test module solution track"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.enable = M_SOLUTION_TRACK_ENABLE(conn, module_id)
        """Enable or disable the solution track.
        
        :type: M_SOLUTION_TRACK_ENABLE
        """

        self.indices = M_SOLUTION_TRACK_INDICES(conn, module_id)
        """Get the indices of the enabled solution tracks.
        
        :type: M_SOLUTION_TRACK_INDICES
        """

        self.demo_exp = M_SOLUTION_TRACK_DEMO_EXP(conn, module_id)
        """Get the demonstration expire information of the solution track.
        
        :type: M_SOLUTION_TRACK_DEMO_EXP
        """


class ModuleFamilyEdun(ModuleL23):
    """Test module Edun family"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.clock_sweep = MClockSweep(conn, self.module_id)
        """Clock ppm sweep control"""

        self.health = MHealth(conn, self.module_id)
        """Module health information"""
        
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


@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP[a]")
class MEdun1600G4S1POSFP_a(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP[a]"""
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
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-IHS[a]")
class MEdun1600G4S1POSFP_IHS_a(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-IHS[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_IHS_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_IHS_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP-IHS[a]"""
        
        
@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-RHS[a]")
class MEdun1600G4S1POSFP_RHS_a(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-RHS[a]"""
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
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP[c]")
class MEdun1600G4S1POSFP_c(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP[c]"""
        

@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-IHS[c]")
class MEdun1600G4S1POSFP_IHS_c(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-IHS[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_IHS_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_IHS_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP-IHS[c]"""
        
        
@typing.final
@revisions.register_valkyrie_module(rev="Edun-1600G-4S-1P-OSFP-RHS[c]")
class MEdun1600G4S1POSFP_RHS_c(ModuleFamilyEdun):
    """Test module Edun-1600G-4S-1P-OSFP-RHS[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PEdun1600G4S1POSFP_RHS_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PEdun1600G4S1POSFP_RHS_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Edun-1600G-4S-1P-OSFP-RHS[c]"""