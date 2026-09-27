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
    

class L1EventLogging:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.read = PL1_EVENT_LOGGING_READ(conn, module_id, port_id)
        """Read the event logging entries.

        :type: PL1_EVENT_LOGGING_READ
        """

        self.config = PL1_EVENT_LOGGING_CONFIG(conn, module_id, port_id)
        """Configure the event logging.

        :type: PL1_EVENT_LOGGING_CONFIG
        """

        self.sublist = PL1_EVENT_LOGGING_SUBLIST(conn, module_id, port_id)
        """Get the sublist of event logging entries.

        :type: PL1_EVENT_LOGGING_SUBLIST
        """

        self.state = PL1_EVENT_LOGGING_STATE(conn, module_id, port_id)
        """Get the current state of event logging.

        :type: PL1_EVENT_LOGGING_STATE
        """

        self.mark = PL1_EVENT_LOGGING_MARK(conn, module_id, port_id)
        """Mark the event logging.

        :type: PL1_EVENT_LOGGING_MARK
        """

        self.qlen = PL1_EVENT_LOGGING_QLEN(conn, module_id, port_id)
        """Get the queue length of event logging.

        :type: PL1_EVENT_LOGGING_QLEN
        """

        self.rsfec_thresh = PL1_EVENT_LOGGING_RSFEC_THRESH(conn, module_id, port_id)
        """Get the RSFEC threshold of event logging.

        :type: PL1_EVENT_LOGGING_RSFEC_THRESH
        """