"""The cmis cdb high-level function module."""

from __future__ import annotations
import asyncio
from dataclasses import dataclass
from typing import (TYPE_CHECKING, Callable, Awaitable, Dict)
from ._utils import *
from ._constants import *
from ._replies import *
import time
# from contextlib import suppress
from xoa_driver import exceptions

if TYPE_CHECKING:
    from xoa_driver.ports import GenericL23Port


# CMD 0000h: Query Status

async def cmd_0000h_query_status_cmd(port: GenericL23Port, cdb_instance: int, response_delay: int) -> None:
    """Send CMD 0000h Query Status

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0000h_query_status_reply(port: GenericL23Port, cdb_instance: int) -> CMD0000hQueryStatusReply:
    """Read the module response to CMD 0000h Query Status

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0001h_enter_password_cmd(port: GenericL23Port, cdb_instance: int, password: bytearray) -> None:
    """Send CMD 0001h Enter Password

    :param port: the port object to send the command to
    :type port: GenericL23Port

        :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    :param password: password to be entered
    :type password: int
    """

    cmd_data = {
        "password": password
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0001h_enter_password.set(cmd_data=cmd_data)

async def cmd_0001h_enter_password_reply(port: GenericL23Port, cdb_instance: int) -> CMD0001hEnterPasswordReply:
    """Read the module response to CMD 0001h Enter Password

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0002h_change_password_cmd(port: GenericL23Port, cdb_instance: int, new_password: bytearray) -> None:
    """Send CMD 0002h Change Password

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    :param new_password: new password to be entered
    :type new_password: int
    """
    cmd_data = {
        "new_password": new_password
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0002h_change_password.set(cmd_data=cmd_data)

async def cmd_0002h_change_password_reply(port: GenericL23Port, cdb_instance: int) -> CMD0002hChangePasswordReply:
    """Read the module response to CMD 0002h Change Password

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0004h_abort_processing_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0004h Abort Processing

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0004h_abort_processing.set()

async def cmd_0004h_abort_processing_reply(port: GenericL23Port, cdb_instance: int) -> CMD0004hAbortProcessingReply:
    """Read the module response to CMD 0004h Abort Processing

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0040h_module_features_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0040h Module Features

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0040h_module_features.set()

async def cmd_0040h_module_features_reply(port: GenericL23Port, cdb_instance: int) -> CMD0040hModuleFeaturesReply:
    """Read the module response to CMD 0040h Module Features

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0041h_fw_mgmt_features_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0041h Firmware Management Features

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0041h_fw_mgmt_features.set()

async def cmd_0041h_fw_mgmt_features_reply(port: GenericL23Port, cdb_instance: int) -> CMD0041hFirmwareManagementFeaturesReply:
    """Read the module response to CMD 0041h Firmware Management Features

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0044h_sec_feat_capabilities_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0044h Security Features and Capabilities

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0044h_sec_feat_capabilities.set()

async def cmd_0044h_sec_feat_and_capabilities_reply(port: GenericL23Port, cdb_instance: int) -> CMD0044hSecFeaturesAndCapabilitiesReply:
    """Read the module response to CMD 0044h Security Features and Capabilities

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0045h_externally_defined_features_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0045h Externally Defined Features

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0045h_external_features.set()

async def cmd_0045h_externally_defined_features_reply(port: GenericL23Port, cdb_instance: int) -> CMD0045hExternallyDefinedFeaturesReply:
    """Read the module response to CMD 0045h Externally Defined Features

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0050h_get_application_attributes_cmd(port: GenericL23Port, cdb_instance: int, application_number: int) -> None:
    """Send CMD 0050h Get Application Attributes

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0050h_get_application_attributes_reply(port: GenericL23Port, cdb_instance: int) -> CMD0050hGetApplicationAttributesReply:
    """Read the module response to CMD 0050h Get Application Attributes

    :param port: the port object to read the response from
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    :return: REPLY of CMD 0050h Get Application Attributes
    :rtype: CMD0050hGetApplicationAttributesReply
    """
    while True:
        try:
            resp = await port.transceiver.cmis.cdb(cdb_instance).cmd_0050h_get_app_attributes.get()
            return CMD0050hGetApplicationAttributesReply(resp.reply)
        except exceptions.XmpPendingError:
            time.sleep(0.1)


# CMD 0051h: Get Interface Code Description

async def cmd_0051h_get_interface_code_description_cmd(port: GenericL23Port, cdb_instance: int, interface_id: int, interface_location: int) -> None:
    """Send CMD 0051h Get Interface Code Description

    :param port: the port object to send the command to
    :type port: GenericL23Port
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
        "interface_location": interface_location
    }
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0051h_get_if_code_descr.set(cmd_data=cmd_data)

async def cmd_0051h_get_interface_code_description_reply(port: GenericL23Port, cdb_instance: int) -> CMD0051hGetInterfaceCodeDescriptionReply:
    """Read the module response to CMD 0051h Get Interface Code Description

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0100h_get_firmware_info_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0100h Get Firmware Info

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0100h_get_firmware_info.set()

async def cmd_0100h_get_firmware_info_reply(port: GenericL23Port, cdb_instance: int) -> CMD0100hGetFirmwareInfoReply:
    """Read the module response to CMD 0100h Get Firmware Info

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0101h_start_firmware_download_cmd(port: GenericL23Port, cdb_instance: int, image_size: int, vendor_data: str) -> None:
    """Send CMD 0101h Start Firmware Download

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0101h_start_firmware_download_reply(port: GenericL23Port, cdb_instance: int) -> CMD0101hStartFirmwareDownloadReply:
    """Read the module response to CMD 0101h Start Firmware Download

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0102h_abort_firmware_download_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0102h Abort Firmware Download

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0102h_abort_firmware_download.set()

async def cmd_0102h_abort_firmware_download_reply(port: GenericL23Port, cdb_instance: int) -> CMD0102hAbortFirmwareDownloadReply:
    """Read the module response to CMD 0102h Abort Firmware Download

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0103h_write_firmware_block_lpl_cmd(port: GenericL23Port, cdb_instance: int, block_address: int, firmware_block: bytes) -> None:
    """Send CMD 0103h Write Firmware Block LPL

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0103h_write_firmware_block_lpl_reply(port: GenericL23Port, cdb_instance: int) -> CMD0103hWriteFirmwareBlockLPLReply:
    """Read the module response to CMD 0103h Write Firmware Block LPL

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0104h_write_firmware_block_epl_cmd(port: GenericL23Port, cdb_instance: int, block_address: int, firmware_block: bytes) -> None:
    """Send CMD 0104h Write Firmware Block EPL

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0104h_write_firmware_block_epl_reply(port: GenericL23Port, cdb_instance: int) -> CMD0104hWriteFirmwareBlockEPLReply:
    """Read the module response to CMD 0104h Write Firmware Block EPL

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0105h_read_firmware_block_lpl_cmd(port: GenericL23Port, cdb_instance: int, block_address: int, length: int) -> None:
    """Send CMD 0105h Read Firmware Block LPL

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0105h_read_firmware_block_lpl_reply(port: GenericL23Port, cdb_instance: int) -> CMD0105hReadFirmwareBlockLPLReply:
    """Read the module response to CMD 0105h Read Firmware Block LPL

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0106h_read_firmware_block_epl_cmd(port: GenericL23Port, cdb_instance: int, block_address: int, length: int) -> None:
    """Send CMD 0106h Read Firmware Block EPL

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0106h_read_firmware_block_epl_reply(port: GenericL23Port, cdb_instance: int) -> CMD0106hReadFirmwareBlockEPLReply:
    """Read the module response to CMD 0106h Read Firmware Block EPL

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0107h_complete_firmware_download_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 0107h Complete Firmware Download

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_0107h_complete_firmware_download.set()

async def cmd_0107h_complete_firmware_download_reply(port: GenericL23Port, cdb_instance: int) -> CMD0107hCompleteFirmwareDownloadReply:
    """Read the module response to CMD 0107h Complete Firmware Download

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0108h_copy_firmware_image_cmd(port: GenericL23Port, cdb_instance: int, copy_direction: int) -> None:
    """Send CMD 0108h Copy Firmware Image

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0108h_copy_firmware_image_reply(port: GenericL23Port, cdb_instance: int) -> CMD0108hCopyFirmwareImageReply:
    """Read the module response to CMD 0108h Copy Firmware Image

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_0109h_run_firmware_image_cmd(port: GenericL23Port, cdb_instance: int, image_to_run: int, delay_to_reset: int) -> None:
    """Send CMD 0109h Run Firmware Image

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cmd_0109h_run_firmware_image_reply(port: GenericL23Port, cdb_instance: int) -> CMD0109hRunFirmwareImageReply:
    """Read the module response to CMD 0109h Run Firmware Image

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_010ah_commit_firmware_image_cmd(port: GenericL23Port, cdb_instance: int) -> None:
    """Send CMD 010Ah Commit Firmware Image

    :param port: the port object to send the command to
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.

        * 0 = CBD Instance 1
        * 1 = CDB Instance 2

    :type cdb_instance: int
    """
    await port.transceiver.cmis.cdb(cdb_instance).cmd_010ah_commit_firmware_image.set()

async def cmd_010ah_commit_firmware_image_reply(port: GenericL23Port, cdb_instance: int) -> CMD010AhCommitFirmwareImageReply:
    """Read the module response to CMD 010Ah Commit Firmware Image

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_custom_cmd_reply(port: GenericL23Port, cdb_instance: int) -> CustomCMDReply:
    """Read the module response to CMD 8000h-FFFFh Custom Command

    :param port: the port object to read the response from
    :type port: GenericL23Port
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

async def cmd_custom_cmd_request(port: GenericL23Port, cdb_instance: int, cmd_id: str, epl_length: int, lpl_length: int, rpl_length: int, rpl_check_code: int, data: str) -> None:
    """Send CMD 8000h-FFFFh Custom Command

    :param port: the port object to send the command to
    :type port: GenericL23Port
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

async def cdb_instances_supported_reply(port: GenericL23Port) -> int:
    resp = await port.transceiver.cmis.cdb_instances_supported.get()
    return resp.reply["cdb_instances_supported"]


async def firmware_download_procedure(port: GenericL23Port, cdb_instance: int, firmware_file: str, use_epl_write: bool, use_abort_for_failure: bool) -> bool:
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
    :type port: GenericL23Port
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
    write_mechanism = reply_obj.write_mechanism
    if write_mechanism == WriteMechanism.NONE_SUPPORTED:
        print("Write Mechanism is not supported. Unable to proceed with firmware update.")
        return False
    elif write_mechanism == WriteMechanism.LPL_ONLY:
        print("Only CMD 0103h Write Firmware Block LPL is supported. Will use LPL write mechanism.")
        use_epl_write = False
    elif write_mechanism == WriteMechanism.EPL_ONLY:
        print("Only CMD 0104h Write Firmware Block EPL is supported. Will use EPL write mechanism.")
        use_epl_write = True
    else:
        print(("Both CMD 0103h and CMD 0104h are supported. Will use the preferred write mechanism."))

    # Read the erased byte value
    erased_byte = reply_obj.erased_byte
    if reply_obj.abort_cmd == 0 and use_abort_for_failure:
        use_abort_for_failure = False
        print("CMD 0102h Abort Firmware Download is not supported by the module. Will use CMD 0107h Complete Firmware Download instead.")

    # Start the data block write loop
    return await _write_data_block_loop(port, cdb_instance, firmware_file, firmware_header_size, erased_byte, use_epl_write, use_abort_for_failure)


##################
# Helper functions
##################

async def _write_data_block_loop(port: GenericL23Port, cdb_instance: int, firmware_filename: str, firmware_header_size: int, erased_byte: int, use_epl_write: bool, use_abort_for_failure: bool) -> bool:
    """Write data block loop

    :param port: the port object
    :type port: GenericL23Port
    :param cdb_instance: CDB instance number.
    :type cdb_instance: int
    :param firmware_filename: module firmware filename
    :type firmware_filename: str
    :param firmware_header_size: firmware header size
    :type firmware_header_size: int
    :param erased_byte: value of the erased byte to check against
    :type erased_byte: int
    :param use_epl_write: should the procedure use EPL write mechanism for data block write.
    :type use_epl_write: bool
    :param use_abort_for_failure: should the procedure use CMD 0102h Abort Firmware Download to abort the firmware download on failure.
    :type use_abort_for_failure: bool
    """
    if use_epl_write:
        write_func_map = {
            "block_size": 2048,
            "write_cmd_func": cmd_0104h_write_firmware_block_epl_cmd,
            "write_reply_func": cmd_0104h_write_firmware_block_epl_reply,
            "description": "CMD 0104h: (Write Firmware Block EPL)"
        }
    else:
        write_func_map = {
            "block_size": 116,
            "write_cmd_func": cmd_0103h_write_firmware_block_lpl_cmd,
            "write_reply_func": cmd_0103h_write_firmware_block_lpl_reply,
            "description": "CMD 0103h: (Write Firmware Block LPL)"
        }

    with open(firmware_filename, "rb") as f:
        # Read the header data
        firmware_header_data = "0x" + f.read(firmware_header_size).hex()

        # Send the header data using CMD 0101h: (Start Firmware Download), and wait for completion
        await cmd_0101h_start_firmware_download_cmd(port, cdb_instance, firmware_header_size, firmware_header_data)
        while True:
            reply = await cmd_0101h_start_firmware_download_reply(port, cdb_instance)
            if reply.cdb_io_status == 1 or reply.cdb_io_status == 2:
                break
            await asyncio.sleep(0.1)

        if reply.cdb_io_status != 1 or reply.cdb_status != 1:
            print(f"CMD 0101h: (Start Firmware Download) failed. cdb_io_status={reply.cdb_io_status}, cdb_status={reply.cdb_status}")
            await _abort_firmware_download(port, cdb_instance, use_abort_for_failure)
            return False

        addr = 0
        while True:
            # Read a block of firmware data
            data_block = f.read(write_func_map["block_size"])
            if not data_block:
                print("EOF. No more data to read.")
                break
            data_block_len = len(data_block)
            data_block_hex = "0x" + data_block.hex()
            erased_byte_hex = f"0x{erased_byte:02X}"
            if check_erased_byte(data_block_hex, erased_byte_hex):
                addr += data_block_len
                continue
            else:
                # Send the data block
                await write_func_map["write_cmd_func"](port, cdb_instance, addr, data_block)

                # Wait for completion by polling cdb_io_status
                while True:
                    reply = await write_func_map["write_reply_func"](port, cdb_instance)
                    if reply.cdb_io_status == 1 or reply.cdb_io_status == 2:
                        break
                    await asyncio.sleep(0.1)

                if reply.cdb_io_status != 1 or reply.cdb_status != 1:
                    print(f"{write_func_map['description']} failed. cdb_io_status={reply.cdb_io_status}, cdb_status={reply.cdb_status}")
                    await _abort_firmware_download(port, cdb_instance, use_abort_for_failure)
                    return False
                else:
                    addr += data_block_len
                    continue

        # Send CMD 0107h: (Complete Firmware Download) to complete the firmware download
        await cmd_0107h_complete_firmware_download_cmd(port, cdb_instance)
        while True:
            reply = await cmd_0107h_complete_firmware_download_reply(port, cdb_instance)
            if reply.cdb_io_status == 1 or reply.cdb_io_status == 2:
                break
            await asyncio.sleep(0.1)

        if reply.cdb_io_status != 1 or reply.cdb_status != 1:
            print(f"CMD 0107h: (Complete Firmware Download) failed. cdb_io_status={reply.cdb_io_status}, cdb_status={reply.cdb_status}")
            print("Firmware Update Failed.")
            return False

        print("Firmware Update Successful.")
        return True


async def _abort_firmware_download(port: GenericL23Port, cdb_instance: int, use_abort_for_failure: bool) -> None:
    """Abort firmware download

    :param port: the port object
    :type port: GenericL23Port
    :param cdb_instance: the CDB instance number
    :type cdb_instance: int
    :param use_abort_for_failure: should the procedure use CMD 0102h Abort Firmware Download to abort the firmware download on failure.
    :type use_abort_for_failure: bool
    """
    if use_abort_for_failure:
        # Send CMD 0102h: (Abort Firmware Download) to abort the firmware download
        await cmd_0102h_abort_firmware_download_cmd(port, cdb_instance)
        while True:
            reply = await cmd_0102h_abort_firmware_download_reply(port, cdb_instance)
            if reply.cdb_io_status == 1 or reply.cdb_io_status == 2:
                break
            await asyncio.sleep(0.1)

        if reply.cdb_io_status != 1 or reply.cdb_status != 1:
            print("CMD 0102h: (Abort Firmware Download) failed.")
        else:
            print("CMD 0102h: (Abort Firmware Download) successful.")
    else:
        # Send CMD 0107h: (Complete Firmware Download) to complete the firmware download
        await cmd_0107h_complete_firmware_download_cmd(port, cdb_instance)
        while True:
            reply = await cmd_0107h_complete_firmware_download_reply(port, cdb_instance)
            if reply.cdb_io_status == 1 or reply.cdb_io_status == 2:
                break
            await asyncio.sleep(0.1)

        if reply.cdb_io_status != 1 or reply.cdb_status != 1:
            print("CMD 0107h: (Complete Firmware Download) failed.")
        else:
            print("CMD 0107h: (Complete Firmware Download) successful.")

    print("Firmware Update Failed.")


__all__ = (
    "cmd_0000h_query_status_cmd",
    "cmd_0000h_query_status_reply",
    "cmd_0001h_enter_password_cmd",
    "cmd_0001h_enter_password_reply",
    "cmd_0002h_change_password_cmd",
    "cmd_0002h_change_password_reply",
    "cmd_0004h_abort_processing_cmd",
    "cmd_0004h_abort_processing_reply",
    "cmd_0040h_module_features_cmd",
    "cmd_0040h_module_features_reply",
    "cmd_0041h_fw_mgmt_features_cmd",
    "cmd_0041h_fw_mgmt_features_reply",
    "cmd_0044h_sec_feat_and_capabilities_reply",
    "cmd_0044h_sec_feat_capabilities_cmd",
    "cmd_0045h_externally_defined_features_cmd",
    "cmd_0045h_externally_defined_features_reply",
    "cmd_0050h_get_application_attributes_cmd",
    "cmd_0050h_get_application_attributes_reply",
    "cmd_0051h_get_interface_code_description_cmd",
    "cmd_0051h_get_interface_code_description_reply",
    "cmd_0100h_get_firmware_info_cmd",
    "cmd_0100h_get_firmware_info_reply",
    "cmd_0101h_start_firmware_download_cmd",
    "cmd_0101h_start_firmware_download_reply",
    "cmd_0102h_abort_firmware_download_cmd",
    "cmd_0102h_abort_firmware_download_reply",
    "cmd_0103h_write_firmware_block_lpl_cmd",
    "cmd_0103h_write_firmware_block_lpl_reply",
    "cmd_0104h_write_firmware_block_epl_cmd",
    "cmd_0104h_write_firmware_block_epl_reply",
    "cmd_0105h_read_firmware_block_lpl_cmd",
    "cmd_0105h_read_firmware_block_lpl_reply",
    "cmd_0106h_read_firmware_block_epl_cmd",
    "cmd_0106h_read_firmware_block_epl_reply",
    "cmd_0107h_complete_firmware_download_cmd",
    "cmd_0107h_complete_firmware_download_reply",
    "cmd_0108h_copy_firmware_image_cmd",
    "cmd_0108h_copy_firmware_image_reply",
    "cmd_0109h_run_firmware_image_cmd",
    "cmd_0109h_run_firmware_image_reply",
    "cmd_010ah_commit_firmware_image_cmd",
    "cmd_010ah_commit_firmware_image_reply",
    "cmd_custom_cmd_reply",
    "cmd_custom_cmd_request",
    "CMD0000hQueryStatusReply",
    "CMD0001hEnterPasswordReply",
    "CMD0002hChangePasswordReply",
    "CMD0004hAbortProcessingReply",
    "CMD0040hModuleFeaturesReply",
    "CMD0041hFirmwareManagementFeaturesReply",
    "CMD0044hSecFeaturesAndCapabilitiesReply",
    "CMD0045hExternallyDefinedFeaturesReply",
    "CMD0050hGetApplicationAttributesReply",
    "CMD0051hGetInterfaceCodeDescriptionReply",
    "CMD0100hGetFirmwareInfoReply",
    "CMD0101hStartFirmwareDownloadReply",
    "CMD0102hAbortFirmwareDownloadReply",
    "CMD0103hWriteFirmwareBlockLPLReply",
    "CMD0104hWriteFirmwareBlockEPLReply",
    "CMD0105hReadFirmwareBlockLPLReply",
    "CMD0106hReadFirmwareBlockEPLReply",
    "CMD0107hCompleteFirmwareDownloadReply",
    "CMD0108hCopyFirmwareImageReply",
    "CMD0109hRunFirmwareImageReply",
    "CMD010AhCommitFirmwareImageReply",
    "CustomCMDReply",
    "firmware_download_procedure",
)