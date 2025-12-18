import functools
from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_TXPREAMBLE_REMOVE,
    P_RXPREAMBLE_INSERT,

)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class Preamble:
    """Preamble settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)
        """L23 port's removal of preamble from outgoing packets.
        
        :type: P_TXPREAMBLE_REMOVE
        """

        self.rx_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)
        """L23 port's insertion of preamble into incoming packets.
        
        :type: P_RXPREAMBLE_INSERT
        """