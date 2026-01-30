"""
Transceiver R/W functions
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
    from xoa_driver.ports import Z800FreyaPort, Z1600EdunPort, Z100LokiPort, Z10OdinPort, Z400ThorPort

from ..misc import Hex



async def get_xcvr_rw_seq_bank(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", bank: int, page: int, register: int, length: int) -> str:
    """Read a number of bytes from transceiver register interface via I2C.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param bank: The bank address, e.g. 10 or 0xA
    :type bank: int
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param length: The number of bytes to read
    :type length: int
    :return: The read bytes as a string, e.g. 'DEADBEEF'
    :rtype: str
    """

    resp = await port.transceiver.access_rw_seq_bank(bank_address=bank, page_address=page, register_address=register, byte_count=length).get()
    return resp.value

async def set_xcvr_rw_seq_bank(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", bank: int, page: int, register: int, value: str) -> None:
    """Write a number of bytes to transceiver register interface via I2C.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param bank: The bank address, e.g. 10 or 0xA
    :type bank: int
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param value: The bytes to write as a string, e.g. 'DEADBEEF'
    :type value: str
    """
    await port.transceiver.access_rw_seq_bank(bank_address=bank, page_address=page, register_address=register, byte_count=len(value)//2).set(value=Hex(value))


async def get_xcvr_rw_seq(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", page: int, register: int, length: int) -> str:
    """Read a number of bytes from transceiver register interface via I2C.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param length: The number of bytes to read
    :type length: int
    :return: The read bytes as a string, e.g. 'DEADBEEF'
    :rtype: str
    """

    resp = await port.transceiver.access_rw_seq(page_address=page, register_address=register, byte_count=length).get()
    return resp.value

async def set_xcvr_rw_seq(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", page: int, register: int, value: str) -> None:
    """Write a number of bytes to transceiver register interface via I2C.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param value: The bytes to write as a string, e.g. 'DEADBEEF'
    :type value: str
    """
    await port.transceiver.access_rw_seq(page_address=page, register_address=register, byte_count=len(value)//2).set(value=Hex(value))


async def get_xcvr_rw(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", page: int, register: int) -> str:
    """Read 4 bytes from transceiver register interface.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :return: The read bytes as a string, e.g. 'DEADBEEF'
    :rtype: str
    """

    resp = await port.transceiver.access_rw(page_address=page, register_address=register).get()
    return resp.value

async def set_xcvr_rw(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", page: int, register: int, value: str) -> None:
    """Write 4 bytes to transceiver register interface.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param value: The bytes to write as a string, e.g. 'DEADBEEF'
    :type value: str
    """
    await port.transceiver.access_rw(page_address=page, register_address=register).set(value=Hex(value))

async def get_xcvr_mii(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", register: int) -> str:
    """Read 2 bytes from transceiver register interface.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :return: The read 2 bytes as a string, e.g. 'DEAF'
    :rtype: str
    """

    resp = await port.transceiver.access_mii(register_address=register).get()
    return resp.value

async def set_xcvr_mii(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort",register: int, value: str) -> None:
    """Write 2 bytes to transceiver register interface.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param page: The page address, e.g. 10 or 0xA
    :type page: int
    :param register: The register address, e.g. 10 or 0xA
    :type register: int
    :param value: The 2 bytes to write as a string, e.g. 'DEAF'
    :type value: str
    """
    await port.transceiver.access_mii(register_address=register).set(value=Hex(value))

async def get_i2c_freq_khz(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort") -> int:
    """Read access speed on a transceiver I2C access in the unit of KHz. Default to 100. 
    
    When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from P_CAPABILITIES. 
    
    The I2C speed configuration will not be included in the port configuration file (.xpc). 
    When you load a port configuration to a port, the transceiver I2C access speed will be reset to default 100.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :return: The current I2C access speed in KHz
    :rtype: int
    """

    resp = await port.transceiver.i2c_config.get()
    return resp.frequency

async def set_i2c_freq_khz(port: "Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort", frequency: int) -> None:
    """Set access speed on a transceiver I2C access in the unit of KHz.
    
    When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from P_CAPABILITIES. 
    
    The I2C speed configuration will not be included in the port configuration file (.xpc). 
    When you load a port configuration to a port, the transceiver I2C access speed will be reset to default 100.

    :param port: The port object
    :type port: Z1600EdunPort | Z800FreyaPort | Z400ThorPort | Z100LokiPort | Z10OdinPort
    :param frequency: The desired I2C access speed in KHz
    :type frequency: int
    """

    await port.transceiver.i2c_config.set(frequency=frequency)




__all__ = (
    "get_xcvr_rw_seq_bank",
    "set_xcvr_rw_seq_bank",
    "get_xcvr_rw_seq",
    "set_xcvr_rw_seq",
    "get_xcvr_rw",
    "set_xcvr_rw",
    "get_xcvr_mii",
    "set_xcvr_mii",
    "get_i2c_freq_khz",
    "set_i2c_freq_khz",
)