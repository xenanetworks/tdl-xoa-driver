import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

from xoa_driver.internals.commands import (
    M_MEDIA,
    M_STATUS,
    M_UPGRADE,
    M_UPGRADEPROGRESS,
    M_TIMESYNC,
    M_CFPTYPE,
    M_CFPCONFIGEXT,
    M_COMMENT,
    # M_TIMEADJUSTMENT,
    M_CAPABILITIES,
    M_MEDIASUPPORT,
    M_FPGAREIMAGE,
    M_MULTIUSER,
    M_CLOCKPPB,
    M_SMAINPUT,
    M_SMAOUTPUT,
    M_SMASTATUS,
    M_NAME,
    M_REVISION,
    M_CLOCKSYNCSTATUS,
    M_TXCLOCKSOURCE_NEW,
    M_TXCLOCKSTATUS_NEW,
    M_TXCLOCKFILTER_NEW,
    M_UPGRADEPAR,
    M_VERSIONSTR,
    M_RECONFIG_STATUS,
)

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from ... import __interfaces as m_itf


class MUpgrade:
    """Test module upgrade"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.start = M_UPGRADE(conn, module_id)
        """Start the upgrade progress of the test module.

        :type: M_UPGRADE
        """

        self.progress = M_UPGRADEPROGRESS(conn, module_id)
        """Upgrade progress status of the test module.

        :type: M_UPGRADEPROGRESS
        """

        self.reload_image = M_FPGAREIMAGE(conn, module_id)
        """Reload the FPGA image of the test module.

        :type: M_FPGAREIMAGE
        """
        self.start_parallel = M_UPGRADEPAR(conn, module_id)
        """
        Start the parallel upgrade progress of the test module.

        :type: M_UPGRADEPAR
        """