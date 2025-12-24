``cdb`` module
=========================

Command Data Block (CDB) is a data structure used in SCSI (Small Computer System Interface) and other storage protocols to encapsulate commands sent to storage devices. It contains information about the command being executed, such as the operation code, parameters, and data transfer direction. CDBs are essential for communication between a host system and storage devices, enabling efficient data transfer and control operations.


.. currentmodule:: xoa_driver.hlfuncs.cmis.cdb

.. autosummary::

    cmd_0000h_query_status_cmd
    cmd_0000h_query_status_reply
    cmd_0001h_enter_password_cmd
    cmd_0001h_enter_password_reply
    cmd_0002h_change_password_cmd
    cmd_0002h_change_password_reply
    cmd_0004h_abort_processing_cmd
    cmd_0004h_abort_processing_reply
    cmd_0040h_module_features_cmd
    cmd_0040h_module_features_reply
    cmd_0041h_fw_mgmt_features_cmd
    cmd_0041h_fw_mgmt_features_reply
    cmd_0044h_sec_feat_and_capabilities_reply
    cmd_0044h_sec_feat_capabilities_cmd
    cmd_0045h_externally_defined_features_cmd
    cmd_0045h_externally_defined_features_reply
    cmd_0050h_get_application_attributes_cmd
    cmd_0050h_get_application_attributes_reply
    cmd_0051h_get_interface_code_description_cmd
    cmd_0051h_get_interface_code_description_reply
    cmd_0100h_get_firmware_info_cmd
    cmd_0100h_get_firmware_info_reply
    cmd_0101h_start_firmware_download_cmd
    cmd_0101h_start_firmware_download_reply
    cmd_0102h_abort_firmware_download_cmd
    cmd_0102h_abort_firmware_download_reply
    cmd_0103h_write_firmware_block_lpl_cmd
    cmd_0103h_write_firmware_block_lpl_reply
    cmd_0104h_write_firmware_block_epl_cmd
    cmd_0104h_write_firmware_block_epl_reply
    cmd_0105h_read_firmware_block_lpl_cmd
    cmd_0105h_read_firmware_block_lpl_reply
    cmd_0106h_read_firmware_block_epl_cmd
    cmd_0106h_read_firmware_block_epl_reply
    cmd_0107h_complete_firmware_download_cmd
    cmd_0107h_complete_firmware_download_reply
    cmd_0108h_copy_firmware_image_cmd
    cmd_0108h_copy_firmware_image_reply
    cmd_0109h_run_firmware_image_cmd
    cmd_0109h_run_firmware_image_reply
    cmd_010ah_commit_firmware_image_cmd
    cmd_010ah_commit_firmware_image_reply
    cmd_custom_cmd_reply
    cmd_custom_cmd_request
    CMD0000hQueryStatusReply
    CMD0001hEnterPasswordReply
    CMD0002hChangePasswordReply
    CMD0004hAbortProcessingReply
    CMD0040hModuleFeaturesReply
    CMD0041hFirmwareManagementFeaturesReply
    CMD0044hSecFeaturesAndCapabilitiesReply
    CMD0045hExternallyDefinedFeaturesReply
    CMD0050hGetApplicationAttributesReply
    CMD0051hGetInterfaceCodeDescriptionReply
    CMD0100hGetFirmwareInfoReply
    CMD0101hStartFirmwareDownloadReply
    CMD0102hAbortFirmwareDownloadReply
    CMD0103hWriteFirmwareBlockLPLReply
    CMD0104hWriteFirmwareBlockEPLReply
    CMD0105hReadFirmwareBlockLPLReply
    CMD0106hReadFirmwareBlockEPLReply
    CMD0107hCompleteFirmwareDownloadReply
    CMD0108hCopyFirmwareImageReply
    CMD0109hRunFirmwareImageReply
    CMD010AhCommitFirmwareImageReply
    CustomCMDReply
    firmware_download_procedure
    
Module Contents
-----------------

.. automodule:: xoa_driver.hlfuncs.cmis.cdb
    :members:
    :no-undoc-members:
    :member-order: bysource
    :exclude-members: __init__