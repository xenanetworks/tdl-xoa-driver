"""Port Ultra Ethernet CtlOS Commands"""
from __future__ import annotations
from dataclasses import dataclass
import ipaddress
import typing
import functools

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpHex,
    XmpInt,
    XmpLong,
    XmpSequence,
    XmpStr,
    Hex,
    XmpJson
)

from .enums import (
    UecCtlosClearDirection,
)

@register_command
@dataclass
class P_UE_CTLOS_CLEAR:
    """
    Clear UE CtlOS counters in the specified direction(s).
    """

    code: typing.ClassVar[int] = 1020
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int


    class SetDataAttr(RequestBodyStruct):
        direction: UecCtlosClearDirection = field(XmpByte())
        """UE CtlOS clear direction."""


    def set(self, direction: UecCtlosClearDirection) -> Token[None]:
        """Set the UE CtlOS clear direction.

        :param direction: the UE CtlOS clear direction
        :type direction: UecCtlosClearDirection
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, direction=direction))
    
    clear_none = functools.partialmethod(set, UecCtlosClearDirection.NONE)
    """Not clear UE CtlOS counters
    """

    clear_rx = functools.partialmethod(set, UecCtlosClearDirection.RX)
    """Clear RX UE CtlOS counters
    """

    clear_tx = functools.partialmethod(set, UecCtlosClearDirection.TX)
    """Clear TX UE CtlOS counters
    """

    clear_all = functools.partialmethod(set, UecCtlosClearDirection.ALL)
    """Clear all UE CtlOS counters (RX and TX).
    """
    

@register_command
@dataclass
class P_UE_CTLOS_RX_STATS:
    """
    CtlOS Rx statistics, including counters of all UE CtlOS message type values.
    """

    code: typing.ClassVar[int] = 1012
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        llr_init_cnt: int = field(XmpLong())
        """The number of LLR_INIT CtlOS received."""

        llr_init_echo_cnt: int = field(XmpLong())
        """The number of LLR_INIT_ECHO CtlOS received."""

        llr_ack_cnt: int = field(XmpLong())
        """The number of LLR_ACK CtlOS received."""

        llr_nack_cnt: int = field(XmpLong())
        """The number of LLR_NACK CtlOS received."""

        llr_init_seq: Hex = field(XmpHex(3))
        """The LLR_INIT sequence number. 3 bytes in hex format."""

        llr_init_data: Hex = field(XmpHex(2))
        """The LLR_INIT data. 2 bytes in hex format."""

        llr_init_echo_seq: Hex = field(XmpHex(3))
        """The LLR_INIT_ECHO sequence number. 3 bytes in hex format."""

        llr_init_echo_data: Hex = field(XmpHex(2))
        """The LLR_INIT_ECHO data. 2 bytes in hex format."""

        llr_init_echo_mismatch: int = field(XmpLong())
        """The number of Rx LLR_INIT_ECHO CtlOS with a sequence number or data that does not match the most recently transmitted LLR_INIT CtlOS."""


    def get(self) -> Token[GetDataAttr]:
        """Get UE CtlOS Rx statistics.

        :return: the UE CtlOS Rx statistics
        :rtype: P_UE_CTLOS_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_CTLOS_TX_STATS:
    """
    CtlOS Tx statistics, including counters of all UE CtlOS message type values.
    """

    code: typing.ClassVar[int] = 1011
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        llr_init_cnt: int = field(XmpLong())
        """The number of LLR_INIT CtlOS transmitted."""

        llr_init_echo_cnt: int = field(XmpLong())
        """The number of LLR_INIT_ECHO CtlOS transmitted."""

        llr_ack_cnt: int = field(XmpLong())
        """The number of LLR_ACK CtlOS transmitted."""

        llr_nack_cnt: int = field(XmpLong())
        """The number of LLR_NACK CtlOS transmitted."""

        llr_init_seq: Hex = field(XmpHex(3))
        """The LLR_INIT sequence number. 3 bytes in hex format."""

        llr_init_data: Hex = field(XmpHex(2))
        """The LLR_INIT data. 2 bytes in hex format."""

        llr_init_echo_seq: Hex = field(XmpHex(3))
        """The LLR_INIT_ECHO sequence number. 3 bytes in hex format."""

        llr_init_echo_data: Hex = field(XmpHex(2))
        """The LLR_INIT_ECHO data. 2 bytes in hex format."""


    def get(self) -> Token[GetDataAttr]:
        """Get UE CtlOS Tx statistics.

        :return: the UE CtlOS Tx statistics
        :rtype: P_UE_CTLOS_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



__all__ = [
    "P_UE_CTLOS_CLEAR",
    "P_UE_CTLOS_RX_STATS",
    "P_UE_CTLOS_TX_STATS",
]