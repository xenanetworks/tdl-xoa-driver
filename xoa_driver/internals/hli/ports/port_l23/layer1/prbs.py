from typing import (
    TYPE_CHECKING,
    Tuple,
)
from typing import Self
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_TXPRBSCONFIG,
    PP_RXPRBSSTATUS,
    PP_PRBSTYPE,
)
from xoa_driver import enums

class PrbsConfig:
    """L23 high-speed port PRBS configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.type = PP_PRBSTYPE(conn, module_id, port_id)
        """PRBS type used when in PRBS mode.

        :type: PP_PRBSTYPE
        """

class Prbs:
    """L23 high-speed port SerDes PRBS configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.control = PP_TXPRBSCONFIG(conn, module_id, port_id, serdes_xindex)
        """TX PRBS configuration of a SerDes.

        :type: PP_TXPRBSCONFIG
        """

        self.status = PP_RXPRBSSTATUS(conn, module_id, port_id, serdes_xindex)
        """RX PRBS status on a SerDes

        :type: PP_RXPRBSSTATUS
        """