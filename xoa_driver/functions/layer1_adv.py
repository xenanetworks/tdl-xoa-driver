"""
The advanced Layer 1 functions
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
    type FreyaEdunModule = Union[Z800FreyaModule, Z1600EdunModule]
    type FreyaEdunPort = Union[Z800FreyaPort, Z1600EdunPort]



async def get_current_tx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return current port Tx frequency in Hz.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Tx frequency in Hz.
    :rtype: int
    """
    return 1


async def get_current_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return current port Rx frequency in Hz.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The current Rx frequency in Hz.
    :rtype: int
    """
    return 1


async def get_minimum_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return minimum port Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The minimum Rx frequency in Hz since last query.
    :rtype: int
    """
    return 1


async def get_maximum_rx_frequency(port: "Z800FreyaPort") -> int:
    """
    Return maximum port Rx frequency in Hz since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The maximum Rx frequency in Hz since last query.
    :rtype: int
    """
    return 1


async def get_rx_frequencies(port: "Z800FreyaPort") -> Tuple[int, int, int]:
    """
    Return port current, minimum, and maximum Rx frequency in Hz.

    The minimum and maximum values are since last query.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: The port current, minimum, and maximum Rx frequency in Hz.
    :rtype: Tuple[int, int, int]
    """
    current = await get_current_rx_frequency(port)
    minimum = await get_minimum_rx_frequency(port)
    maximum = await get_maximum_rx_frequency(port)
    return (current, minimum, maximum)


async def get_loss_of_lock(port: "Z800FreyaPort", serdes_index: int) -> Tuple[bool, bool]:
    """
    Returns current + sticky Loss of Lock (LOL) status of the specified SerDes.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and sticky LOL status.
    :rtype: Tuple[bool, bool]
    """
    return (False, False)


async def get_rx_lane_skew(port: "Z800FreyaPort", lane_index: int) -> int:
  """Returns relative skew of the PCS lane measured in bits

  :param port: The port instance.
  :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
  :param lane_index: The index of the PCS lane.
  :type lane_index: int
  :return: Relative skew of the PCS lane measured in bits
  :rtype: int
  """
  return 1


async def get_hi_ber(port: "Z800FreyaPort") -> Tuple[bool, bool]:
    """
    Returns current + sticky High BER status.

    Sticky means latched clear-on-read.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: A tuple containing current and sticky High BER status.
    :rtype: Tuple[bool, bool]
    """
    return (False, False)


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
    return (False, False)


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
    return (False, False)


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
    pass


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
    return (1, 1, 1)


async def get_cw_error_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of erroneous 64b/66b codewords since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of erroneous 64b/66b codewords since last call.
    :rtype: int
    """
    return 1


async def get_itb_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of invalid 256b/257b transcode blocks since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of invalid 256b/257b transcode blocks since last call.
    :rtype: int
    """
    return 1


async def get_link_sync_loss_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of times link sync has been lost since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of times link sync has been lost since last call.
    :rtype: int
    """
    return 1


async def get_local_fault_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of local fault conditions since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of local fault conditions since last call.
    :rtype: int
    """
    return 1


async def get_remote_fault_count(port: "Z800FreyaPort") -> int:
    """
    Returns number of remote fault conditions since last call.

    :param port: The port instance.
    :type port: :class:`~xoa_driver.ports.Z800FreyaPort`
    :return: Number of remote fault conditions since last call.
    :rtype: int
    """
    return 1


__all__ = (
    "get_current_tx_frequency",
    "get_current_rx_frequency",
    "get_minimum_rx_frequency",
    "get_maximum_rx_frequency",
    "get_rx_frequencies",
    "get_loss_of_lock",
    "get_rx_lane_skew",
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