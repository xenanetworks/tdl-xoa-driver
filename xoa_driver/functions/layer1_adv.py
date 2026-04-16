"""
The Advanced Layer 1 functions
"""

from __future__ import annotations
import asyncio
from typing import (
    TYPE_CHECKING,
    Any,
    Union,
    List,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.ports import Z800FreyaPort, Z1600EdunPort
    from xoa_driver.modules import Z800FreyaModule, Z1600EdunModule
    FreyaEdunModule = Union[Z800FreyaModule, Z1600EdunModule]
    FreyaEdunPort = Union[Z800FreyaPort, Z1600EdunPort]

from ..utils import apply
from ..enums import (
    OnOff,
    PcsErrorInjectionType,
)
import warnings
from collections import namedtuple
from random import sample


async def get_tx_freq_curr(port: "FreyaEdunPort") -> int:
    """
    Get the current Tx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current Tx frequency in Hz.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_freq.get()
    return resp.current


async def get_tx_freq_min(port: "FreyaEdunPort") -> int:
    """
    Get the minimum Tx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The minimum Tx frequency in Hz.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_freq.get()
    return resp.minimum


async def get_tx_freq_max(port: "FreyaEdunPort") -> int:
    """
    Get the maximum Tx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The maximum Tx frequency in Hz.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_freq.get()
    return resp.maximum


TxFreq = namedtuple("TxFreq", ["current", "minimum", "maximum"])
async def get_tx_freq_all(port: "FreyaEdunPort") -> TxFreq:
    """
    Get the current, minimum, and maximum Tx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current, minimum, and maximum Tx frequency in Hz.
    :rtype: TxFreq
    """

    resp = await port.layer1_adv.tx_freq.get()
    return TxFreq(current=resp.current, minimum=resp.minimum, maximum=resp.maximum)
    # return (resp.current, resp.minimum, resp.maximum)


async def get_tx_ppm_curr(port: "FreyaEdunPort") -> int:
    """
    Get the current Tx PPM of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current Tx PPM.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_ppm.get()
    return resp.current


async def get_tx_ppm_min(port: "FreyaEdunPort") -> int:
    """
    Get the minimum Tx PPM of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The minimum Tx PPM.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_ppm.get()
    return resp.minimum


async def get_tx_ppm_max(port: "FreyaEdunPort") -> int:
    """
    Get the maximum Tx PPM of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The maximum Tx PPM.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_ppm.get()
    return resp.maximum


TxPpm = namedtuple("TxPpm", ["current", "minimum", "maximum"])
async def get_tx_ppm_all(port: "FreyaEdunPort") -> TxPpm:
    """
    Get the current, minimum, and maximum Tx PPM of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current, minimum, and maximum Tx PPM.
    :rtype: TxPpm
    """

    resp = await port.layer1_adv.tx_ppm.get()
    return TxPpm(current=resp.current, minimum=resp.minimum, maximum=resp.maximum)


TxFreqPpm = namedtuple("TxFreqPpm", ["freq", "ppm"])
async def get_tx_freq(port: "FreyaEdunPort") -> TxFreqPpm:
    """
    Get the current, minimum, and maximum Tx frequency (Hz) and frequency offset (ppm) of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Tx frequency current, minimum, and maximum, and frequency offset (ppm) current, minimum, and maximum.
    :rtype: TxFreqPpm
    """

    freq_resp, ppm_resp = await apply(
        port.layer1_adv.tx_freq.get(),
        port.layer1_adv.tx_ppm.get(),
        )
    return TxFreqPpm(
        freq=TxFreq(current=freq_resp.current, minimum=freq_resp.minimum, maximum=freq_resp.maximum),
        ppm=TxPpm(current=ppm_resp.current, minimum=ppm_resp.minimum, maximum=ppm_resp.maximum)
    )


async def get_rx_freq_curr(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the current Rx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current Rx frequency in Hz of the specified Serdes.
    :rtype: List[int]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.current)
    return results


async def get_rx_freq_min(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the minimum Rx frequency in Hz since last query of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The minimum Rx frequency in Hz since last query of the specified Serdes.
    :rtype: List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.minimum)
    return results


async def get_rx_freq_max(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the maximum Rx frequency in Hz since last query of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The maximum Rx frequency in Hz since last query of the specified Serdes.
    :rtype: List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.maximum)
    return results


RxFreq = namedtuple("RxFreq", ["current", "minimum", "maximum"])
async def get_rx_freq_all(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[RxFreq]:
    """
    Get the current, minimum, and maximum Rx frequencies in Hz of the specified Serdes.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx frequencies in Hz of the specified Serdes.
    :rtype: List[RxFreq]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(RxFreq(current=resp.current, minimum=resp.minimum, maximum=resp.maximum))
    return results


async def get_rx_ppm_curr(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the current Rx PPM of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current Rx PPM of the specified Serdes.
    :rtype: List[int]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.current)
    return results


async def get_rx_ppm_min(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the minimum Rx PPM since last query of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The minimum Rx PPM since last query of the specified Serdes.
    :rtype: List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.minimum)
    return results


async def get_rx_ppm_max(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int]:
    """
    Get the maximum Rx PPM since last query of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The maximum Rx PPM since last query of the specified Serdes.
    :rtype: List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.maximum)
    return results


RxPpm = namedtuple("RxPpm", ["current", "minimum", "maximum"])
async def get_rx_ppm_all(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[RxPpm]:
    """
    Get the current, minimum, and maximum Rx PPM of the specified Serdes.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx PPM of the specified Serdes.
    :rtype: List[RxPpm]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(RxPpm(current=resp.current, minimum=resp.minimum, maximum=resp.maximum))
    return results


RxFreqPpm = namedtuple("RxFreqPpm", ["freq", "ppm"])
async def get_rx_freq(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[RxFreqPpm]:
    """
    Get the current, minimum, and maximum Rx frequency (Hz) and frequency offset (ppm) of the specified Serdes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Rx frequency current, minimum, and maximum, and frequency offset (ppm) current, minimum, and maximum of the specified Serdes.
    :rtype: List[RxFreqPpm]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for i in range(0, len(resps), 2):
        freq_resp = resps[i]
        ppm_resp = resps[i + 1]
        results.append(RxFreqPpm(
            freq=RxFreq(current=freq_resp.current, minimum=freq_resp.minimum, maximum=freq_resp.maximum),
            ppm=RxPpm(current=ppm_resp.current, minimum=ppm_resp.minimum, maximum=ppm_resp.maximum)
        ))
    return results


async def get_tx_datarate_curr(port: "FreyaEdunPort") -> int:
    """
    Get the current Tx datarate in bps of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current Tx datarate in bps.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_datarate.get()
    return resp.current


async def get_tx_datarate_min(port: "FreyaEdunPort") -> int:
    """
    Get the minimum Tx datarate in bps since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The minimum Tx datarate in bps since last query.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_datarate.get()
    return resp.minimum

async def get_tx_datarate_max(port: "FreyaEdunPort") -> int:
    """
    Get the maximum Tx datarate in bps since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The maximum Tx datarate in bps since last query.
    :rtype: int
    """

    resp = await port.layer1_adv.tx_datarate.get()
    return resp.maximum


TxDatarate = namedtuple("TxDatarate", ["current", "minimum", "maximum"])
async def get_tx_datarate_all(port: "FreyaEdunPort") -> TxDatarate:
    """
    Get the current, minimum, and maximum Tx datarate in bps of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The current, minimum, and maximum Tx datarate in bps.
    :rtype: TxDatarate
    """

    resp = await port.layer1_adv.tx_datarate.get()
    return TxDatarate(current=resp.current, minimum=resp.minimum, maximum=resp.maximum)


async def get_rx_datarate_curr(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the current Rx datarate in bps of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current Rx datarate in bps. If multiple Serdes indices are provided, a list of datarates is returned.
    :rtype: int or List[int]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_datarate.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.current)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_datarate_min(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the minimum Rx datarate in bps since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The minimum Rx datarate in bps since last query. If multiple Serdes indices are provided, a list of minimum datarates is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_datarate.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.minimum)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_datarate_max(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the maximum Rx datarate in bps since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The maximum Rx datarate in bps since last query. If multiple Serdes indices are provided, a list of maximum datarates is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_datarate.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.maximum)
    if len(results) == 1:
        return results[0]
    return results


RxDatarate = namedtuple("RxDatarate", ["current", "minimum", "maximum"])
async def get_rx_datarate_all(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[RxDatarate]:
    """
    Get the current, minimum, and maximum Rx datarates in bps of the specified Serdes.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx datarates in bps of the specified Serdes. 
    :rtype: List[RxDatarate]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_datarate.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(RxDatarate(current=resp.current, minimum=resp.minimum, maximum=resp.maximum))
    return results


CdrLolStatus = namedtuple("CdrLolStatus", ["current", "latched"])
async def get_cdr_lol_status(port: "FreyaEdunPort", serdes_indices: List[int]) -> List[CdrLolStatus]:
    """
    Get the per-SerDes current and latched CDR LOL status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: A list of CdrLolStatus namedtuples containing current and latched CDR LOL status for each Serdes.
    :rtype: List[CdrLolStatus]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_cdr_lol.get())
    resps = await apply(*cmds)
    for resp in resps:
        curr = True if resp.current.value == 1 else False
        latched = True if resp.latched.value == 1 else False
        results.append(CdrLolStatus(current=curr, latched=latched))
    return results


PcslSkew = namedtuple("PcslSkew", ["pcsl", "skew"])
async def get_rx_pcsl_skew(port: "FreyaEdunPort", lane_indices: List[int]) -> List[PcslSkew]:
    """Get per-physical lane Rx relative skew measured in bits and the corresponding PCSL of the specified physical PCS lanes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: PCSL and relative skew of the specified physical PCS lanes measured in bits
    :rtype: List[PcslSkew]
    """
    results = []
    cmds = []
    for lane in lane_indices:
        cmds.append(port.layer1.pcs.lane[lane].rx_status.status.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(PcslSkew(pcsl=resp.virtual_lane, skew=resp.skew))
    return results


HiBerStatus = namedtuple("HiBerStatus", ["current", "latched"])
async def get_hi_ber_status(port: "FreyaEdunPort") -> HiBerStatus:
    """
    Get the per-port current and latched HI-BER status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A HiBerStatus namedtuple containing current and latched HI-BER status.
    :rtype: HiBerStatus
    """
    resp = await port.layer1_adv.pcs.hi_ber.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return HiBerStatus(current=curr, latched=latched)


HiSerStatus = namedtuple("HiSerStatus", ["alarm_state", "current", "latched"])
async def get_hi_ser_status(port: "FreyaEdunPort") -> HiSerStatus:
    """
    Get the per-port current and latched HI-SER status.

    True means error condition is present, while False means error condition is not present.

    HI-SER is signalled if 5560 RS-FEC symbol errors are detected in contiguous block of 8192 non-overlapping RS-FEC codewords.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A HiSerStatus namedtuple containing alarm state, current and latched HI-SER status.
    :rtype: HiSerStatus
    """
    resp = await port.layer1_adv.pcs.hi_ser.status.get()
    alarm_state = True if resp.alarm_state == OnOff.ON else False
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return HiSerStatus(alarm_state=alarm_state, current=curr, latched=latched)


DegSerStatus = namedtuple("DegSerStatus", ["current", "latched"])
async def get_deg_ser_status(port: "FreyaEdunPort") -> DegSerStatus:
    """
    Get the per-port current and latched Degraded SER status.

    True means error condition is present, while False means error condition is not present.

    The thresholds for signaling Degraded SER is programmable using
    :py:func:`set_deg_ser_thresholds`.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A DegSerStatus namedtuple containing current and latched Degraded SER status.
    :rtype: DegSerStatus
    """
    resp = await port.layer1_adv.pcs.deg_ser.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return DegSerStatus(current=curr, latched=latched)


async def set_deg_ser_thresholds(port: "FreyaEdunPort", activate_threshold: int, deactivate_threshold: int, interval: int) -> None:
    """
    Configure signaling Degraded SER thresholds of the port.

    If more than `activate_threshold` number of RS-FEC symbol errors are detected
    in a contiguous block of `interval` RS-FEC codewords, Degraded SER
    is signalled on the port.

    If less than `deactivate_threshold` number of RS-FEC symbol errors are detected
    in a contiguous block of `interval` RS-FEC codewords, Degraded SER
    is no longer signalled on the port.

    `interval` must be an even number and a multiple of the number of PCS flows:

        - 100G:      2 (one flow, but must be even)
        - 200G/400G: 2 (two flows)
        - 800G/1.6T: 4 (four flows)

    An uncorrectable codeword is counted as 16 erroneous RS-FEC symbols.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param activate_threshold: The activate threshold.
    :type activate_threshold: int
    :param deactivate_threshold: The deactivate threshold.
    :type deactivate_threshold: int
    :param interval: The interval.
    :type interval: int
    """
    await port.layer1_adv.pcs.deg_ser.threshold.set(
        act_thresh=activate_threshold,
        deact_thresh=deactivate_threshold,
        degrade_interval=interval,
    )


DegSerThresholds = namedtuple("DegSerThresholds", ["activate_threshold", "deactivate_threshold", "interval"])
async def get_deg_ser_thresholds(
    port: "FreyaEdunPort",
) -> DegSerThresholds:
    """
    Get signaling Degraded SER thresholds of the port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A DegSerThresholds namedtuple containing activate threshold, deactivate threshold, and interval.
    :rtype: DegSerThresholds
    """
    resp = await port.layer1_adv.pcs.deg_ser.threshold.get()

    return DegSerThresholds(activate_threshold=resp.act_thresh, deactivate_threshold=resp.deact_thresh, interval=resp.degrade_interval)


LocalFaultStatus = namedtuple("LocalFaultStatus", ["current", "latched"])
async def get_lf_status(port: "FreyaEdunPort") -> LocalFaultStatus:
    """
    Get the per-port current and latched Local Fault status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A LocalFaultStatus namedtuple containing current and latched Local Fault status.
    :rtype: LocalFaultStatus
    """
    resp = await port.layer1.rs_fault.status.get()
    curr = True if resp.lf_current.value == 1 else False
    latched = True if resp.lf_latched.value == 1 else False
    return LocalFaultStatus(current=curr, latched=latched)


RemoteFaultStatus = namedtuple("RemoteFaultStatus", ["current", "latched"])
async def get_rf_status(port: "FreyaEdunPort") -> RemoteFaultStatus:
    """
    Get the per-port current and latched Remote Fault status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A RemoteFaultStatus namedtuple containing current and latched Remote Fault status.
    :rtype: RemoteFaultStatus
    """
    resp = await port.layer1.rs_fault.status.get()
    curr = True if resp.rf_current.value == 1 else False
    latched = True if resp.rf_latched.value == 1 else False
    return RemoteFaultStatus(current=curr, latched=latched)


async def get_lf_rf_status(port: "FreyaEdunPort") -> Tuple[LocalFaultStatus, RemoteFaultStatus]:
    """
    Get the per-port current and latched Local Fault and Remote Fault status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched Local Fault and Remote Fault status.
    :rtype: Tuple[LocalFaultStatus, RemoteFaultStatus]
    """
    resp = await port.layer1.rs_fault.status.get()
    lf_curr = True if resp.lf_current.value == 1 else False
    lf_latched = True if resp.lf_latched.value == 1 else False
    rf_curr = True if resp.rf_current.value == 1 else False
    rf_latched = True if resp.rf_latched.value == 1 else False
    return (LocalFaultStatus(current=lf_curr, latched=lf_latched), RemoteFaultStatus(current=rf_curr, latched=rf_latched))

LinkDownStatus = namedtuple("LinkDownStatus", ["current", "latched"])
async def get_link_down_status(port: "FreyaEdunPort") -> LinkDownStatus:
    """
    Get the per-port current and latched Link Down status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A LinkDownStatus namedtuple containing current and latched Link Down status.
    :rtype: LinkDownStatus
    """
    resp = await port.layer1_adv.pcs.link_down.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return LinkDownStatus(current=curr, latched=latched)


RxPcsErrors = namedtuple("RxPcsErrors", ["loa", "itb", "err_cw", "link_down", "remote_fault", "local_fault"])
async def get_rx_errors_since_clear(port: "FreyaEdunPort") -> RxPcsErrors:
    """
    Get the per-port number of Rx error events since the last counter clear, including LOA, 256b/257 ITBs, 64b/66b erroneous codewords, link down, local fault, and remote fault events.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A RxPcsErrors namedtuple containing the received number of LOA, 256b/257 ITBs, 64b/66b erroneous codewords, link down, local fault, and remote fault events, since the last counter clear per port.
    :rtype: RxPcsErrors
    """

    resp1, resp2 = await apply(
        port.layer1_adv.pcs.err_inject.rx_cnt.get(),
        port.layer1.rs_fault.stats.get(),
    )
    return RxPcsErrors(loa=resp1.loa_count, itb=resp1.itb_count, err_cw=resp1.err_cw_count, link_down=resp1.link_down_count, local_fault=resp2.lf_count, remote_fault=resp2.rf_count)


TxPcsErrors = namedtuple("TxPcsErrors", ["hi_ser", "itb", "err_cw"])
async def get_tx_errors_since_clear(port: "FreyaEdunPort") -> TxPcsErrors:
    """
    Get the per-port number of Tx error events since the last counter clear, including HI-SER, 256b/257 ITBs, and 64b/66b erroneous codewords.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A TxPcsErrors namedtuple containing the injected number of HI-SER, 256b/257 ITBs, 64b/66b erroneous codewords, since the last counter clear per port.
    :rtype: TxPcsErrors
    """

    resp = await port.layer1_adv.pcs.err_inject.tx_cnt.get()
    return TxPcsErrors(hi_ser=resp.hi_ser_count, itb=resp.itb_count, err_cw=resp.err_cw_count)
    
        
async def inject_errcwd_once(port: "FreyaEdunPort") -> None:
    """
    Inject a 64b/66b codeword error from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.err_inject.inject.set(type=PcsErrorInjectionType.ERRCWD)


async def inject_itb_once(port: "FreyaEdunPort") -> None:
    """
    Inject an invalid 256b/257b transcode block (ITB) from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.err_inject.inject.set(type=PcsErrorInjectionType.ITB)


async def inject_hi_ser_once(port: "FreyaEdunPort") -> None:
    """
    Inject a High SER (HI-SER) event from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.err_inject.inject.set(type=PcsErrorInjectionType.HISER)


async def set_hi_ser_alarm(port: "FreyaEdunPort", on: bool) -> None:
    """
    Set the HI-SER alarm on or off on the port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param on: Set to `True` to enable the HI-SER alarm, or `False` to disable the HI-SER alarm.
    """
    if on:
        await port.layer1_adv.pcs.hi_ser.alarm.set_on()
    else:
        await port.layer1_adv.pcs.hi_ser.alarm.set_off()


async def clear_rx_err_cnt(port: "FreyaEdunPort") -> None:
    """
    Clear Rx Layer 1 advanced statistics error counters on the port.
    """

    await port.layer1_adv.clear.set_rx()


async def clear_tx_err_cnt(port: "FreyaEdunPort") -> None:
    """
    Clear Tx Layer 1 advanced statistics error counters on the port.
    """

    await port.layer1_adv.clear.set_tx()


AmEncoding = namedtuple("AMEncoding", ["cm0", "cm1", "cm2", "cm3", "cm4", "cm5"])
async def get_am_encoding(port: "FreyaEdunPort", pcsl_indices: List[int]) -> List[AmEncoding]:
    """Get the standard alignment marker (AM) encoding of the specified PCSLs. 

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param pcsl_indices: The indices of the PCS lanes.
    :type pcsl_indices: List[int]
    :return: The AM encodings of the specified PCSLs.
    :rtype: List[AmEncoding]
    """
    results = []
    cmds = []
    for pcsl in pcsl_indices:
        cmds.append(port.layer1_adv.pcs.pcsl[pcsl].am.encoding.get())
    resps = await apply(*cmds)
    for resp in resps:
        encoding_nibbles = [resp.cm0, resp.cm1, resp.cm2, resp.cm3, resp.cm4, resp.cm5]
        results.append(AmEncoding(*encoding_nibbles))
    return results


async def inject_am_error_once(port: "FreyaEdunPort", pcsl: int, cm_nibbles: List[int], bad_count: int) -> None:
    """
    Inject an Alignment Marker (AM) error with the AM corruption parameters on the specified PCS lane immediately when called.

    This function first sets the AM corruption parameters on the specified PCS lane. It selects which CM nibbles in the AM to be corrupted and how many successive corrupted AMs should be sent on a specified PCSL.

    To successfully inject an LOA error on a PCSL, the following conditions must be met:

      * When RS-FEC is enabled, at least 4 CM nibbles should be errored.
      * When RS-FEC is disabled, a single CM nibble corruption is enough to trigger an LOA.
    
    (Only one bit in a CM nibble will be corrupted.)

    To trigger an LOA error on the PCSL, bad_count should be:

      * At least 4, for 40G (no FEC or FC-FEC), 50G ETC (no FEC or FC-FEC), 50GAUI-2 (RS-FEC KP), 100G (no FEC)
      * At least 5, for 50G ETC (RS-FEC KR), 50G IEEE (RS-FEC KP), 100G (RS-FEC KR, RS-FEC KP, RS-FEC KP-Int), 200G (RS-FEC KP-Int), 400G (RS-FEC KP-Int), 800G (RS-FEC KP-Int), 1.6T (RS-FEC KP-Int)

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param pcsl: The index of the PCS lane.
    :type pcsl: int
    :param cm_nibbles: The indices of the CM nibbles in the AM to be corrupted.
    :type cm_nibbles: List[int]
    :param bad_count: The number of successive corrupted AMs to be sent.
    :type bad_count: int
    """
    await port.layer1_adv.pcs.pcsl[pcsl].am.corrupt_config.set(cm_nibble_indices=cm_nibbles, am_bad_count=bad_count)
    await port.layer1_adv.pcs.pcsl[pcsl].err_inject.inject.inject_am()


async def inject_loa_once(port: "FreyaEdunPort", pcsl: int) -> None:
    """
    Inject a Loss of Alignment (LOA) error on the specified PCS lane immediately when called.

    This function uses the :py:func:`inject_am_error_once` function to inject an AM error with predefined AM corruption parameters that can trigger an LOA on the specified PCSL.

    * Number of CM nibbles to be corrupted: 4, randomly selected from the 6 CM nibbles in the AM. 
    * Number of successive corrupted AMs to be sent: 5, which is sufficient to trigger LOA for all supported speeds and FEC configurations.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param pcsl: The index of the PCS lane.
    :type pcsl: int

    """
    # generate a list of 4 integers ranging from 0 to 5 randomly
    cm_nibbles: list[int] = sample(range(6), k=4)
    await inject_am_error_once(port=port, pcsl=pcsl, cm_nibbles=cm_nibbles, bad_count=5)


LoaStatus = namedtuple("LoaStatus", ["current", "latched"])
async def get_port_loa_status(port: "FreyaEdunPort") -> LoaStatus:
    """
    Get the per-port current and latched Loss of Alignment (LOA) status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing the current and latched LOA status of the port.
    :rtype: LoaStatus
    """
    resp = await port.layer1_adv.pcs.loa.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return LoaStatus(current=curr, latched=latched)


async def get_pcsl_loa_status(port: "FreyaEdunPort", pcsl_indices: List[int]) -> List[LoaStatus]:
    """Get the per-PCSL current and latched Loss of Alignment (LOA) status.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param pcsl_indices: The indices of the PCS lanes.
    :type pcsl_indices: List[int]
    :return: A list of tuples containing the current and latched LOA status of the specified PCSLs.
    :rtype: List[LoaStatus]
    """
    results = []
    cmds = []
    for pcsl in pcsl_indices:
        cmds.append(port.layer1_adv.pcs.pcsl[pcsl].loa.status.get())
    resps = await apply(*cmds)
    for resp in resps:
        curr = True if resp.current.value == 1 else False
        latched = True if resp.latched.value == 1 else False
        results.append(LoaStatus(current=curr, latched=latched))
    return results


TxPcslErrors = namedtuple("TxPcslErrors", ["am_err"])
async def get_tx_pcsl_errors_since_clear(port: "FreyaEdunPort", pcsl_indices: List[int]) -> List[TxPcslErrors]:
    """
    Get the per-PCSL number of injected (Tx) AM errors since the last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param pcsl_indices: The indices of the PCS lanes.
    :type pcsl_indices: List[int]
    :return: A list of TxPcslErrors namedtuples containing the injected number of AM errors since the last counter clear per PCSL.
    :rtype: List[TxPcslErrors]
    """
    results = []
    cmds = []
    for pcsl in pcsl_indices:
        cmds.append(port.layer1_adv.pcs.pcsl[pcsl].am.err_inject.tx_cnt.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(TxPcslErrors(am_err=resp.tx_am_err_count))
    return results


##########################################
#                                        #
# Deprecated functions                   #
#                                        #
##########################################
async def get_cdr_lol(port: "FreyaEdunPort", serdes_indices: List[int]) -> List[Tuple[bool, bool]]:

    """
    :py:func:`get_cdr_lol` is deprecated and will be removed in a future release. Please use :py:func:`get_cdr_lol_status` instead.

    .. deprecated:: 1.8
    
    Get the current and latched CDR LOL status of the specified Serdes.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: A list of tuples containing the current and latched CDR LOL status for each specified Serdes.
    :rtype: List[Tuple[bool, bool]]

    """

    warnings.warn(message="get_cdr_lol is deprecated and will be removed in a future release. Please use get_cdr_lol_status instead.", category=DeprecationWarning, stacklevel=2)

    return await get_cdr_lol_status(port, serdes_indices)


async def get_rx_lane_skew(port: "FreyaEdunPort", lane_indices: List[int]) -> List[Tuple[int, int]]:

    """
    :py:func:`get_rx_lane_skew` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_pcsl_skew` instead.

    .. deprecated:: 1.8

    Get Rx relative skew measured in bits of the specified PCS lanes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: A list of tuples containing the current and latched RX lane skew for each specified PCS lane.
    :rtype: List[Tuple[int, int]]
    """

    warnings.warn(message="get_rx_lane_skew is deprecated and will be removed in a future release. Please use get_rx_pcsl_skew instead.", category=DeprecationWarning, stacklevel=2)

    return await get_rx_pcsl_skew(port, lane_indices)


async def get_hi_ber(port: "FreyaEdunPort") -> Tuple[bool, bool]:

    """
    :py:func:`get_hi_ber` is deprecated and will be removed in a future release. Please use :py:func:`get_hi_ber_status` instead.

    .. deprecated:: 1.8

    Get the current and latched HI-BER status of the specified port.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing the current and latched HI-BER status of the port.
    :rtype: Tuple[bool, bool]
    """

    warnings.warn(message="get_hi_ber is deprecated and will be removed in a future release. Please use get_hi_ber_status instead.", category=DeprecationWarning, stacklevel=2)

    return await get_hi_ber_status(port)


async def get_hi_ser(port: "FreyaEdunPort") -> Tuple[bool, bool, bool]:

    """
    :py:func:`get_hi_ser` is deprecated and will be removed in a future release. Please use :py:func:`get_hi_ser_status` instead.

    .. deprecated:: 1.8

    Get the current and latched HI-SER status of the specified port.
    True means error condition is present, while False means error condition is not present.
    HI-SER is signalled if 5560 RS-FEC symbol errors are detected in contiguous block of 8192 non-overlapping RS-FEC codewords.
    
    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing the current and latched HI-SER status of the port.
    :rtype: Tuple[bool, bool, bool]
    """
    warnings.warn(message="get_hi_ser is deprecated and will be removed in a future release. Please use get_hi_ser_status instead.", category=DeprecationWarning, stacklevel=2)

    return await get_hi_ser_status(port)


async def get_deg_ser(port: "FreyaEdunPort") -> Tuple[bool, bool]:

    """
    :py:func:`get_deg_ser` is deprecated and will be removed in a future release. Please use :py:func:`get_deg_ser_status` instead.

    .. deprecated:: 1.8

    Get the current and latched DEG-SER status of the specified port.
    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing the current and latched DEG-SER status of the port.
    :rtype: Tuple[bool, bool]
    """

    warnings.warn(message="get_deg_ser is deprecated and will be removed in a future release. Please use get_deg_ser_status instead.", category=DeprecationWarning, stacklevel=2)

    return await get_deg_ser_status(port)


async def set_cw_err(port: "FreyaEdunPort") -> None:

    """
    :py:func:`set_cw_err` is deprecated and will be removed in a future release. Please use :py:func:`inject_errcwd_once` instead.

    .. deprecated:: 1.8

    Inject a 64b/66b codeword error from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort
    """

    warnings.warn(message="set_cw_err is deprecated and will be removed in a future release. Please use inject_errcwd_once instead.", category=DeprecationWarning, stacklevel=2)

    await inject_errcwd_once(port)


async def set_itb(port: "FreyaEdunPort") -> None:

    """
    :py:func:`set_itb` is deprecated and will be removed in a future release. Please use :py:func:`inject_itb_once` instead.

    .. deprecated:: 1.8

    Inject an invalid 256b/257b transcode block (ITB) from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """

    warnings.warn(message="set_itb is deprecated and will be removed in a future release. Please use inject_itb_once instead.", category=DeprecationWarning, stacklevel=2)

    await inject_itb_once(port)


async def get_cw_err_since_last(port: "FreyaEdunPort") -> int:

    """
    :py:func:`get_cw_err_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of 64b/66b erroneous codewords received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of 64b/66b erroneous codewords received since last counter clear.
    :rtype: int
    """

    warnings.warn(message="get_cw_err_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1_adv.pcs.err_inject.rx_cnt.get()
    return resp.err_cw_count


async def get_itb_since_last(port: "FreyaEdunPort") -> int:

    """
    :py:func:`get_itb_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of 256b/257 ITBs received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of 256b/257 ITBs received since last counter clear.
    :rtype: int
    """

    warnings.warn(message="get_itb_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1_adv.pcs.err_inject.rx_cnt.get()
    return resp.itb_count


async def get_total_loa_since_last(port: "FreyaEdunPort") -> int:

    """
    :py:func:`get_total_loa_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of LOA events received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of LOA events received since last counter clear.
    :rtype: int
    """
    warnings.warn(message="get_total_loa_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1_adv.pcs.err_inject.rx_cnt.get()
    return resp.loa_count


async def get_link_down_since_last(port: "FreyaEdunPort") -> int:

    """
    :py:func:`get_link_down_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of link down events received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of link down events received since last counter clear.
    :rtype: int
    """

    warnings.warn(message="get_link_down_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1_adv.pcs.err_inject.rx_cnt.get()
    return resp.link_down_count


async def get_local_fault_since_last(port: "FreyaEdunPort") -> int:

    """
    :py:func:`get_local_fault_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of local fault events received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of local fault events received since last counter clear.
    :rtype: int
    """

    warnings.warn(message="get_local_fault_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1.rs_fault.stats.get()
    return resp.lf_count


async def get_remote_fault_since_last(port: "FreyaEdunPort") -> int:

    """
    
    :py:func:`get_remote_fault_since_last` is deprecated and will be removed in a future release. Please use :py:func:`get_rx_errors_since_clear` instead.

    .. deprecated:: 1.8

    Get the number of remote fault events received since last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: The number of remote fault events received since last counter clear.
    :rtype: int
    """

    warnings.warn(message="get_remote_fault_since_last is deprecated and will be removed in a future release. Please use get_rx_errors_since_clear instead.", category=DeprecationWarning, stacklevel=2)

    resp = await port.layer1.rs_fault.stats.get()
    return resp.rf_count




__all__ = (
    "get_tx_freq_curr",
    "get_tx_freq_min",
    "get_tx_freq_max",
    "get_tx_freq_all",
    "get_tx_ppm_curr",
    "get_tx_ppm_min",
    "get_tx_ppm_max",
    "get_tx_ppm_all",
    "get_tx_freq",
    "get_rx_freq_curr",
    "get_rx_freq_min",
    "get_rx_freq_max",
    "get_rx_freq_all",
    "get_rx_ppm_curr",
    "get_rx_ppm_min",
    "get_rx_ppm_max",
    "get_rx_ppm_all",
    "get_rx_freq",
    "get_tx_datarate_curr",
    "get_tx_datarate_min",
    "get_tx_datarate_max",
    "get_tx_datarate_all",
    "get_rx_datarate_curr",
    "get_rx_datarate_min",
    "get_rx_datarate_max",
    "get_rx_datarate_all",

    "set_hi_ser_alarm",
    "set_deg_ser_thresholds",
    "get_deg_ser_thresholds",
    "get_am_encoding",

    "get_cdr_lol_status",
    "get_rx_pcsl_skew",
    "get_hi_ber_status",
    "get_hi_ser_status",
    "get_deg_ser_status",
    "get_lf_status",
    "get_rf_status",
    "get_lf_rf_status",
    "get_link_down_status",
    "get_port_loa_status",
    "get_pcsl_loa_status",

    "get_rx_errors_since_clear",
    "get_tx_errors_since_clear",
    "get_tx_pcsl_errors_since_clear",

    "inject_errcwd_once",
    "inject_itb_once",
    "inject_am_error_once",
    "inject_loa_once",
    "inject_hi_ser_once",

    "clear_rx_err_cnt",
    "clear_tx_err_cnt",
    
    # Deprecated functions
    "get_cw_err_since_last",
    "get_itb_since_last",
    "get_total_loa_since_last",
    "get_link_down_since_last",
    "get_local_fault_since_last",
    "get_remote_fault_since_last",
    "get_cdr_lol",
    "get_rx_lane_skew",
    "get_hi_ber",
    "get_hi_ser",
    "get_deg_ser",
    "set_cw_err",
    "set_itb",
)