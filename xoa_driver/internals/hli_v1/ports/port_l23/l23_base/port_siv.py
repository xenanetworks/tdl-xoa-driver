from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums


class LokiEyeDiagram:
    """L23 high-speed port SerDes eye diagram."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.__conn = conn
        self.__module_id = module_id
        self.__port_id = port_id
        self.__serdes_index = serdes_xindex
        self.measure = PP_EYEMEASURE(conn, module_id, port_id, serdes_xindex)
        """BER eye measurement.

        :type: PP_EYEMEASURE
        """

        self.resolution = PP_EYERESOLUTION(conn, module_id, port_id, serdes_xindex)
        """Resolution for BER eye measurement.

        :type: PP_EYERESOLUTION
        """

        self.info = PP_EYEINFO(conn, module_id, port_id, serdes_xindex)
        """Information of BER eye measurement.

        :type: PP_EYEINFO
        """

        self.ber = PP_EYEBER(conn, module_id, port_id, serdes_xindex)
        """BER estimation of an eye diagram.

        :type: PP_EYEBER
        """

        self.dwell_bits = PP_EYEDWELLBITS(conn, module_id, port_id, serdes_xindex)
        """Dwell bits for an eye capture.

        :type: PP_EYEDWELLBITS
        """

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> Self:
        resolution = await self.resolution.get()
        self.read_column = tuple(
            PP_EYEREAD(
                self.__conn,
                self.__module_id,
                self.__port_id,
                self.__serdes_index,
                _colum_xindex=x
            )
            for x in range(resolution.x_resolution)
        )
        return self


class FreyaSIV:
    """Freya Signal Integrity View"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.control = PL1_CTRL(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Control SIV scan. (only for Freya)

        :type: PL1_CTRL
        """

        self.data = PL1_GET_DATA(conn, module_id, port_id, serdes_xindex, enums.Layer1Control.SAMPLED_SIGNAL_INTEGRITY_SCAN)
        """Get SIV scan data. (only for Freya)

        :type: PL1_GET_DATA
        """
