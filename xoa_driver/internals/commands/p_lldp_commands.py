"""Port LLDP Commands"""
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
    LLDPClearTarget,
    LLDPOpMode,
)

@register_command
@dataclass
class P_LLDP_CLEAR:
    """
    Clear LLDP information for the specified target.
    """

    code: typing.ClassVar[int] = 1009
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int


    class SetDataAttr(RequestBodyStruct):
        target: LLDPClearTarget = field(XmpByte())
        """LLDP clear target."""


    def set(self, target: LLDPClearTarget) -> Token[None]:
        """Set the LLDP clear target.

        :param target: the LLDP clear target
        :type target: LLDPClearTarget
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, target=target))
    
    clear_none = functools.partialmethod(set, LLDPClearTarget.NONE)
    """Not clear LLDP stats or neighbors
    """

    clear_neighbor = functools.partialmethod(set, LLDPClearTarget.NEIGHBOR)
    """Clear LLDP neighbor information, but not LLDP statistics.
    """

    clear_stats = functools.partialmethod(set, LLDPClearTarget.STATS)
    """Clear LLDP statistics, but not LLDP neighbor information.
    """

    clear_all = functools.partialmethod(set, LLDPClearTarget.ALL)
    """Clear both LLDP statistics and neighbor information.
    """
    

@register_command
@dataclass
class P_LLDP_CONFIG:
    """
    LLDP agent configuration for the port, including reinit delay, transmission interval, and transmission hold multiplier.
    """

    code: typing.ClassVar[int] = 1006
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        reinit_delay: int = field(XmpInt())
        """Reinitialization delay in seconds. When a port is disabled, LLDP is disabled or the switch is rebooted, a LLDP shutdown frame is transmitted to the neighboring units, signaling that the LLDP information is not valid anymore. Tx Reinit controls the amount of seconds between the shutdown frame and a new LLDP initialization. 
        
        Default is 2, range is 1 to 10.
        """

        tx_interval: int = field(XmpInt())
        """Transmission interval in seconds. This variable defines the time interval in seconds between transmissions during normal transmission periods. 
        
        Default is 30, range is 1 to 3600.
        """

        tx_hold_multiplier: int = field(XmpInt())
        """Transmission hold multiplier. The number of times the transmission interval is multiplied to determine the hold time for the LLDP packet. It is also used to determine the value of TTL that is carried in LLDP frames transmitted the port.
        
        Default is 4, range is 1 to 100.
        """

        tx_delay: int = field(XmpInt())
        """Minimum time between LLDP frames in seconds. If some configuration is changed (for example, the IP address) a new LLDP frame is transmitted, but the time between the LLDP frames will always be at least the value of ``tx_delay`` seconds. ``tx_delay`` cannot be larger than 1/4 of the ``tx_interval`` value. 
        
        Valid values are restricted to 1 - 8192 seconds.
        """

    class SetDataAttr(RequestBodyStruct):
        reinit_delay: int = field(XmpInt())
        """Reinitialization delay in seconds. When a port is disabled, LLDP is disabled or the switch is rebooted, a LLDP shutdown frame is transmitted to the neighboring units, signaling that the LLDP information is not valid anymore. Tx Reinit controls the amount of seconds between the shutdown frame and a new LLDP initialization. 
        
        Default is 2, range is 1 to 10.
        """

        tx_interval: int = field(XmpInt())
        """Transmission interval in seconds. This variable defines the time interval in seconds between transmissions during normal transmission periods. 
        
        Default is 30, range is 1 to 3600.
        """

        tx_hold_multiplier: int = field(XmpInt())
        """Transmission hold multiplier. The number of times the transmission interval is multiplied to determine the hold time for the LLDP packet. It is also used to determine the value of TTL that is carried in LLDP frames transmitted the port.
        
        Default is 4, range is 1 to 100.
        """

        tx_delay: int = field(XmpInt())
        """Minimum time between LLDP frames in seconds. If some configuration is changed (for example, the IP address) a new LLDP frame is transmitted, but the time between the LLDP frames will always be at least the value of ``tx_delay`` seconds. ``tx_delay`` cannot be larger than 1/4 of the ``tx_interval`` value. 
        
        Valid values are restricted to 1 - 8192 seconds.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the LLDP configuration for the port.

        :return: the LLDP configuration for the port
        :rtype: P_LLDP_CONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, reinit_delay: int, tx_interval: int, tx_hold_multiplier: int, tx_delay: int) -> Token[None]:
        """Set the LLDP configuration for the port.

        :param reinit_delay: Reinitialization delay in seconds
        :type reinit_delay: int
        :param tx_interval: Transmission interval in seconds
        :type tx_interval: int
        :param tx_hold_multiplier: Transmission hold multiplier
        :type tx_hold_multiplier: int
        :param tx_delay: Minimum time between LLDP frames in seconds
        :type tx_delay: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, reinit_delay=reinit_delay, tx_interval=tx_interval, tx_hold_multiplier=tx_hold_multiplier, tx_delay=tx_delay))


@register_command
@dataclass
class P_LLDP_CREATE:
    """
    Create a LLDP agent on the port.
    """

    code: typing.ClassVar[int] = 1000
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lldp_agent_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a LLDP agent on the port.

        LLDP agent index, ranges from 0 to 7. (maximum 8 LLDP agents)
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lldp_agent_xindex]))
    


@register_command
@dataclass
class P_LLDP_DATA:
    """
    Configures the LLDPDU (LLDP Data Unit) for a specified LLDP agent on the port.
    """

    code: typing.ClassVar[int] = 1004
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        data_unit: Hex = field(XmpHex())
        """LLDPDU in hexadecimal string format."""

    class SetDataAttr(RequestBodyStruct):
        
        data_unit: Hex = field(XmpHex())
        """LLDPDU in hexadecimal string format."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLDPDU for the specified LLDP agent on the port.

        :return: the LLDPDU for the specified LLDP agent on the port
        :rtype: P_LLDP_DATA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, data_unit: Hex) -> Token[None]:
        """Set the LLDPDU for the specified LLDP agent on the port.

        :param data_unit: the LLDPDU in hexadecimal string format
        :type data_unit: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, data_unit=data_unit))
    

@register_command
@dataclass
class P_LLDP_DELETE:
    """
    Delete a LLDP agent on the port.
    """

    code: typing.ClassVar[int] = 1002
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lldp_agent_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete a LLDP agent on the port.

        LLDP agent index, ranges from 0 to 7. (maximum 8 LLDP agents)
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._lldp_agent_xindex]))
    


@register_command
@dataclass
class P_LLDP_HEADER:
    """
    Configures the LLDP header (DMAC, SMAC, EtherType) for a specified LLDP agent on the port.
    """

    code: typing.ClassVar[int] = 1005
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int


    class GetDataAttr(ResponseBodyStruct):
        
        header: Hex = field(XmpHex())
        """LLDP frame header in hexadecimal string format. The header includes DMAC, SMAC, and Ethertype.
        
        * The default DMAC is the MAC address of the test port. If the port MAC address is changed, the default DMAC will also be updated to match the new port MAC address.
        * The default SMAC is Nearest Bridge MAC address, ``0x0180C200000E``, as specified in IEEE 802.3-2018.
        * The default Ethertype is ``0x88CC`` for LLDP frames, as specified in IEEE 802.3-2018.
        
        """

    class SetDataAttr(RequestBodyStruct):
        
        header: Hex = field(XmpHex())
        """LLDP frame header in hexadecimal string format. The header includes DMAC, SMAC, and Ethertype.
        
        * The default DMAC is the MAC address of the test port. If the port MAC address is changed, the default DMAC will also be updated to match the new port MAC address.
        * The default SMAC is Nearest Bridge MAC address, ``0x0180C200000E``, as specified in IEEE 802.3-2018.
        * The default Ethertype is ``0x88CC`` for LLDP frames, as specified in IEEE 802.3-2018.
        
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the LLDP header.

        :return: the LLDP header 
        :rtype: P_LLDP_HEADER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, header: Hex) -> Token[None]:
        """Set the description of the port.

        :param header: the LLDP header in hexadecimal string format
        :type header: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, header=header))
    

@register_command
@dataclass
class P_LLDP_INDICES:
    """
    Create multiple LLDP agents or query the existing LLDP agents on the port.
    """

    code: typing.ClassVar[int] = 1001
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        lldp_agent_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """List of LLDP agent indices on the port. Each index ranges from 0 to 7, and a maximum of 8 LLDP agents can be created on the port. The integers do not have to be consecutive. If the list is empty, it indicates that there are no LLDP agents on the port."""

    class SetDataAttr(RequestBodyStruct):
        
        lldp_agent_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """List of LLDP agent indices on the port. Each index ranges from 0 to 7, and a maximum of 8 LLDP agents can be created on the port. The integers do not have to be consecutive. If the list is empty, it indicates that there are no LLDP agents on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the indices of the LLDP agents on the port.

        :return: the indices of the LLDP agents on the port
        :rtype: P_LLDP_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, lldp_agent_indices: typing.List[int]) -> Token[None]:
        """Set the indices of the LLDP agents on the port.

        :param lldp_agent_indices: the list of LLDP agent indices
        :type lldp_agent_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, lldp_agent_indices=lldp_agent_indices))


@register_command
@dataclass
class P_LLDP_NEIGHBORS:
    """
    Displays LLDP neighbors discovered by the port.
    """

    code: typing.ClassVar[int] = 1007
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        neighbors: dict = field(XmpJson(min_len=16))
        """Information of LLDP neighbors."""


    def get(self) -> Token[GetDataAttr]:
        """Get the LLDP neighbors discovered by the port.

        :return: the LLDP neighbors discovered by the port
        :rtype: P_LLDP_NEIGHBORS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_LLDP_OPMODE:
    """
    This configures the LLDP operational mode for the port.
    """

    code: typing.ClassVar[int] = 1003
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        op_mode: LLDPOpMode = field(XmpByte())
        """LLDP operational mode for the port."""

    class SetDataAttr(RequestBodyStruct):
        
        op_mode: LLDPOpMode = field(XmpByte())
        """LLDP operational mode for the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLDP operational mode of the port.

        :return: the LLDP operational mode of the port
        :rtype: P_LLDP_OPMODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, op_mode: LLDPOpMode) -> Token[None]:
        """Set the LLDP operational mode of the port.

        :param op_mode: the LLDP operational mode of the port
        :type op_mode: LLDPOpMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, op_mode=op_mode))


@register_command
@dataclass
class P_LLDP_STATS:
    """
    Displays LLDP interface statistics for the port (all agents on the port combined).
    """

    code: typing.ClassVar[int] = 1008
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        tx_frame_count: int = field(XmpLong())
        """Number of LLDP frames transmitted."""

        rx_frame_count: int = field(XmpLong())
        """Number of LLDP frames received."""

        rx_frame_discard_count: int = field(XmpLong())
        """Number of LLDP frames discarded. LLDP frames that contain detectable errors in the first three mandatory TLVs are discarded."""

        rx_tlv_discarded: int = field(XmpLong())
        """Number of TLVs discarded. Optional TLVs that contain detectable errors are discarded."""

        rx_tlv_unrecognized: int = field(XmpLong())
        """Number of unrecognized TLVs received. An unrecognized TLV is referred to as the TLV whose type value is in the range of reserved TLV types. An unrecognized TLV may be a basic management TLV from a later LLDP version."""

        rx_aged_out_count: int = field(XmpLong())
        """Number of aged out. This counter provides a count of the times that a neighbor’s information has been deleted due to TTL expiration."""


    def get(self) -> Token[GetDataAttr]:
        """Get the description of the port.

        :return: the description of the port
        :rtype: P_COMMENT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


__all__ = [
    "P_LLDP_CLEAR",
    "P_LLDP_CONFIG",
    "P_LLDP_CREATE",
    "P_LLDP_DATA",
    "P_LLDP_DELETE",
    "P_LLDP_HEADER",
    "P_LLDP_INDICES",
    "P_LLDP_NEIGHBORS",
    "P_LLDP_OPMODE",
    "P_LLDP_STATS",
]