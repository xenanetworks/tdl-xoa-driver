from enum import IntEnum

class WriteMechanism(IntEnum):
    """Firmware update supported mechanism."""
    NONE_SUPPORTED = 0
    LPL_ONLY = 1
    EPL_ONLY = 2
    BOTH_SUPPORTED = 3

class ReadMechanism(IntEnum):
    """Firmware update supported mechanism."""
    NONE_SUPPORTED = 0
    LPL_ONLY = 1
    EPL_ONLY = 2
    BOTH_SUPPORTED = 3

class CdbCommandCoarseStatus(IntEnum):
    """The status of the most recently triggered CDB command.

    Coarse query results that are encoded by the pair of bit 7 (CdbIsBusy) and bit 6 (CdbHasFailed).
    """
    NA          = 0x00
    SUCCESS     = 0x01
    IN_PROGRESS = 0x80
    FAILED      = 0x40