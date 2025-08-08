from __future__ import annotations
import typing as t
from xoa_driver.ports import Z800FreyaPort
from ._utils import *
from ._constants import *
import time
from contextlib import suppress
from xoa_driver import exceptions
import json


# CMD 0000h: Query Status
class CMD0000hQueryStatusReply:
    """REPLY message of CMD 0000h Query Status
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        In Progress

        * ``10 000001b``: Busy capturing command
        * ``10 000010b``: Busy checking/validating command
        * ``10 000011b``: Busy executing command
        
        On Success

        * ``00 000001b``: Success
        
        On Failure

        * ``01 000000b``: Failed, no specific failure
        * ``01 000101b``: CdbChkCode error

        """
        
        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.status: str = reply["status"]
        """hex string

            * ``0000 0000b``: Module Boot Up.
            * ``0000 0001b``: Host Password Accepted.
            * ``1xxx xxxxb``: Module Password accepted.
            * Bits ‘x’ may contain custom information.

        """

async def cmd_0000h_query_status_cmd(port: Z800FreyaPort, cdb_instance: int, response_delay: int) -> None:
    """Send CMD 0000h Query Status

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param response_delay: Programmable delay in ms for module responding to this command. A value of 0 asks for module response as fast as possible.
    :type response_delay: int
    """

    cmd_data = {
        "response_delay": response_delay
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0000h_query_status.set(cmd_data=cmd_data)

async def cmd_0000h_query_status_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0000hQueryStatusReply:
    """Read the module response to CMD 0000h Query Status

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0000h Query Status
    :rtype: CMD0000hQueryStatusReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0000h_query_status.get()
            return CMD0000hQueryStatusReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)

# CMD 0001h: Enter Password
class CMD0001hEnterPasswordReply:
    """REPLY message of CMD 0001h Enter Password
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        On Success

            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000101b``: CdbChkCode error
            * ``01 000110b``: Password error – not accepted

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0001h_enter_password_cmd(port: Z800FreyaPort, cdb_instance: int, password: str) -> None:
    """Send CMD 0001h Enter Password

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param password: password to be entered
    :type password: hex str
    """

    cmd_data = {
        "password": password
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0001h_enter_password.set(cmd_data=cmd_data)

async def cmd_0001h_enter_password_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0001hEnterPasswordReply:
    """Read the module response to CMD 0001h Enter Password

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0001h Enter Password
    :rtype: CMD0001hEnterPasswordReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0001h_enter_password.get()
            return CMD0001hEnterPasswordReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)
    

# CMD 0002h: Change Password
class CMD0002hChangePasswordReply:
    """REPLY message of CMD 0002h Change Password
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        On Success
        
            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error (e.g. Bit 31 is set).
            * ``01 000101b``: CdbChkCode error
            * ``01 000110b``: Insufficient privilege to change password

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0002h_change_password_cmd(port: Z800FreyaPort, cdb_instance: int, new_password: str) -> None:
    """Send CMD 0002h Change Password

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param new_password: new password to be entered
    :type new_password: hex str
    """
    cmd_data = {
        "new_password": new_password
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0002h_change_password.set(cmd_data=cmd_data)

async def cmd_0002h_change_password_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0002hChangePasswordReply:
    """Read the module response to CMD 0002h Change Password

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0002h Change Password
    :rtype: CMD0002hChangePasswordReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0002h_change_password.get()
            return CMD0002hChangePasswordReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0004h: Abort Processing
class CMD0004hAbortProcessingReply:
    """REPLY message of CMD 0004h Abort Processing
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        On Success
        
            * ``00 000001b``: Success
        
        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0004h_abort_processing_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0004h Abort Processing

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0004h_abort_processing.set()

async def cmd_0004h_abort_processing_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0004hAbortProcessingReply:
    """Read the module response to CMD 0004h Abort Processing

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0004h Abort Processing
    :rtype: CMD0004hAbortProcessingReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0004h_abort_processing.get()
            return CMD0004hAbortProcessingReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0040h: Module Features
class CMD0040hModuleFeaturesReply:
    """REPLY message of CMD 0040h Module Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        On Success
        
            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.cmd_support_0000h_0007h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][2:4]
        """Support mask for CMD 0000h to CMD 0007h"""
        self.cmd_support_0008h_000fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][4:6]
        """Support mask for CMD 0008h to CMD 000fh"""
        self.cmd_support_0010h_0017h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][6:8]
        """Support mask for CMD 0010h to CMD 0017h"""
        self.cmd_support_0018h_001fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][8:10]
        """Support mask for CMD 0018h to CMD 001fh"""
        self.cmd_support_0020h_0027h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][10:12]
        """Support mask for CMD 0020h to CMD 0027h"""
        self.cmd_support_0028h_002fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][12:14]
        """Support mask for CMD 0028h to CMD 002fh"""
        self.cmd_support_0030h_0037h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][14:16]
        """Support mask for CMD 0030h to CMD 0037h"""
        self.cmd_support_0038h_003fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][16:18]
        """Support mask for CMD 0038h to CMD 003fh"""
        self.cmd_support_0040h_0047h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][18:20]
        """Support mask for CMD 0040h to CMD 0047h"""
        self.cmd_support_0048h_004fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][20:22]
        """Support mask for CMD 0048h to CMD 004fh"""
        self.cmd_support_0050h_0057h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][22:24]
        """Support mask for CMD 0050h to CMD 0057h"""
        self.cmd_support_0058h_005fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][24:26]
        """Support mask for CMD 0058h to CMD 005fh"""
        self.cmd_support_0060h_0067h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][26:28]
        """Support mask for CMD 0060h to CMD 0067h"""
        self.cmd_support_0068h_006fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][28:30]
        """Support mask for CMD 0068h to CMD 006fh"""
        self.cmd_support_0070h_0077h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][30:32]
        """Support mask for CMD 0070h to CMD 0077h"""
        self.cmd_support_0078h_007fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][32:34]
        """Support mask for CMD 0078h to CMD 007fh"""
        self.cmd_support_0080h_0087h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][34:36]
        """Support mask for CMD 0080h to CMD 0087h"""
        self.cmd_support_0088h_008fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][36:38]
        """Support mask for CMD 0088h to CMD 008fh"""
        self.cmd_support_0090h_0097h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][38:40]
        """Support mask for CMD 0090h to CMD 0097h"""
        self.cmd_support_0098h_009fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][40:42]
        """Support mask for CMD 0098h to CMD 009fh"""
        self.cmd_support_00a0h_00a7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][42:44]
        """Support mask for CMD 00a0h to CMD 00a7h"""
        self.cmd_support_00a8h_00afh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][44:46]
        """Support mask for CMD 00a8h to CMD 00afh"""
        self.cmd_support_00b0h_00b7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][46:48]
        """Support mask for CMD 00b0h to CMD 00b7h"""
        self.cmd_support_00b8h_00bfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][48:50]
        """Support mask for CMD 00b8h to CMD 00bfh"""
        self.cmd_support_00c0h_00c7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][50:52]
        """Support mask for CMD 00c0h to CMD 00c7h"""
        self.cmd_support_00c8h_00cfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][52:54]
        """Support mask for CMD 00c8h to CMD 00cfh"""
        self.cmd_support_00d0h_00d7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][54:56]
        """Support mask for CMD 00d0h to CMD 00d7h"""
        self.cmd_support_00d8h_00dfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][56:58]
        """Support mask for CMD 00d8h to CMD 00dfh"""
        self.cmd_support_00e0h_00e7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][58:60]
        """Support mask for CMD 00e0h to CMD 00e7h"""
        self.cmd_support_00e8h_00efh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][60:62]
        """Support mask for CMD 00e8h to CMD 00efh"""
        self.cmd_support_00f0h_00f7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][62:64]
        """Support mask for CMD 00f0h to CMD 00f7h"""
        self.cmd_support_00f8h_00ffh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][64:66]
        """Support mask for CMD 00f8h to CMD 00ffh"""
        self.max_completion_time: int = reply["max_completion_time"]
        """integer, U16 Maximum CDB command execution time in ms, of all supported CDB commands
        """

async def cmd_0040h_module_features_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0040h Module Features

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0040h_module_features.set()

async def cmd_0040h_module_features_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0040hModuleFeaturesReply:
    """Read the module response to CMD 0040h Module Features

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0040h Module Features
    :rtype: CMD0040hModuleFeaturesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0040h_module_features.get()
            return CMD0040hModuleFeaturesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0041h: Firmware Management Features
class CMD0041hFirmwareManagementFeaturesReply:
    """REPLY message of CMD 0041h Firmware Management Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.

        On Success
            
            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.image_readback: int = 1 if int(reply["feature_support_mask"], 16) & 0x80 else 0
        """
        * 0b = Full Image Readback Not Supported
        * 1b = Full Image Readback Supported

        """
        self.max_duration_coding: int = 1 if int(reply["feature_support_mask"], 16) & 0x08 else 0
        """
        * 0b = max duration multiplier M is 1
        * 1b = max duration multiplier M is 10
        
        This bit encodes a multiplier value M which governs the interpretation of values found in the U16 array of advertised max durations in Bytes 144-153 of this message: These advertised values are multiplied by M.

        """
        self.skipping_erased_blocks: int = 1 if int(reply["feature_support_mask"], 16) & 0x04 else 0
        """
        * 0b = Skipping erased blocks Not Supported
        * 1b = Skipping erased blocks Supported

        """
        self.copy_cmd: int = 1 if int(reply["feature_support_mask"], 16) & 0x02 else 0
        """
        * 0b = CMD 0108h (Copy image) Not Supported
        * 1b = CMD 0108h (Copy image) Supported

        """
        self.abort_cmd: int = 1 if int(reply["feature_support_mask"], 16) & 0x01 else 0
        """
        * 0b = CMD 0102h (Abort) Not Supported
        * 1b = CMD 0102h (Abort) Supported

        """
        self.start_cmd_payload_size: int = reply["start_cmd_payload_size"]
        """integer, This defines the number of bytes that the host must extract from the beginning of the vendor-delivered binary firmware image file and send to the module in CMD 0101h (Start)
        """
        self.erased_byte: str = reply["erased_byte"]
        """hex string, This is the value representing an erased byte. The purpose of advertising this byte is to optionally reduce download time by allowing the host to skip sending blocks of the image containing ErasedByte values only.
        """
        self.read_write_length_ext: int = reply["read_write_length_ext"]
        """integer, specifies the allowable additional number of byte octets in a READ or a WRITE, specifically for Firmware Management Commands (IDs 0100h-01FFh) as follows:

        EPL: For accessing the multi-page EPL field, the allowable length extension is i byte octets (8 bytes).
        
        LPL: For accessing the LPL field on page 9Fh, the allowable length extension is min(i, 15) byte octets.

        This leads to the maximum length of a READ or a WRITE

        Value Maximum Number of Bytes (EPL)

        * 0:    8 bytes (no extension of general length limit)
        * i:    8 * (1+i) bytes (0 ≤ i ≤ 255)
        * 255:  8 * 256 = 2048 bytes

        Value  Maximum Number of Bytes (LPL)
        
        * 0:     8 bytes (no extension of general length limit)
        * i:     8 * (1+i) bytes (0 ≤ i ≤ 15)
        * i:     8 * 16 = 128 bytes (16 ≤ i ≤ 256)

        """
        self.write_mechanism: str = reply["write_mechanism"]
        """hex string, Firmware update supported mechanism

        * 00h: None Supported.
        * 01h: Write to LPL supported.
        * 10h: Write to EPL supported.
        * 11h: Both Write to LPL and EPL supported.

        """
        self.read_mechanism: str = reply["read_mechanism"]
        """hex string, Firmware read / readback support mechanism.

        * 00h: None Supported.
        * 01h: Read via LPL supported.
        * 10h: Read via EPL supported.
        * 11h: Both Read via LPL and EPL supported.

        """
        self.hitless_restart: int = reply["hitless_restart"]
        """integer
        
        * 0: CMD Run Image causes a reset. Traffic is affected. 
        * 1: CMD Run Image may reset but module will do its best to maintain traffic and management states. Data path functions are not reset.

        """
        self.max_duration_start: int = reply["max_duration_start"]
        """integer, U16 Maximum time in M ms for a CDB Start command to complete execution
        """
        self.max_duration_abort: int = reply["max_duration_abort"]
        """integer, U16 Maximum time in M ms for a CDB Abort command to complete execution
        """
        self.max_duration_write: int = reply["max_duration_write"]
        """integer, U16 Maximum time in M ms for a CDB Write command to complete execution
        """
        self.max_duration_complete: int = reply["max_duration_complete"]
        """integer, U16 Maximum time in M ms for a CDB Complete command to complete execution
        """
        self.max_duration_copy: int = reply["max_duration_copy"]
        """integer, U16 Maximum time in M ms for a CDB Copy command to complete execution
        """

async def cmd_0041h_fw_mgmt_features_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0041h Firmware Management Features

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0041h_fw_mgmt_features.set()

async def cmd_0041h_fw_mgmt_features_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0041hFirmwareManagementFeaturesReply:
    """Read the module response to CMD 0041h Firmware Management Features

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0041h Firmware Management Features
    :rtype: CMD0041hFirmwareManagementFeaturesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0041h_fw_mgmt_features.get()
            return CMD0041hFirmwareManagementFeaturesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0044h: Security Features and Capabilities
class CMD0044hSecFeaturesAndCapabilitiesReply:
    """REPLY message of CMD 0044h Security Features and Capabilities
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        On Success
        
            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.cmd_support_0400h_0407h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][2:4]
        """
        CMD 0400h-0407h support.

        Each bit represents a mask. If a bit is set, the corresponding command is supported
        
        * D0: CMD 0400h is supported.
        * ..
        * D7: CMD 0407h is supported

        """
        self.cmd_support_0408h_040fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][4:6]
        """CMD 0408h-040Fh support
        """
        self.cmd_support_0410h_0417h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][6:8]
        """CMD 0410h-0417h support
        """
        self.cmd_support_0418h_041fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][8:10]
        """CMD 0418h-041Fh support
        """
        self.cmd_support_0420h_0427h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][10:12]
        """CMD 0420h-0427h support
        """
        self.cmd_support_0428h_042fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][12:14]
        """CMD 0428h-042Fh support
        """
        self.cmd_support_0430h_0437h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][14:16]
        """CMD 0430h-0437h support
        """
        self.cmd_support_0438h_043fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][16:18]
        """CMD 0438h-043Fh support
        """
        self.cmd_support_0440h_0447h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][18:20]
        """CMD 0440h-0447h support
        """
        self.cmd_support_0448h_044fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][20:22]
        """CMD 0448h-044Fh support
        """
        self.cmd_support_0450h_0457h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][22:24]
        """CMD 0450h-0457h support
        """
        self.cmd_support_0458h_045fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][24:26]
        """CMD 0458h-045Fh support
        """
        self.cmd_support_0460h_0467h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][26:28]
        """CMD 0460h-0467h support
        """
        self.cmd_support_0468h_046fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][28:30]
        """CMD 0468h-046Fh support
        """
        self.cmd_support_0470h_0477h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][30:32]
        """CMD 0470h-0477h support
        """
        self.cmd_support_0478h_047fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][32:34]
        """CMD 0478h-047Fh support
        """
        self.cmd_support_0480h_0487h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][34:36]
        """CMD 0480h-0487h support
        """
        self.cmd_support_0488h_048fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][36:38]
        """CMD 0488h-048Fh support
        """
        self.cmd_support_0490h_0497h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][38:40]
        """CMD 0490h-0497h support
        """
        self.cmd_support_0498h_049fh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][40:42]
        """CMD 0498h-049Fh support
        """
        self.cmd_support_04a0h_04a7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][42:44]
        """CMD 04a0h-04a7h support
        """
        self.cmd_support_04a8h_04afh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][44:46]
        """CMD 04a8h-04afh support
        """
        self.cmd_support_04b0h_04b7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][46:48]
        """CMD 04b0h-04b7h support
        """
        self.cmd_support_04b8h_04bfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][48:50]
        """CMD 04b8h-04bfh support
        """
        self.cmd_support_04c0h_04c7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][50:52]
        """CMD 04c0h-04c7h support
        """
        self.cmd_support_04c8h_04cfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][52:54]
        """CMD 04c8h-04cfh support
        """
        self.cmd_support_04d0h_04d7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][54:56]
        """CMD 04d0h-04d7h support
        """
        self.cmd_support_04d8h_04dfh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][56:58]
        """CMD 04d8h-04dfh support
        """
        self.cmd_support_04e0h_04e7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][58:60]
        """CMD 04e0h-04e7h support
        """
        self.cmd_support_04e8h_04efh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][60:62]
        """CMD 04e8h-04efh support
        """
        self.cmd_support_04f0h_04f7h: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][62:64]
        """CMD 04f0h-04f7h support
        """
        self.cmd_support_04f8h_04ffh: str = reply["cmd_support_mask"][0:2]+reply["cmd_support_mask"][64:66]
        """CMD 04f8h-04ffh support
        """
        self.num_certificates: int = reply["num_certificates"]
        """integer, Number of public certificates the host may obtain from the module. 
        
        The device must contain a single leaf certificate and it may optionally contain one or more intermediate certificates optionally followed by a root certificate. For X.509 certificates, intermediate certificates are not self-signed, and the root cert is self-signed.

        ``num_certificates <= 4``

        """
        self.cert_chain_supported: int = reply["cert_chain_supported"]
        """integer
        
        * 0: Certificate chain is not supported. Module contains leaf certificate instance i = 0 only. 
        * 1: Module supports certificate chain and host must specify the instance when downloading a certificate.
        
        Instance i = 0 is the start of the chain, i.e. the leaf certificate, and any instance i+1 is another certificate used to sign the certificate instance i, where ``i < num_certificates <= 4``

        """
        self.certificate_format: int = reply["certificate_format"]
        """integer
        
        * 0: Not supported. 
        * 1: **Custom**. 
        * 2: X509v3 DER encoding. 
        * 3-255: Reserved.

        """
        self.certificate_length_1: int = reply["certificate_length_1"]
        """integer, Length of leaf certificate i = 0.
        """
        self.certificate_length_2: int = reply["certificate_length_2"]
        """integer, Length of certificate i = 1 or 0 when not supported.
        """
        self.certificate_length_3: int = reply["certificate_length_3"]
        """integer, Length of certificate i = 2 or 0 when not supported.
        """
        self.certificate_length_4: int = reply["certificate_length_4"]
        """integer, Length of certificate i = 3 or 0 when not supported.
        """
        self.digest_length: int = reply["digest_length"]
        """integer, Required message hash digest length (in bytes) 
        
        * 0: Not supported. 
        * 1: 28 bytes (SHA224). 
        * 2: 32 bytes (SHA256). 
        * 3: 48 bytes (SHA384). 
        * 4: 64 bytes (SHA512). 
        * 5-255: **Reserved**.

        """
        self.signature_time: int = reply["signature_time"]
        """integer, Maximum time (in milliseconds) for signature generation.
        """
        self.signature_length: int = reply["signature_length"]
        """integer, Length (in bytes) of the encoded/padded (if applicable) digest signature
        """
        self.signature_format: int = reply["signature_format"]
        """integer
        * 0: Not supported. 
        * 1: **Custom, vendor specific encoding**. 
        * 2: Raw binary byte stream. 
        * 3: DER encoding. 
        * 4: ECDSA (R,S) integer pair, integers prefixed with length. 
        * 5-255: Reserved.

        """
        self.signature_pad_scheme: int = reply["signature_pad_scheme"]
        """integer
        
        * 0: None. 
        * 1: **Custom**. 
        * 2: PKCS#1 v1.5. 
        * 3: OAEP. 
        * 4: PSS. 
        * 5-255: Reserved

        """

async def cmd_0044h_sec_feat_capabilities_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0044h Security Features and Capabilities

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0044h_sec_feat_capabilities.set()

async def cmd_0044h_sec_feat_and_capabilities_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0044hSecFeaturesAndCapabilitiesReply:
    """Read the module response to CMD 0044h Security Features and Capabilities

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0044h Security Features and Capabilities
    :rtype: CMD0044hSecFeaturesAndCapabilitiesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0044h_sec_feat_capabilities.get()
            return CMD0044hSecFeaturesAndCapabilitiesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)

# CMD 0045h: Externally Defined Features
class CMD0045hExternallyDefinedFeaturesReply:
    """REPLY message of CMD 0045h Externally Defined Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.supplement_support: str = reply["supplement_support"]
        """Bit 0 = 0/1: CMIS-VCS not supported/supported
        """

async def cmd_0045h_externally_defined_features_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0045h Externally Defined Features

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0045h_external_features.set()

async def cmd_0045h_externally_defined_features_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0045hExternallyDefinedFeaturesReply:
    """Read the module response to CMD 0045h Externally Defined Features

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0045h Externally Defined Features
    :rtype: CMD0045hExternallyDefinedFeaturesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0045h_external_features.get()
            return CMD0045hExternallyDefinedFeaturesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)

# CMD 0050h: Get Application Attributes
class CMD0050hGetApplicationAttributesReply:
    """REPLY message of CMD 0050h Get Application Attributes
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution

        On Success

            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.application_number: int = reply["application_number"]
        """integer, U16 Application number. 
        
        * 15-8: reserved (0). 
        * 7-4: NADBlockIndex (0-15) or 0. 
        * 3-0: AppSelCode (1-15).

        """
        self.max_module_power: int = reply["max_module_power"]
        """integer, U16: Worst case module power dissipation when this Application is instantiated homogeneously as often as possible in parallel (when applicable) with worst case configuration options. 
        
        Unit: 0.25 W.

        """
        self.prog_output_power_min: int = reply["prog_output_power_min"]
        """integer, S16: Minimum Programmable Output Power, Unit: 0.01 dBm.
        """
        self.prog_output_power_max: int = reply["prog_output_power_max"]
        """integer, S16: Maximum Programmable Output Power, Unit: 0.01 dBm.
        """
        self.pre_fec_ber_threshold: float = reply["pre_fec_ber_threshold"]
        """float, F16: Pre FEC BER VDM high alarm threshold.
        """
        self.rx_los_optical_power_threshold: int = reply["rx_los_optical_power_threshold"]
        """integer, S16: Optical power threshold for RxLOS alarm. Unit: 0.01dBm.
        """
        self.rx_power_high_alarm_threshold: int = reply["rx_power_high_alarm_threshold"]
        """integer, U16: OpticalPowerRxHighAlarmThreshold. Unit: 0.1uW.
        """
        self.rx_power_low_alarm_threshold: int = reply["rx_power_low_alarm_threshold"]
        """integer, U16: OpticalPowerRxLowAlarmThreshold. Unit: 0.1uW.
        """
        self.rx_power_high_warning_threshold: int = reply["rx_power_high_warning_threshold"]
        """integer, U16: OpticalPowerRxHighWarningThreshold.Unit: 0.1uW.
        """
        self.rx_power_low_warning_threshold: int = reply["rx_power_low_warning_threshold"]
        """integer, U16: OpticalPowerRxLowWarningThreshold. Unit: 0.1uW.
        """

async def cmd_0050h_get_application_attributes_cmd(port: Z800FreyaPort, cdb_instance: int, application_number: int) -> None:
    """Send CMD 0050h Get Application Attributes

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param application_number: U16 Application number. 15-8: reserved (0). 7-4: NADBlockIndex (0-15) or 0. 3-0: AppSelCode (1-15)
    :type application_number: int
    """
    cmd_data = {
        "application_number": application_number
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0050h_get_app_attributes.set(cmd_data=cmd_data)

async def cmd_0050h_get_application_attributes_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0050hGetApplicationAttributesReply:
    """Read the module response to CMD 0050h Get Application Attributes

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0050h Get Application Attributes
    :rtype: CMD0050hGetApplicationAttributesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0045h_external_features.get()
            return CMD0050hGetApplicationAttributesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)
        

# CMD 0051h: Get Interface Code Description
class CMD0051hGetInterfaceCodeDescriptionReply:
    """REPLY message of CMD 0051h Get Interface Code Description
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success

            * ``00 000001b``: Success
        
        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.interface_id: str = reply["interface_id"]
        """hex string, U16: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
        """
        self.interface_location: str = reply["interface_location"]
        """integer, 0: media side. 1: host side.
        """
        self.interfacre_name: str = reply["interfacre_name"]
        """string, 16-byte long ACII string. Name of the interface.
        """
        self.interfacre_description: str = reply["interfacre_description"]
        """string, 48-byte long ACII string. Description of the interface.
        """
        self.interfacre_data_rate: float = reply["interfacre_data_rate"]
        """float, F16: Application Bit Rate in Gb/s
        """
        self.interfacre_lane_count: str = reply["interfacre_lane_count"]
        """integer, U16: Number of parallel lanes.
        """
        self.lane_signaling_rate: float = reply["lane_signaling_rate"]
        """float, F16: Lane Signaling Rate in GBd.
        """
        self.modulation: str = reply["modulation"]
        """string, 16-byte long ACII string. Lane Modulation Format.
        """
        self.bits_per_symbol: int = reply["bits_per_symbol"]
        """ integer, U16: Bits per Symbol.
        """

async def cmd_0051h_get_interface_code_description_cmd(port: Z800FreyaPort, cdb_instance: int, interface_id: str, interface_location: int) -> None:
    """Send CMD 0051h Get Interface Code Description

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param interface_id: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
    :type interface_id: hex str
    :param interface_location: 0: Media side. 1: Host side
    :type interface_location: int
    """
    cmd_data = {
        "interface_id": interface_id,
        "interface_location": "0x{:02x}".format(interface_location)
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0051h_get_if_code_descr.set(cmd_data=cmd_data)

async def cmd_0051h_get_interface_code_description_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0051hGetInterfaceCodeDescriptionReply:
    """Read the module response to CMD 0051h Get Interface Code Description

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0051h Get Interface Code Description
    :rtype: CMD0051hGetInterfaceCodeDescriptionReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0051h_get_if_code_descr.get()
            return CMD0051hGetInterfaceCodeDescriptionReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0100h: Get Firmware Info
class CMD0100hGetFirmwareInfoReply:
    """REPLY message of CMD 0100h Get Firmware Info
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """
        hex string, provides the status of the most recently triggered CDB command.
        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

        self.firmware_status: int = reply["firmware_status"]
        """
        integer, Firmware Status.

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

        """
        self.image_information: int = reply["image_information"]
        """
        integer, Image Information.

            * Bit 0: Firmware image A information
            * Bit 1: Firmware image B information
            * Bit 2: Factory or Boot image information

        """
        self.image_a_major: int = reply["image_a_major"]
        """integer, Image A firmware major revision.
        """
        self.image_a_minor: int = reply["image_a_minor"]
        """integer, Image A firmware minor revision.
        """
        self.image_a_build: int = reply["image_a_build"]
        """integer, Image A firmware build number.
        """
        self.image_a_extra_string: str = reply["image_a_extra_string"]
        """string, Image A additional information (32-byte long ASCII string).
        """
        self.image_b_major: int = reply["image_b_major"]
        """integer, Image B firmware major revision.
        """
        self.image_b_minor: int = reply["image_b_minor"]
        """integer, Image B firmware minor revision.
        """
        self.image_b_build: int = reply["image_b_build"]
        """integer, Image B firmware build number.
        """
        self.image_b_extra_string: str = reply["image_b_extra_string"]
        """string, Image B additional information (32-byte long ASCII string).
        """
        self.factory_boot_major: int = reply["factory_boot_major"]
        """integer, Factory or Boot firmware major revision.
        """
        self.factory_boot_minor: int = reply["factory_boot_minor"]
        """integer, Factory or Boot firmware minor revision.
        """
        self.factory_boot_build: int = reply["factory_boot_build"]
        """integer, Factory or Boot firmware build number.
        """
        self.factory_boot_extra_string: int = reply["factory_boot_extra_string"]
        """string, Factory or Boot additional information (32-byte long ASCII string).
        """

async def cmd_0100h_get_firmware_info_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0100h Get Firmware Info

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0100h_get_firmware_info.set()

async def cmd_0100h_get_firmware_info_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0100hGetFirmwareInfoReply:
    """Read the module response to CMD 0100h Get Firmware Info

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0100h Get Firmware Info
    :rtype: CMD0100hGetFirmwareInfoReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0100h_get_firmware_info.get()
            return CMD0100hGetFirmwareInfoReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0101h: Start Firmware Download
class CMD0101hStartFirmwareDownloadReply:
    """REPLY message of CMD 0101h Start Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution

        On Success

            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0101h_start_firmware_download_cmd(port: Z800FreyaPort, cdb_instance: int, image_size: int, vendor_data: str) -> None:
    """Send CMD 0101h Start Firmware Download

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param image_size: U32 Size of firmware image to download into the module. This should be the file size including the LPL bytes sent as vendor data in this message.
    :type image_size: int
    :param vendor_data: U8 Array of vendor specific data to be sent to the module. This data is sent as part of the firmware download message. The size of this data is included in the image_size parameter
    :type vendor_data: hex str
    """
    cmd_data = {
        "image_size": image_size,
        "vendor_data": vendor_data
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0101h_start_firmware_download.set(cmd_data=cmd_data)

async def cmd_0101h_start_firmware_download_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0101hStartFirmwareDownloadReply:
    """Read the module response to CMD 0101h Start Firmware Download

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0101h Start Firmware Download
    :rtype: CMD0101hStartFirmwareDownloadReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0101h_start_firmware_download.get()
            return CMD0101hStartFirmwareDownloadReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0102h: Abort Firmware Download
class CMD0102hAbortFirmwareDownloadReply:
    """REPLY message of CMD 0102h Abort Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.
        
        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0102h_abort_firmware_download_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0102h Abort Firmware Download

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0102h_abort_firmware_download.set()

async def cmd_0102h_abort_firmware_download_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0102hAbortFirmwareDownloadReply:
    """Read the module response to CMD 0102h Abort Firmware Download

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0102h Abort Firmware Download
    :rtype: CMD0102hAbortFirmwareDownloadReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0102h_abort_firmware_download.get()
            return CMD0102hAbortFirmwareDownloadReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0103h: Write Firmware Block LPL
class CMD0103hWriteFirmwareBlockLPLReply:
    """REPLY message of CMD 0103h Write Firmware Block LPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution

        On Success
        
            * ``00 000001b``: Success

        On Failure

            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0103h_write_firmware_block_lpl_cmd(port: Z800FreyaPort, cdb_instance: int, block_address: int, firmware_block: bytes) -> None:
    """Send CMD 0103h Write Firmware Block LPL

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the “Start Command Payload Size”.
    :type block_address: int
    :param firmware_block: U8[116] One block of the firmware image. The actually needed length may be shorter than the available FirmwareBlock field size. This actual length of the block is defined in Byte 132 (LPLLength)
    :type firmware_block: bytes
    """
    cmd_data = {
        "block_address": block_address,
        "firmware_block": "0x" + bytes.hex(firmware_block).upper()
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0103h_write_firmware_block_lpl.set(cmd_data=cmd_data)

async def cmd_0103h_write_firmware_block_lpl_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0103hWriteFirmwareBlockLPLReply:
    """Read the module response to CMD 0103h Write Firmware Block LPL

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0103h Write Firmware Block LPL
    :rtype: CMD0103hWriteFirmwareBlockLPLReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0103h_write_firmware_block_lpl.get()
            return CMD0103hWriteFirmwareBlockLPLReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0104h: Write Firmware Block EPL
class CMD0104hWriteFirmwareBlockEPLReply:
    """REPLY message of CMD 0104h Write Firmware Block EPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress
        
            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution

        On Success
        
            * ``00 000001b``: Success

        On Failure
            
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0104h_write_firmware_block_epl_cmd(port: Z800FreyaPort, cdb_instance: int, block_address: int, firmware_block: bytes) -> None:
    """Send CMD 0104h Write Firmware Block EPL

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the “Start Command Payload Size”.
    :type block_address: int
    :param firmware_block: Up to 2048 Bytes. Actual Length specified in EPLLength
    :type firmware_block: hex str
    """

    cmd_data = {
        "block_address": block_address,
        "firmware_block": "0x" + bytes.hex(firmware_block).upper()
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0104h_write_firmware_block_epl.set(cmd_data=cmd_data)

async def cmd_0104h_write_firmware_block_epl_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0104hWriteFirmwareBlockEPLReply:
    """Read the module response to CMD 0104h Write Firmware Block EPL

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0104h Write Firmware Block EPL
    :rtype: CMD0104hWriteFirmwareBlockEPLReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0104h_write_firmware_block_epl.get()
            return CMD0104hWriteFirmwareBlockEPLReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0105h: Read Firmware Block LPL
class CMD0105hReadFirmwareBlockLPLReply:
    """REPLY message of CMD 0105h Read Firmware Block LPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress
        
            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """
        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """
        self.base_address_block: str = reply["base_address_block"]
        """hex string, Base address of the data block within the firmware image.
        """
        self.image_data: bytes = bytes.fromhex(reply["image_data"].replace("0x", ""))
        """hex string, Up to 116 bytes.
        """

async def cmd_0105h_read_firmware_block_lpl_cmd(port: Z800FreyaPort, cdb_instance: int, block_address: int, length: int) -> None:
    """Send CMD 0105h Read Firmware Block LPL

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
    :type block_address: int
    :param length: U16 Number of bytes to read back to the LPL in this command, starting at the indicated address.
    :type length: int
    """
    cmd_data = {
        "block_address": block_address,
        "length": length
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0105h_read_firmware_block_lpl.set(cmd_data=cmd_data)

async def cmd_0105h_read_firmware_block_lpl_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0105hReadFirmwareBlockLPLReply:
    """Read the module response to CMD 0105h Read Firmware Block LPL

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”.
    :type block_address: int
    :param length: U16 Number of bytes to read back to the LPL in this command, starting at the indicated address
    :type length: int
    :return: REPLY of CMD 0105h Read Firmware Block LPL
    :rtype: CMD0105hReadFirmwareBlockLPLReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0105h_read_firmware_block_lpl.get()
            return CMD0105hReadFirmwareBlockLPLReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)
    

# CMD 0106h: Read Firmware Block EPL
class CMD0106hReadFirmwareBlockEPLReply:
    """REPLY message of CMD 0106h Read Firmware Block EPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
            
            * ``00 000001b``: Success
        
        On Failure
            
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """
        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """
        self.image_data: bytes = bytes.fromhex(reply["image_data"].replace("0x", ""))
        """Up to 2048 Bytes. Actual Length specified in RPLLength
        """

async def cmd_0106h_read_firmware_block_epl_cmd(port: Z800FreyaPort, cdb_instance: int, block_address: int, length: int) -> None:
    """Send CMD 0106h Read Firmware Block EPL

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”
    :type block_address: int
    :param length: U16 Number of bytes to read back to the EPL in this command, starting at the indicated address.
    :type length: int
    """
    cmd_data = {
        "block_address": block_address,
        "length": length
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0106h_read_firmware_block_epl.set(cmd_data=cmd_data)

async def cmd_0106h_read_firmware_block_epl_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0106hReadFirmwareBlockEPLReply:
    """Read the module response to CMD 0106h Read Firmware Block EPL

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the “Start Command Payload Size”
    :type block_address: int
    :param length: U16 Number of bytes to read back to the EPL in this command, starting at the indicated address.
    :type length: int
    :return: REPLY of CMD 0106h Read Firmware Block EPL
    :rtype: CMD0106hReadFirmwareBlockEPLReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0106h_read_firmware_block_epl.get()
            return CMD0106hReadFirmwareBlockEPLReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0107h: Complete Firmware Download
class CMD0107hCompleteFirmwareDownloadReply:
    """REPLY message of CMD 0107h Complete Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0107h_complete_firmware_download_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 0107h Complete Firmware Download

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0107h_complete_firmware_download.set()

async def cmd_0107h_complete_firmware_download_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0107hCompleteFirmwareDownloadReply:
    """Read the module response to CMD 0107h Complete Firmware Download

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0107h Complete Firmware Download
    :rtype: CMD0107hCompleteFirmwareDownloadReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0107h_complete_firmware_download.get()
            return CMD0107hCompleteFirmwareDownloadReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0108h: Copy Firmware Image
class CMD0108hCopyFirmwareImageReply:
    """REPLY message of CMD 0108h Copy Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """
        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """
        self.length: int = reply["length"]
        """integer, number of bytes copied.
        """
        self.copy_direction: str = reply["copy_direction"]
        """hex string, copy direction.

        * ``0xAB``, Copy Image A into Image B
        * ``0xBA``,Copy Image B into Image A

        """
        self.copy_status: str = reply["copy_status"]
        """hex string, copy status.

        * ``0x00``, Copy Successful
        * ``0x01``, Copy Failed

        """

async def cmd_0108h_copy_firmware_image_cmd(port: Z800FreyaPort, cdb_instance: int, copy_direction: str) -> None:
    """Send CMD 0108h Copy Firmware Image

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param copy_direction: copy direction. 
    
        * ``0xAB``, Copy Image A into Image B
        * ``0xBA``,Copy Image B into Image A

    :type copy_direction: hex str
    """
    cmd_data = {
        "copy_direction": copy_direction
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0108h_copy_firmware_image.set(cmd_data=cmd_data)

async def cmd_0108h_copy_firmware_image_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0108hCopyFirmwareImageReply:
    """Read the module response to CMD 0108h Copy Firmware Image

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0108h Copy Firmware Image
    :rtype: CMD0108CopyFirmwareImageReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0108h_copy_firmware_image.get()
            return CMD0108hCopyFirmwareImageReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0109h: Run Firmware Image
class CMD0109hRunFirmwareImageReply:
    """REPLY message of CMD 0109h Run Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_0109h_run_firmware_image_cmd(port: Z800FreyaPort, cdb_instance: int, image_to_run: int, delay_to_reset: int) -> None:
    """Send CMD 0109h Run Firmware Image

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param image_to_run: integer, index of the image to run.

        * 0 = Traffic affecting Reset to Inactive Image.
        * 1 = Attempt Hitless Reset to Inactive Image
        * 2 = Traffic affecting Reset to Running Image.
        * 3 = Attempt Hitless Reset to Running Image
    
    :type image_to_run: int
    :param delay_to_reset: integer, Indicates the delay in ms after receiving this command before a reset will occur, starting from the time the CDB complete Flag is set.
    :type delay_to_reset: int
    """
    cmd_data = {
        "image_to_run": image_to_run,
        "delay_to_reset": delay_to_reset
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0109h_run_firmware_image.set(cmd_data=cmd_data)

async def cmd_0109h_run_firmware_image_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD0109hRunFirmwareImageReply:
    """Read the module response to CMD 0109h Run Firmware Image

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 0109h Run Firmware Image
    :rtype: CMD0109RunFirmwareImageReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0109h_run_firmware_image.get()
            return CMD0109hRunFirmwareImageReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 010Ah: Commit Firmware Image
class CMD010AhCommitFirmwareImageReply:
    """REPLY message of CMD 010Ah Commit Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_status: str = reply["cdb_status"]
        """hex string, provides the status of the most recently triggered CDB command.

        In Progress

            * ``10 000001b``: Busy processing command, CMD captured
            * ``10 000010b``: Busy processing command, CMD checking
            * ``10 000011b``: Busy processing command, CMD execution
        
        On Success
        
            * ``00 000001b``: Success
        
        On Failure
        
            * ``01 000000b``: Failed, no specific failure
            * ``01 000010b``: Parameter range error or not supported
            * ``01 000101b``: CdbChkCode error

        """

        self.cdb_cmd_complete_flag: bool = reply["cdb_cmd_complete_flag"]
        """
        Latched Flag to indicate completion of a CDB command for CDB instance.

        Set by module when the CDB command is complete.

        """

async def cmd_010ah_commit_firmware_image_cmd(port: Z800FreyaPort, cdb_instance: int) -> None:
    """Send CMD 010Ah Commit Firmware Image

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_010ah_commit_firmware_image.set()

async def cmd_010ah_commit_firmware_image_reply(port: Z800FreyaPort, cdb_instance: int) -> CMD010AhCommitFirmwareImageReply:
    """Read the module response to CMD 010Ah Commit Firmware Image

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 010Ah Commit Firmware Image
    :rtype: CMD010AhCommitFirmwareImageReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_010ah_commit_firmware_image.get()
            return CMD010AhCommitFirmwareImageReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 8000h-FFFFh: Custom Command

class CustomCMDReply:
    """Defines the custom reply to receiver for the CDB instance.
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_cmd_complete_flag: str = reply["reply_status"]["cdb_cmd_complete_flag"]
        """hex string, REPLY Status.CdbCmdCompleteFlag. 
        
        Indicates whether the CDB command is complete.

        """
        self.cdb_status: str = reply["reply_status"]["cdb_status"]
        """hex string, REPLY Status.CdbStatus. 
        
        Provides the status of the most recently triggered CDB command.

        """
        self.rpl_length: str = reply["reply_header"]["rpl_length"]
        """integer, REPLY Header.RPLLength.

        Length of the reply data.

        """
        self.rpl_check_code: str = reply["reply_header"]["rpl_check_code"]
        """integer, REPLY Header.RPLChkCode.
        
        Check code for the reply data.

        """
        self.data = reply["reply_data"]["data"]
        """hex string, REPLY Data.Data
        
        The actual data to be sent in the reply.

        """

async def cmd_custom_cmd_reply(port: Z800FreyaPort, cdb_instance: int) -> CustomCMDReply:
    """Read the module response to CMD 8000h-FFFFh Custom Command

    :param port: the port object to read the response from
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :return: REPLY of CMD 8000h-FFFFh Custom Command
    :rtype: CustomCMDReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).custom_cmd.get()
            return CustomCMDReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)

async def cmd_custom_cmd_request(port: Z800FreyaPort, cdb_instance: int, cmd_id: str, epl_length: int, lpl_length: int, rpl_length: int, rpl_check_code: int, data: str) -> None:
    """Send CMD 8000h-FFFFh Custom Command

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    
        * 0 = CBD Instance 1
        * 1 = CDB Instance 2
    
    :type cdb_instance: int
    :param cmd_id: ``CMD Header.CMDID``. Command ID.
    :type cmd_id: hex str

    :param epl_length: ``CMD Header.EPLLength``. Length of the EPL.
    :type epl_length: int

    :param lpl_length: ``CMD Header.LPLLength``. Length of the LPL.
    :type lpl_length: int

    :param rpl_length: ``CMD Header.RPLLength``. Length of the RPL (optional).
    :type rpl_length: int

    :param rpl_check_code: ``CMD Header.RPLChkCode``. Check code for the RPL. (optional)
    :type rpl_check_code: int
    
    :param data: ``CMD Data.Data``. The data to be sent in the command.
    :type data: hex str
    """
    cmd = {
        "cmd_header": {
            "cmd_id": cmd_id,
            "epl_length": epl_length,
            "lpl_length": lpl_length,
            "rpl_length": rpl_length,
            "rpl_check_code": rpl_check_code
        },
        "cmd_data": {
            "data": data
        }
    }
    await port.transceiver.cmis.cdb(cdb_instance).custom_cmd.set(cmd=cmd)

async def cdb_instances_supported_reply(port: Z800FreyaPort) -> int:
    resp = await port.transceiver.cmis.cdb_instances_supported.get()
    return resp.reply["cdb_instances_supported"]


async def firmware_download_procedure(port: Z800FreyaPort, cdb_instance: int, firmware_file: str, use_epl_write: bool, use_abort_for_failure: bool) -> bool:
    """Specified in **OIF-CMIS-05.3**

    Start transceiver firmware update on the specified port.

    The host begins by reading module capabilities using CMD 0041h: (Firmware Management Features).

    The host then reads (and possibly converts to binary format) the vendor specific and vendor provided firmware download file into a contiguous addressable byte array defined as the binary download image.

    To start the firmware download, the host sends the download image header consisting of the first StartCmdPayloadSize bytes from the download image using CMD 0101h: (Start Firmware Download). This header instructs the module in a vendor specific way about the full or partial download content to be expected. 

    Before the module updates an image bank in a download procedure the module ensures that the bank is marked as empty or corrupt until the download has eventually finished successfully.

    When CMD 0101h: was successful, the module is ready to accept data from the host using the advertised method, either CMD 0103h: (Write Firmware Block LPL) or CMD 0104h: (Write Firmware Block EPL). These command differ only in the allowed size of a download image block, which: is advertised for the EPL variant.

    The host zero-initializes a variable containing the address of the next data block to be sent or received in subsequent Write Firmware Block or Read Firmware Block commands, respectively.

    In a loop the host then reads subsequent bytes of the download image in blocks not exceeding the allowed block site and sends it using CMD 0103h: or 0104h.

    :param port: the port object to send the command to
    :type port: Z800FreyaPort
    :param cdb_instance: the CDB instance number.
    :type cdb_instance: int
    :param firmware_file: the module firmware filename
    :type firmware_file: str
    :param use_epl_write: should the procedure use EPL write mechanism for data block write.
    :type use_epl_write: bool
    :param use_abort_for_failure: should the procedure use CMD 0102h Abort Firmware Download to abort the firmware download on failure.
    :type use_abort_for_failure: bool
    """
    cdb_instances_supported = await cdb_instances_supported_reply(port)
    # Check if the specified CDB instance is supported
    if cdb_instance >= cdb_instances_supported:
        print(f"CDB instance {cdb_instance} is not supported. Only {cdb_instances_supported} CDB instances are supported.")
        return False
    
    # Log the start of the firmware update
    print(f"Starting firmware update on {port}")
    
    # Read capabilities (CMD 0041h)
    # Read size of START_LPL, erase byte
    reply_obj = await cmd_0041h_fw_mgmt_features_reply(port, cdb_instance)
    firmware_header_size = reply_obj.start_cmd_payload_size

    # Determine the write mechanism
    write_mechanism = reply_obj.write_mechanism.lower().lstrip("0x")
    if write_mechanism == WriteMechanism.NONE_SUPPORTED:
        print(f"Write Mechanism is not supported. Unable to proceed with firmware update.")
        return False
    elif write_mechanism == WriteMechanism.LPL_ONLY:
        print(f"Only CMD 0103h Write Firmware Block LPL is supported. Will use LPL write mechanism.")
        use_epl_write = False
    elif write_mechanism == WriteMechanism.EPL_ONLY:
        print(f"Only CMD 0104h Write Firmware Block EPL is supported. Will use EPL write mechanism.")
        use_epl_write = True
    else:
        print((f"Both CMD 0103h and CMD 0104h are supported. Will use the preferred write mechanism."))
    
    # Read the erased byte value
    erased_byte = reply_obj.erased_byte
    if reply_obj.abort_cmd == 0 and use_abort_for_failure == True:
        use_abort_for_failure = False
        print(f"CMD 0102h Abort Firmware Download is not supported by the module. Will use CMD 0107h Complete Firmware Download instead.")
    
    # Start the data block write loop
    return await __write_data_block_loop(port, cdb_instance, firmware_file, firmware_header_size, erased_byte, use_epl_write, use_abort_for_failure)


##################
# Helper functions
##################

async def __write_data_block_loop(port: Z800FreyaPort, cdb_instance: int, firmware_filename: str, firmware_header_size: int, erased_byte: str, use_epl_write: bool, use_abort_for_failure: bool) -> bool:
    """Write data block loop

    :param port: the port object
    :type port: Z800FreyaPort
    :param cdb_instance: CDB instance number.
    :type cdb_instance: int
    :param firmware_filename: module firmware filename
    :type firmware_filename: str
    :param firmware_header_size: firmware header size
    :type firmware_header_size: int
    :param erased_byte: value of the erased byte in hex string format
    :type erased_byte: str
    :param use_epl_write: should the procedure use EPL write mechanism for data block write.
    :type use_epl_write: bool
    :param use_abort_for_failure: should the procedure use CMD 0102h Abort Firmware Download to abort the firmware download on failure.
    :type use_abort_for_failure: bool
    """
    if use_epl_write == True:
        write_func_map = {
            "block_size": 2048,
            "write_func": cmd_0104h_write_firmware_block_epl_cmd,
            "description": "CMD 0104h: (Write Firmware Block EPL)"
        }
    else:
        write_func_map = {
            "block_size": 116,
            "write_func": cmd_0103h_write_firmware_block_lpl_cmd,
            "description": "CMD 0103h: (Write Firmware Block LPL)"
        }

    with open(firmware_filename, "rb") as f:        
        # Read the header data
        firmware_header_data = "0x" + f.read(firmware_header_size).hex()

        # Send the header data using CMD 0101h: (Start Firmware Download), and wait for SUCCESS response
        await cmd_0101h_start_firmware_download_cmd(port, cdb_instance, firmware_header_size, firmware_header_data)
        if await __is_cmd_successful("cmd_0101h_start_firmware_download_cmd", port, cdb_instance) == False:
            print(f"CMD 0101h: (Start Firmware Download) failed to become SUCCESS.")

        addr = 0
        while True:
            # Read the a block of firmware data
            data_block = f.read(write_func_map["block_size"])
            if not data_block:
                print(f"EOF. No more data to read.")
                break
            data_block_len = len(data_block)
            data_block_hex = "0x" + data_block.hex()
            if check_erased_byte(data_block_hex, erased_byte) == True:
                addr += data_block_len
                continue
            else:
                # Send the data block
                func = write_func_map["write_func"]
                await func(port, cdb_instance, addr, data_block_hex)
                if await __is_cmd_successful(str(write_func_map["write_func"]), port, cdb_instance) == False:
                    print(f"{write_func_map['description']} failed.")
                    await __abort_firmware_download(port, cdb_instance, use_abort_for_failure)
                    return False
                else:
                    addr += data_block_len
                    continue

        # Send CMD 0107h: (Complete Firmware Download) to complete the firmware download
        await cmd_0107h_complete_firmware_download_cmd(port, cdb_instance)
        if await __is_cmd_successful("cmd_0107h_complete_firmware_download_cmd", port, cdb_instance) == False:
            print(f"CMD 0107h: (Complete Firmware Download) failed.")
            print(f"Firmware Update Failed.")
            return False
        
        print(f"Firmware Update Successful.")
        return True


async def __abort_firmware_download(port: Z800FreyaPort, cdb_instance: int, use_abort_for_failure: bool) -> None:
    """Abort firmware download

    :param port: the port object
    :type port: Z800FreyaPort
    :param cdb_instance: the CDB instance number
    :type cdb_instance: int
    :param use_abort_for_failure: should the procedure use CMD 0102h Abort Firmware Download to abort the firmware download on failure.
    :type use_abort_for_failure: bool
    """
    if use_abort_for_failure == True:
        # Send CMD 0102h: (Abort Firmware Download) to abort the firmware download
        await cmd_0102h_abort_firmware_download_cmd(port, cdb_instance)
        if await __is_cmd_successful("cmd_0102h_abort_firmware_download_cmd", port, cdb_instance) == False:
            print(f"CMD 0102h: (Abort Firmware Download) failed.")
        else:
            print(f"CMD 0102h: (Abort Firmware Download) successful.")
    else:
        # Send CMD 0107h: (Complete Firmware Download) to complete the firmware download
        await cmd_0107h_complete_firmware_download_cmd(port, cdb_instance)
        if await __is_cmd_successful("cmd_0107h_complete_firmware_download_cmd", port, cdb_instance) == False:
            print(f"CMD 0107h: (Complete Firmware Download) failed.")
        else:
            print(f"CMD 0107h: (Complete Firmware Download) successful.")

    print(f"Firmware Update Failed.")


async def __is_cmd_successful(cmd_name: str, port: Z800FreyaPort, cdb_instance: int, timeout = 5.0) -> bool:
    """Check if the CDB command is successful.

    :param cmd_name: the function name of the command to check
    :type cmd_name: str
    :param port: the port object
    :type port: Z800FreyaPort
    :param cdb_instance: the CDB instance number
    :type cdb_instance: int
    :param timeout: the timeout, defaults to 5.0
    :type timeout: float, optional
    :return: if the command is successful or not
    :rtype: bool
    """
    func_map = {
        "cmd_0101h_start_firmware_download_reply": cmd_0101h_start_firmware_download_reply,
        "cmd_0103h_write_firmware_block_lpl_reply": cmd_0103h_write_firmware_block_lpl_reply,
        "cmd_0104h_write_firmware_block_epl_reply": cmd_0104h_write_firmware_block_epl_reply,
        "cmd_0107h_complete_firmware_download_reply": cmd_0107h_complete_firmware_download_reply,
    }
    if cmd_name not in func_map:
        print(f"Invalid command name: {cmd_name}. Valid commands are: {list(func_map.keys())}")
        return False
    start = time.time()
    while time.time() - start < timeout:
        reply_obj = await func_map[cmd_name](port, cdb_instance)
        if reply_obj.cdb_cmd_complete_flag == True:
            if check_cdb_status(reply_obj.cdb_status) == CdbCommandCoarseStatus.SUCCESS:
                return True
            elif check_cdb_status(reply_obj.cdb_status) == CdbCommandCoarseStatus.FAILED:
                return False
        else:
            time.sleep(timeout/100)
    return False
