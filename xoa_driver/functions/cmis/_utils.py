from __future__ import annotations
from ._utils import *
from ._constants import *

def get_cdb_coarse_status(cdb_status: int) -> CdbCommandCoarseStatus:
    """Convert CDB status to CDB command coarse status

    :param cdb_status: CDB status
    :type cdb_status: int
    :raises ValueError: value error if CDB status is invalid
    :return: CDB command coarse status
    :rtype: CdbCommandCoarseStatus
    """
    if cdb_status & 0x80 == 0x80:
        return CdbCommandCoarseStatus.IN_PROGRESS
    elif cdb_status & 0xC0 == 0x40:
        return CdbCommandCoarseStatus.FAILED
    elif cdb_status & 0x01 == 0x01:
        return CdbCommandCoarseStatus.SUCCESS
    elif cdb_status == 0x00:
        return CdbCommandCoarseStatus.NA
    else:
        raise ValueError(f"Invalid CDB status: {cdb_status}")
    

def check_erased_byte(data_block: str, erased_byte: str) -> bool:
    """Check erased byte against data block

    :param data_block: data block hex string
    :type data_block: str
    :param erased_byte: erased byte hex string
    :type erased_byte: str
    :return: True if data block matches erased byte pattern, False otherwise
    :rtype: bool
    """
    data_block = data_block.lower().lstrip("0x")
    erased_byte = erased_byte.lower().lstrip("0x")

    # Edge case: erased byte must be non-zero
    if not erased_byte:
        return False
    
    # Length of data block must be a multiple of length of erased byte
    if len(data_block) % len(erased_byte) != 0:
        return False
    
    # Repeat erased byte to match length of data block and compare
    multiplier = len(data_block) // len(erased_byte)
    return data_block == erased_byte * multiplier