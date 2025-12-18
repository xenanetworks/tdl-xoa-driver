from typing import (
    TYPE_CHECKING,
    Tuple,
)
from typing import Self
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_ALARMS_ERRORS,
    PP_TXLANECONFIG,
    PP_TXLANEINJECT,
    PP_TXPRBSCONFIG,
    PP_TXERRORRATE,
    PP_TXINJECTONE,
    PP_RXTOTALSTATS,
    PP_RXFECSTATS,
    PP_RXLANELOCK,
    PP_RXLANESTATUS,
    PP_RXLANEERRORS,
    PP_RXPRBSSTATUS,
    PP_RXCLEAR,
    PP_RXLASERPOWER,
    PP_TXLASERPOWER,
    PP_EYEMEASURE,
    PP_EYERESOLUTION,
    PP_EYEREAD,
    PP_EYEINFO,
    PP_PHYTXEQ,
    PP_PHYRETUNE,
    PP_PHYAUTOTUNE,
    PP_EYEBER,
    PP_PHYAUTONEG,
    # PP_FECMODE, # moved to all genuine ports
    PP_EYEDWELLBITS,
    PP_PHYSIGNALSTATUS,
    PP_PRBSTYPE,
    PP_PHYSETTINGS,
    PP_PHYRXEQ,
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