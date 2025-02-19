from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_AUTONEG,
    PP_AUTONEGSTATUS,
    PP_LINKTRAIN,
    PP_LINKTRAINSTATUS,
)


class AutoNeg:
    """L23 high-speed port PCS/PMA auto-negotiation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.settings = PP_AUTONEG(conn, module_id, port_id)
        """Auto-negotiation settings of the PHY.
        Representation of PP_AUTONEG
        """

        self.status = PP_AUTONEGSTATUS(conn, module_id, port_id)
        """Status of auto-negotiation settings of the PHY.
        Representation of PP_AUTONEGSTATUS
        """


class LinkTrain:
    """L23 high-speed port PCS/PMA link training"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.settings = PP_LINKTRAIN(conn, *port.kind)
        """Link training settings.
        Representation of PP_LINKTRAIN
        """

        self.per_lane_status: Tuple[PP_LINKTRAINSTATUS, ...] = tuple(
            PP_LINKTRAINSTATUS(conn, *port.kind, _serdes_xindex=idx)
            for idx in range(port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because virtual_lanes are created before awaiting the port
        """Link training status.
        Representation of PP_LINKTRAINSTATUS
        """


class PcsPma:
    """L23 high-speed port PCS/PMA settings"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.auto_neg = AutoNeg(conn, *port.kind)
        """PCS/PMA auto-negotiation settings"""

        self.link_training = LinkTrain(conn, port)
        """PCS/PMA link training settings"""


# Temporary ports are not supporting LinkTrain, in future release of xenaserver it will be the same as regular PcsPma
class PcsPmaL1:
    """L23 high-speed port PCS/PMA settings"""

    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.auto_neg = AutoNeg(conn, *port.kind)
        """PCS/PMA auto-negotiation settings"""
