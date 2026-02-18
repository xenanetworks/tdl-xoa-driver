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


async def get_rx_ppm_curr(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the current Rx PPM of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current Rx PPM. If multiple Serdes indices are provided, a list of PPM values is returned.
    :rtype: int or List[int]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.current)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_ppm_min(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the minimum Rx PPM since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The minimum Rx PPM since last query. If multiple Serdes indices are provided, a list of minimum PPM values is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.minimum)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_ppm_max(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the maximum Rx PPM since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The maximum Rx PPM since last query. If multiple Serdes indices are provided, a list of maximum PPM values is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.maximum)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_ppm(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[Tuple[int, int, int]] | Tuple[int, int, int]:
    """
    Get the current, minimum, and maximum Rx PPM of the specified port.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx PPM of the specified port. If multiple Serdes indices are provided, a list of tuples is returned.
    :rtype: Tuple[int, int, int] or List[Tuple[int, int, int]]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_ppm.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append((resp.current, resp.minimum, resp.maximum))
    if len(results) == 1:
        return results[0]
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


async def get_rx_datarate(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[Tuple[int, int, int]] | Tuple[int, int, int]:
    """
    Get the current, minimum, and maximum Rx datarates in bps of the specified port.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx datarates in bps of the specified port. If multiple Serdes indices are provided, a list of tuples is returned.
    :rtype: Tuple[int, int, int] or List[Tuple[int, int, int]]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_datarate.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append((resp.current, resp.minimum, resp.maximum))
    if len(results) == 1:
        return results[0]
    return results


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


async def get_rx_freq_curr(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the current Rx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current Rx frequency in Hz. If multiple Serdes indices are provided, a list of frequencies is returned.
    :rtype: int or List[int]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.current)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_freq_min(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the minimum Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The minimum Rx frequency in Hz since last query. If multiple Serdes indices are provided, a list of minimum frequencies is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.minimum)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_freq_max(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[int] | int:
    """
    Get the maximum Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The maximum Rx frequency in Hz since last query. If multiple Serdes indices are provided, a list of maximum frequencies is returned.
    :rtype: int or List[int]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.maximum)
    if len(results) == 1:
        return results[0]
    return results


async def get_rx_freq(port: "FreyaEdunPort", serdes_indices: List[int] = [0]) -> List[Tuple[int, int, int]] | Tuple[int, int, int]:
    """
    Get the current, minimum, and maximum Rx frequencies in Hz of the specified port.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: The current, minimum, and maximum Rx frequencies in Hz of the specified port. If multiple Serdes indices are provided, a list of tuples is returned.
    :rtype: Tuple[int, int, int] or List[Tuple[int, int, int]]
    """

    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_freq.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append((resp.current, resp.minimum, resp.maximum))
    if len(results) == 1:
        return results[0]
    return results




async def get_cdr_lol_status(port: "FreyaEdunPort", serdes_indices: List[int]) -> List[Tuple[bool, bool]]:
    """
    Get the current and latched CDR LOL status of the specified Serdes.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: A list of tuples containing current and latched CDR LOL status for each Serdes.
    :rtype: List[Tuple[bool, bool]]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_cdr_lol.get())
    resps = await apply(*cmds)
    for resp in resps:
        curr = True if resp.current_lol.value == 1 else False
        latched = True if resp.latched_lol.value == 1 else False
        results.append((curr, latched))
    return results


async def get_rx_pcsl_skew(port: "FreyaEdunPort", lane_indices: List[int]) -> List[Tuple[int, int]]:
    """Get Rx relative skew measured in bits of the specified PCS lanes.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: PCSL and relative skew of the specified PCS lanes measured in bits
    :rtype: List[Tuple[int, int]]
    """
    results = []
    cmds = []
    for lane in lane_indices:
        cmds.append(port.layer1.pcs.lane[lane].rx_status.status.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append((resp.virtual_lane, resp.skew))
    return results


async def get_hi_ber_status(port: "FreyaEdunPort") -> Tuple[bool, bool]:
    """
    Get the current and latched HI-BER status of the specified port.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched HI-BER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.hi_ber.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return (curr, latched)


async def get_hi_ser_status(port: "FreyaEdunPort") -> Tuple[bool, bool, bool]:
    """
    Get the current and latched HI-SER status of the specified port.

    True means error condition is present, while False means error condition is not present.

    HI-SER is signalled if 5560 RS-FEC symbol errors are detected in contiguous block of 8192 non-overlapping RS-FEC codewords.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing alarm state, current and latched HI-SER status.
    :rtype: Tuple[bool, bool, bool]
    """
    resp = await port.layer1_adv.pcs.hi_ser.status.get()
    alarm_state = True if resp.alarm_state == OnOff.ON else False
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return (alarm_state, curr, latched)


async def get_deg_ser_status(port: "FreyaEdunPort") -> Tuple[bool, bool]:
    """
    Get the current and latched Degraded SER status of the specified port.

    True means error condition is present, while False means error condition is not present.

    The thresholds for signaling Degraded SER is programmable using
    :py:func:`set_deg_ser_thresholds`.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched Degraded SER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.deg_ser.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return (curr, latched)


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


async def get_deg_ser_thresholds(
    port: "FreyaEdunPort",
) -> Tuple[int, int, int]:
    """
    Get signaling Degraded SER thresholds of the port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing activate threshold, deactivate threshold, and interval.
    :rtype: Tuple[int, int, int]
    """
    resp = await port.layer1_adv.pcs.deg_ser.threshold.get()

    return (resp.act_thresh, resp.deact_thresh, resp.degrade_interval)


async def get_lf_status(port: "FreyaEdunPort") -> Tuple[bool, bool]:
    """
    Get the current and latched Local Fault status of the specified port.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched Local Fault status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1.rs_fault.status.get()
    curr = True if resp.lf_current.value == 1 else False
    latched = True if resp.lf_latched.value == 1 else False
    return (curr, latched)


async def get_rf_status(port: "FreyaEdunPort") -> Tuple[bool, bool]:
    """
    Get the current and latched Remote Fault status of the specified port.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched Remote Fault status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1.rs_fault.status.get()
    curr = True if resp.rf_current.value == 1 else False
    latched = True if resp.rf_latched.value == 1 else False
    return (curr, latched)


async def get_link_down_status(port: "FreyaEdunPort") -> Tuple[bool, bool]:
    """
    Get the current and latched Link Down status of the specified port.

    True means error condition is present, while False means error condition is not present.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: A tuple containing current and latched Link Down status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.link_down.status.get()
    curr = True if resp.current.value == 1 else False
    latched = True if resp.latched.value == 1 else False
    return (curr, latched)

async def get_errcwd_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of erroneous 64b/66b codewords since the last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of erroneous 64b/66b codewords since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_stats.get()
    return resp.err_cw_count


async def get_itb_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of invalid 256b/257b transcode blocks since the last counter clear.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of invalid 256b/257b transcode blocks since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_stats.get()
    return resp.itb_count


async def get_link_down_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of cumulated link down events since the last counter clear per port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of cumulated link down events since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_stats.get()
    return resp.link_down_count


async def get_loa_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of cumulated Loss of Alignment (LOA) events since the last counter clear per port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of cumulated Loss of Alignment (LOA) events since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_stats.get()
    return resp.loa_count


async def get_lf_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of cumulated local fault conditions since the last counter clear per port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of cumulated local fault conditions since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1.rs_fault.stats.get()
    return resp.lf_count


async def get_rf_cnt_since_clear(port: "FreyaEdunPort") -> int:
    """
    Get the number of cumulated remote fault conditions since the last counter clear per port.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    :return: Number of cumulated remote fault conditions since the last counter clear per port.
    :rtype: int
    """
    resp = await port.layer1.rs_fault.stats.get()
    return resp.rf_count



async def set_errcwd(port: "FreyaEdunPort") -> None:
    """
    Inject a 64b/66b codeword error (CW Err) from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.tx_err_inject.set(type=PcsErrorInjectionType.ERRCWD)


async def set_itb(port: "FreyaEdunPort") -> None:
    """
    Inject an invalid 256b/257b transcode block (ITB) from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.tx_err_inject.set(type=PcsErrorInjectionType.ITB)


async def set_loa(port: "FreyaEdunPort") -> None:
    """
    Inject a Loss of Alignment (LOA) event from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.tx_err_inject.set(type=PcsErrorInjectionType.LOA)


async def set_hi_ser(port: "FreyaEdunPort") -> None:
    """
    Inject a High SER (HI-SER) event from the port immediately when called.

    :param port: The port instance.
    :type port: Union[Z800FreyaPort, Z1600EdunPort]
    """
    await port.layer1_adv.pcs.tx_err_inject.set(type=PcsErrorInjectionType.HISER)


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


async def clear_layer1_counters(port: "FreyaEdunPort") -> None:
    """
    Clear Layer 1 advanced statistics counters on the port.
    """

    await port.layer1_adv.clear.set_all()



__all__ = (
    "get_tx_ppm_curr",
    "get_rx_ppm_curr",
    "get_rx_ppm_min",
    "get_rx_ppm_max",
    "get_rx_ppm",
    "get_tx_datarate_curr",
    "get_rx_datarate_curr",
    "get_rx_datarate_min",
    "get_rx_datarate_max",
    "get_rx_datarate",
    "get_tx_freq_curr",
    "get_rx_freq_curr",
    "get_rx_freq_min",
    "get_rx_freq_max",
    "get_rx_freq",
    "get_cdr_lol_status",
    "get_rx_pcsl_skew",
    "get_hi_ber_status",
    "get_hi_ser_status",
    "get_deg_ser_status",
    "set_deg_ser_thresholds",
    "get_deg_ser_thresholds",
    "get_lf_status",
    "get_rf_status",
    "get_link_down_status",
    "get_errcwd_cnt_since_clear",
    "get_itb_cnt_since_clear",
    "get_link_down_cnt_since_clear",
    "get_loa_cnt_since_clear",
    "get_lf_cnt_since_clear",
    "get_rf_cnt_since_clear",
    "set_errcwd",
    "set_itb",
    "set_loa",
    "set_hi_ser",
    "set_hi_ser_alarm",
    "clear_layer1_counters",
)