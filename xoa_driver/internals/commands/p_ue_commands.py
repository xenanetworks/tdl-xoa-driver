"""Port Commands - Ultra Ethernet"""
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
    XmpJson,
)
from .enums import (
    OnOff,
    YesNo,
    UecCtlosClearDirection,
    UecLinkOptionLlr,
    UecLlrBehavior,
    UecLlrInitEchoMode,
    UecLlrEchoCheck,
    UecLlrTxErrType,
    UecLlrTxErrPattern,
    UecLlrTxFsmState,
    UecLlrRxFsmState,
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

        llr_init_seq: Hex = field(XmpHex(size=3))
        """The LLR_INIT sequence number. 3 bytes in hex format."""

        llr_init_data: Hex = field(XmpHex(size=2))
        """The LLR_INIT data. 2 bytes in hex format."""

        llr_init_echo_seq: Hex = field(XmpHex(size=3))
        """The LLR_INIT_ECHO sequence number. 3 bytes in hex format."""

        llr_init_echo_data: Hex = field(XmpHex(size=2))
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

        llr_init_seq: Hex = field(XmpHex(size=3))
        """The LLR_INIT sequence number. 3 bytes in hex format."""

        llr_init_data: Hex = field(XmpHex(size=2))
        """The LLR_INIT data. 2 bytes in hex format."""

        llr_init_echo_seq: Hex = field(XmpHex(size=3))
        """The LLR_INIT_ECHO sequence number. 3 bytes in hex format."""

        llr_init_echo_data: Hex = field(XmpHex(size=2))
        """The LLR_INIT_ECHO data. 2 bytes in hex format."""


    def get(self) -> Token[GetDataAttr]:
        """Get UE CtlOS Tx statistics.

        :return: the UE CtlOS Tx statistics
        :rtype: P_UE_CTLOS_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_UE_LINKNEG_OPTIONS:
    """
    This command selects which LLDP agent to use for UE Link Negotiation Options, and configures the desired LLR-W (local) setting. After the set operation, the UE Link Negotiation Options TLV will be added to the LLDPDU (if it is not already present in the LLDPDU) or replace the existing one (if Options TLV was previously added in LLDP configurataion).

    The UE Link Negotiation Options TLV is used to discover and configure advanced UE link capabilities. Currently, the Options TLV is used to advertise the following UEC Link features:

      * Link Layer Retry (LLR): Provides link level re-transmissions for packets with errors.

    .. note::

        In Link Negotiation for LLR, the R/W access of the four flags are:

        * LLR-W (local): RW
        * LLR-W (remote): RO
        * LLR-E (local): RO
        * LLR-E (remote): RO

        When Link Negotiation is enabled on a LLDP agent, the only configurable parameter is ``LLR-W (local)``. To read ``LLR-W (remote)``, use ``P_UE_LINKNEG_OPTIONS_STATUS``. To read ``LLR-E (local)`` and ``LLR-E (remote)``, use ``P_UE_LLR_MODE``

    To disable Link Negotation for UE Link Options, send the command with no parameters. This will remove the Options TLV from the LLDPDU and disable Link Negotiation for UE Link Options.
    """

    code: typing.ClassVar[int] = 1016
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        lldp_agent_index: int = field(XmpByte())
        """integer, The LLDP agent index to use for advertising the advanced UE link capabilities. An LLDP agent must be created and configured separately using the LLDP commands before it can be used with this command. 
        
        Values: 0 to 7.
        """

        llr_wanted_local: UecLinkOptionLlr = field(XmpByte())
        """coded integer, Indicates whether the local port wants LLR.
        """

    class SetDataAttr(RequestBodyStruct):
        lldp_agent_index: int = field(XmpByte())
        """integer, The LLDP agent index to use for advertising the advanced UE link capabilities. An LLDP agent must be created and configured separately using the LLDP commands before it can be used with this command. 
        
        Values: 0 to 7.
        """

        llr_wanted_local: UecLinkOptionLlr = field(XmpByte())
        """coded integer, Indicates whether the local port wants LLR.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the port.

        :return: the description of the port
        :rtype: P_UE_LINKNEG_OPTIONS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, lldp_agent_index: int, llr_wanted_local: UecLinkOptionLlr) -> Token[None]:
        """Set the UE Link Negotiation Options.

        :param lldp_agent_index: The LLDP agent index to use for advertising the advanced UE link capabilities. Values: 0 to 7.
        :type lldp_agent_index: int
        :param llr_wanted_local: Indicates whether the local port wants LLR. 
        :type llr_wanted_local: UecLinkOptionLlr
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, lldp_agent_index=lldp_agent_index, llr_wanted_local=llr_wanted_local))


@register_command
@dataclass
class P_UE_LINKNEG_OPTIONS_STATUS:
    """
    Read ``LLR-W (local)`` and ``LLR-W (remote)`` of the port, which indicates whether the local and remote ports want to use LLR. This command is for read-only purposes and does not change any configuration or behavior of the LLR.
    """

    code: typing.ClassVar[int] = 1029
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        llr_wanted_local: UecLinkOptionLlr = field(XmpByte())
        """coded integer, Indicates whether the local port wants LLR.
        """

        llr_wanted_remote: UecLinkOptionLlr = field(XmpByte())
        """coded integer, Indicates whether the remote port wants LLR.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the current UE link negotiation options status.

        :return: the current UE link negotiation options status
        :rtype: P_UE_LINKNEG_OPTIONS_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



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
        llr_mode_local: OnOff = field(XmpByte())
        """coded integer, LLR mode of the local port."""

        llr_mode_remote: OnOff = field(XmpByte())
        """coded integer, LLR mode of the remote port."""


    class SetDataAttr(RequestBodyStruct):
        llr_mode_local: OnOff = field(XmpByte())
        """coded integer, LLR mode of the local port."""

        llr_mode_remote: OnOff = field(XmpByte())
        """coded integer, LLR mode of the remote port."""


    def get(self) -> Token[GetDataAttr]:
        """Get the LLR mode of the local port.

        :return: the LLR mode of the local port
        :rtype: P_UE_LLR_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, llr_mode_local: OnOff, llr_mode_remote: OnOff) -> Token[None]:
        """Set the LLR mode of the local port.

        :param llr_mode_local: the LLR mode of the local port
        :type llr_mode_local: OnOff
        :param llr_mode_remote: the LLR mode of the remote port
        :type llr_mode_remote: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, llr_mode_local=llr_mode_local, llr_mode_remote=llr_mode_remote))


    set_on = functools.partialmethod(set, llr_mode_local=OnOff.ON, llr_mode_remote=OnOff.ON)
    """Set LLR local to ON, LLR remote to ON."""

    set_off = functools.partialmethod(set, llr_mode_local=OnOff.OFF, llr_mode_remote=OnOff.OFF)
    """Set LLR local to OFF, LLR remote to OFF."""




@register_command
@dataclass
class P_UE_LLR_RX_STATS:
    """
    Get the LLR Rx link-layer traffic statistics of the port. 
    """

    code: typing.ClassVar[int] = 1024
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        rx_llr_eligible_good_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames received with a good FCS."""

        rx_llr_eligible_poisoned_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames received with a poisoned FCS."""

        rx_llr_eligible_bad_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames received with a bad FCS."""

        rx_llr_eligible_total: int = field(XmpLong())
        """The total number of LLR-eligible frames received."""

        rx_llr_eligible_good_fcs_exp_seq: int = field(XmpLong())
        """The number of LLR-eligible frames received with a good FCS that had the expected sequence number."""

        rx_llr_eligible_poisoned_fcs_exp_seq: int = field(XmpLong())
        """The number of LLR-eligible frames received with a poisoned FCS that had the expected sequence number."""

        rx_llr_eligible_bad_fcs_exp_seq: int = field(XmpLong())
        """The number of LLR-eligible frames received with a bad FCS that had the expected sequence number."""

        rx_llr_eligible_total_exp_seq: int = field(XmpLong())
        """The total number of LLR-eligible frames received with the expected sequence number (irrespective of FCS status)."""

        rx_llr_eligible_missing_seq: int = field(XmpLong())
        """The number of LLR-eligible frames received that had a sequence number that indicated a missing LLR-eligible frame in the sequence (irrespective of FCS status)."""

        rx_llr_eligible_duplicate_seq: int = field(XmpLong())
        """The number of LLR-eligible frames received that had a duplicate sequence number (irrespective of FCS status)."""

        rx_llr_ineligible_good_fcs: int = field(XmpLong())
        """The number of LLR-ineligible frames received with a good FCS."""

        rx_llr_ineligible_bad_fcs: int = field(XmpLong())
        """The number of LLR-ineligible frames received with a bad FCS."""

        rx_llr_ineligible_total: int = field(XmpLong())
        """The total number of LLR-ineligible frames received."""

        rx_replay_operations: int = field(XmpLong())
        """The number of replay operations detected."""


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

    code: typing.ClassVar[int] = 1023
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        
        tx_llr_eligible_good_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a good FCS."""

        tx_llr_eligible_poisoned_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a poisoned FCS."""

        tx_llr_eligible_bad_fcs: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a bad FCS."""

        tx_llr_eligible_discard: int = field(XmpLong())
        """The number of LLR-eligible frames discarded by the LLR TX when the TX state machine is in the INIT state and the llr_init_behavior is set to DISCARD, or when the TX state machine is in the FLUSH state and the llr_flush_behavior is set to DISCARD."""

        tx_llr_eligible_total: int = field(XmpLong())
        """The total number of LLR-eligible frames transmitted."""

        tx_llr_ineligible_good_fcs: int = field(XmpLong())
        """The number of LLR-ineligible frames transmitted with a good FCS."""

        tx_llr_ineligible_bad_fcs: int = field(XmpLong())
        """The number of LLR-ineligible frames transmitted with a bad FCS."""

        tx_llr_ineligible_total: int = field(XmpLong())
        """The total number of LLR-ineligible frames transmitted."""

        tx_replayed: int = field(XmpLong())
        """The number of frames transmitted by the LLR TX that were replayed from the LLR replay buffer."""

        tx_llr_eligible_good_fcs_good_seq: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a good FCS and a good sequence number."""

        tx_llr_eligible_poisoned_fcs_good_seq: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a poisoned FCS and a good sequence number."""

        tx_llr_eligible_bad_fcs_good_seq: int = field(XmpLong())
        """The number of LLR-eligible frames transmitted with a bad FCS and a good sequence number."""

        tx_llr_eligible_missing_seq: int = field(XmpLong())
        """The number of LLR-eligible frames that with missing sequence number (irrespective of the FCS)."""

        tx_llr_eligible_duplicate_seq: int = field(XmpLong())
        """The number of LLR-eligible frames that with duplicate sequence number (irrespective of the FCS)."""

        tx_replay_operations: int = field(XmpLong())
        """The number of times the LLR TX state machine has exited the REPLAY state (replay operations)."""


    
    def get(self) -> Token[GetDataAttr]:
        """Get the LLR Tx link-layer traffic statistics of the port. 

        :return: the LLR Tx link-layer traffic statistics
        :rtype: P_UE_LLR_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_UE_CTLOS_SPACING:
    """
    Configures the CtlOS spacing parameters of the port.
    """

    code: typing.ClassVar[int] = 1010
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        reserved1: int = field(XmpInt())
        """integer, reserved."""

        min_spacing: int = field(XmpInt())
        """integer, the minimum CtlOS spacing."""

        reserved2: int = field(XmpInt())
        """integer, reserved."""

        reserved3: int = field(XmpInt())
        """integer, reserved."""

    class SetDataAttr(RequestBodyStruct):
        reserved1: int = field(XmpInt())
        """integer, reserved."""

        min_spacing: int = field(XmpInt())
        """integer, the minimum CtlOS spacing."""

        reserved2: int = field(XmpInt())
        """integer, reserved."""

        reserved3: int = field(XmpInt())
        """integer, reserved."""

    def get(self) -> Token[GetDataAttr]:
        """Get the CtlOS spacing parameters of the port.

        :return: the CtlOS spacing parameters of the port
        :rtype: P_UE_CTLOS_SPACING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, reserved1: int, min_spacing: int, reserved2: int, reserved3: int) -> Token[None]:
        """Set the CtlOS spacing parameters of the port.

        :param reserved1: the target CtlOS spacing
        :type reserved1: int
        :param min_spacing: the minimum CtlOS spacing
        :type min_spacing: int
        :param reserved2: reserved
        :type reserved2: int
        :param reserved3: reserved
        :type reserved3: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, target_spacing=target_spacing, min_spacing=min_spacing, reserved1=reserved1, reserved2=reserved2))


@register_command
@dataclass
class P_UE_LLR_REPLAY:
    """
    Configures the LLR replay parameters of the port.
    """

    code: typing.ClassVar[int] = 1014
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        outstanding_seq_max: int = field(XmpInt())
        """integer, a configuration for the maximum permitted value of outstanding_seq. Values: 0 to 524288. The absolute maximum permitted value for outstanding_seq_max is 524288, which is equivalent to consuming half of the total sequence number space."""

        reserved1: int = field(XmpInt())
        """integer, reserved for future use. Value is ignored in the current implementation."""

        replay_timer_max: int = field(XmpInt())
        """integer, configuration to set the value of replay_timer at which replay_timer_expired is set and a replay is initiated. Values: 0 to 65535 ns with a resolution better than 10 ns."""

        replay_ct_max: int = field(XmpInt())
        """integer, a configuration to set the maximum number of times a replay is performed before the LLR mechanism gives up and enters the FLUSH state. A value of 255 (i.e., all-ones) is used to indicate that there is no maximum. Values: 0 to 255."""

        reserved2: int = field(XmpLong())
        """long integer, reserved for future use. Value is ignored in the current implementation."""

        data_age_timer_max: int = field(XmpLong())
        """long integer, the value at which the data_age_timer is considered to have expired. Values: 0 to 4,290,000,000 ns with a resolution better than 100 ns."""

    class SetDataAttr(RequestBodyStruct):
        outstanding_seq_max: int = field(XmpInt())
        """integer, a configuration for the maximum permitted value of outstanding_seq. Values: 0 to 524288. The absolute maximum permitted value for outstanding_seq_max is 524288, which is equivalent to consuming half of the total sequence number space."""

        reserved1: int = field(XmpInt())
        """integer, reserved for future use. Value is ignored in the current implementation."""

        replay_timer_max: int = field(XmpInt())
        """integer, configuration to set the value of replay_timer at which replay_timer_expired is set and a replay is initiated. Values: 0 to 65535 ns with a resolution better than 10 ns."""

        replay_ct_max: int = field(XmpInt())
        """integer, a configuration to set the maximum number of times a replay is performed before the LLR mechanism gives up and enters the FLUSH state. A value of 255 (i.e., all-ones) is used to indicate that there is no maximum. Values: 0 to 255."""

        reserved2: int = field(XmpLong())
        """long integer, reserved for future use. Value is ignored in the current implementation."""

        data_age_timer_max: int = field(XmpLong())
        """long integer, the value at which the data_age_timer is considered to have expired. Values: 0 to 4,290,000,000 ns with a resolution better than 100 ns."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR replay parameters of the port.

        :return: the LLR replay parameters of the port
        :rtype: P_UE_LLR_REPLAY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, outstanding_seq_max: int, reserved1: int, replay_timer_max: int, replay_ct_max: int, reserved2: int, data_age_timer_max: int) -> Token[None]:
        """Set the LLR replay parameters of the port.

        :param outstanding_seq_max: a configuration for the maximum permitted value of outstanding_seq. Values: 0 to 524288.
        :type outstanding_seq_max: int
        :param reserved1: reserved for future use. Value is ignored in the current implementation.
        :type reserved1: int
        :param replay_timer_max: configuration to set the value of replay_timer at which replay_timer_expired is set and a replay is initiated. Values: 0 to 65535 ns with a resolution better than 10 ns.
        :type replay_timer_max: int
        :param replay_ct_max: the maximum number of times a replay is performed before the LLR mechanism gives up and enters the FLUSH state. A value of 255 indicates no maximum. Values: 0 to 255.
        :type replay_ct_max: int
        :param reserved2: reserved for future use. Value is ignored in the current implementation.
        :type reserved2: int
        :param data_age_timer_max: the value at which the data_age_timer is considered to have expired. Values: 0 to 4,290,000,000 ns with a resolution better than 100 ns.
        :type data_age_timer_max: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, outstanding_seq_max=outstanding_seq_max, reserved1=reserved1, replay_timer_max=replay_timer_max, replay_ct_max=replay_ct_max, reserved2=reserved2, data_age_timer_max=data_age_timer_max))


@register_command
@dataclass
class P_UE_LLR_BEHAVIOR:
    """
    Configures the LLR behavior of the port for the INIT and FLUSH states.
    """

    code: typing.ClassVar[int] = 1015
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        llr_init_behavior: UecLlrBehavior = field(XmpByte())
        """coded byte, the LLR behavior for LLR-eligible frames when the TX state machine is in the INIT state."""

        llr_flush_behavior: UecLlrBehavior = field(XmpByte())
        """coded byte, the LLR behavior for LLR-eligible frames when the TX state machine is in the FLUSH state."""

        re_init_on_discard: YesNo = field(XmpByte())
        """coded byte, whether to re-initialize the LLR on discard."""

    class SetDataAttr(RequestBodyStruct):
        llr_init_behavior: UecLlrBehavior = field(XmpByte())
        """coded byte, the LLR behavior for LLR-eligible frames when the TX state machine is in the INIT state."""

        llr_flush_behavior: UecLlrBehavior = field(XmpByte())
        """coded byte, the LLR behavior for LLR-eligible frames when the TX state machine is in the FLUSH state."""

        re_init_on_discard: YesNo = field(XmpByte())
        """coded byte, whether to re-initialize the LLR on discard."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR behavior of the port.

        :return: the LLR behavior of the port
        :rtype: P_UE_LLR_BEHAVIOR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, llr_init_behavior: UecLlrBehavior, llr_flush_behavior: UecLlrBehavior, re_init_on_discard: YesNo) -> Token[None]:
        """Set the LLR behavior of the port.

        :param llr_init_behavior: the LLR behavior for LLR-eligible frames when the TX state machine is in the INIT state
        :type llr_init_behavior: UecLlrBehavior
        :param llr_flush_behavior: the LLR behavior for LLR-eligible frames when the TX state machine is in the FLUSH state
        :type llr_flush_behavior: UecLlrBehavior
        :param re_init_on_discard: whether to re-initialize the LLR on discard
        :type re_init_on_discard: YesNo
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, llr_init_behavior=llr_init_behavior, llr_flush_behavior=llr_flush_behavior, re_init_on_discard=re_init_on_discard))


@register_command
@dataclass
class P_UE_LLR_INIT:
    """
    Configures the LLR INIT parameters of the port.
    """

    code: typing.ClassVar[int] = 1017
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        init_seq: Hex = field(XmpHex(size=3))
        """3 bytes in hex format, the 24-bit LLR_INIT sequence number."""

        init_data: Hex = field(XmpHex(size=2))
        """2 bytes in hex format, the 16-bit LLR_INIT data."""

        min_spacing_multiplier: int = field(XmpInt())
        """integer, the minimum spacing multiplier."""

    class SetDataAttr(RequestBodyStruct):
        init_seq: Hex = field(XmpHex(size=3))
        """3 bytes in hex format, the 24-bit LLR_INIT sequence number."""

        init_data: Hex = field(XmpHex(size=2))
        """2 bytes in hex format, the 16-bit LLR_INIT data."""

        min_spacing_multiplier: int = field(XmpInt())
        """integer, the minimum spacing multiplier."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR INIT parameters of the port.

        :return: the LLR INIT parameters of the port
        :rtype: P_UE_LLR_INIT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, init_seq: Hex, init_data: Hex, min_spacing_multiplier: int) -> Token[None]:
        """Set the LLR INIT parameters of the port.

        :param init_seq: the 24-bit LLR_INIT sequence number (3 bytes)
        :type init_seq: Hex
        :param init_data: the 16-bit LLR_INIT data (2 bytes)
        :type init_data: Hex
        :param min_spacing_multiplier: the minimum spacing multiplier
        :type min_spacing_multiplier: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, init_seq=init_seq, init_data=init_data, min_spacing_multiplier=min_spacing_multiplier))


@register_command
@dataclass
class P_UE_LLR_INIT_ECHO:
    """
    Configures the LLR INIT_ECHO parameters of the port.
    """

    code: typing.ClassVar[int] = 1018
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        init_seq_mode: UecLlrInitEchoMode = field(XmpByte())
        """coded byte, the source mode of the INIT_ECHO sequence number."""

        init_seq: Hex = field(XmpHex(size=3))
        """3 bytes in hex format, the 24-bit INIT_ECHO sequence number when manual mode is used."""

        init_data_mode: UecLlrInitEchoMode = field(XmpByte())
        """coded byte, the source mode of the INIT_ECHO data."""

        init_data: Hex = field(XmpHex(size=2))
        """2 bytes in hex format, the 16-bit INIT_ECHO data when manual mode is used."""

    class SetDataAttr(RequestBodyStruct):
        init_seq_mode: UecLlrInitEchoMode = field(XmpByte())
        """coded byte, the source mode of the INIT_ECHO sequence number."""

        init_seq: Hex = field(XmpHex(size=3))
        """3 bytes in hex format, the 24-bit INIT_ECHO sequence number when manual mode is used."""

        init_data_mode: UecLlrInitEchoMode = field(XmpByte())
        """coded byte, the source mode of the INIT_ECHO data."""

        init_data: Hex = field(XmpHex(size=2))
        """2 bytes in hex format, the 16-bit INIT_ECHO data when manual mode is used."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR INIT_ECHO parameters of the port.

        :return: the LLR INIT_ECHO parameters of the port
        :rtype: P_UE_LLR_INIT_ECHO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, init_seq_mode: UecLlrInitEchoMode, init_seq: Hex, init_data_mode: UecLlrInitEchoMode, init_data: Hex) -> Token[None]:
        """Set the LLR INIT_ECHO parameters of the port.

        :param init_seq_mode: the source mode of the INIT_ECHO sequence number
        :type init_seq_mode: UecLlrInitEchoMode
        :param init_seq: the 24-bit INIT_ECHO sequence number when manual mode is used (3 bytes)
        :type init_seq: Hex
        :param init_data_mode: the source mode of the INIT_ECHO data
        :type init_data_mode: UecLlrInitEchoMode
        :param init_data: the 16-bit INIT_ECHO data when manual mode is used (2 bytes)
        :type init_data: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, init_seq_mode=init_seq_mode, init_seq=init_seq, init_data_mode=init_data_mode, init_data=init_data))


@register_command
@dataclass
class P_UE_LLR_ACKNACK:
    """
    Configures the LLR ACK/NACK spacing parameters of the port.
    """

    code: typing.ClassVar[int] = 1019
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        target_spacing: int = field(XmpInt())
        """integer, the target ACK/NACK spacing."""

        min_spacing: int = field(XmpInt())
        """integer, the minimum ACK/NACK spacing."""

        max_spacing: int = field(XmpInt())
        """integer, the maximum ACK/NACK spacing."""

    class SetDataAttr(RequestBodyStruct):
        target_spacing: int = field(XmpInt())
        """integer, the target ACK/NACK spacing."""

        min_spacing: int = field(XmpInt())
        """integer, the minimum ACK/NACK spacing."""

        max_spacing: int = field(XmpInt())
        """integer, the maximum ACK/NACK spacing."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR ACK/NACK spacing parameters of the port.

        :return: the LLR ACK/NACK spacing parameters of the port
        :rtype: P_UE_LLR_ACKNACK.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, target_spacing: int, min_spacing: int, max_spacing: int) -> Token[None]:
        """Set the LLR ACK/NACK spacing parameters of the port.

        :param target_spacing: the target ACK/NACK spacing
        :type target_spacing: int
        :param min_spacing: the minimum ACK/NACK spacing
        :type min_spacing: int
        :param max_spacing: the maximum ACK/NACK spacing
        :type max_spacing: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, target_spacing=target_spacing, min_spacing=min_spacing, max_spacing=max_spacing))


@register_command
@dataclass
class P_UE_LLR_TXERR:
    """
    Configures the LLR TX error injection of the port.
    """

    code: typing.ClassVar[int] = 1025
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        error_type: UecLlrTxErrType = field(XmpByte())
        """coded byte, the type of error to inject."""

        pattern: UecLlrTxErrPattern = field(XmpByte())
        """coded byte, the pattern of error injection."""

        burst_size: int = field(XmpInt())
        """integer, the number of errors in a burst."""

        burst_interval: int = field(XmpInt())
        """integer, the interval between bursts."""

    class SetDataAttr(RequestBodyStruct):
        error_type: UecLlrTxErrType = field(XmpByte())
        """coded byte, the type of error to inject."""

        pattern: UecLlrTxErrPattern = field(XmpByte())
        """coded byte, the pattern of error injection."""

        burst_size: int = field(XmpInt())
        """integer, the number of errors in a burst."""

        burst_interval: int = field(XmpInt())
        """integer, the interval between bursts."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR TX error injection configuration of the port.

        :return: the LLR TX error injection configuration of the port
        :rtype: P_UE_LLR_TXERR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, error_type: UecLlrTxErrType, pattern: UecLlrTxErrPattern, burst_size: int, burst_interval: int) -> Token[None]:
        """Set the LLR TX error injection configuration of the port.

        :param error_type: the type of error to inject
        :type error_type: UecLlrTxErrType
        :param pattern: the pattern of error injection
        :type pattern: UecLlrTxErrPattern
        :param burst_size: the number of errors in a burst
        :type burst_size: int
        :param burst_interval: the interval between bursts
        :type burst_interval: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, error_type=error_type, pattern=pattern, burst_size=burst_size, burst_interval=burst_interval))


@register_command
@dataclass
class P_UE_LLR_POISONFCS:
    """
    Configure the FCS poison pattern for LLR-eligible frames when injecting poisoned FCS errors using ``P_UE_LLR_INJECT_ERR`` with the ``type = FCS_POISONED``.
    """

    code: typing.ClassVar[int] = 1028
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        pattern: Hex = field(XmpHex(size=4))
        """4 bytes in hex format, FCS poison pattern. Length is 32 bits (4 bytes). The default value is 0xAAAAAAAA."""

    class SetDataAttr(RequestBodyStruct):
        pattern: Hex = field(XmpHex(size=4))
        """4 bytes in hex format, FCS poison pattern. Length is 32 bits (4 bytes). The default value is 0xAAAAAAAA."""

    def get(self) -> Token[GetDataAttr]:
        """Get the FCS poison pattern of the port.

        :return: the FCS poison pattern of the port
        :rtype: P_UE_LLR_POISONFCS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, pattern: Hex) -> Token[None]:
        """Set the FCS poison pattern of the port.

        :param pattern: FCS poison pattern. Length is 32 bits (4 bytes). The default value is 0xAAAAAAAA.
        :type pattern: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, pattern=pattern))


@register_command
@dataclass
class P_UE_LLR_INIT_ECHO_CHK:
    """
    Configures the validation of the LLR INIT_ECHO sequence number and data of the port.
    """

    code: typing.ClassVar[int] = 1031
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        validate_init_seq: UecLlrEchoCheck = field(XmpByte())
        """coded byte, whether to validate the INIT_ECHO sequence number."""

        validate_init_data: UecLlrEchoCheck = field(XmpByte())
        """coded byte, whether to validate the INIT_ECHO data."""

    class SetDataAttr(RequestBodyStruct):
        validate_init_seq: UecLlrEchoCheck = field(XmpByte())
        """coded byte, whether to validate the INIT_ECHO sequence number."""

        validate_init_data: UecLlrEchoCheck = field(XmpByte())
        """coded byte, whether to validate the INIT_ECHO data."""

    def get(self) -> Token[GetDataAttr]:
        """Get the LLR INIT_ECHO validation configuration of the port.

        :return: the LLR INIT_ECHO validation configuration of the port
        :rtype: P_UE_LLR_INIT_ECHO_CHK.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, validate_init_seq: UecLlrEchoCheck, validate_init_data: UecLlrEchoCheck) -> Token[None]:
        """Set the LLR INIT_ECHO validation configuration of the port.

        :param validate_init_seq: whether to validate the INIT_ECHO sequence number
        :type validate_init_seq: UecLlrEchoCheck
        :param validate_init_data: whether to validate the INIT_ECHO data
        :type validate_init_data: UecLlrEchoCheck
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, validate_init_seq=validate_init_seq, validate_init_data=validate_init_data))


@register_command
@dataclass
class P_UE_LLR_TXFSM_STATE:
    """
    Return the current state of the LLR Tx FSM that the port is in, along with the current values of the relevant timers and counters for that state. The possible states are: LLR_OFF, INIT, ADVANCE, REPLAY, and FLUSH. The specific timers and counters returned depend on the current state of the FSM.
    """

    code: typing.ClassVar[int] = 1021
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        txfsm_state: UecLlrTxFsmState = field(XmpByte())
        """coded byte, the current state of the LLR Tx FSM that the port is in."""

        ns_in_llr_off: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the LLR_OFF state since the last time it was cleared."""

        ns_in_init: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the INIT state since the last time it was cleared."""

        ns_in_advance: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the ADVANCE state since the last time it was cleared."""

        ns_in_replay: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the REPLAY state since the last time it was cleared."""

        ns_in_flush: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the FLUSH state since the last time it was cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get the state of the LLR TX finite state machine of the port.

        :return: the state of the LLR TX finite state machine of the port
        :rtype: P_UE_LLR_TXFSM_STATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_LLR_RXFSM_STATE:
    """
    Return the current state of the LLR Rx FSM that the port is in, along with the current values of the relevant timers and counters for that state. The possible states are: OFF, SEND_ACKS, SEND_NACK, and NACK_SENT. The specific timers and counters returned depend on the current state of the FSM.
    """

    code: typing.ClassVar[int] = 1022
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rxfsm_state: UecLlrRxFsmState = field(XmpByte())
        """coded byte, the current state of the LLR Rx FSM that the port is in."""

        ns_in_off: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the OFF state since the last time it was cleared."""

        ns_in_send_acks: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the SEND_ACKS state since the last time it was cleared."""

        ns_in_send_nack: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the SEND_NACK state since the last time it was cleared."""

        ns_in_nack_sent: int = field(XmpLong())
        """long integer, the number of nanoseconds the FSM has been in the NACK_SENT state since the last time it was cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get the state of the LLR RX finite state machine of the port.

        :return: the state of the LLR RX finite state machine of the port
        :rtype: P_UE_LLR_RXFSM_STATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_LLR_STATUS:
    """
    Get the active status of the LLR of the port.
    """

    code: typing.ClassVar[int] = 1030
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        status: YesNo = field(XmpByte())
        """coded byte, whether the LLR is active."""

    def get(self) -> Token[GetDataAttr]:
        """Get the active status of the LLR of the port.

        :return: the active status of the LLR of the port
        :rtype: P_UE_LLR_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_CTLOS_TX_INTERVAL:
    """
    Get the CtlOS Tx interval statistics of the port. For each CtlOS message type, the minimum, maximum, and average intervals are reported.
    """

    code: typing.ClassVar[int] = 1032
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ctlos_min: int = field(XmpLong())
        """long integer, the minimum CtlOS Tx interval."""

        ctlos_max: int = field(XmpLong())
        """long integer, the maximum CtlOS Tx interval."""

        ctlos_avg: int = field(XmpLong())
        """long integer, the average CtlOS Tx interval."""

        llr_init_min: int = field(XmpLong())
        """long integer, the minimum LLR_INIT Tx interval."""

        llr_init_max: int = field(XmpLong())
        """long integer, the maximum LLR_INIT Tx interval."""

        llr_init_avg: int = field(XmpLong())
        """long integer, the average LLR_INIT Tx interval."""

        llr_init_echo_min: int = field(XmpLong())
        """long integer, the minimum LLR_INIT_ECHO Tx interval."""

        llr_init_echo_max: int = field(XmpLong())
        """long integer, the maximum LLR_INIT_ECHO Tx interval."""

        llr_init_echo_avg: int = field(XmpLong())
        """long integer, the average LLR_INIT_ECHO Tx interval."""

        llr_ack_min: int = field(XmpLong())
        """long integer, the minimum LLR_ACK Tx interval."""

        llr_ack_max: int = field(XmpLong())
        """long integer, the maximum LLR_ACK Tx interval."""

        llr_ack_avg: int = field(XmpLong())
        """long integer, the average LLR_ACK Tx interval."""

        llr_nack_min: int = field(XmpLong())
        """long integer, the minimum LLR_NACK Tx interval."""

        llr_nack_max: int = field(XmpLong())
        """long integer, the maximum LLR_NACK Tx interval."""

        llr_nack_avg: int = field(XmpLong())
        """long integer, the average LLR_NACK Tx interval."""

    def get(self) -> Token[GetDataAttr]:
        """Get the CtlOS Tx interval statistics of the port.

        :return: the CtlOS Tx interval statistics of the port
        :rtype: P_UE_CTLOS_TX_INTERVAL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_CTLOS_RX_INTERVAL:
    """
    Get the CtlOS Rx interval statistics of the port. For each CtlOS message type, the minimum, maximum, and average intervals are reported.
    """

    code: typing.ClassVar[int] = 1033
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ctlos_min: int = field(XmpLong())
        """long integer, the minimum CtlOS Rx interval."""

        ctlos_max: int = field(XmpLong())
        """long integer, the maximum CtlOS Rx interval."""

        ctlos_avg: int = field(XmpLong())
        """long integer, the average CtlOS Rx interval."""

        llr_init_min: int = field(XmpLong())
        """long integer, the minimum LLR_INIT Rx interval."""

        llr_init_max: int = field(XmpLong())
        """long integer, the maximum LLR_INIT Rx interval."""

        llr_init_avg: int = field(XmpLong())
        """long integer, the average LLR_INIT Rx interval."""

        llr_init_echo_min: int = field(XmpLong())
        """long integer, the minimum LLR_INIT_ECHO Rx interval."""

        llr_init_echo_max: int = field(XmpLong())
        """long integer, the maximum LLR_INIT_ECHO Rx interval."""

        llr_init_echo_avg: int = field(XmpLong())
        """long integer, the average LLR_INIT_ECHO Rx interval."""

        llr_ack_min: int = field(XmpLong())
        """long integer, the minimum LLR_ACK Rx interval."""

        llr_ack_max: int = field(XmpLong())
        """long integer, the maximum LLR_ACK Rx interval."""

        llr_ack_avg: int = field(XmpLong())
        """long integer, the average LLR_ACK Rx interval."""

        llr_nack_min: int = field(XmpLong())
        """long integer, the minimum LLR_NACK Rx interval."""

        llr_nack_max: int = field(XmpLong())
        """long integer, the maximum LLR_NACK Rx interval."""

        llr_nack_avg: int = field(XmpLong())
        """long integer, the average LLR_NACK Rx interval."""

    def get(self) -> Token[GetDataAttr]:
        """Get the CtlOS Rx interval statistics of the port.

        :return: the CtlOS Rx interval statistics of the port
        :rtype: P_UE_CTLOS_RX_INTERVAL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class P_UE_CTLOS_RX_ERRORS:
    """
    Get the CtlOS Rx error counters of the port.
    """

    code: typing.ClassVar[int] = 1034
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        ctlos_msg_type_errors: int = field(XmpLong())
        """long integer, the number of CtlOS message type errors."""

        ctlos_padding_errors: int = field(XmpLong())
        """long integer, the number of CtlOS padding errors."""

        llr_init_echo_invalid_init_seq: int = field(XmpLong())
        """long integer, the number of LLR_INIT_ECHO with an invalid INIT sequence number."""

        llr_init_echo_invalid_init_data: int = field(XmpLong())
        """long integer, the number of LLR_INIT_ECHO with invalid INIT data."""

        llr_init_interval_low: int = field(XmpLong())
        """long integer, the number of LLR_INIT received with an interval that is too low."""

        llr_ack_nack_interval_high: int = field(XmpLong())
        """long integer, the number of LLR_ACK/NACK received with an interval that is too high."""

        llr_ack_nack_interval_low: int = field(XmpLong())
        """long integer, the number of LLR_ACK/NACK received with an interval that is too low."""

        llr_ctlos_padding_error: int = field(XmpLong())
        """long integer, the number of LLR CtlOS padding errors."""

    def get(self) -> Token[GetDataAttr]:
        """Get the CtlOS Rx error counters of the port.

        :return: the CtlOS Rx error counters of the port
        :rtype: P_UE_CTLOS_RX_ERRORS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



__all__ = [
    "P_UE_CTLOS_CLEAR",
    "P_UE_CTLOS_RX_STATS",
    "P_UE_CTLOS_TX_STATS",
    "P_UE_LINKNEG_OPTIONS",
    "P_UE_LINKNEG_OPTIONS_STATUS",
    "P_UE_LLR_MODE",
    "P_UE_LLR_RX_STATS",
    "P_UE_LLR_TX_STATS",
    "P_UE_CTLOS_SPACING",
    "P_UE_LLR_REPLAY",
    "P_UE_LLR_BEHAVIOR",
    "P_UE_LLR_INIT",
    "P_UE_LLR_INIT_ECHO",
    "P_UE_LLR_ACKNACK",
    "P_UE_LLR_TXERR",
    "P_UE_LLR_POISONFCS",
    "P_UE_LLR_INIT_ECHO_CHK",
    "P_UE_LLR_TXFSM_STATE",
    "P_UE_LLR_RXFSM_STATE",
    "P_UE_LLR_STATUS",
    "P_UE_CTLOS_TX_INTERVAL",
    "P_UE_CTLOS_RX_INTERVAL",
    "P_UE_CTLOS_RX_ERRORS",
]