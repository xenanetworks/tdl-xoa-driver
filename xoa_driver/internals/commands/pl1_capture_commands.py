"""Port Commands - Layer 1 Event Logging"""

from __future__ import annotations
from dataclasses import dataclass
import typing
from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.protocol.payload.types import XmpSequence
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpInt,
    XmpLong,
    XmpJson,
)
from .enums import (
    L1CGMIICaptureTriggerType,
    L1EventLoggingType,
    L1EventLoggingCondition,
    L1EventLoggingSubscription,
    IsEnabled,
)
from .subtypes import CGMIICodeword

@register_command
@dataclass
class PL1_EVENT_LOGGING_READ:
    """
    Read the list of logged Layer-1 event entries. Each entry consists of four parameters, event type, event condition, event lane, and timestamp.
    
    * For port-specific events, the JSON response is structured as follows::

        {
          "evread": [
          {
            "$po-type": "l1_event_logging_entry",
            "payload": {
            "evtype_s": "PCS_LOA",
            "evtype": 6,
            "asserted": true,
            "ts": 1234
            }
          }
          ]
        }

    * For lane-specific events, the JSON response is structured as follows::

        {
          "evread": [
          {
            "$po-type": "l1_event_logging_entry_with_lane",
            "payload": {
            "evtype_s": "LANE_PRBS_LOCK",
            "evtype": 14,
            "asserted": true,
            "lane": 0,
            "ts": 1234
            }
          }
          ]
        }

    where 

    - ``evtype_s``: Event type as a string.
    - ``evtype``: Event type as an integer. See :ref:`layer_1_event_logging_types_table` for the list of supported event types.
    - ``asserted``: Boolean indicating if the event is asserted. See :ref:`layer_1_event_logging_event_conditions_table` for the list of supported event conditions.
    - ``lane``: Lane number (>= 0) for lane-specific events.
    - ``ts``: Timestamp of the event in the unit of 0.5 nanosecond. The timestamp is relative to the previously delivered event, not an absolute hardware timestamp.
    """

    code: typing.ClassVar[int] = 1300
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        evread: dict = field(XmpJson(min_len=2))
        """event read value. Reads up to 32 events per call and returns them as JSON."""


    def get(self) -> Token[GetDataAttr]:
        """Read the list of logged Layer-1 event entries.

        :return: List of logged Layer-1 event entries
        :rtype: PL1_EVENT_LOGGING_READ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class PL1_EVENT_LOGGING_CONFIG:
    """
    Subscribes/unsubscribes to a specific Layer-1 event. 
    """

    code: typing.ClassVar[int] = 1301
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _serdes_lane: int  # SerDes lane index associated with the event. Use 0 if the event is not SerDes-specific.

    class SetDataAttr(RequestBodyStruct):

        action: L1EventLoggingSubscription = field(XmpByte())
        """Subscribe or unsubscribe to the event."""
        
        event_type: L1EventLoggingType = field(XmpByte())
        """Type of the event to subscribe to."""

        event_cond: L1EventLoggingCondition = field(XmpByte())
        """Condition that triggers the event."""

    def set(self, action: L1EventLoggingSubscription, event_type: L1EventLoggingType, event_cond: L1EventLoggingCondition) -> Token[None]:
        """Subscribe or unsubscribe to the event.
        
        :param action: Subscribe or unsubscribe to the event
        :type action: L1EventLoggingSubscription
        :param event_type: Type of the event to subscribe to
        :type event_type: L1EventLoggingType
        :param event_cond: Condition that triggers the event
        :type event_cond: L1EventLoggingCondition
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port,
                                                        action=action, event_type=event_type,
                                                        event_cond=event_cond, indices=[self._serdes_lane]))



@register_command
@dataclass
class PL1_EVENT_LOGGING_SUBLIST:
    """
    Return the currently configured event subscriptions.
    
    * For port-specific events, the JSON response is structured as follows::

        {
          "evsub": [
          {
            "$po-type": "l1_event_logging_entry",
            "payload": {
            "evtype_s": "PCS_LOA",
            "evtype": 6,
            "asserted": true,
            }
          }
          ]
        }

    * For lane-specific events, the JSON response is structured as follows::

        {
          "evsub": [
          {
            "$po-type": "l1_event_logging_entry_with_lane",
            "payload": {
            "evtype_s": "LANE_PRBS_LOCK",
            "evtype": 14,
            "asserted": true,
            "lane": 0,
            }
          }
          ]
        }

    where 

    - ``evtype_s``: Event type as a string.
    - ``evtype``: Event type as an integer. See :ref:`l1_event_types_n_conds` for the list of supported event types.
    - ``asserted``: Boolean indicating if the event is asserted. See :ref:`layer_1_event_logging_event_conditions_table` for the list of supported event conditions.
    - ``lane``: SerDes index number (>= 0) for SerDes-specific events.
    """

    code: typing.ClassVar[int] = 1302
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        evsub: dict = field(XmpJson(min_len=2))
        """event read value. Reads up to 32 events per call and returns them as JSON."""


    def get(self) -> Token[GetDataAttr]:
        """Read the list of currently configured Layer-1 event subscriptions.

        :return: List of currently configured Layer-1 event subscriptions
        :rtype: PL1_EVENT_LOGGING_SUBLIST.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    class SetDataAttr(RequestBodyStruct):

        evsublist: dict = field(XmpJson(min_len=1))
        """Write the list of new configured Layer-1 event subscriptions."""

    def set(self, evsublist: dict) -> Token[None]:
        """Set the list of new configured Layer-1 event subscriptions.
        NOTE: Events not included in this list will be unsubscribed automatically.

        :param evsublist: Dictionary of new configured Layer-1 event subscriptions
        :type evsublist: dict
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, evsublist=evsublist))



@register_command
@dataclass
class PL1_EVENT_LOGGING_STATE:
    """
    Layer-1 Event Logging state. It is used to enable or disable the Layer-1 Event Logging feature.
    """

    code: typing.ClassVar[int] = 1303
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        state: IsEnabled = field(XmpByte())
        """Layer-1 Event Logging state. Indicates if the feature is enabled or disabled."""

    class SetDataAttr(RequestBodyStruct):

        state: IsEnabled = field(XmpByte())
        """Enable/Disable event logging."""

    def get(self) -> Token[GetDataAttr]:
        """Returns the Layer-1 Event Logging state.

        :return: Layer-1 Event Logging state
        :rtype: PL1_EVENT_LOGGING_STATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, state: IsEnabled) -> Token[None]:
        """Set the Layer-1 Event Logging state.

        :param state: Layer-1 Event Logging state.
        :type state: IsEnabled
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, state=state))


@register_command
@dataclass
class PL1_EVENT_LOGGING_MARK:
    """
    Trigger the hardware to generate a **Marker Event**.
    It is useful for marking specific points in time during the logging process,
    allowing you to correlate events with specific actions or occurrences in the system.
    """

    code: typing.ClassVar[int] = 1304
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Trigger a Marker Event.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_EVENT_LOGGING_QLEN:
    """
    Return the current Layer-1 Event Logging queue length.
    """

    code: typing.ClassVar[int] = 1305
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        qlen: int = field(XmpInt())
        """Current Layer-1 Event Logging queue length."""


    def get(self) -> Token[GetDataAttr]:
        """Returns the current Layer-1 Event Logging queue length.

        :return: Current Layer-1 Event Logging queue length
        :rtype: PL1_EVENT_LOGGING_QLEN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_EVENT_LOGGING_RSFEC_THRESH:
    """
    Get or set the RS-FEC threshold for Layer-1 Event Logging.
    """

    code: typing.ClassVar[int] = 1306
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        rsfec_thresh: int = field(XmpInt())
        """Current RS-FEC threshold."""

    class SetDataAttr(RequestBodyStruct):
        rsfec_thresh: int = field(XmpInt())
        """RS-FEC threshold to set."""

    def get(self) -> Token[GetDataAttr]:
        """Returns the current RS-FEC threshold.

        :return: Current RS-FEC threshold
        :rtype: PL1_EVENT_LOGGING_RSFEC_THRESH.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rsfec_thresh: int) -> Token[None]:
        """Set the RS-FEC threshold.

        :param rsfec_thresh: RS-FEC threshold to set.
        :type rsfec_thresh: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rsfec_thresh=rsfec_thresh))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_STATE:
    """
    Layer-1 CGMII capture state. It is used to enable or disable the Layer-1 CGMII capture feature.
    """

    code: typing.ClassVar[int] = 1313
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        state: IsEnabled = field(XmpByte())
        """Layer-1 CGMII capture state. Indicates if the feature is enabled or disabled."""

    class SetDataAttr(RequestBodyStruct):

        state: IsEnabled = field(XmpByte())
        """Enable/Disable Layer-1 CGMII capture."""

    def get(self) -> Token[GetDataAttr]:
        """Returns the Layer-1 CGMII capture state.

        :return: Layer-1 CGMII capture state
        :rtype: PL1_CGMII_CAPTURE_STATE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, state: IsEnabled) -> Token[None]:
        """Set the Layer-1 CGMII capture state.

        :param state: Layer-1 CGMII capture state.
        :type state: IsEnabled
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, state=state))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_READ:
    """
    Read the meta data of the oldest Layer-1 CGMII capture. 
    """

    code: typing.ClassVar[int] = 1310
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        triggertype: L1CGMIICaptureTriggerType = field(XmpByte())
        """The trigger type of the oldest captured Layer-1 CGMII capture."""

        timestamp: int = field(XmpLong(signed=False))
        """The timestamp of the oldest Layer-1 CGMII capture."""

        triggerpos: int = field(XmpInt(signed=False))
        """The position of CGMII codeword that triggered the oldest Layer-1 CGMII capture."""
        
        cgmii_data_size: int = field(XmpInt(signed=False))
        """The CGMII data size of the oldest Layer-1 CGMII capture."""

    def get(self) -> Token[GetDataAttr]:
        """Read the meta data of the oldest captured Layer-1 CGMII entry.

        :return: Meta data of the oldest captured Layer-1 CGMII entry
        :rtype: PL1_CGMII_CAPTURE_READ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_DATA:
    """
    Read some CGMII codeword data of the oldest Layer-1 CGMII capture.
    The amount of data read is determined by the offset and count parameters.
    """

    code: typing.ClassVar[int] = 1318
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _offset: int  # The starting offset of the CGMII codeword data to read.
    _count: int  # The maximum number of CGMII codeword data elements to read. If zero read as many as possible.

    class GetDataAttr(ResponseBodyStruct):

        gcmii_data: typing.List[CGMIICodeword] = field(XmpSequence(types_chunk=[CGMIICodeword]))
        """The CGMII codeword data chunk of the oldest captured Layer-1 CGMII entry from _offset and max _count elements."""

    def get(self) -> Token[GetDataAttr]:
        """Read the CGMII codeword data of the oldest captured Layer-1 CGMII entry.

        :return: CGMII codeword data of the oldest captured Layer-1 CGMII entry
        :rtype: PL1_CGMII_CAPTURE_DATA.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, offset=self._offset, count=self._count))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_CONSUMED:
    """
    Inform the system that the oldest CGMII capture trace for the specified port has been consumed and is no longer needed.
    Any resource related to this capture will be released.
    """

    code: typing.ClassVar[int] = 1319
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """
        Inform the system that the oldest CGMII capture trace has been consumed.
        """

        """
        :return: None
        :rtype: None
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_QLEN:
    """
    Return the current Layer-1 CGMII capture queue length.
    """

    code: typing.ClassVar[int] = 1315
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):

        qlen: int = field(XmpInt())
        """Current Layer-1 CGMII capture queue length."""


    def get(self) -> Token[GetDataAttr]:
        """Returns the current Layer-1 CGMII capture queue length.

        :return: Current Layer-1 CGMII capture queue length
        :rtype: PL1_CGMII_CAPTURE_QLEN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_FORCE:
    """
    Trigger a CGMII capture for the specified port.
    Any resource related to this capture will be released.
    """

    code: typing.ClassVar[int] = 1314
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """
        Trigger a CGMII capture for the specified port.
        """

        """
        :return: None
        :rtype: None
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))


@register_command
@dataclass
class PL1_CGMII_CAPTURE_CONFIG:
    """
    Enable/Disable the Layer-1 CGMII capture for a specific event.``. 
    """

    code: typing.ClassVar[int] = 1311
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):

        enable: IsEnabled = field(XmpByte())
        """Enable or disable the trigger."""
        
        trigger_type: L1CGMIICaptureTriggerType = field(XmpByte())
        """Type of the trigger to subscribe to."""


    def set(self, enable: IsEnabled, trigger_type: L1CGMIICaptureTriggerType) -> Token[None]:
        """Enable or disable the trigger.
        
        :param enable: Enable or disable the trigger
        :type enable: IsEnabled
        :param trigger_type: Type of the trigger to subscribe to
        :type trigger_type: L1CGMIICaptureTriggerType
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, enable=enable, trigger_type=trigger_type))



__all__ = [
    "PL1_CGMII_CAPTURE_CONFIG",
    "PL1_CGMII_CAPTURE_CONSUMED",
    "PL1_CGMII_CAPTURE_DATA",
    "PL1_CGMII_CAPTURE_FORCE",
    "PL1_CGMII_CAPTURE_READ",
    "PL1_CGMII_CAPTURE_STATE",
    "PL1_EVENT_LOGGING_READ",
    "PL1_EVENT_LOGGING_CONFIG",
    "PL1_EVENT_LOGGING_SUBLIST",
    "PL1_EVENT_LOGGING_STATE",
    "PL1_EVENT_LOGGING_MARK",
    "PL1_EVENT_LOGGING_QLEN",
    "PL1_EVENT_LOGGING_RSFEC_THRESH"
]
