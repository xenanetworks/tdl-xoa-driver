"""Port Edun Commands"""
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
    XmpIPv4Address,
    XmpIPv6Address,
    XmpLong,
    XmpShort,
    XmpMacAddress,
    XmpSequence,
    XmpStr,
    Hex,
)


@register_command
@dataclass
class P_EDUN_RX_STATUS:
    """
    Edun Rx status values for the specified SerDes index on the port.
    """

    code: typing.ClassVar[int] = 598
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        signal_detected: int = field(XmpByte())
        """1=Detected, 0=not detected"""
        pmd_lock: int = field(XmpByte())
        """1=Lock, 0=No Lock"""
        tuning_done: int = field(XmpByte())
        """1=Done, 0=Not Done"""
        eye_slicer_upper: int = field(XmpInt())
        """Upper eye slicer value. Unit is in mV."""
        eye_slicer_middle: int = field(XmpInt())
        """Middle eye slicer value. Unit is in mV."""
        eye_slicer_lower: int = field(XmpInt())
        """Lower eye slicer value. Unit is in mV."""
        snr: int = field(XmpInt())
        """Signal to Noise ratio, 1/100 dB"""
        vga: int = field(XmpInt())
        """Variable Gain Amplifier setting (0 to 64)"""
        dco: int = field(XmpInt())
        """DC Offset compensation value"""
        ffe_pre3: int = field(XmpInt())
        """Pre-cursor 3 of the RX equalizer"""
        ffe_pre2: int = field(XmpInt())
        """Pre-cursor 2 of the RX equalizer"""
        ffe_pre1: int = field(XmpInt())
        """Pre-cursor 1 of the RX equalizer"""
        ffe_main: int = field(XmpInt())
        """Main cursor of the RX equalizer"""
        ffe_post1: int = field(XmpInt())
        """Post-cursor 1 of the RX equalizer"""
        ffe_post2: int = field(XmpInt())
        """Post-cursor 2 of the RX equalizer"""
        tp0: int = field(XmpInt())
        """RX Channel Loss hint given by user (dB)"""
        tp1: int = field(XmpInt())
        """RX Channel Loss (initial) estimate"""
        tp2: int = field(XmpInt())
        """AFE static bandwitdh setting (200G  == 0 else 100G if < 3 else 50GPAM4/NRZ if <5 else LinkCAT)"""
        dfe1: int = field(XmpInt())
        """ISI correction tap 1"""
        dfe2: int = field(XmpInt())
        """ISI correction tap 2"""
        flt_m: int = field(XmpInt())
        """Max. floating tap value"""
        flt_s: int = field(XmpInt())
        """Sum of floating taps"""

    def get(self) -> Token[GetDataAttr]:
        """Get Edun Rx status values for the specified SerDes index on the port.

        :return: Edun Rx status values for the specified SerDes index on the port.
        :rtype: P_EDUN_RX_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


__all__ = [
    "P_EDUN_RX_STATUS",
]