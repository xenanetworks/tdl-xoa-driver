Command Data Block (CDB) 
=========================

Command Data Block (CDB) is a data structure used in SCSI (Small Computer System Interface) and other storage protocols to encapsulate commands sent to storage devices. It contains information about the command being executed, such as the operation code, parameters, and data transfer direction. CDBs are essential for communication between a host system and storage devices, enabling efficient data transfer and control operations.

.. currentmodule:: xoa_driver.hlfuncs.cmis.cdb

CMD 0000h: Query Status
-----------------------------

.. autoclass:: CMD0000hQueryStatusReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0000h_query_status_cmd

.. autofunction:: cmd_0000h_query_status_reply


CMD 0001h: Enter Password
-----------------------------

.. autoclass:: CMD0001hEnterPasswordReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0001h_enter_password_cmd

.. autofunction:: cmd_0001h_enter_password_reply


CMD 0002h: Change Password
-----------------------------

.. autoclass:: CMD0002hChangePasswordReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0002h_change_password_cmd

.. autofunction:: cmd_0002h_change_password_reply


CMD 0004h: Abort Processing
-----------------------------

.. autoclass:: CMD0004hAbortProcessingReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0004h_abort_processing_cmd

.. autofunction:: cmd_0004h_abort_processing_reply


CMD 0040h: Module Features
-----------------------------

.. autoclass:: CMD0040hModuleFeaturesReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0040h_module_features_reply


CMD 0041h: Firmware Management Features
---------------------------------------

.. autoclass:: CMD0041hFirmwareManagementFeaturesReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0041h_fw_mgmt_features_reply


CMD 0044h: Security Features and Capabilities
---------------------------------------------

.. autoclass:: CMD0044hSecFeaturesAndCapabilitiesReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0044h_sec_feat_and_capabilities_reply


CMD 0045h: Externally Defined Features
---------------------------------------------

.. autoclass:: CMD0045hExternallyDefinedFeaturesReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0045h_externally_defined_features_reply


CMD 0050h: Get Application Attributes
---------------------------------------------

.. autoclass:: CMD0050hGetApplicationAttributesReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0050h_get_application_attributes_cmd

.. autofunction:: cmd_0050h_get_application_attributes_reply


CMD 0051h: Get Interface Code Description
---------------------------------------------

.. autoclass:: CMD0051hGetInterfaceCodeDescriptionReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0051h_get_interface_code_description_cmd

.. autofunction:: cmd_0051h_get_interface_code_description_reply


CMD 0100h: Get Firmware Info
---------------------------------------------

.. autoclass:: CMD0100hGetFirmwareInfoReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0100h_get_firmware_info_reply


CMD 0101h: Start Firmware Download
---------------------------------------------

.. autoclass:: CMD0101hStartFirmwareDownloadReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0101h_start_firmware_download_cmd

.. autofunction:: cmd_0101h_start_firmware_download_reply


CMD 0102h: Abort Firmware Download
---------------------------------------------

.. autoclass:: CMD0102hAbortFirmwareDownloadReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0102h_abort_firmware_download_cmd

.. autofunction:: cmd_0102h_abort_firmware_download_reply


CMD 0103h: Write Firmware Block LPL
---------------------------------------------

.. autoclass:: CMD0103hWriteFirmwareBlockLPLReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0103h_write_firmware_block_lpl_cmd

.. autofunction:: cmd_0103h_write_firmware_block_lpl_reply

CMD 0104h: Write Firmware Block EPL
---------------------------------------------

.. autoclass:: CMD0104hWriteFirmwareBlockEPLReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0104h_write_firmware_block_epl_cmd

.. autofunction:: cmd_0104h_write_firmware_block_epl_reply


CMD 0105h: Read Firmware Block LPL
---------------------------------------------

.. autoclass:: CMD0105hReadFirmwareBlockLPLReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0105h_read_firmware_block_lpl_reply


CMD 0106h: Read Firmware Block EPL
---------------------------------------------

.. autoclass:: CMD0106hReadFirmwareBlockEPLReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0106h_read_firmware_block_epl_reply


CMD 0107h: Complete Firmware Download
---------------------------------------------

.. autoclass:: CMD0107hCompleteFirmwareDownloadReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0107h_complete_firmware_download_cmd

.. autofunction:: cmd_0107h_complete_firmware_download_reply


CMD 0108h: Copy Firmware Image
---------------------------------------------

.. autoclass:: CMD0108hCopyFirmwareImageReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0108h_copy_firmware_image_cmd

.. autofunction:: cmd_0108h_copy_firmware_image_reply

CMD 0109h: Run Firmware Image
---------------------------------------------

.. autoclass:: CMD0109hRunFirmwareImageReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_0109h_run_firmware_image_cmd

.. autofunction:: cmd_0109h_run_firmware_image_reply


CMD 010Ah: Commit Firmware Image
---------------------------------------------

.. autoclass:: CMD010AhCommitFirmwareImageReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_010ah_commit_firmware_image_cmd

.. autofunction:: cmd_010ah_commit_firmware_image_reply


CMD 8000h-FFFFh: Custom Command
---------------------------------------------

.. autoclass:: CustomCMDReply
    :members:
    :undoc-members:
    :exclude-members: __init__

.. autofunction:: cmd_custom_cmd_reply

.. autofunction:: cmd_custom_cmd_request


CMIS Firmware Download Procedure using CDB
------------------------------------------------

.. autofunction:: start_firmware_update
