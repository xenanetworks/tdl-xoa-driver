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


class TXClock:
    """Advanced timing clock"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TXCLOCKSOURCE_NEW(conn, module_id)
        """The source that drives the TX clock rate of the ports on the test module.

        :type: M_TXCLOCKSOURCE_NEW
        """

        self.status = M_TXCLOCKSTATUS_NEW(conn, module_id)
        """TX clock status of the test module.

        :type: M_TXCLOCKSTATUS_NEW
        """

        self.filter = M_TXCLOCKFILTER_NEW(conn, module_id)
        """Loop bandwidth on the TX clock filter of the test module.

        :type: M_TXCLOCKFILTER_NEW
        """


class SMA:
    """SMA connector"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.input = M_SMAINPUT(conn, module_id)
        """SMA input of the test module.

        :type: M_SMAINPUT
        """

        self.output = M_SMAOUTPUT(conn, module_id)
        """SMA output of the test module.

        :type: M_SMAOUTPUT
        """

        self.status = M_SMASTATUS(conn, module_id)
        """SMA input status of the test module.

        :type: M_SMASTATUS
        """


class AdvancedTiming:
    """Advanced Timing config and control"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.clock_tx = TXClock(conn, module_id)
        """Advanced timing clock config and status

        :type: TXClock
        """

        self.sma = SMA(conn, module_id)
        """SMA connector

        :type: SMA
        """



class MTiming:
    """Test module timing and clock configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int) -> None:
        self.source = M_TIMESYNC(conn, module_id)
        """Timing source of the test module.

        :type: M_TIMESYNC
        """

        self.clock_local_adjust = M_CLOCKPPB(conn, module_id)
        """Time adjustment controlling of the local clock of the test module, which drives the TX rate of the test ports.

        :type: M_CLOCKPPB
        """

        self.clock_sync_status = M_CLOCKSYNCSTATUS(conn, module_id)
        """Test module's clock sync status.

        :type: M_CLOCKSYNCSTATUS
        """