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
        