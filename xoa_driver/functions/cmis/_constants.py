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


class CdbIoStatus(IntEnum):
    """Xena-specific state of the CDB operation in the tester (``cdb_io_status`` in the replies)."""
    IDLE        = 0
    FINISHED    = 1
    TIMEOUT     = 2
    IN_PROGRESS = 3
    FAILED      = 4


#: cdb_io_status values that end a CDB operation; stop polling the reply on these.
CDB_IO_STATUS_DONE = (CdbIoStatus.FINISHED, CdbIoStatus.TIMEOUT, CdbIoStatus.FAILED)
