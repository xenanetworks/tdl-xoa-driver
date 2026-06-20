import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

from .bases.module_l23 import ModuleL23
from xoa_driver.internals.commands import (
    M_CLOCKPPBSWEEP,
    M_CLOCKSWEEPSTATUS,
    M_HEALTH,
)
from .solution_track.solution_track import MSolutionTrack
from .health.health import MHealth
from .timing_clock.ppm_sweep import MClockSweep

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf


#region - Module Family Freya
class ModuleFamilyFreya(ModuleL23):
    """Test module Freya family"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self.clock_sweep = MClockSweep(conn, self.module_id)
        """Clock ppm sweep control"""

        self.health = MHealth(conn, self.module_id)
        """Module health information"""
        
        self.solution_track = MSolutionTrack(conn, self.module_id)
        """Module solution track control"""

#endregion


#region - Freya-800G-1S-1P QSFPDD Category
        
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a]")
class MFreya800G1S1P_a(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b]")
class MFreya800G1S1P_b(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b]"""

#endregion

#region - Freya-800G-1S-1P  Category

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a]")
class MFreya800G1S1POSFP_a(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b]")
class MFreya800G1S1POSFP_b(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b]"""


#endregion

#region - Freya-800G-1S-1P G1 QSFPDD Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a] G1")
class MFreya800G1S1P_a_g1(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b] G1")
class MFreya800G1S1P_b_g1(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b] G1"""

#endregion

#region - Freya-800G-1S-1P G1 OSFP Category

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a] G1")
class MFreya800G1S1POSFP_a_g1(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b] G1")
class MFreya800G1S1POSFP_b_g1(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b] G1"""


#endregion

#region - Freya-800G-1S-1P G2 QSFPDD Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[a] G2")
class MFreya800G1S1P_a_g2(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P[b] G2")
class MFreya800G1S1P_b_g2(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P[b] G2"""

#endregion

#region - Freya-800G-1S-1P G2 OSFP Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[a] G2")
class MFreya800G1S1POSFP_a_g2(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-1S-1P-OSFP[b] G2")
class MFreya800G1S1POSFP_b_g2(ModuleFamilyFreya):
    """Test module Freya-800G-1S-1P-OSFP[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G1S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G1S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-1S-1P-OSFP[b] G2"""


#endregion

#region - Freya-800G-4S-1P QSFPDD Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a]")
class MFreya800G4S1P_a(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b]")
class MFreya800G4S1P_b(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c]")
class MFreya800G4S1P_c(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d]")
class MFreya800G4S1P_d(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e]")
class MFreya800G4S1P_e(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[e]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f]")
class MFreya800G4S1P_f(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[f]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f]"""

#endregion

#region - Freya-800G-4S-1P OSFP Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a]")
class MFreya800G4S1POSFP_a(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b]")
class MFreya800G4S1POSFP_b(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c]")
class MFreya800G4S1POSFP_c(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d]")
class MFreya800G4S1POSFP_d(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e]")
class MFreya800G4S1POSFP_e(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[e]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e]"""



@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f]")
class MFreya800G4S1POSFP_f(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[f]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f]"""


#endregion

#region - Freya-800G-4S-1P G1 QSFPDD Category

@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a] G1")
class MFreya800G4S1P_a_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b] G1")
class MFreya800G4S1P_b_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c] G1")
class MFreya800G4S1P_c_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[c] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d] G1")
class MFreya800G4S1P_d_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[d] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e] G1")
class MFreya800G4S1P_e_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[e] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f] G1")
class MFreya800G4S1P_f_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[f] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f] G1"""

#endregion

#region - Freya-800G-4S-1P G1 OSFP Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a] G1")
class MFreya800G4S1POSFP_a_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[a] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b] G1")
class MFreya800G4S1POSFP_b_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[b] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c] G1")
class MFreya800G4S1POSFP_c_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[c] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d] G1")
class MFreya800G4S1POSFP_d_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[d] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e] G1")
class MFreya800G4S1POSFP_e_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[e] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e] G1"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f] G1")
class MFreya800G4S1POSFP_f_g1(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[f] G1"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f] G1"""


#endregion

#region - Freya-800G-4S-1P G2 QSFPDD Category   

@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[a] G2")
class MFreya800G4S1P_a_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[a] G2"""
        

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[b] G2")
class MFreya800G4S1P_b_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[b] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[c] G2")
class MFreya800G4S1P_c_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[c] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[c] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[d] G2")
class MFreya800G4S1P_d_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[d] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[d] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[e] G2")
class MFreya800G4S1P_e_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[e] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[e] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P[f] G2")
class MFreya800G4S1P_f_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P[f] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P[f] G2"""

#endregion

#region - Freya-800G-4S-1P G2 OSFP Category
@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[a] G2")
class MFreya800G4S1POSFP_a_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[a] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[a] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[b] G2")
class MFreya800G4S1POSFP_b_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[b] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[b] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[c] G2")
class MFreya800G4S1POSFP_c_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[c] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[c] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[d] G2")
class MFreya800G4S1POSFP_d_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[d] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[d] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[e] G2")
class MFreya800G4S1POSFP_e_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[e] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[e] G2"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-1P-OSFP[f] G2")
class MFreya800G4S1POSFP_f_g2(ModuleFamilyFreya):
    """Test module Freya-800G-4S-1P-OSFP[f] G2"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S1POSFP_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S1POSFP_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-1P-OSFP[f] G2"""

#endregion

#region - Freya-800G-4S-2P Category

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[a]")
class MFreya800G4S2P_a(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[a]"""

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[b]")
class MFreya800G4S2P_b(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[b]"""

@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[c]")
class MFreya800G4S2P_c(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[c]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[d]")
class MFreya800G4S2P_d(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[d]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[e]")
class MFreya800G4S2P_e(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[e]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_e] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_e,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[e]"""


@typing.final
@revisions.register_valkyrie_module(rev="Freya-800G-4S-2P[f]")
class MFreya800G4S2P_f(ModuleFamilyFreya):
    """Test module Freya-800G-4S-2P[f]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PFreya800G4S2P_f] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PFreya800G4S2P_f,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Freya-800G-4S-2P[f]"""

#endregion
