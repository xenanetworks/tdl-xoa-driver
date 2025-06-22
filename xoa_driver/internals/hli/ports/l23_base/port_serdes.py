from typing import (
    TYPE_CHECKING,
    Tuple,
    Self,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver import enums

from .port_prbs import PRBSSerdes
from .port_pma import PMASerdes
from .port_eq import SerdesEQ
from .port_anlt import FreyaLinkTrainingSerdes, ThorLinkTrainingSerdes
from .port_siv import FreyaSIV, LokiEyeDiagram

class SerdesLane:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = PRBSSerdes(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: PRBSSerdes
        """
        
        self.pma = PMASerdes(conn, module_id, port_id, serdes_xindex)
        """Freya PMA

        :type: PMASerdes
        """

        self.eq = SerdesEQ(conn, module_id, port_id, serdes_xindex)
        """Freya medium

        :type: SerdesEQ
        """

        self.lt = FreyaLinkTrainingSerdes(conn, module_id, port_id, serdes_xindex)
        """Freya Link Training on serdes level

        :type: FreyaLinkTrainingSerdes
        """

        self.lt_thor = ThorLinkTrainingSerdes(conn, module_id, port_id, serdes_xindex)
        """Thor Link Training on serdes level

        :type: ThorLinkTrainingSerdes
        """

        self.eye_loki = LokiEyeDiagram(conn, module_id, port_id, serdes_xindex)
        """Eye diagram (Loki only)

        :type: LokiEyeDiagram
        """

        self.siv = FreyaSIV(conn, module_id, port_id, serdes_xindex)
        """Signal Integrity View (Freya only)

        :type: FreyaSIV
        """

    def __await__(self):
        return self._setup().__await__()

    async def _setup(self) -> Self:
        await self.eye_loki
        return self
