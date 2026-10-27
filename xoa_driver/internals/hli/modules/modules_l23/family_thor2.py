import typing
import functools
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.utils import attributes as utils

from .bases.module_l23 import ModuleL23
from .solution_track.solution_track import MSolutionTrack

from xoa_driver.internals.commands import (
    M_SOLUTION_TRACK_ACTIVATE,
)

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

__all__ = (
    "MThor400G7S2P_a",
    "MThor400G7S2P_c",
)


#region - Module Family Thor-II
class ModuleFamilyThor2(ModuleL23):
    """Test module Thor2 family"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        
        self.solution_track = MSolutionTrack(conn, self.module_id)
        """Module solution track control"""
        
    on_solution_track_activation = functools.partialmethod(utils.on_event, M_SOLUTION_TRACK_ACTIVATE)
    """
    Register a callback to the event that the module's currently activated Solution Track changes.
    """

#endregion

#region - Thor-400G-7S-2P Category
@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-2P[a]")
class MThor400G7S2P_a(ModuleFamilyThor2):
    """Test module Thor-400G-7S-2P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S2P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S2P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Thor-400G-7S-2P[a]"""

@typing.final
@revisions.register_valkyrie_module(rev="Thor-400G-7S-2P[c]")
class MThor400G7S2P_c(ModuleFamilyThor2):
    """Test module Thor-400G-7S-2P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PThor400G7S2P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PThor400G7S2P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Thor-400G-7S-2P[c]"""
        
#endregion
