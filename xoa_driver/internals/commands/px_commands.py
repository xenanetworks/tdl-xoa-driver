"""Port Transceiver Commands"""
from __future__ import annotations
from dataclasses import dataclass
import typing

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
    XmpSequence,
    XmpInt,
    Hex,
    XmpStr,
    XmpJson,
)


@register_command
@dataclass
class PX_RW:
    """
    Provides read and write access to the register interface supported by the port transceiver. It is possible to both read and write register values.
    """

    code: typing.ClassVar[int] = 501
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _page_xindex: int
    _register_xaddress: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex(size=4))
        """4 hex bytes, register value of the port transceiver"""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex(size=4))
        """4 hex bytes, register value of the port transceiver"""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_RW.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress], value=value))


@register_command
@dataclass
class PX_RW_SEQ:
    """
    I2C sequential access to a transceiver's register. When invoked, the <byte_count> number of bytes will be read or written in one I2C transaction, in which the <value> is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

    * <_byte_xcount> number of bytes will be read or written in one I2C transaction

    * <_page_xindex>: the transceiver page address, integer, 0x00 - 0xFF (0-255).

    * <_register_xaddress>: the address within the page, integer, 0x00 - 0xFF (0-255).

    If <_register_xaddress> < 128, the page index <_page_xindex> is ignored by the server. The server will read from page 0 without writing 0 into byte 127.

    If <_register_xaddress> >=128, the page index <_page_xindex> will be written into byte 127.
    """

    code: typing.ClassVar[int] = 503
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _page_xindex: int
    _register_xaddress: int
    _byte_xcount: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the <value> equals <byte_count>."""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the <value> equals <byte_count>."""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver in one I2C transaction.

        :return: the register value of a transceiver
        :rtype: PX_RW_SEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._page_xindex, self._register_xaddress, self._byte_xcount]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver in one I2C transaction.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._page_xindex, self._register_xaddress, self._byte_xcount],
                value=value
            )
        )


@register_command
@dataclass
class PX_RW_SEQ_BANK:
    """
    I2C sequential access to a transceiver's register. When invoked, the <byte_count> number of bytes will be read or written in one I2C transaction, in which the <value> is read or written with only a single register address setup. A subsequent invocation will perform a second I2C transaction in the same manner.

    * <_bank_xindex>: the bank address, integer, 0x00 - 0xFF (0-255).

    * <_page_xindex>: the transceiver page address, integer, 0x00 - 0xFF (0-255).

    * <_register_xaddress>: the address within the page, integer, 0x00 - 0xFF (0-255).

    * <_byte_xcount> number of bytes will be read or written in one I2C transaction

    If <_register_xaddress> < 128, the page index <page> and the bank index <_bank_xindex> is ignored by the server. The server will read from page 0 without writing 0 into byte 127.

    If <_register_xaddress> >=128, the page index <page> will be written into byte 127, and the bank index <_bank_xindex> will be written into byte 126.
    """

    code: typing.ClassVar[int] = 504
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _bank_xindex: int
    _page_xindex: int
    _register_xaddress: int
    _byte_xcount: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the <value> equals <byte_count>."""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex())
        """the bytes to be read or written in one I2C transaction. The number of bytes in the <value> equals <byte_count>."""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver in one I2C transaction.

        :return: the register value of a transceiver
        :rtype: PX_RW_SEQ.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._bank_xindex, self._page_xindex, self._register_xaddress, self._byte_xcount]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver in one I2C transaction.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(
            self._connection,
            build_set_request(
                self,
                module=self._module,
                port=self._port,
                indices=[self._bank_xindex, self._page_xindex, self._register_xaddress, self._byte_xcount],
                value=value
            )
        )

@register_command
@dataclass
class PX_MII:
    """Provides access to the register interface supported by the media-independent interface (MII) transceiver. It
    is possible to both read and write register values."""

    code: typing.ClassVar[int] = 537
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _register_xaddress: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex(size=2))
        """2 hex bytes, register value of the transceiver"""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex(size=2))
        """2 hex bytes, register value of the transceiver"""

    def get(self) -> Token[GetDataAttr]:
        """Get the register value of a transceiver.

        :return: the register value of a transceiver
        :rtype: PX_MII.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._register_xaddress]))

    def set(self, value: Hex) -> Token[None]:
        """Set the register value of a transceiver.

        :param value: register value of a transceiver
        :type value: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._register_xaddress], value=value))


@register_command
@dataclass
class PX_TEMPERATURE:
    """
    Transceiver temperature in degrees Celsius.
    """

    code: typing.ClassVar[int] = 538
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        integral_part: int = field(XmpByte())
        """byte, temperature value before the decimal digit."""
        fractional_part: int = field(XmpByte())
        """byte, 1/256th of a degree Celsius after the decimal digit."""

    def get(self) -> Token[GetDataAttr]:
        """Get transceiver temperature in degrees Celsius.

        :return: temperature value before the decimal digit, and 1/256th of a degree Celsius after the decimal digit.
        :rtype: PX_TEMPERATURE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

@register_command
@dataclass
class PX_I2C_CONFIG:
    """
    Access speed on a transceiver I2C access in the unit of KHz. Default to 100. When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from P_CAPABILITIES. The I2C speed configuration will not be included in the port configuration file (.xpc). When you load a port configuration to a port, the transceiver I2C access speed will be reset to default 100.
    """

    code: typing.ClassVar[int] = 539
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        frequency: int = field(XmpInt())
        """integer, frequency in kHz, default is 100."""
    
    class SetDataAttr(RequestBodyStruct):
        frequency: int = field(XmpInt())
        """integer, frequency in kHz, default is 100."""

    def get(self) -> Token[GetDataAttr]:
        """Get the speed on a transceiver I2C access in the unit of KHz.

        :return: frequency in kHz.
        :rtype: PX_I2C_CONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
    def set(self, frequency: int) -> Token[None]:
        """Set the speed on a transceiver I2C access in the unit of KHz.

        :param frequency: frequency in kHz
        :type frequency: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, frequency=frequency))
    
# region CDB
@register_command
@dataclass
class PX_CDB_SUPPORT:
    """Return the supported CDB instances.
    """
    code: typing.ClassVar[int] = 485
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """
        dict, json.

        .. code-block:: json 
        
            {
              "cdb_instances_supported": 2
            }
        
       * ``cdb_instances_supported``: CDP instnaces supported
            
            * 0 = CDB functionality not supported
            * 1 = One CDB instance supported
            * 2 = Two CDB instances supported

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: CDB REPLY
        :rtype: PX_CDB_SUPPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    
@register_command
@dataclass
class PX_CDB_ABORT_PROCESSING:
    """This is CMD 0004h: Abort Processing
    """
    code: typing.ClassVar[int] = 464
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json
        
            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: CDB REPLY
        :rtype: PX_CDB_ABORT_PROCESSING.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_CHANGE_PASSWORD:
    """This is CMD 0002h: Change Password
    """
    code: typing.ClassVar[int] = 463
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json 
        
            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_CHANGE_PASSWORD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json 
        
            {
              "new_password": [54,55,56,57]
            }

        * ``new_password``: array of four integers, new password to be entered.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))


@register_command
@dataclass
class PX_CDB_ENTER_PASSWORD:
    """This is CMD 0001h: Enter Password
    """
    code: typing.ClassVar[int] = 462
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json 
        
            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json
            
            {
                "password": [54,55,56,57]
            }

        * ``password``: array of four integers, password to be entered.

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_ENTER_PASSWORD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json
        
            {
              "password": [54,55,56,57]
            }

        * ``password``: array of four integers, password to be entered.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))


@register_command
@dataclass
class PX_CDB_QUERY_STATUS:
    """This is CMD 0000h: Query Status
    """
    code: typing.ClassVar[int] = 461
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json
        
            {
              "cdb_status": 0, 
              "status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``status``: integer

            * 0000 0000b: Module Boot Up.
            * 0000 0001b: Host Password Accepted.
            * 1xxx xxxxb: Module Password accepted.
            * Bits ‘x’ may contain custom information.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json
        
            {
              "response_delay": 0
            }

        * ``response_delay``: Programmable delay in ms for module responding to this command. A value of 0 asks for module response as fast as possible.

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_QUERY_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json
        
            {
              "response_delay": 0
            }

        * ``response_delay``: Programmable delay in ms for module responding to this command. A value of 0 asks for module response as fast as possible.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))



@register_command
@dataclass
class PX_CDB_EXTERNAL_FEATURES:
    """This is CMD 0045h: Externally Defined Features
    """
    code: typing.ClassVar[int] = 468
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json
        
            {
              "cdb_status": 0,
              "supplement_support": "0x00"
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``supplement_support``: hex string, Bit 0 = 0/1: CMIS-VCS not supported/supported

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_EXTERNAL_FEATURES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_FW_MGMT_FEATURES:
    """This is CMD 0041h: Firmware Management Features
    """
    code: typing.ClassVar[int] = 466
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "feature_support_mask": "0x00",
              "start_cmd_payload_size": 2,
              "erased_byte": "0x00",
              "read_write_length_ext": 2,
              "write_mechanism": "0x00",
              "read_mechanism": "0x00",
              "hitless_restart": 0,
              "max_duration_start": 123,
              "max_duration_abort": 123,
              "max_duration_write": 123,
              "max_duration_complete": 123,
              "max_duration_copy": 123
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``feature_support_mask``: hex string, indicates support of Firmware Management features.
        * ``start_cmd_payload_size``: integer, This defines the number of bytes that the host must extract from the beginning of the vendor-delivered binary firmware image file and send to the module in CMD 0101h (Start).
        * ``erased_byte``: hex string, This is the value representing an erased byte. The purpose of advertising this byte is to optionally reduce download time by allowing the host to skip sending blocks of the image containing ErasedByte values only.
        * ``read_write_length_ext``: integer, specifies the allowable additional number of byte octets in a READ or a WRITE, specifically for Firmware Management Commands (IDs 0100h-01FFh).
        * ``write_mechanism``: hex string, Firmware update supported mechanism
        * ``read_mechanism`` : hex string, Firmware read / readback support mechanism.
        * ``hitless_restart``: integer, 0: CMD Run Image causes a reset. Traffic is affected. 1: CMD Run Image may reset but module will do its best to maintain traffic and management states. Data path functions are not reset.
        * ``max_duration_start``: integer, U16 Maximum time in M ms for a CDB Start command to complete execution
        * ``max_duration_abort``: integer, U16 Maximum time in M ms for a CDB Abort command to complete execution
        * ``max_duration_write``: integer, U16 Maximum time in M ms for a CDB Write command to complete execution
        * ``max_duration_complete``: integer, U16 Maximum time in M ms for a CDB Complete command to complete execution
        * ``max_duration_copy``: integer, U16 Maximum time in M ms for a CDB Copy command to complete execution

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_FW_MGMT_FEATURES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_GET_APP_ATTRIBUTES:
    """This is CMD 0050h: Get Application Attributes
    """
    code: typing.ClassVar[int] = 469
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "application_number": 123,
              "max_module_power": 123,
              "prog_output_power_min": 123,
              "prog_output_power_max": 123,
              "pre_fec_ber_threshold": 123.123,
              "rx_los_optical_power_threshold": 123,
              "rx_power_high_alarm_threshold": 123,
              "rx_power_low_alarm_threshold": 123,
              "rx_power_high_warning_threshold": 123,
              "rx_power_low_warning_threshold": 123
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``application_number``: integer, U16 Application number. 15-8: reserved (0). 7-4: NADBlockIndex (0-15) or 0. 3-0: AppSelCode (1-15).
        * ``max_module_power``: integer, U16: Worst case module power dissipation when this Application is instantiated homogeneously as often as possible in parallel (when applicable) with worst case configuration options. Unit: 0.25 W.
        * ``prog_output_power_min``: integer, S16: Minimum Programmable Output Power, Unit: 0.01 dBm.
        * ``prog_output_power_max``: integer, S16: Maximum Programmable Output Power, Unit: 0.01 dBm.
        * ``pre_fec_ber_threshold``: float, F16: Pre FEC BER VDM high alarm threshold.
        * ``rx_los_optical_power_threshold``: integer, S16: Optical power threshold for RxLOS alarm. Unit: 0.01dBm.
        * ``rx_power_high_alarm_threshold``: integer, U16: OpticalPowerRxHighAlarmThreshold. Unit: 0.1uW.
        * ``rx_power_low_alarm_threshold``: integer, U16: OpticalPowerRxLowAlarmThreshold. Unit: 0.1uW.
        * ``rx_power_high_warning_threshold``: integer, U16: OpticalPowerRxHighWarningThreshold.Unit: 0.1uW.
        * ``rx_power_low_warning_threshold``: integer, U16: OpticalPowerRxLowWarningThreshold. Unit: 0.1uW.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json
        
            {
                "application_number": 1
            }

        * ``application_number``: integer, U16 Application number. 15-8: reserved (0). 7-4: NADBlockIndex (0-15) or 0. 3-0: AppSelCode (1-15)

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_GET_APP_ATTRIBUTES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json
        
            {
              "application_number": 1
            }

        * ``application_number``: integer, U16 Application number. 15-8: reserved (0). 7-4: NADBlockIndex (0-15) or 0. 3-0: AppSelCode (1-15)

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))
    

@register_command
@dataclass
class PX_CDB_GET_IF_CODE_DESCR:
    """This is CMD 0051h: Get Interface Code Description
    """
    code: typing.ClassVar[int] = 470
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "interface_id": "0x01",
              "interface_location": "0x00",
              "interfacre_name": "10G Ethernet",
              "interfacre_description": "10G Ethernet",
              "interfacre_data_rate": 10.3125,
              "interfacre_lane_count": 1,
              "lane_signaling_rate": 10.3125,
              "modulation": "PAM4",
              "bits_per_symbol": 2
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``interface_id``: hex string, U16: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
        * ``interface_location``: integer, 0: media side. 1: host side.
        * ``interfacre_name``: string, 16-byte long ACII string. Name of the interface.
        * ``interfacre_description``: string, 48-byte long ACII string. Description of the interface.
        * ``interfacre_data_rate``: float, F16: Application Bit Rate in Gb/s
        * ``interfacre_lane_count``: integer, U16: Number of parallel lanes.
        * ``lane_signaling_rate``: float, F16: Lane Signaling Rate in GBd.
        * ``modulation``: string, 16-byte long ACII string. Lane Modulation Format.
        * ``bits_per_symbol``: integer, U16: Bits per Symbol.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json

            {
              "interface_id": "0x01",
              "interface_location": "0x00"
            }

        * ``interface_id``: hex string, U16: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
        * ``interface_location``: integer, 0: media side. 1: host side.

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_GET_IF_CODE_DESCR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json

            {
              "interface_id": "0x01",
              "interface_location": "0x00"
            }

        * ``interface_id``: hex string, U16: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
        * ``interface_location``: integer, 0: media side. 1: host side.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))
    

@register_command
@dataclass
class PX_CDB_MODULE_FEATURES:
    """This is CMD 0040h: Module Features
    """
    code: typing.ClassVar[int] = 465
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "cmd_support_mask": "0x0000000000000000000000000000000000000000000000000000000000000000",
              "max_completion_time": 1000
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``cmd_support_mask``: :hex string, indicates support of CDB commands 0000h-00FFh. This array of 32 bytes indicates support of CDB commands CMD <i>, with identifiers 0 <= <i> <= 255, as follows: CMD <i> is supported when bit<j>=<i>mod 8 of byte<k> = 138+floor(<i>/8) is set.
        * ``max_completion_time``: integer, U16 Maximum CDB command execution time in ms, of all supported CDB commands.

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_MODULE_FEATURES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))
    
@register_command
@dataclass
class PX_CDB_SEC_FEAT_CAPABILITIES:
    """This is CMD 0044h: Security Features and Capabilities
    """
    code: typing.ClassVar[int] = 467
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "cmd_support_mask": "0xFF",
              "num_certificates": 0,
              "cert_chain_supported": 0,
              "certificate_format": 0,
              "certificate_length_1": 0,
              "certificate_length_2": 0,
              "certificate_length_3": 0,
              "certificate_length_4": 0,
              "digest_length": 0,
              "signature_time": 0,
              "signature_length": 0,
              "signature_format": 0,
              "signature_pad_scheme": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``cmd_support_mask``: hex string, indicates support of CDB commands 0400-04FFh. 
        * ``num_certificates``: integer, number of public certificates the host may obtain from the module. The device must contain a single leaf certificate and it may optionally contain one or more intermediate certificates optionally followed by a root certificate. For X.509 certificates, intermediate certificates are not self-signed, and the root cert is self-signed. ``num_certificates <= 4``.
        * ``cert_chain_supported``: integer, 0: Certificate chain is not supported. Module contains leaf certificate instance i = 0 only. 1: Module supports certificate chain and host must specify the instance when downloading a certificate. Instance i = 0 is the start of the chain, i.e. the leaf certificate, and any instance i+1 is another certificate used to sign the certificate instance i, where ``i < num_certificates <= 4``
        * ``certificate_format``: integer, 0: Not supported. 1: **Custom**. 2: X509v3 DER encoding. 3-255: Reserved.
        * ``certificate_length_1``: integer, Length of leaf certificate i = 0.
        * ``certificate_length_2``: integer, Length of certificate i = 1 or 0 when not supported.
        * ``certificate_length_3``: integer, Length of certificate i = 2 or 0 when not supported.
        * ``certificate_length_4``: integer, Length of certificate i = 3 or 0 when not supported.
        * ``digest_length``: integer, Required message hash digest length (in bytes) 0: Not supported. 1: 28 bytes (SHA224). 2: 32 bytes (SHA256). 3: 48 bytes (SHA384). 4: 64 bytes (SHA512). 5-255: **Reserved**.
        * ``signature_time``: integer, Maximum time (in milliseconds) for signature generation.
        * ``signature_length``: integer, Length (in bytes) of the encoded/padded (if applicable) digest signature
        * ``signature_format``: integer, 0: Not supported. 1: **Custom, vendor specific encoding**. 2: Raw binary byte stream. 3: DER encoding. 4: ECDSA (R,S) integer pair, integers prefixed with length. 5-255: Reserved.
        * ``signature_pad_scheme``: integer, 0: None. 1: **Custom**. 2: PKCS#1 v1.5. 3: OAEP. 4: PSS. 5-255: Reserved

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_SEC_FEAT_CAPABILITIES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_ABORT_FW_DOWNLOAD:
    """This is CMD 0102h: Abort Firmware Download
    """
    code: typing.ClassVar[int] = 473
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json
        
            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_ABORT_FIRMWARE_DOWNLOAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))
    

@register_command
@dataclass
class PX_CDB_COMMIT_FW_IMAGE:
    """This is CMD 010Ah: Commit Firmware Image
    """
    code: typing.ClassVar[int] = 483
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_COMMIT_FIRMWARE_IMAGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_COMPLETE_FW_DOWNLOAD:
    """This is CMD 0107h: Complete Firmware Download
    """
    code: typing.ClassVar[int] = 478
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json
        
            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_COMPLETE_FIRMWARE_DOWNLOAD.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))
    

@register_command
@dataclass
class PX_CDB_COPY_FW_IMAGE:
    """This is CMD 0108h: Copy Firmware Image
    """
    code: typing.ClassVar[int] = 479
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "copy_direction": "0xAB",
              "copy_status": "0x00"
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``copy_direction``: hex string, copy direction.

            * ``0xAB``, Copy Image A into Image B
            * ``0xBA``,Copy Image B into Image A

        * ``copy_status``: hex string, copy status.

            * ``0x00``, Copy Successful
            * ``0x01``, Copy Failed

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_COPY_FIRMWARE_IMAGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data
        
        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json
        
            {
              "copy_direction": "0xAB"
            }

        * ``copy_direction``: hex string, copy direction.

            * ``0xAB``, Copy Image A into Image B
            * ``0xBA``, Copy Image B into Image A

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))
    

@register_command
@dataclass
class PX_CDB_GET_FW_INFO:
    """This is CMD 0100h: Get Firmware Info
    """
    code: typing.ClassVar[int] = 471
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "firmware_status": 0,
              "image_information": 0,
              "image_a_major": 0,
              "image_a_minor": 0,
              "image_a_build": 0,
              "image_a_extra_string": "abcdef",
              "image_b_major": 0,
              "image_b_minor": 0,
              "image_b_build": 0,
              "image_b_extra_string": "abcdef",
              "factory_boot_major": 0,
              "factory_boot_minor": 0,
              "factory_boot_build": 0,
              "factory_boot_extra_string": "abcdef"
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``firmware_status``: integer, Firmware Status.

        Bitmask to indicate FW Status.
        
        * Image in Bank A:

        * Bit 0: Operational Status
        * Bit 1: Administrative Status
        * Bit 2: Validity Status
        * Bit 3: Reserved
        
        * Image in Bank B:

        * Bit 4: Operational Status
        * Bit 5: Administrative Status
        * Bit 6: Validity Status
        * Bit 7: Reserved
        
        * Encoding as follows:
        
        * Operational Status: 1 = running, 0 = not running
        * Administrative Status: 1=committed, 0=uncommitted
        * Validity Status: 1 = invalid, 0 = valid

        * ``image_information``: integer, Image Information.

            * Bit 0: Firmware image A information
            * Bit 1: Firmware image B information
            * Bit 2: Factory or Boot image information

        * ``image_a_major``: integer, Image A firmware major revision.
        * ``image_a_minor``: integer, Image A firmware minor revision.
        * ``image_a_build``: integer, Image A firmware build number.
        * ``image_a_extra_string``: string, Image A additional information (32-byte long ASCII string).
        * ``image_b_major``: integer, Image B firmware major revision.
        * ``image_b_minor``: integer, Image B firmware minor revision.
        * ``image_b_build``: integer, Image B firmware build number.
        * ``image_b_extra_string``: string, Image B additional information (32-byte long ASCII string).
        * ``factory_boot_major``: integer, Factory or Boot firmware major revision.
        * ``factory_boot_minor``: integer, Factory or Boot firmware minor revision.
        * ``factory_boot_build``: integer, Factory or Boot firmware build number.
        * ``factory_boot_extra_string``: string, Factory or Boot additional information (32-byte long ASCII string).

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_GET_FIRMWARE_INFO.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self) -> Token[None]:
        """
        Set CMD Data
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data='{}'))


@register_command
@dataclass
class PX_CDB_READ_FW_BLOCK_EPL:
    """This is CMD 0106h: Read Firmware Block EPL
    """
    code: typing.ClassVar[int] = 477
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "image_data": "0x00010203040506070809"
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``image_data``: hex string, Up to 2048 bytes.

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """


    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_READ_FIRMWARE_BLOCK_EPL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json 
        
            {
              "block_address": 12,
              "length": 10
            }

        * ``block_address``: integer, U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
        
        * ``length``: integer, Number of bytes to read back to the EPL in this command, starting at the indicated address.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))


@register_command
@dataclass
class PX_CDB_READ_FW_BLOCK_LPL:
    """This is CMD 0105h: Read Firmware Block LPL
    """
    code: typing.ClassVar[int] = 476
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0,
              "base_address_block": "0x0000000C",
              "image_data": "0x00010203040506070809"
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.
        * ``base_address_block``:  hex string, Base address of the data block within the firmware image.
        * ``image_data``: : hex string, Up to 2048 bytes.

        """

    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_WRITE_FIRMWARE_BLOCK_EPL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json 
        
            {
              "block_address": 12,
              "length": 10
            }

        * ``block_address``: integer, U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
        
        * ``length``: integer, Number of bytes to read back to the EPL in this command, starting at the indicated address.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))


@register_command
@dataclass
class PX_CDB_RUN_FW_IMAGE:
    """This is CMD 0109h: Run Firmware Image
    """
    code: typing.ClassVar[int] = 482
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json

            {
              "image_to_run": 0,
              "delay_to_reset": 100
            }

        * ``image_to_run``: integer, index of the image to run.

            * 0 = Traffic affecting Reset to Inactive Image.
            * 1 = Attempt Hitless Reset to Inactive Image
            * 2 = Traffic affecting Reset to Running Image.
            * 3 = Attempt Hitless Reset to Running Image

        * ``delay_to_reset``: integer, Indicates the delay in ms after receiving this command before a reset will occur, starting from the time the CDB complete Flag is set.

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_COPY_FIRMWARE_IMAGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json

            {
              "image_to_run": 0,
              "delay_to_reset": 100
            }

        * ``image_to_run``: integer, index of the image to run.

            * 0 = Traffic affecting Reset to Inactive Image.
            * 1 = Attempt Hitless Reset to Inactive Image
            * 2 = Traffic affecting Reset to Running Image.
            * 3 = Attempt Hitless Reset to Running Image

        * ``delay_to_reset``: integer, Indicates the delay in ms after receiving this command before a reset will occur, starting from the time the CDB complete Flag is set.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))


@register_command
@dataclass
class PX_CDB_START_FW_DOWNLOAD:
    """This is CMD 0101h: Start Firmware Download
    """
    code: typing.ClassVar[int] = 472
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json

            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "image_size": 12,
              "vendor_data": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            }

        * ``image_size``: integer, U32 Size of firmware image to download into the module. This should be the file size including the LPL bytes sent as vendor data in this message.
        * ``vendor_data``: hex string, U8 Array of vendor specific data to be sent to the module. This data is sent as part of the firmware download message. The size of this data is included in the image_size parameter.
        
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_COPY_FIRMWARE_IMAGE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json

            {
              "image_size": 12,
              "vendor_data": "0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
            }

        * ``image_size``: integer, U32 Size of firmware image to download into the module. This should be the file size including the LPL bytes sent as vendor data in this message.
        * ``vendor_data``: hex string, U8 Array of vendor specific data to be sent to the module. This data is sent as part of the firmware download message. The size of this data is included in the image_size parameter.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))
    

@register_command
@dataclass
class PX_CDB_WRITE_FW_BLOCK_EPL:
    """This is CMD 0104h: Write Firmware Block EPL
    """
    code: typing.ClassVar[int] = 475
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json

        .. code-block:: json

            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_WRITE_FIRMWARE_BLOCK_EPL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json

            {   
              "block_address": 12,
              "firmware_block": "0x00010203040506070809"
            }

        * ``block_address``: integer, U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
        * ``firmware_block``: hex string, Up to 2048 Bytes.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))
    

@register_command
@dataclass
class PX_CDB_WRITE_FW_BLOCK_LPL:
    """This is CMD 0103h: Write Firmware Block LPL
    """
    code: typing.ClassVar[int] = 474
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "cdb_status": 0
            }

        * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        """
    class SetDataAttr(RequestBodyStruct):
        cmd_data: dict = field(XmpJson(min_len=2))
        """dict, json
        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CDB_WRITE_FIRMWARE_BLOCK_LPL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    def set(self, cmd_data: dict) -> Token[None]:
        """
        Set CMD Data

        :param cmd_data: CMD DATA
        :type cmd_data: dict

        .. code-block:: json

            {
              "block_address": 12,
              "firmware_block": "0x00010203040506070809"
            }

        * ``block_address``: integer, U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
        * ``firmware_block``: hex string, Up to 116 bytes. One block of the firmware image. The actually needed length may be shorter than the available FirmwareBlock field size.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))



@register_command
@dataclass
class PX_CUST_CMD:
    """Defines the custom request and reply to be sent to the CDB instance.
    """
    code: typing.ClassVar[int] = 486
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _cdb_instance_xindex: int

    class SetDataAttr(RequestBodyStruct):
        cmd: dict = field(XmpJson(min_len=2))
        """Set CMD
        """

    
    def set(self, cmd: dict) -> Token[None]:
        """
        Set CMD

        :param cmd: CMD
        :type cmd: dict

        .. code-block:: json

            {
              "cmd_header": 
                {
                  "cmd_id": "0x00",
                  "epl_length": 0,
                  "lpl_length": 0,
                  "rpl_length": 0,
                  "rpl_check_code": 0
                },
              "cmd_data": 
                {
                  "data": "0x00"
                }
            }

        * ``cmd_header``: dict, contains the command header fields.

            * ``cmd_id``: hex string, command ID.
            * ``epl_length``: integer, length of the EPL.
            * ``lpl_length``: integer, length of the LPL.
            * ``rpl_length``: integer, length of the RPL. (optional)
            * ``rpl_check_code``: integer, check code for the RPL. (optional)

        * ``cmd_data``: dict, contains the command data fields.

            * ``data``: hex string, command data.

        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd=cmd))
    
    class GetDataAttr(ResponseBodyStruct):
        reply: dict = field(XmpJson(min_len=2))
        """dict, json
        
        .. code-block:: json

            {
              "reply_status": {
                "cdb_cmd_complete_flag": "0x00",
                "cdb_status": 0,
              },
              "reply_header": {
                "rpl_length": 9,
                "rpl_check_code": 9
              }
              "reply_data": {
                "data": "0x00"
              }
            }

        * ``reply_status``: dict, JSON formatted string containing the following fields:

            * ``cdb_cmd_complete_flag``: hex string, indicates whether the CDB command is complete.
            * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

        * ``reply_header``: dict, JSON formatted string containing the following fields:

            * ``rpl_length``: integer, length of the reply data.
            * ``rpl_check_code``: integer, check code for the reply data.

        * ``reply_data``: dict, JSON formatted string containing the following fields:

            * ``data``: hex string, the actual data to be sent in the reply.

        """

    def get(self) -> Token[GetDataAttr]:
        """Get REPLY

        :return: REPLY
        :rtype: PX_CUST_CMD.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    


# @register_command
# @dataclass
# class PX_CUST_REPLY:
#     """Defines the custom reply to receiver for the CDB instance.
#     """
#     code: typing.ClassVar[int] = 487
#     pushed: typing.ClassVar[bool] = False

#     _connection: 'interfaces.IConnection'
#     _module: int
#     _port: int
#     _cdb_instance_xindex: int

#     class GetDataAttr(ResponseBodyStruct):
#         reply: bytes = field(XmpJson(min_len=2))
#         """bytes, json
        
#         .. code-block:: json

#             {
#                 "reply_status": {
#                     "cdb_cmd_complete_flag": "0x00",
#                     "cdb_status": 0,
#                 },
#                 "reply_header": {
#                     "rpl_length": 9,
#                     "rpl_check_code": 9
#                 }
#                 "reply_data": {
#                     "data": "0x00"
#                 }
#             }

#         * ``reply_status``: dict, JSON formatted string containing the following fields:

#             * ``cdb_cmd_complete_flag``: hex string, indicates whether the CDB command is complete.
#             * ``cdb_status``: integer, provides the status of the most recently triggered CDB command.

#         * ``reply_header``: dict, JSON formatted string containing the following fields:

#             * ``rpl_length``: integer, length of the reply data.
#             * ``rpl_check_code``: integer, check code for the reply data.

#         * ``reply_data``: dict, JSON formatted string containing the following fields:

#             * ``data``: hex string, the actual data to be sent in the reply.

#         """

#     def get(self) -> Token[GetDataAttr]:
#         """Get REPLY

#         :return: REPLY
#         :rtype: PX_CUST_REPLY.GetDataAttr
#         """
#         return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex]))
    
    
# @register_command
# @dataclass
# class PX_CUST_REQUEST:
#     """Defines the custom request to be sent to the CDB instance.
#     """
#     code: typing.ClassVar[int] = 486
#     pushed: typing.ClassVar[bool] = False

#     _connection: 'interfaces.IConnection'
#     _module: int
#     _port: int
#     _cdb_instance_xindex: int

#     class SetDataAttr(RequestBodyStruct):
#         cmd_data: bytes = field(XmpJson(min_len=2))
#         """Set CMD Data
#         """

    
#     def set(self, cmd_data: dict) -> Token[None]:
#         """
#         Set CMD Data
#         :param cmd_data: CMD DATA
#         :type cmd_data: dict

#         .. code-block:: json

#             {
#                 "cmd_header": {
#                     "cmd_id": "0x00",
#                     "epl_length": 0,
#                     "lpl_length": 0,
#                     "rpl_length": 0,
#                     "rpl_check_code": 0
#                 },
#                 "cmd_data": {
#                     "data": "0x00"
#                 }
#             }

#         * ``cmd_header``: dict, contains the command header fields.

#             * ``cmd_id``: hex string, command ID.
#             * ``epl_length``: integer, length of the EPL.
#             * ``lpl_length``: integer, length of the LPL.
#             * ``rpl_length``: integer, length of the RPL. (optional)
#             * ``rpl_check_code``: integer, check code for the RPL. (optional)

#         * ``cmd_data``: dict, contains the command data fields.

#             * ``data``: hex string, command data.

#         """

#         return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._cdb_instance_xindex], cmd_data=cmd_data))

    
# endregion

__all__ = [
    "PX_CDB_ABORT_FW_DOWNLOAD",
    "PX_CDB_ABORT_PROCESSING",
    "PX_CDB_CHANGE_PASSWORD",
    "PX_CDB_COMMIT_FW_IMAGE",
    "PX_CDB_COMPLETE_FW_DOWNLOAD",
    "PX_CDB_COPY_FW_IMAGE",
    "PX_CDB_ENTER_PASSWORD",
    "PX_CDB_EXTERNAL_FEATURES",
    "PX_CDB_FW_MGMT_FEATURES",
    "PX_CDB_GET_APP_ATTRIBUTES",
    "PX_CDB_GET_FW_INFO",
    "PX_CDB_GET_IF_CODE_DESCR",
    "PX_CDB_MODULE_FEATURES",
    "PX_CDB_QUERY_STATUS",
    "PX_CDB_READ_FW_BLOCK_EPL",
    "PX_CDB_READ_FW_BLOCK_LPL",
    "PX_CDB_RUN_FW_IMAGE",
    "PX_CDB_SEC_FEAT_CAPABILITIES",
    "PX_CDB_START_FW_DOWNLOAD",
    "PX_CDB_SUPPORT",
    "PX_CDB_WRITE_FW_BLOCK_EPL",
    "PX_CDB_WRITE_FW_BLOCK_LPL",
    "PX_CUST_CMD",
    "PX_I2C_CONFIG",
    "PX_MII",
    "PX_RW",
    "PX_RW_SEQ",
    "PX_RW_SEQ_BANK",
    "PX_TEMPERATURE",
]