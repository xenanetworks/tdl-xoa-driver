from __future__ import annotations
from xoa_driver.ports import PortL23
from ._utils import *
from ._constants import *

def check_cdb_status(cdb_status: str) -> CdbCommandCoarseStatus:
    cdb_status_int = int(cdb_status, 16)
    if cdb_status_int & 0x80 == 0x80:
        return CdbCommandCoarseStatus.IN_PROGRESS
    elif cdb_status_int & 0xC0 == 0x40:
        return CdbCommandCoarseStatus.FAILED
    elif cdb_status_int & 0xC0 == 0x00:
        return CdbCommandCoarseStatus.SUCCESS
    else:
        raise ValueError(f"Invalid CDB status: {cdb_status}")
    

def check_erased_byte(data_block: str, erased_byte: str) -> bool:
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