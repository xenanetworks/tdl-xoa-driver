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



async def get_current_tx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return current port Tx frequency in Hz.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Tx frequency in Hz.
    :rtype: int
    """

    resp = await port.layer1_adv.freq.tx_curr.get()
    return resp.frequency_hz


async def get_current_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return current port Rx frequency in Hz.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Rx frequency in Hz.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_curr.get()
    return resp.frequency_hz


async def get_minimum_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return minimum port Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The minimum Rx frequency in Hz since last query.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_min.get()
    return resp.frequency_hz


async def get_maximum_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return maximum port Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The maximum Rx frequency in Hz since last query.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_max.get()
    return resp.frequency_hz


async def get_rx_frequencies(port: "Z800FreyaPort") -> Tuple[int, int, int]:
    """
    Return port current, minimum, and maximum Rx frequency in Hz.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The port current, minimum, and maximum Rx frequency in Hz.
    :rtype: Tuple[int, int, int]
    """

    resp1, resp2, resp3 = await apply(
        port.layer1_adv.freq.rx_curr.get(),
        port.layer1_adv.freq.rx_min.get(),
        port.layer1_adv.freq.rx_max.get(),
    )

    return (resp1.frequency_hz, resp2.frequency_hz, resp3.frequency_hz)


async def get_loss_of_locks(port: "Z800FreyaPort", lane_indices: List[int]) -> List[Tuple[bool, bool]]:
    """
    Returns current + sticky Loss of Lock (LOL) status of the specified PCS lanes.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: A list of tuples containing current and sticky LOL status for each lane.
    :rtype: List[Tuple[bool, bool]]
    """
    results = []
    cmds = []
    for lane in lane_indices:
        cmds.append(port.layer1_adv.lane[lane].rx_lol.get())
    resps = await apply(*cmds)
    for resp in resps:
        curr = True if resp.current_lol.value == 1 else False
        latched = True if resp.latched_lol.value == 1 else False
        results.append((curr, latched))
    return results


async def get_rx_lane_skews(port: "Z800FreyaPort", lane_indices: List[int]) -> List[int]:
    """Returns relative skew of the PCS lanes measured in bits

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: Relative skew of the PCS lanes measured in bits
    :rtype: List[int]
    """
    results = []
    cmds = []
    for lane in lane_indices:
        cmds.append(port.layer1_adv.lane[lane].rx_skew.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.skew_bits)
    return results


async def get_hi_ber(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Returns current + sticky High BER status.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and sticky High BER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.hi_ber.status.get()
    curr = True if resp.current_hiber.value == 1 else False
    latched = True if resp.latched_hiber.value == 1 else False
    return (curr, latched)


async def get_hi_ser(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Returns current + sticky High SER status.

    High SER is signalled if 5560 RS-FEC symbol errors are detected in
    contiguous block of 8192 non-overlapping RS-FEC codewords.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and sticky High SER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.hi_ser.status.get()
    curr = True if resp.current_hiser.value == 1 else False
    latched = True if resp.latched_hiser.value == 1 else False
    return (curr, latched)


async def get_degraded_ser(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Returns current + sticky Degraded SER status.

    The criteria for signaling Degraded SER is programmable using
    :py:func:`set_degraded_ser_criteria`.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and sticky Degraded SER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.degraded_ser.status.get()
    curr = True if resp.current_deg_ser.value == 1 else False
    latched = True if resp.latched_deg_ser.value == 1 else False
    return (curr, latched)


async def set_degraded_ser_criteria(port: "Z800FreyaPort", activate_threshold: int, deactivate_threshold: int, interval: int) -> None:
    """
    Set criteria for signaling Degraded SER.

    If more than `activate_threshold` RS-FEC symbol errors are detected
    in a contiguous block of `interval` RS-FEC codewords, Degraded SER
    is signalled.

    If less than `deactivate_threshold` RS-FEC symbol errors are detected
    in a contiguous block of `interval` RS-FEC codewords, Degraded SER
    is no longer signalled.

    `interval` must be an even number and a multiple of the number of PCS flows:

        - 100G:      2 (one flow, but must be even)
        - 200G/400G: 2 (two flows)
        - 800G/1.6T: 4 (four flows)

    An uncorrectable codeword is counted as 16 erroneous RS-FEC symbols.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :param activate_threshold: The activate threshold.
    :type activate_threshold: int
    :param deactivate_threshold: The deactivate threshold.
    :type deactivate_threshold: int
    :param interval: The interval.
    :type interval: int
    """
    await port.layer1_adv.degraded_ser.threshold.set(
        act_thresh=activate_threshold,
        deact_thresh=deactivate_threshold,
        degrade_interval=interval,
    )


async def get_degraded_ser_criteria(
    port: "Z800FreyaPort",
) -> Tuple[int, int, int]:
    """
    Get criteria for signaling Degraded SER.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing activate threshold, deactivate threshold, and interval.
    :rtype: Tuple[int, int, int]
    """
    resp = await port.layer1_adv.degraded_ser.threshold.get()

    return (resp.act_thresh, resp.deact_thresh, resp.degrade_interval)


async def get_cw_error_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of erroneous 64b/66b codewords since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of erroneous 64b/66b codewords since last call.
    :rtype: int
    """
    resp = await port.layer1_adv.err_cw.rx_count.get()
    return resp.err_cw_count


async def get_itb_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of invalid 256b/257b transcode blocks since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of invalid 256b/257b transcode blocks since last call.
    :rtype: int
    """
    resp = await port.layer1_adv.itb.rx_count.get()
    return resp.itb_count


async def get_link_sync_loss_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of times link sync has been lost since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of times link sync has been lost since last call.
    :rtype: int
    """
    resp = await port.layer1_adv.err_stats.rx_losync_count.get()
    return resp.losync_count


async def get_local_fault_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of local fault conditions since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of local fault conditions since last call.
    :rtype: int
    """
    resp = await port.layer1_adv.err_stats.rx_lf_count.get()
    return resp.lf_count


async def get_remote_fault_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of remote fault conditions since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of remote fault conditions since last call.
    :rtype: int
    """
    resp = await port.layer1_adv.err_stats.rx_rf_count.get()
    return resp.rf_count


__all__ = (
    "get_current_tx_frequency",
    "get_current_rx_frequency",
    "get_minimum_rx_frequency",
    "get_maximum_rx_frequency",
    "get_rx_frequencies",
    "get_loss_of_locks",
    "get_rx_lane_skews",
    "get_hi_ber",
    "get_hi_ser",
    "get_degraded_ser",
    "set_degraded_ser_criteria",
    "get_degraded_ser_criteria",
    "get_cw_error_count",
    "get_itb_count",
    "get_link_sync_loss_count",
    "get_local_fault_count",
    "get_remote_fault_count",
)