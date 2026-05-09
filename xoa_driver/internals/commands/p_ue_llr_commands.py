"""Port Ultra Ethernet LLR Commands"""
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
class P_UE_LLR_MODE:
    """
    Configures the mode of operation of the LLR. Only when both local and remote ports have LLR ``ON``, the LLR will be active. If either port has LLR disabled, the LLR will be inactive.

    """

    code: typing.ClassVar[int] = 1013
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        llr_mode_local: int = field(XmpByte())
        """short integer, LLR mode of the local port."""

        llr_mode_remote: int = field(XmpByte())
        """short integer, LLR mode of the remote port."""


    class SetDataAttr(RequestBodyStruct):
        llr_mode_local: int = field(XmpByte())
        """short integer, LLR mode of the local port."""

        llr_mode_remote: int = field(XmpByte())
        """short integer, LLR mode of the remote port."""


    def get(self) -> Token[GetDataAttr]:
        """Get the LLR mode of the local port.

        :return: the LLR mode of the local port
        :rtype: P_UE_LLR_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, llr_mode_local: int, llr_mode_remote: int) -> Token[None]:
        """Set the LLR mode of the local port.

        :param llr_mode_local: the LLR mode of the local port
        :type llr_mode_local: int
        :param llr_mode_remote: the LLR mode of the remote port
        :type llr_mode_remote: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, llr_mode_local=llr_mode_local, llr_mode_remote=llr_mode_remote))



@register_command
@dataclass
class P_UE_LLR_RX_STATS:
    """
    Get the LLR Rx link-layer traffic statistics of the port. 
    """

    code: typing.ClassVar[int] = 1012
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        rx_ok: int = field(XmpLong())
        """The number of LLR-eligible frames received with a good FCS."""

        rx_poisoned: int = field(XmpLong())
        """The number of LLR-eligible frames received with a poisoned FCS."""

        rx_bad: int = field(XmpLong())
        """The number of LLR-eligible frames received with a bad FCS."""

        rx_llr_eligible_total: int = field(XmpLong())
        """Rx total LLR-eligible frames count. (not yet implemented, will be -1)"""

        rx_expected_seq_poisoned: int = field(XmpLong())
        """A count of the number of LLR-eligible frames received with a poisoned FCS that had the expected sequence number. """

        rx_expected_seq_bad: int = field(XmpLong())
        """A count of the total number of LLR-eligible frames received with the expected sequence number (irrespective of FCS status). (not yet implemented, will be -1)"""

        rx_missing_seq: int = field(XmpLong())
        """A count of the number of LLR-eligible frames received that had a sequence number that indicated a missing LLR-eligible frame in the sequence (irrespective of FCS status). """

        rx_duplicate_seq: int = field(XmpLong())
        """A count of the number of LLR-eligible frames received that had a duplicate sequence number (irrespective of FCS status). """

        rx_llr_ineligible_ok: int = field(XmpLong())
        """A count of the number of LLR-ineligible frames received with a good FCS. (not yet implemented, will be -1)"""

        rx_llr_ineligible_bad: int = field(XmpLong())
        """A count of the number of LLR-ineligible frames received with a bad FCS. (not yet implemented, will be -1)"""

        rx_llr_ineligible_total: int = field(XmpLong())
        """Rx total LLR-ineligible frames count. (not yet implemented, will be -1)"""


    
    def get(self) -> Token[GetDataAttr]:
        """Get the LLR Rx link-layer traffic statistics of the port. 

        :return: the LLR Rx link-layer traffic statistics
        :rtype: P_UE_LLR_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_UE_LLR_TX_STATS:
    """
    Get the LLR Tx link-layer traffic statistics of the port. 
    """

    code: typing.ClassVar[int] = 1013
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        tx_ok: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a good FCS."""

        tx_poisoned: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a poisoned FCS."""

        tx_bad: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a bad FCS."""

        tx_discard: int = field(XmpLong())
        """The number of LLR-eligible frames discarded by the LLR TX when the TX state machine is in the INIT state and the llr_init_behavior is set to DISCARD, or when the TX state machine is in the FLUSH state and the llr_flush_behavior is set to DISCARD."""

        tx_llr_eligible_total: int = field(XmpLong())
        """Tx total LLR-eligible frames count. (not yet implemented, will be -1)"""

        tx_llr_ineligible_ok: int = field(XmpLong())
        """A count of the number of LLR-ineligible frames transmitted with a good FCS. (not yet implemented, will be -1)"""

        tx_llr_ineligible_bad: int = field(XmpLong())
        """A count of the number of LLR-ineligible frames transmitted with a bad FCS. (not yet implemented, will be -1)"""

        tx_llr_ineligible_total: int = field(XmpLong())
        """Tx total LLR-ineligible frames count. (not yet implemented, will be -1)"""

        tx_replayed: int = field(XmpLong())
        """The number of frames transmitted by the LLR TX that were replayed from the LLR replay buffer."""


    
    def get(self) -> Token[GetDataAttr]:
        """Get the LLR Tx link-layer traffic statistics of the port. 

        :return: the LLR Tx link-layer traffic statistics
        :rtype: P_UE_LLR_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


__all__ = [
    "P_UE_LLR_MODE",
    "P_UE_LLR_RX_STATS",
    "P_UE_LLR_TX_STATS",
]