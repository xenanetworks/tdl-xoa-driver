import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

from xoa_driver.internals.commands.m_commands import (
    M_SOLUTION_TRACK_ACTIVATE,
    M_SOLUTION_TRACK,
    M_SOLUTION_TRACK_INDICES,
    M_SOLUTION_TRACK_DEMO_EXP,
    M_SOLUTION_TRACK_INSTALL,
)

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ... import __interfaces as m_itf

class MSolutionTrack:
    """Test module solution track"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.install = M_SOLUTION_TRACK_INSTALL(conn, module_id)
        """Install a solution track key.

        :type: M_SOLUTION_TRACK_INSTALL
        """

        self.indices = M_SOLUTION_TRACK_INDICES(conn, module_id)
        """Get the indices of the enabled solution tracks.

        :type: M_SOLUTION_TRACK_INDICES
        """

        self.demo_exp = M_SOLUTION_TRACK_DEMO_EXP(conn, module_id)
        """Get the demonstration expire information of the solution track.

        :type: M_SOLUTION_TRACK_DEMO_EXP
        """

        self.activate = M_SOLUTION_TRACK_ACTIVATE(conn, module_id)
        """Activate the solution track.

        :type: M_SOLUTION_TRACK_ACTIVATE
        """

        self.solution_track = M_SOLUTION_TRACK(conn, module_id)
        """Get the solution track feature information.

        :type: M_SOLUTION_TRACK
        """