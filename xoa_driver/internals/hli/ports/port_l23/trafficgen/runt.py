import functools
from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_DYNAMIC,
    P_TXRUNTLENGTH,
    P_RXRUNTLENGTH,
    P_RXRUNTLEN_ERRS,
    P_TXPREAMBLE_REMOVE,
    P_RXPREAMBLE_INSERT,

)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class Runt:
    """Runt settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's TX runt length.
        
        :type: P_TXRUNTLENGTH
        """

        self.rx_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's RX runt length.
        
        :type: P_RXRUNTLENGTH
        """

        self.has_length_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)
        """L23 port's RX runt length errors..
        
        :type: P_RXRUNTLEN_ERRS
        """