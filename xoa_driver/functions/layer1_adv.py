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



async def get_tx_freq_curr(port: "Z800FreyaPort") -> int:
    """
    Get the current Tx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Tx frequency in Hz.
    :rtype: int
    """

    resp = await port.layer1_adv.freq.tx_curr.get()
    return resp.frequency_hz*10


async def get_rx_freq_curr(port: "Z800FreyaPort") -> int:
    """
    Get the current Rx frequency in Hz of the specified port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Rx frequency in Hz.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_curr.get()
    return resp.frequency_hz


async def get_rx_freq_min(port: "Z800FreyaPort") -> int:
    """
    Get the minimum Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The minimum Rx frequency in Hz since last query.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_min.get()
    return resp.frequency_hz


async def get_rx_freq_max(port: "Z800FreyaPort") -> int:
    """
    Get the maximum Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The maximum Rx frequency in Hz since last query.
    :rtype: int
    """
    resp = await port.layer1_adv.freq.rx_max.get()
    return resp.frequency_hz


async def get_rx_freq_all(port: "Z800FreyaPort") -> Tuple[int, int, int]:
    """
    Get the current, minimum, and maximum Rx frequencies in Hz of the specified port.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current, minimum, and maximum Rx frequencies in Hz of the specified port.
    :rtype: Tuple[int, int, int]
    """

    resp1, resp2, resp3 = await apply(
        port.layer1_adv.freq.rx_curr.get(),
        port.layer1_adv.freq.rx_min.get(),
        port.layer1_adv.freq.rx_max.get(),
    )

    return (resp1.frequency_hz, resp2.frequency_hz, resp3.frequency_hz)


async def get_cdr_lol_since_last(port: "Z800FreyaPort", serdes_indices: List[int]) -> List[Tuple[bool, bool]]:
    """
    Get the current and latched CDR LOL status of the specified Serdes.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :param serdes_indices: The indices of the Serdes.
    :type serdes_indices: List[int]
    :return: A list of tuples containing current and latched CDR LOL status for each Serdes.
    :rtype: List[Tuple[bool, bool]]
    """
    results = []
    cmds = []
    for serdes_id in serdes_indices:
        cmds.append(port.layer1_adv.serdes[serdes_id].rx_cdr_lol_since_last.get())
    resps = await apply(*cmds)
    for resp in resps:
        curr = True if resp.current_lol.value == 1 else False
        latched = True if resp.latched_lol.value == 1 else False
        results.append((curr, latched))
    return results


async def get_rx_lane_skew(port: "Z800FreyaPort", lane_indices: List[int]) -> List[int]:
    """Get Rx relative skew measured in bits of the specified PCS lanes.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :param lane_indices: The indices of the PCS lanes.
    :type lane_indices: List[int]
    :return: Relative skew of the specified PCS lanes measured in bits
    :rtype: List[int]
    """
    results = []
    cmds = []
    for lane in lane_indices:
        cmds.append(port.layer1_adv.pcs.lane[lane].rx_skew.get())
    resps = await apply(*cmds)
    for resp in resps:
        results.append(resp.skew_bits)
    return results


async def get_hi_ber(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Get the current and latched HI-BER status of the specified port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and latched HI-BER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.hi_ber.status.get()
    curr = True if resp.current_hiber.value == 1 else False
    latched = True if resp.latched_hiber.value == 1 else False
    return (curr, latched)


async def get_hi_ser(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Get the current and latched HI-SER status of the specified port.

    HI-SER is signalled if 5560 RS-FEC symbol errors are detected in contiguous block of 8192 non-overlapping RS-FEC codewords.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and latched HI-SER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.hi_ser.status.get()
    curr = True if resp.current_hiser.value == 1 else False
    latched = True if resp.latched_hiser.value == 1 else False
    return (curr, latched)


async def get_deg_ser(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Get the current and latched Degraded SER status of the specified port.

    The thresholds for signaling Degraded SER is programmable using
    :py:func:`set_deg_ser_thresholds`.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and latched Degraded SER status.
    :rtype: Tuple[bool, bool]
    """
    resp = await port.layer1_adv.pcs.deg_ser.status.get()
    curr = True if resp.current_deg_ser.value == 1 else False
    latched = True if resp.latched_deg_ser.value == 1 else False
    return (curr, latched)


async def set_deg_ser_thresholds(port: "Z800FreyaPort", activate_threshold: int, deactivate_threshold: int, interval: int) -> None:
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
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
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
    port: "Z800FreyaPort",
) -> Tuple[int, int, int]:
    """
    Get signaling Degraded SER thresholds of the port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing activate threshold, deactivate threshold, and interval.
    :rtype: Tuple[int, int, int]
    """
    resp = await port.layer1_adv.pcs.deg_ser.threshold.get()

    return (resp.act_thresh, resp.deact_thresh, resp.degrade_interval)


async def get_cw_err_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of erroneous 64b/66b codewords since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of erroneous 64b/66b codewords since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.err_cw.rx_err_cw_since_last.get()
    return resp.err_cw_count


async def get_itb_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of invalid 256b/257b transcode blocks since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of invalid 256b/257b transcode blocks since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.itb.rx_itb_since_last.get()
    return resp.itb_count


async def get_link_sync_loss_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of cumulated link sync loss events since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of cumulated link sync loss events since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_link_sync_loss_since_last.get()
    return resp.losync_count


async def get_local_fault_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of cumulated local fault conditions since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of cumulated local fault conditions since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.rs_fault.rx_local_fault_since_last.get()
    return resp.lf_count


async def get_remote_fault_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of cumulated remote fault conditions since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of cumulated remote fault conditions since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.rs_fault.rx_remote_fault_since_last.get()
    return resp.rf_count


async def get_total_loa_since_last(port: "Z800FreyaPort") -> int:
    """
    Get the number of cumulated Loss of Alignment (LOA) events since the previous query per port.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of cumulated Loss of Alignment (LOA) events since the previous query per port.
    :rtype: int
    """
    resp = await port.layer1_adv.pcs.rx_total_loa_since_last.get()
    return resp.loa_count


__all__ = (
    "get_tx_freq_curr",
    "get_rx_freq_curr",
    "get_rx_freq_min",
    "get_rx_freq_max",
    "get_rx_freq_all",
    "get_cdr_lol_since_last",
    "get_rx_lane_skew",
    "get_hi_ber",
    "get_hi_ser",
    "get_deg_ser",
    "set_deg_ser_thresholds",
    "get_deg_ser_thresholds",
    "get_cw_err_since_last",
    "get_itb_since_last",
    "get_link_sync_loss_since_last",
    "get_local_fault_since_last",
    "get_remote_fault_since_last",
    "get_total_loa_since_last",
)