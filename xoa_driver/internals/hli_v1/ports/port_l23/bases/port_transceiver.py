from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PX_RW,
    PX_MII,
    PX_TEMPERATURE,
    PX_RW_SEQ,
    PX_I2C_CONFIG,
    PX_RW_SEQ_BANK,
    PX_CDB_SUPPORT,
    PX_CDB_ABORT_PROCESSING,
    PX_CDB_CHANGE_PASSWORD,
    PX_CDB_ENTER_PASSWORD,
    PX_CDB_QUERY_STATUS,
    PX_CDB_EXTERNAL_FEATURES,
    PX_CDB_FW_MGMT_FEATURES,
    PX_CDB_GET_APP_ATTRIBUTES,
    PX_CDB_GET_IF_CODE_DESCR,
    PX_CDB_MODULE_FEATURES,
    PX_CDB_SEC_FEAT_CAPABILITIES,
    PX_CDB_ABORT_FIRMWARE_DOWNLOAD,
    PX_CDB_COMMIT_FIRMWARE_IMAGE,
    PX_CDB_COMPLETE_FIRMWARE_DOWNLOAD,
    PX_CDB_COPY_FIRMWARE_IMAGE,
    PX_CDB_GET_FIRMWARE_INFO,
    PX_CDB_READ_FIRMWARE_BLOCK_EPL,
    PX_CDB_READ_FIRMWARE_BLOCK_LPL,
    PX_CDB_RUN_FIRMWARE_IMAGE,
    PX_CDB_START_FIRMWARE_DOWNLOAD,
    PX_CDB_WRITE_FIRMWARE_BLOCK_EPL,
    PX_CDB_WRITE_FIRMWARE_BLOCK_LPL,
    PX_CUST_REPLY,
    PX_CUST_REQUEST,
)


class PortTransceiver:
    """L23 port transceiver."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.i2c_config = PX_I2C_CONFIG(conn, module_id, port_id)
        """Access speed on a transceiver.
        :type: PX_I2C_CONFIG
        """

    def access_temperature(self):
        """Transceiver temperature in Celsius.

        :return: Transceiver temperature integral and decimal parts
        :rtype: PX_TEMPERATURE
        """

        return PX_TEMPERATURE(
            self.__conn,
            self.__module_id,
            self.__port_id,
        )

    def access_rw(self, page_address: int, register_address: int) -> "PX_RW":
        """Access to register interface by the transceiver.

        :param page_address: page address
        :type page_address: int
        :param register_address: register address
        :type register_address: int
        :return: transceiver register values
        :rtype: PX_RW
        """

        return PX_RW(
            self.__conn,
            self.__module_id,
            self.__port_id,
            page_address,
            register_address
        )

    def access_mii(self, register_address: int) -> "PX_MII":
        """Access to the register interface supported by the media-independent interface (MII) transceiver.

        :param register_address: register address
        :type register_address: int
        :return: register values
        :rtype: PX_MII
        """
        return PX_MII(
            self.__conn,
            self.__module_id,
            self.__port_id,
            register_address
        )

    def access_rw_seq(self, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ":
        """Sequential read/write a number of bytes to the register interface supported by the media-independent interface (MII) transceiver.

        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ
        """
        return PX_RW_SEQ(
            self.__conn,
            self.__module_id,
            self.__port_id,
            page_address,
            register_address,
            byte_count
        )
    
    def access_rw_seq_bank(self, bank_address: int, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ_BANK":
        """Sequential read/write a number of bytes to the register interface supported by the media-independent interface (MII) transceiver.

        :param bank_address: bank address (0-255)
        :type bank_address: int
        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ_BANK
        """
        return PX_RW_SEQ_BANK(
            self.__conn,
            self.__module_id,
            self.__port_id,
            bank_address,
            page_address,
            register_address,
            byte_count
        )
    
    def cdb_support(self) -> "PX_CDB_SUPPORT":
        """Return the supported CDB instances.

        :return: the supported CDB instances
        :rtype: PX_CDB_SUPPORT
        """
        
        return PX_CDB_SUPPORT(
            self.__conn,
            self.__module_id,
            self.__port_id
        )
    
    def cdb_abort_processing(self, cdb_instance_xindex: int) -> "PX_CDB_ABORT_PROCESSING":
        """This is CMD 0004h: Abort Processing

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_ABORT_PROCESSING(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_change_password(self, cdb_instance_xindex: int) -> "PX_CDB_CHANGE_PASSWORD":
        """This is CMD 0002h: Change Password

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_CHANGE_PASSWORD(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_enter_password(self, cdb_instance_xindex: int) -> "PX_CDB_ENTER_PASSWORD":
        """This is CMD 0001h: Enter Password

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_ENTER_PASSWORD(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_query_status(self, cdb_instance_xindex: int) -> "PX_CDB_QUERY_STATUS":
        """This is CMD 0000h: Query Status

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_QUERY_STATUS(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_external_features(self, cdb_instance_xindex: int) -> "PX_CDB_EXTERNAL_FEATURES":
        """This is CMD 0045h: Externally Defined Features

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_EXTERNAL_FEATURES(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_fw_mgmt_features(self, cdb_instance_xindex: int) -> "PX_CDB_FW_MGMT_FEATURES":
        """This is CMD 0041h: Firmware Management Features

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_FW_MGMT_FEATURES(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_get_app_attributes(self, cdb_instance_xindex: int) -> "PX_CDB_GET_APP_ATTRIBUTES":
        """This is CMD 0050h: Get Application Attributes

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_GET_APP_ATTRIBUTES(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_get_if_code_descr(self, cdb_instance_xindex: int) -> "PX_CDB_GET_IF_CODE_DESCR":
        """This is CMD 0051h: Get Interface Code Description

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_GET_IF_CODE_DESCR(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_module_features(self, cdb_instance_xindex: int) -> "PX_CDB_MODULE_FEATURES":
        """This is CMD 0040h: Module Features

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_MODULE_FEATURES(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_sec_feat_capabilities(self, cdb_instance_xindex: int) -> "PX_CDB_SEC_FEAT_CAPABILITIES":
        """This is CMD 0044h: Security Features and Capabilities

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_SEC_FEAT_CAPABILITIES(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_abort_firmware_download(self, cdb_instance_xindex: int) -> "PX_CDB_ABORT_FIRMWARE_DOWNLOAD":
        """This is CMD 0102h: Abort Firmware Download

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_ABORT_FIRMWARE_DOWNLOAD(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_commit_firmware_image(self, cdb_instance_xindex: int) -> "PX_CDB_COMMIT_FIRMWARE_IMAGE":
        """This is CMD 010Ah: Commit Firmware Image

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_COMMIT_FIRMWARE_IMAGE(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_complete_firmware_download(self, cdb_instance_xindex: int) -> "PX_CDB_COMPLETE_FIRMWARE_DOWNLOAD":
        """TThis is CMD 0107h: Complete Firmware Download

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_COMPLETE_FIRMWARE_DOWNLOAD(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_copy_firmware_image(self, cdb_instance_xindex: int) -> "PX_CDB_COPY_FIRMWARE_IMAGE":
        """This is CMD 0107h: Complete Firmware Download

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_COPY_FIRMWARE_IMAGE(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_get_firmware_info(self, cdb_instance_xindex: int) -> "PX_CDB_GET_FIRMWARE_INFO":
        """This is CMD 0100h: Get Firmware Info

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """        
        return PX_CDB_GET_FIRMWARE_INFO(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex
        )
    
    def cdb_read_firmware_block_epl(self, cdb_instance_xindex: int, block_address: int, length: int) -> "PX_CDB_READ_FIRMWARE_BLOCK_EPL":
        """This is CMD 0106h: Read Firmware Block EPL

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the "Start Command Payload Size"
        :type block_address: int
        :param length: Number of bytes to read back to the EPL in this command, starting at the indicated address.
        :type length: int
        """
        return PX_CDB_READ_FIRMWARE_BLOCK_EPL(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
            block_address,
            length
        )
    
    def cdb_read_firmware_block_lpl(self, cdb_instance_xindex: int, block_address: int, length: int) -> "PX_CDB_READ_FIRMWARE_BLOCK_LPL":
        """This is CMD 0106h: Read Firmware Block LPL

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the "Start Command Payload Size"
        :type block_address: int
        :param length: Number of bytes to read back to the LPL in this command, starting at the indicated address.
        :type length: int
        :rtype: PX_CDB_READ_FIRMWARE_BLOCK_LPL
        """
        return PX_CDB_READ_FIRMWARE_BLOCK_LPL(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
            block_address,
            length
        )
    
    def cdb_run_firmware_image(self, cdb_instance_xindex: int) -> "PX_CDB_RUN_FIRMWARE_IMAGE":
        """This is CMD 0109h: Run Firmware Image

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """
        return PX_CDB_RUN_FIRMWARE_IMAGE(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
        )
    
    def cdb_start_firmware_download(self, cdb_instance_xindex: int) -> "PX_CDB_START_FIRMWARE_DOWNLOAD":
        """This is CMD 0101h: Start Firmware Download

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """
        return PX_CDB_START_FIRMWARE_DOWNLOAD(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
        )
    
    def cdb_write_firmware_block_epl(self, cdb_instance_xindex: int, block_address: int) -> "PX_CDB_WRITE_FIRMWARE_BLOCK_EPL":
        """This is CMD 0104h: Write Firmware Block EPL

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the "Start Command Payload Size"
        :type block_address: int
        """
        return PX_CDB_WRITE_FIRMWARE_BLOCK_EPL(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
            block_address,
        )
    
    def cdb_write_firmware_block_lpl(self, cdb_instance_xindex: int, block_address: int) -> "PX_CDB_WRITE_FIRMWARE_BLOCK_LPL":
        """This is CMD 0103h: Write Firmware Block LPL

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        :param block_address: U32 Starting byte address of this block of data within the supplied image file minus the size of the size of the "Start Command Payload Size"
        :type block_address: int
        """
        return PX_CDB_WRITE_FIRMWARE_BLOCK_LPL(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
            block_address,
        )
    
    def cdb_custom_reply(self, cdb_instance_xindex: int) -> "PX_CUST_REPLY":
        """Defines the custom reply to receiver for the CDB instance.

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """
        return PX_CUST_REPLY(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
        )
    
    
    def cdb_custom_request(self, cdb_instance_xindex: int) -> "PX_CUST_REQUEST":
        """Defines the custom request to be sent to the CDB instance.

        :param cdb_instance_xindex: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_xindex: int
        """
        return PX_CUST_REQUEST(
            self.__conn,
            self.__module_id,
            self.__port_id,
            cdb_instance_xindex,
        )