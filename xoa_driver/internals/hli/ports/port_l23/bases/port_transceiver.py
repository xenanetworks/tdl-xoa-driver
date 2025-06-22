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
    PX_CDB_ABORT_FW_DOWNLOAD,
    PX_CDB_COMMIT_FW_IMAGE,
    PX_CDB_COMPLETE_FW_DOWNLOAD,
    PX_CDB_COPY_FW_IMAGE,
    PX_CDB_GET_FW_INFO,
    PX_CDB_READ_FW_BLOCK_EPL,
    PX_CDB_READ_FW_BLOCK_LPL,
    PX_CDB_RUN_FW_IMAGE,
    PX_CDB_START_FW_DOWNLOAD,
    PX_CDB_WRITE_FW_BLOCK_EPL,
    PX_CDB_WRITE_FW_BLOCK_LPL,
    PX_CUST_CMD,
)


class PortTransceiver:
    """Transceiver access class."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.i2c_config = PX_I2C_CONFIG(conn, module_id, port_id)
        """
        Access speed on a transceiver I2C access in the unit of KHz. Default to 100. 
        
        When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from port.capabilities(). 
        
        The I2C speed configuration will not be included in the port configuration file (.xpc). When you load a port configuration to a port, the transceiver I2C access speed will be reset to default.
        """

        self.temperature = PX_TEMPERATURE(conn, module_id, port_id)
        """Transceiver temperature in Celsius.

        Temperature value before the decimal digit, and 1/256th of a degree Celsius after the decimal digit.
        """

        self.cmis = CMIS(conn, module_id, port_id)
        """
        Access CMIS interface.
        """

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

class CMIS():
    """CMIS access class.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.cdb_instances_supported = PX_CDB_SUPPORT(conn, module_id, port_id)
        """Return the number of supported CDB instances.
        """

    def cdb(self, cdb_instance_id: int) -> "CDB":
        """Access CMIS CDB command interface.

        :param cdb_instance_id: 0 for CDB Instance 1, 1 for CDB Instance 2
        :type cdb_instance_id: int
        """
        return CDB(self.__conn, self.__module_id, self.__port_id, cdb_instance_id)
        

class CDB():
    """CMIS CDB command access class.
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, cdb_instance_id: int) -> None:

        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__cdb_instance_id = cdb_instance_id

        # CDB Module Commands
        self.cmd_0000h_query_status = PX_CDB_QUERY_STATUS(conn, module_id, port_id, cdb_instance_id)
        """CMD 0000h: Query Status
        """
        self.cmd_0001h_enter_password = PX_CDB_ENTER_PASSWORD(conn, module_id, port_id, cdb_instance_id)
        """CMD 0001h: Enter Password
        """
        self.cmd_0002h_change_password = PX_CDB_CHANGE_PASSWORD(conn, module_id, port_id, cdb_instance_id)
        """CMD 0002h: Change Password
        """
        self.cmd_0004h_abort_processing = PX_CDB_ABORT_PROCESSING(conn, module_id, port_id, cdb_instance_id)
        """CMD 0004h: Abort Processing
        """ 

        # CDB Features and Capabilities Inquiry Commands
        self.cmd_0040h_module_features = PX_CDB_MODULE_FEATURES(conn, module_id, port_id, cdb_instance_id)
        """CMD 0040h: Module Features
        """
        self.cmd_0041h_fw_mgmt_features = PX_CDB_FW_MGMT_FEATURES(conn, module_id, port_id, cdb_instance_id)
        """CMD 0041h: Firmware Management Features
        """
        self.cmd_0044h_sec_feat_capabilities = PX_CDB_SEC_FEAT_CAPABILITIES(conn, module_id, port_id, cdb_instance_id)
        """CMD 0044h: Security Features and Capabilities
        """
        self.cmd_0045h_external_features = PX_CDB_EXTERNAL_FEATURES(conn, module_id, port_id, cdb_instance_id)
        """CMD 0045h: Externally Defined Features
        """
        self.cmd_0050h_get_app_attributes = PX_CDB_GET_APP_ATTRIBUTES(conn, module_id, port_id, cdb_instance_id)
        """CMD 0050h: Get Application Attributes
        """
        self.cmd_0051h_get_if_code_descr = PX_CDB_GET_IF_CODE_DESCR(conn, module_id, port_id, cdb_instance_id)
        """CMD 0051h: Get Interface Code Description
        """

        # CDB Firmware Management Commands
        self.cmd_0100h_get_firmware_info = PX_CDB_GET_FW_INFO(conn, module_id, port_id, cdb_instance_id)
        """CMD 0100h: Get Firmware Info
        """
        self.cmd_0101h_start_firmware_download = PX_CDB_START_FW_DOWNLOAD(conn, module_id, port_id, cdb_instance_id)
        """CMD 0101h: Start Firmware Download
        """
        self.cmd_0102h_abort_firmware_download = PX_CDB_ABORT_FW_DOWNLOAD(conn, module_id, port_id, cdb_instance_id)
        """CMD 0102h: Abort Firmware Download
        """
        self.cmd_0103h_write_firmware_block_lpl = PX_CDB_WRITE_FW_BLOCK_LPL(conn, module_id, port_id, cdb_instance_id)
        """CMD 0103h: Write Firmware Block LPL
        """
        self.cmd_0104h_write_firmware_block_epl = PX_CDB_WRITE_FW_BLOCK_EPL(conn, module_id, port_id, cdb_instance_id)
        """CMD 0104h: Write Firmware Block EPL
        """
        self.cmd_0105h_read_firmware_block_lpl = PX_CDB_READ_FW_BLOCK_LPL(conn, module_id, port_id, cdb_instance_id)
        """CMD 0105h: Read Firmware Block LPL
        """
        self.cmd_0106h_read_firmware_block_epl = PX_CDB_READ_FW_BLOCK_EPL(conn, module_id, port_id, cdb_instance_id)
        """CMD 0106h: Read Firmware Block EPL
        """
        self.cmd_0107h_complete_firmware_download = PX_CDB_COMPLETE_FW_DOWNLOAD(conn, module_id, port_id, cdb_instance_id)
        """CMD 0107h: Complete Firmware Download
        """
        self.cmd_0108h_copy_firmware_image = PX_CDB_COPY_FW_IMAGE(conn, module_id, port_id, cdb_instance_id)
        """CMD 0108h: Copy Firmware Image
        """
        self.cmd_0109h_run_firmware_image = PX_CDB_RUN_FW_IMAGE(conn, module_id, port_id, cdb_instance_id)
        """CMD 0109h: Run Firmware Image
        """
        self.cmd_010ah_commit_firmware_image = PX_CDB_COMMIT_FW_IMAGE(conn, module_id, port_id, cdb_instance_id)
        """CMD 010Ah: Commit Firmware Image
        """
        
        # Custom Commands
        self.custom_cmd = PX_CUST_CMD(conn, module_id, port_id, cdb_instance_id)
        """Defnes the custom CDB commdand (CMD and Reply) to be sent to the CDB instance.
        """