import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

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
    from ... import __interfaces as m_itf

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
