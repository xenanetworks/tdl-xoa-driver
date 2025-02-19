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
from xoa_driver.internals.utils import attributes as utils
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

from .bases.port_l23_genuine import BasePortL23Genuine


class FamilyF(BasePortL23Genuine):
    ...


class POdin10G1S2P(FamilyF):
    """L23 port on Odin-10G-1S-2P module.
    """
    ...


class POdin10G1S2P_b(FamilyF):
    """L23 port on Odin-10G-1S-2P[b] module.
    """
    ...


class POdin10G1S2P_c(FamilyF):
    """L23 port on Odin-10G-1S-2P[c] module.
    """
    ...


class POdin10G1S6P(FamilyF):
    """L23 port on Odin-10G-1S-6P module.
    """
    ...


class Runt:
    """Runt settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's TX runt length.
        Representation of P_TXRUNTLENGTH
        """

        self.rx_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's RX runt length.
        Representation of P_RXRUNTLENGTH
        """

        self.has_length_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)
        """L23 port's RX runt length errors..
        Representation of P_RXRUNTLEN_ERRS
        """


class Preamble:
    """Preamble settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)
        """L23 port's removal of preamble from outgoing packets.
        Representation of P_TXPREAMBLE_REMOVE
        """

        self.rx_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)
        """L23 port's insertion of preamble into incoming packets.
        Representation of P_RXPREAMBLE_INSERT
        """


class POdin10G1S6P_b(FamilyF):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.runt = Runt(conn, module_id, port_id)
        """Runt settings."""

        self.preamble = Preamble(conn, module_id, port_id)
        """Preamble settiNgs."""

class POdin10G6S6P_a(FamilyF):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.runt = Runt(conn, module_id, port_id)
        """Runt settings."""

        self.preamble = Preamble(conn, module_id, port_id)
        """Preamble settiNgs."""


class POdin10G1S2PT(FamilyF):
    """L23 port on Odin-10G-1S-2P-T module.
    """
    ...


class POdin10G1S2P_d(FamilyF):
    """L23 port on Odin-10G-1S-2P[d] module.
    """
    ...


class POdin10G1S12P(FamilyF):
    """L23 port on Odin-10G-1S-12P module.
    """
    ...


class POdin40G2S2P(FamilyF):
    """L23 port on Odin-40G-2S-2P module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        Representation of P_DYNAMIC
        """

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""


class POdin40G2S2PB(FamilyF):
    """L23 port on Odin-40G-2S-2P-B module.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        Representation of P_DYNAMIC
        """

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""
