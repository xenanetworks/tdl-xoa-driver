"""Stream Ultra Ethernet Commands"""
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
    UecFrameDesireLlr,
)

@register_command
@dataclass
class PS_UE_LLR_DESIRE:
    """
    Configures the desired LLR mode of the stream.
    """

    code: typing.ClassVar[int] = 1027
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _stream_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        type: UecFrameDesireLlr = field(XmpByte())
        """short integer, indicates the type of frame. Default value is ``LLR_INELIGIBLE (1)``.
        """

    class SetDataAttr(RequestBodyStruct):
        type: UecFrameDesireLlr = field(XmpByte())
        """short integer, indicates the type of frame. Default value is ``LLR_INELIGIBLE (1)``.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR desire mode of the stream.

        :return: the LLR desire mode
        :rtype: PS_UE_LLR_DESIRE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._stream_xindex]))

    def set(self, type: UecFrameDesireLlr) -> Token[None]:
        """Set the LLR desire mode of the stream.

        :param type:  the LLR desire mode
        :type type: UecFrameDesireLlr
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._stream_xindex], type=type))


    set_llr_ineligible = functools.partialmethod(set, UecFrameDesireLlr.LLR_INELIGIBLE)
    """Set the LLR desire mode to ineligible.
    """

    set_llr_eligible = functools.partialmethod(set, UecFrameDesireLlr.LLR_ELIGIBLE)
    """Set the LLR desire mode to eligible.
    """

__all__ = [
    "PS_UE_LLR_DESIRE",
]