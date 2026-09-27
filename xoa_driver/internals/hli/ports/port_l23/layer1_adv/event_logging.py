from typing import (
    TYPE_CHECKING,
    Tuple,
)

from xoa_driver.internals.commands import (
    PL1_EVENT_LOGGING_READ,
    PL1_EVENT_LOGGING_CONFIG,
    PL1_EVENT_LOGGING_SUBLIST,
    PL1_EVENT_LOGGING_STATE,
    PL1_EVENT_LOGGING_MARK,
    PL1_EVENT_LOGGING_QLEN,
    PL1_EVENT_LOGGING_RSFEC_THRESH,
    
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    

class L1EventLoggingSub:
    """Subscription to a specific Layer-1 event."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_lane: int) -> None:
        
        self.config = PL1_EVENT_LOGGING_CONFIG(conn, module_id, port_id, serdes_lane)
        """Configure the event logging.

        :type: PL1_EVENT_LOGGING_CONFIG
        """
    
class L1EventLoggingRead:
    """State of the Layer-1 event logging."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.read = PL1_EVENT_LOGGING_READ(conn, module_id, port_id)
        """Read the event logging entries.

        :type: PL1_EVENT_LOGGING_READ
        """

        self.sublist = PL1_EVENT_LOGGING_SUBLIST(conn, module_id, port_id)
        """Get the sublist of event logging entries.

        :type: PL1_EVENT_LOGGING_SUBLIST
        """

        self.state = PL1_EVENT_LOGGING_STATE(conn, module_id, port_id)
        """Get the current state of event logging.

        :type: PL1_EVENT_LOGGING_STATE
        """
        
        self.qlen = PL1_EVENT_LOGGING_QLEN(conn, module_id, port_id)
        """Get the queue length of event logging.

        :type: PL1_EVENT_LOGGING_QLEN
        """

        self.rsfec_thresh = PL1_EVENT_LOGGING_RSFEC_THRESH(conn, module_id, port_id)
        """Get the RSFEC threshold of event logging.

        :type: PL1_EVENT_LOGGING_RSFEC_THRESH
        """


class L1EventLogging:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.mark = PL1_EVENT_LOGGING_MARK(conn, module_id, port_id)
        """Mark the event logging.

        :type: PL1_EVENT_LOGGING_MARK
        """
        
        self.read = L1EventLoggingRead(conn, module_id, port_id)
        """State of the Layer-1 event logging.

        :type: L1EventLoggingRead
        """
        
        self.sub0 = L1EventLoggingSub(conn, module_id, port_id, 0)
        """Subscription to a specific Layer-1 event for SerDes lane 0.

        :type: L1EventLoggingSub
        """

        self.sub1 = L1EventLoggingSub(conn, module_id, port_id, 1)
        """Subscription to a specific Layer-1 event for SerDes lane 1.

        :type: L1EventLoggingSub
        """
        
        self.sub2 = L1EventLoggingSub(conn, module_id, port_id, 2)
        """Subscription to a specific Layer-1 event for SerDes lane 2.

        :type: L1EventLoggingSub
        """

        self.sub3 = L1EventLoggingSub(conn, module_id, port_id, 3)
        """Subscription to a specific Layer-1 event for SerDes lane 3.

        :type: L1EventLoggingSub
        """
        
        self.sub4 = L1EventLoggingSub(conn, module_id, port_id, 4)
        """Subscription to a specific Layer-1 event for SerDes lane 4.

        :type: L1EventLoggingSub
        """
        
        self.sub5 = L1EventLoggingSub(conn, module_id, port_id, 5)
        """Subscription to a specific Layer-1 event for SerDes lane 5.

        :type: L1EventLoggingSub
        """
        
        self.sub6 = L1EventLoggingSub(conn, module_id, port_id, 6)
        """Subscription to a specific Layer-1 event for SerDes lane 6.

        :type: L1EventLoggingSub
        """

        self.sub7 = L1EventLoggingSub(conn, module_id, port_id, 7)
        """Subscription to a specific Layer-1 event for SerDes lane 7.

        :type: L1EventLoggingSub
        """