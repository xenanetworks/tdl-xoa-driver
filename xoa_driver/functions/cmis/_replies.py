
import typing as t

class CMDBaseReply:
    def __init__(self, reply: t.Dict[str, t.Any]):
        self.cdb_io_status: int = reply.get("cdb_io_status", 0)
        """integer, indicates the CDB IO status.

        * 0: Idle, transceiver is not processing a CDB command.
        * 1: Finished, transceiver has finished processing a CDB command. It is ready to accept a new CDB command.
        * 2: Timeout, transceiver has timed out while processing a CDB command. It is ready to accept a new CDB command.
        * 3: In progress: transceiver is currently processing a CDB command. It is not ready to accept a new CDB command.
        """
        self.cdb_status: int = reply['cdb_status']
        """
        integer, provides the status of the most recently triggered CDB command.

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

class CMD0000hQueryStatusReply(CMDBaseReply):
    """REPLY message of CMD 0000h Query Status
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)
        self.status: int = reply['status']
        """integer

            * ``0000 0000b``: Module Boot Up.
            * ``0000 0001b``: Host Password Accepted.
            * ``1xxx xxxxb``: Module Password accepted.
            * Bits ‘x’ may contain custom information.
        """

class CMD0001hEnterPasswordReply(CMDBaseReply):
    """REPLY message of CMD 0001h Enter Password
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)
        
class CMD0002hChangePasswordReply(CMDBaseReply):
    """REPLY message of CMD 0002h Change Password
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0004hAbortProcessingReply(CMDBaseReply):
    """REPLY message of CMD 0004h Abort Processing
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0040hModuleFeaturesReply(CMDBaseReply):
    """REPLY message of CMD 0040h Module Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

        # Parse cmd_support_mask as a list of integers
        self.cmd_support = reply["cmd_support_mask"]

        self.max_completion_time: int = reply["max_completion_time"]
        """integer, U16 Maximum CDB command execution time in ms, of all supported CDB commands
        """

class CMD0041hFirmwareManagementFeaturesReply(CMDBaseReply):
    """REPLY message of CMD 0041h Firmware Management Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

        feature_support_mask: int = reply["feature_support_mask"]

        self.abort_cmd: int = (feature_support_mask >> 0) & 0x01
        """
        * 0b = CMD 0102h (Abort) Not Supported
        * 1b = CMD 0102h (Abort) Supported

        """
        self.copy_cmd: int = (feature_support_mask >> 1) & 0x01
        """
        * 0b = CMD 0108h (Copy image) Not Supported
        * 1b = CMD 0108h (Copy image) Supported

        """
        self.skipping_erased_blocks: int = (feature_support_mask >> 2) & 0x01
        """
        * 0b = Skipping erased blocks Not Supported
        * 1b = Skipping erased blocks Supported

        """
        self.max_duration_coding: int = (feature_support_mask >> 3) & 0x01
        """
        * 0b = max duration multiplier M is 1
        * 1b = max duration multiplier M is 10

        This bit encodes a multiplier value M which governs the interpretation of values found in the U16 array of advertised max durations in Bytes 144-153 of this message: These advertised values are multiplied by M.

        """
        self.image_readback: int = (feature_support_mask >> 7) & 0x01
        """
        * 0b = Full Image Readback Not Supported
        * 1b = Full Image Readback Supported

        """
        self.start_cmd_payload_size: int = reply["start_cmd_payload_size"]
        """integer, This defines the number of bytes that the host must extract from the beginning of the vendor-delivered binary firmware image file and send to the module in CMD 0101h (Start)
        """
        self.erased_byte: int = reply["erased_byte"]
        """integer, This is the value representing an erased byte. The purpose of advertising this byte is to optionally reduce download time by allowing the host to skip sending blocks of the image containing ErasedByte values only.
        """
        self.read_write_length_ext: int = reply["read_write_length_ext"]
        """integer, specifies the allowable additional number of byte octets in a READ or a WRITE, specifically for Firmware Management Commands (IDs 0100h-01FFh) as follows:

        EPL: For accessing the multi-page EPL field, the allowable length extension is i byte octets (8 bytes).
        
        LPL: For accessing the LPL field on page 9Fh, the allowable length extension is min(i, 15) byte octets.

        This leads to the maximum length of a READ or a WRITE

        Value Maximum Number of Bytes (EPL)

        * 0:    8 bytes (no extension of general length limit)
        * i:    8 x (1+i) bytes (0 <= i <= 255)
        * 255:  8 x 256 = 2048 bytes

        Value  Maximum Number of Bytes (LPL)
        
        * 0:     8 bytes (no extension of general length limit)
        * i:     8 x (1+i) bytes (0 <= i <= 15)
        * i:     8 x 16 = 128 bytes (16 <= i <= 256)

        """
        self.write_mechanism: int = reply['write_mechanism']
        """integer, Firmware update supported mechanism

        * 00h: None Supported.
        * 01h: Write to LPL supported.
        * 10h: Write to EPL supported.
        * 11h: Both Write to LPL and EPL supported.

        """
        self.read_mechanism: int = reply['read_mechanism']
        """integer, Firmware read / readback support mechanism.

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

class CMD0044hSecFeaturesAndCapabilitiesReply(CMDBaseReply):
    """REPLY message of CMD 0044h Security Features and Capabilities
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

        # Parse cmd_support_mask as a list of integers
        self.cmd_support = reply["cmd_support_mask"]

        """
        CMD 0400h-04FFh support.

        Each integer represents a mask. If an integer is set, the corresponding command is supported
        
        * D0: CMD 0400h is supported.
        * ..
        * D255: CMD 04FFh is supported

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

class CMD0045hExternallyDefinedFeaturesReply(CMDBaseReply):
    """REPLY message of CMD 0045h Externally Defined Features
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

        self.supplement_support: int = reply['supplement_support']
        """Bit 0 = 0/1: CMIS-VCS not supported/supported
        """

class CMD0050hGetApplicationAttributesReply(CMDBaseReply):
    """REPLY message of CMD 0050h Get Application Attributes
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

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

class CMD0051hGetInterfaceCodeDescriptionReply(CMDBaseReply):
    """REPLY message of CMD 0051h Get Interface Code Description
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

        self.interface_id: int = reply['interface_id']
        """integer, U16: HostInterfaceID or MediaInterfaceID. 15-8: reserved (0). 7-0: InterfaceID
        """
        self.interface_location: int = reply['interface_location']
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
        self.interfacre_lane_count: int = reply["interfacre_lane_count"]
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

class CMD0100hGetFirmwareInfoReply(CMDBaseReply):
    """REPLY message of CMD 0100h Get Firmware Info
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

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

class CMD0101hStartFirmwareDownloadReply(CMDBaseReply):
    """REPLY message of CMD 0101h Start Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0102hAbortFirmwareDownloadReply(CMDBaseReply):
    """REPLY message of CMD 0102h Abort Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0103hWriteFirmwareBlockLPLReply(CMDBaseReply):
    """REPLY message of CMD 0103h Write Firmware Block LPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0104hWriteFirmwareBlockEPLReply(CMDBaseReply):
    """REPLY message of CMD 0104h Write Firmware Block EPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0105hReadFirmwareBlockLPLReply(CMDBaseReply):
    """REPLY message of CMD 0105h Read Firmware Block LPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)
        self.base_address_block: int = reply["base_address_block"]
        """hex string, Base address of the data block within the firmware image.
        """
        self.image_data = reply["image_data"]
        """hex string, Up to 116 bytes.
        """

class CMD0106hReadFirmwareBlockEPLReply(CMDBaseReply):
    """REPLY message of CMD 0106h Read Firmware Block EPL
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)
        self.image_data = reply["image_data"]
        """Up to 2048 Bytes. Actual Length specified in RPLLength
        """

class CMD0107hCompleteFirmwareDownloadReply(CMDBaseReply):
    """REPLY message of CMD 0107h Complete Firmware Download
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD0108hCopyFirmwareImageReply(CMDBaseReply):
    """REPLY message of CMD 0108h Copy Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)
        self.length: int = reply["length"]
        """integer, number of bytes copied.
        """
        self.copy_direction: int = reply['copy_direction']
        """int, copy direction.

        * ``0xAB``, Copy Image A into Image B
        * ``0xBA``,Copy Image B into Image A

        """
        self.copy_status: int = reply['copy_status']
        """int, copy status.

        * ``0x00``, Copy Successful
        * ``0x01``, Copy Failed

        """

class CMD0109hRunFirmwareImageReply(CMDBaseReply):
    """REPLY message of CMD 0109h Run Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CMD010AhCommitFirmwareImageReply(CMDBaseReply):
    """REPLY message of CMD 010Ah Commit Firmware Image
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        super().__init__(reply)

class CustomCMDReply():
    """Defines the custom reply to receiver for the CDB instance.
    """
    def __init__(self, reply: t.Dict[str, t.Any]) -> None:
        self.cdb_io_status: int = reply["reply_status"]["cdb_io_status"]
        """integer, indicates the CDB IO status.

        * 0: Idle, transceiver is not processing a CDB command.
        * 1: Finished, transceiver has finished processing a CDB command. It is ready to accept a new CDB command.
        * 2: Timeout, transceiver has timed out while processing a CDB command. It is ready to accept a new CDB command.
        * 3: In progress: transceiver is currently processing a CDB command. It is not ready to accept a new CDB command.

        """

        self.cdb_cmd_complete_flag: bool = reply["reply_status"]["cdb_cmd_complete_flag"]
        """Integer, REPLY Status.CdbCmdCompleteFlag. 
        
        Indicates whether the CDB command is complete.

        """

        self.cdb_status: int = reply["reply_status"]["cdb_status"]
        """Integer, REPLY Status.CdbStatus. 
        
        Provides the status of the most recently triggered CDB command.

        """

        self.rpl_length: int = reply["reply_header"]["rpl_length"]
        """integer, REPLY Header.RPLLength.

        Length of the reply data.

        """

        self.rpl_check_code: int = reply["reply_header"]["rpl_check_code"]
        """integer, REPLY Header.RPLChkCode.
        
        Check code for the reply data.

        """

        self.data = reply["reply_data"]["data"]
        """hex string, REPLY Data.Data
        
        The actual data to be sent in the reply.

        """