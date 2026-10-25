import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

from xoa_driver.internals.commands.m_commands import (
    M_TCVR_INDICES,
    M_TCVR_PRESENCE,
)

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ... import __interfaces as m_itf

class MTcvrCage:
    """Test module transceiver cage"""
    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        
        self.conn = conn
        self.module_id = module_id

        self.tcvr_indices = M_TCVR_INDICES(conn, module_id)
        """Get the indices of transceiver cages on a module.

        :type: M_TCVR_INDICES
        """

    def tcvr_presence(self, cage_xindex: int) -> "M_TCVR_PRESENCE":
            """Get the presence state and metadata for a transceiver
            
            :param cage_xindex: The index of the transceiver cage.
            :type cage_xindex: int
            :return: The presence state and metadata for the transceiver cage.
            :rtype: M_TCVR_PRESENCE
            """
    
            return M_TCVR_PRESENCE(
                self.conn,
                self.module_id,
                cage_xindex
            )
