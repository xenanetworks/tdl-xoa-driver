
from argparse import __all__
from typing import (
    NamedTuple,
)

class TxFreq(NamedTuple):
    """Tx frequency in MHz

    Attributes:
        current: int
        minimum: int
        maximum: int
    """

    current: int
    minimum: int
    maximum: int

class TxPpm(NamedTuple):
    """Tx PPM

    Attributes:
        current: int
        minimum: int
        maximum: int
    """

    current: int
    minimum: int
    maximum: int

class TxFreqPpm(NamedTuple):
    freq: TxFreq
    ppm: TxPpm

class RxFreq(NamedTuple):
    current: int
    minimum: int
    maximum: int

class RxPpm(NamedTuple):
    current: int
    minimum: int
    maximum: int

class RxFreqPpm(NamedTuple):
    freq: RxFreq
    ppm: RxPpm

class TxDatarate(NamedTuple):
    current: int
    minimum: int
    maximum: int

class RxDatarate(NamedTuple):
    current: int
    minimum: int
    maximum: int

class CdrLolStatus(NamedTuple):
    current: bool
    latched: bool

class PcslSkew(NamedTuple):
    pcsl: int
    skew: int

class HiBerStatus(NamedTuple):
    current: bool
    latched: bool

class HiSerStatus(NamedTuple):
    alarm_state: bool
    current: bool
    latched: bool

class DegSerStatus(NamedTuple):
    current: bool
    latched: bool

class DegSerThresholds(NamedTuple):
    activate_threshold: int
    deactivate_threshold: int
    interval: int

class LocalFaultStatus(NamedTuple):
    current: bool
    latched: bool

class RemoteFaultStatus(NamedTuple):
    current: bool
    latched: bool

class LinkDownStatus(NamedTuple):
    current: bool
    latched: bool

class RxPcsErrors(NamedTuple):
    loa: int
    itb: int
    err_cw: int
    link_down: int
    remote_fault: int
    local_fault: int

class TxPcsErrors(NamedTuple):
    hi_ser: int
    itb: int
    err_cw: int

class LoaStatus(NamedTuple):
    current: bool
    latched: bool

class TxPcslErrors(NamedTuple):
    am_err: int

__all__ = (
    "TxFreq",
    "TxPpm",
    "TxFreqPpm",
    "RxFreq",
    "RxPpm",
    "RxFreqPpm",
    "TxDatarate",
    "RxDatarate",
    "CdrLolStatus",
    "PcslSkew",
    "HiBerStatus",
    "HiSerStatus",
    "DegSerStatus",
    "DegSerThresholds",
    "LocalFaultStatus",
    "RemoteFaultStatus",
    "LinkDownStatus",
    "RxPcsErrors",
    "TxPcsErrors",
    "LoaStatus",
    "TxPcslErrors",
)