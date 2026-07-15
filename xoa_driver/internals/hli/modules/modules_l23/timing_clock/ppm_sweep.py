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