from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PX_RW,
    PX_MII,
    PX_TEMPERATURE,
    PX_RW_SEQ,
    PX_I2C_CONFIG,
    PX_RW_SEQ_BANK,
)
from xoa_driver.internals.hli.ports.port_l23.layer1.laser_power import LaserPower
from xoa_driver.internals.hli.ports.port_l23.tcvr.cmis import Cmis


class Transceiver:
    """Transceiver access class."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id

        self.i2c_config = PX_I2C_CONFIG(conn, module_id, port_id)
        """
        Access speed on a transceiver I2C access in the unit of KHz. Default to 100. 
        
        When the transceiver is plugged out and in again, the speed will be reset to the default value 100. The speed has a minimum and a maximum, which can be obtained from port.capabilities(). 
        
        The I2C speed configuration will not be included in the port configuration file (.xpc). When you load a port configuration to a port, the transceiver I2C access speed will be reset to default.
        """

        self.temperature = PX_TEMPERATURE(conn, module_id, port_id)
        """Transceiver temperature in Celsius.

        Temperature value before the decimal digit, and 1/256th of a degree Celsius after the decimal digit.
        """

        self.laser_power = LaserPower(conn, module_id, port_id)
        """Laser power status.
        """

        self.cmis = Cmis(conn, module_id, port_id)
        """CMIS transceiver configuration and status
        """

    def access_rw(self, page_address: int, register_address: int) -> "PX_RW":
        """R/W access (4 bytes) to register interface by the transceiver.

        :param page_address: page address
        :type page_address: int
        :param register_address: register address
        :type register_address: int
        :return: transceiver register values
        :rtype: PX_RW
        """

        return PX_RW(
            self.__conn,
            self.__module_id,
            self.__port_id,
            page_address,
            register_address
        )

    def access_mii(self, register_address: int) -> "PX_MII":
        """R/W access (2 bytes) to the register interface supported by MII transceiver.

        :param register_address: register address
        :type register_address: int
        :return: register values
        :rtype: PX_MII
        """
        return PX_MII(
            self.__conn,
            self.__module_id,
            self.__port_id,
            register_address
        )

    def access_rw_seq(self, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ":
        """Sequential R/W a number of bytes to the register interface.

        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ
        """
        return PX_RW_SEQ(
            self.__conn,
            self.__module_id,
            self.__port_id,
            page_address,
            register_address,
            byte_count
        )
    
    def access_rw_seq_bank(self, bank_address: int, page_address: int, register_address: int, byte_count: int) -> "PX_RW_SEQ_BANK":
        """Sequential R/W a number of bytes to the register interface.

        :param bank_address: bank address (0-255)
        :type bank_address: int
        :param page_address: page address (0-255)
        :type page_address: int
        :param register_address: register address (0-255)
        :type register_address: int
        :param byte_count: the number of bytes to read/write
        :type byte_count: int
        :return: transceiver register values
        :rtype: PX_RW_SEQ_BANK
        """
        return PX_RW_SEQ_BANK(
            self.__conn,
            self.__module_id,
            self.__port_id,
            bank_address,
            page_address,
            register_address,
            byte_count
        )
