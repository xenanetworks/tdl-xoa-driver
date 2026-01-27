"""Port Advanced Layer 1 Commands"""
from __future__ import annotations
from dataclasses import dataclass
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
    XmpInt,
    XmpSequence,
    XmpStr,
    Hex,
    XmpHex,
    XmpLong,
)
from .enums import (
    TrueFalse,
    OnOff,
)

@register_command
@dataclass
class PL1AD_RX_FREQ_CURR:
    """
    Return the current port Rx frequency in Hz.

    """

    code: typing.ClassVar[int] = 1303
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency_hz: int = field(XmpInt(signed=False))
        """Current port Rx frequency in Hz."""


    def get(self) -> Token[GetDataAttr]:
        """Get the current port Rx frequency in Hz.

        :return: Current port Rx frequency in Hz
        :rtype: PL1AD_RX_FREQ_CURR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1AD_RX_FREQ_MIN:
    """
    Return the minimum port Rx frequency in Hz since the previous query.

    """

    code: typing.ClassVar[int] = 1305
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency_hz: int = field(XmpInt(signed=False))
        """Minimum port Rx frequency in Hz since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the minimum port Rx frequency in Hz since the previous query.
        :return: Minimum port Rx frequency in Hz since the previous query
        :rtype: PL1AD_RX_FREQ_MIN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1AD_RX_FREQ_MAX:
    """
    Return the maximum port Rx frequency in Hz since the previous query.

    """

    code: typing.ClassVar[int] = 1304
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency_hz: int = field(XmpInt(signed=False))
        """Maximum port Rx frequency in Hz since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the maximum port Rx frequency in Hz since the previous query.
        :return: Maximum port Rx frequency in Hz since the previous query
        :rtype: PL1AD_RX_FREQ_MAX.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_RX_LOL:
    """
    Returns the current and the latched CDR Loss of Lock (LOL) status of the specified Serdes.

    """

    code: typing.ClassVar[int] = 1312
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        current_lol: TrueFalse = field(XmpByte())
        """Current CDR Loss of Lock (LOL) status. `True` indicates a current LOL condition."""

        latched_lol: TrueFalse = field(XmpByte())
        """Latched CDR Loss of Lock (LOL) status. `True` indicates a LOL condition has occurred."""


    def get(self) -> Token[GetDataAttr]:
        """Get the current and latched CDR Loss of Lock (LOL) status of the specified Serdes.

        :return: Current and latched CDR Loss of Lock (LOL) status of the specified Serdes
        :rtype: PL1AD_RX_LOL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._serdes_xindex]))


@register_command
@dataclass
class PL1AD_RX_SKEW:
    """
    Returns the relative skew in bits of the specified PCS lane.

    """

    code: typing.ClassVar[int] = 1315
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _lane_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        skew_bits: int = field(XmpInt(signed=True))
        """Relative skew of the PCS lane measured in bits."""

    def get(self) -> Token[GetDataAttr]:
        """Get the relative skew of the PCS lane measured in bits.

        :return: Relative skew of the PCS lane measured in bits
        :rtype: PL1AD_RX_SKEW.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._lane_xindex]))
    


@register_command
@dataclass
class PL1AD_RX_HIBER:
    """
    Returns the current and the latched High BER status of the port.
    """

    code: typing.ClassVar[int] = 1306
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        current_hiber: TrueFalse = field(XmpByte())
        """Current High BER status. `True` indicates a current High BER condition."""

        latched_hiber: TrueFalse = field(XmpByte())
        """Latched High BER status. `True` indicates a High BER condition has occurred."""

    def get(self) -> Token[GetDataAttr]:
        """Get the current and latched High BER status of the port.

        :return: Current and latched High BER status of the port
        :rtype: PL1AD_RX_HIBER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1AD_RX_HISER:
    """
    Returns the current and latched High SER status of the port, when High SER Alarm, controlled by ``PL1AD_RX_HISER_ALARM`` command, is enabled. If High SER Alarm is disabled, both status will be `False`.

    High SER status is set if 5560 RS-FEC symbol errors are detected in a contiguous block of 8192 non-overlapping RS-FEC codewords.

    """

    code: typing.ClassVar[int] = 1307
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        alarm_state: OnOff = field(XmpByte())
        """Current state of the High SER Alarm of the port. `ON` indicates that High SER Alarm is enabled, `OFF` indicates it is disabled. The same alarm state can also be retrieved using ``PL1AD_RX_HISER_ALARM``."""

        current_hiser: TrueFalse = field(XmpByte())
        """Current High SER status. `True` indicates a current High SER condition."""

        latched_hiser: TrueFalse = field(XmpByte())
        """Latched High SER status. `True` indicates a High SER condition has occurred."""

    def get(self) -> Token[GetDataAttr]:
        """Get the current and latched High SER status of the port.

        :return: Current and latched High SER status of the port
        :rtype: PL1AD_RX_HISER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_RX_HISER_ALARM:
    """
    Controls the High SER Alarm state of the port. When enabled, the port will signal a High SER Alarm if 5560 RS-FEC symbol errors are detected in a contiguous block of 8192 non-overlapping RS-FEC codewords (Use ``PL1AD_RX_HISER`` to retrieve the status). When disabled, the High SER Alarm will not be signaled regardless of the symbol error rate.

    """

    code: typing.ClassVar[int] = 1308
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        alarm_state: OnOff = field(XmpByte())
        """Enables or disables the High SER Alarm on the port. `ON` enables the alarm, `OFF` disables it."""

    class SetDataAttr(RequestBodyStruct):
        alarm_state: OnOff = field(XmpByte())
        """Enables or disables the High SER Alarm on the port. `ON` enables the alarm, `OFF` disables it."""
        

    def get(self) -> Token[GetDataAttr]:
        """Get the High SER Alarm state of the port.

        :return: High SER Alarm state of the port
        :rtype: PL1AD_RX_HISER_ALARM.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    def set(self, alarm_state: OnOff) -> Token[None]:
        """Set the High SER Alarm state of the port.

        :param alarm_state: Enables or disables the High SER Alarm on the port. `ON` enables the alarm, `OFF` disables it.
        :type alarm_state: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, alarm_state=alarm_state))


@register_command
@dataclass
class PL1AD_RX_DEG_SER:
    """
    This command retrieves the current and latched Degraded SER status of the port.

    A Degraded SER (Symbol Error Rate) Alarm indicates that the pre-FEC (Forward Error Correction) SER has exceeded a predefined threshold, signaling potential signal degradation.

    """

    code: typing.ClassVar[int] = 1300
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        current_deg_ser: TrueFalse = field(XmpByte())
        """Current Degraded SER status. `True` indicates a current Degraded SER condition."""

        latched_deg_ser: TrueFalse = field(XmpByte())
        """Latched Degraded SER status. `True` indicates a Degraded SER condition has occurred."""


    def get(self) -> Token[GetDataAttr]:
        """Get the current and latched Degraded SER status of the port.

        :return: Current and latched Degraded SER status of the port
        :rtype: PL1AD_RX_DEG_SER.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    

@register_command
@dataclass
class PL1AD_RX_DEG_SER_THRESH:
    """
    This command configures the thresholds for the Degraded SER Alarm.

    A Degraded SER (Symbol Error Rate) Alarm indicates that the pre-FEC (Forward Error Correction) SER has exceeded a predefined threshold, signaling potential signal degradation.

    Degraded SER is signaled when more than ``act_thresh`` RS-FEC symbol errors are detected within a contiguous block of ``degrade_interval`` RS-FEC codewords. It is no longer signaled when the error count falls below ``deact_thresh`` within a similar degrade_interval.

    An uncorrectable RS-FEC codeword is counted as 16 erroneous symbols to account for the worst-case scenario of complete codeword failure.

    Threshold changes take effect immediately. The activation threshold must be strictly greater than the deactivation threshold.

    The ``degrade_interval`` parameter must be an even number and a multiple of the number of PCS flows as follows:

        - 100G:      2 flows (1 PCS flow, but must be even)
        - 200G/400G: 2 flows (2 PCS flows)
        - 800G/1.6T: 4 flows (4 PCS flows)

    """

    code: typing.ClassVar[int] = 1301
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        act_thresh: int = field(XmpInt(signed=False))
        """Number of RS-FEC symbol errors in the specified ``degrade_interval`` to activate Degraded SER Alarm. Valid range is 1 to 65535. ``act_thresh`` must be strictly greater than ``deact_thresh``"""

        deact_thresh: int = field(XmpInt(signed=False))
        """Number of RS-FEC symbol errors in the specified ``degrade_interval`` to deactivate Degraded SER Alarm. Valid range is 0 to 65534. ``deact_thresh`` must be strictly less than ``act_thresh``."""

        degrade_interval: int = field(XmpInt(signed=False))
        """Number of RS-FEC codewords over which to monitor for symbol errors. Valid range is 2 to 65534. Must be an even number and a multiple of the number of PCS flows."""

    class SetDataAttr(RequestBodyStruct):
        act_thresh: int = field(XmpInt(signed=False))
        """Number of RS-FEC symbol errors in the specified ``degrade_interval`` to activate Degraded SER Alarm. Valid range is 1 to 65535. ``act_thresh`` must be strictly greater than ``deact_thresh``"""

        deact_thresh: int = field(XmpInt(signed=False))
        """Number of RS-FEC symbol errors in the specified ``degrade_interval`` to deactivate Degraded SER Alarm. Valid range is 0 to 65534. ``deact_thresh`` must be strictly less than ``act_thresh``."""

        degrade_interval: int = field(XmpInt(signed=False))
        """Number of RS-FEC codewords over which to monitor for symbol errors. Valid range is 2 to 65534. Must be an even number and a multiple of the number of PCS flows."""
        

    def get(self) -> Token[GetDataAttr]:
        """Get the thresholds for the Degraded SER Alarm.

        :return: Thresholds for the Degraded SER Alarm
        :rtype: PL1AD_RX_DEG_SER_THRESH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    def set(self, act_thresh: int, deact_thresh: int, degrade_interval: int) -> Token[None]:
        """Set the thresholds for the Degraded SER Alarm.

        :param act_thresh: Number of RS-FEC symbol errors in the specified ``degrade_interval`` to activate Degraded SER Alarm.
        :type act_thresh: int
        :param deact_thresh: Number of RS-FEC symbol errors in the specified ``degrade_interval`` to deactivate Degraded SER Alarm.
        :type deact_thresh: int
        :param degrade_interval: Number of RS-FEC codewords over which to monitor for symbol errors.
        :type degrade_interval: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, act_thresh=act_thresh, deact_thresh=deact_thresh, degrade_interval=degrade_interval))


@register_command
@dataclass
class PL1AD_RX_ERR_CW_CNT:
    """
    Returns the number of cumulative erroneous 64b/66b codewords since the previous query.

    Use ``PP_RXCLEAR`` to reset the counter.

    """

    code: typing.ClassVar[int] = 1302
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        err_cw_count: int = field(XmpInt(signed=False))
        """Number of erroneous 64b/66b codewords since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of cumulative erroneous 64b/66b codewords since the previous query.

        :return: Number of erroneous 64b/66b codewords since the previous query
        :rtype: PL1AD_RX_ERR_CW_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_RX_ITB_CNT:
    """
    Returns the number of cumulated Invalid 256b/257b Transcode Blocks since the previous query.

    Use ``PP_RXCLEAR`` to reset the counter.

    """

    code: typing.ClassVar[int] = 1309
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        itb_count: int = field(XmpInt(signed=False))
        """Number of cumulated Invalid 256b/257b Transcode Blocks since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of cumulated Invalid 256b/257b Transcode Blocks since the previous query
        
        :return: Number of cumulated Invalid 256b/257b Transcode Blocks since the previous query
        :rtype: PL1AD_RX_ITB_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_RX_LOSYNC_CNT:
    """
    Reports the number of cumulated Loss of Synchronization (LOSYNC) events since the previous query.

    Use ``PP_RXCLEAR`` to reset the counter.

    """

    code: typing.ClassVar[int] = 1313
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        losync_count: int = field(XmpInt(signed=False))
        """Number of cumulated Loss of Synchronization (LOSYNC) events since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of cumulated Loss of Synchronization (LOSYNC) events since the previous query.
        
        :return: Number of cumulated Loss of Synchronization (LOSYNC) events since the previous query
        :rtype: PL1AD_RX_LOSYNC_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    


@register_command
@dataclass
class PL1AD_RX_LF_CNT:
    """
    Returns the number of cumulated Local Fault conditions since the previous query.

    Use ``PP_RXCLEAR`` to reset the counter.

    """

    code: typing.ClassVar[int] = 1310
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        lf_count: int = field(XmpInt(signed=False))
        """Number of cumulated Local Fault conditions since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of cumulated Local Fault conditions since the previous query.
        
        :return: Number of cumulated Local Fault conditions since the previous query
        :rtype: PL1AD_RX_LF_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1AD_RX_RF_CNT:
    """
    Returns the number of Remote Fault conditions since last query.

    Use ``PP_RXCLEAR`` to reset the counter.

    """

    code: typing.ClassVar[int] = 1314
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        rf_count: int = field(XmpInt(signed=False))
        """Number of Remote Fault conditions since last query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of Remote Fault conditions since last query.
        
        :return: Number of Remote Fault conditions since last query
        :rtype: PL1AD_RX_RF_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1AD_RX_LOA_CNT:
    """
    Reports the number of cumulated Loss of Alignment (LOA) events since the previous query.

    Use ``PP_RXCLEAR`` to reset the counter.
    """

    code: typing.ClassVar[int] = 1311
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        loa_count: int = field(XmpInt(signed=False))
        """Number of cumulated Loss of Alignment (LOA) events since the previous query."""


    def get(self) -> Token[GetDataAttr]:
        """Get the number of cumulated Loss of Alignment (LOA) events since the previous query.
        
        :return: Number of cumulated Loss of Alignment (LOA) events since the previous query
        :rtype: PL1AD_RX_LOA_CNT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_TX_FREQ_CURR:
    """
    Return the current port Tx frequency in Hz.
    """

    code: typing.ClassVar[int] = 1317
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency_hz: int = field(XmpInt(signed=False))
        """Current port Tx frequency in Hz."""


    def get(self) -> Token[GetDataAttr]:
        """Get the current port Tx frequency in Hz.

        :return: Current port Tx frequency in Hz
        :rtype: PL1AD_TX_FREQ_CURR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_TX_ERR_CW:
    """
    Sends an error 64b/66b codeword from the Tx port immediately when called.

    """

    code: typing.ClassVar[int] = 1316
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Send an error 64b/66b codeword from the Tx port immediately.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class PL1AD_TX_ITB:
    """
    Sends an Invalid 256b/257b Transcode Block from the Tx port immediately when called.

    """

    code: typing.ClassVar[int] = 1318
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Send an Invalid 256b/257b Transcode Block from the Tx port immediately.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    
    

__all__ = [
    "PL1AD_RX_FREQ_CURR",
    "PL1AD_RX_FREQ_MIN",
    "PL1AD_RX_FREQ_MAX",
    "PL1AD_RX_LOL",
    "PL1AD_RX_SKEW",
    "PL1AD_RX_HIBER",
    "PL1AD_RX_HISER",
    "PL1AD_RX_HISER_ALARM",
    "PL1AD_RX_DEG_SER",
    "PL1AD_RX_DEG_SER_THRESH",
    "PL1AD_RX_ERR_CW_CNT",
    "PL1AD_RX_ITB_CNT",
    "PL1AD_RX_LOSYNC_CNT",
    "PL1AD_RX_LF_CNT",
    "PL1AD_RX_RF_CNT",
    "PL1AD_RX_LOA_CNT",
    "PL1AD_TX_FREQ_CURR",
    "PL1AD_TX_ERR_CW",
    "PL1AD_TX_ITB",
]
