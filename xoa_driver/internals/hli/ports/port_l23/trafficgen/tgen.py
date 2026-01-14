import functools
import typing
from xoa_driver.internals.commands import (
    P_CAPABILITIES,
    P_SPEED,
    P_SPEEDREDUCTION,
    P_INTERFRAMEGAP,
    P_MACADDRESS,
    P_IPADDRESS,
    P_ARPREPLY,
    P_PINGREPLY,
    P_PAUSE,
    P_RANDOMSEED,
    P_LOOPBACK,
    P_TRAFFIC,
    # P_CAPTURE,
    P_XMITONE,
    P_LATENCYOFFSET,
    P_LATENCYMODE,
    P_AUTOTRAIN,
    P_MIXWEIGHTS,
    P_TRAFFICERR,
    P_GAPMONITOR,
    P_CHECKSUM,
    P_MIXLENGTH,
    P_ARPRXTABLE,
    P_NDPRXTABLE,
    P_MULTICAST,
    P_MULTICASTEXT,
    P_MCSRCLIST,
    P_MULTICASTHDR,
    P_TXMODE,
    P_RATEFRACTION,
    P_RATEPPS,
    P_RATEL2BPS,
    P_PAYLOADMODE,
    P_TXENABLE,
    P_MAXHEADERLENGTH,
    P_TXTIMELIMIT,
    P_TXTIME,
    P_XMITONETIME,
    P_IPV6ADDRESS,
    P_ARPV6REPLY,
    P_PINGV6REPLY,
    P_ERRORS,
    P_TXPREPARE,
    P_TXDELAY,
    P_TPLDMODE,
    P_TXPACKETLIMIT,
    P_PFCENABLE,
    P_TXBURSTPERIOD,
    P_CAPABILITIES_EXT,
    P_IGMPV3_GROUP_RECORD_BUNDLE,
    P_USED_TPLDID,
)
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.hli.ports import base_port
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.hli.indices.length_term import LengthTermIdx
from xoa_driver.internals.hli.indices.match_term import MatchTermIdx

from .capture import PortCapture

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]


class TxSinglePacket:
    """L23 port single-packet transmission"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.send = P_XMITONE(conn, module_id, port_id)
        """Send one packet from the L23 port without a stream config.

        :type: P_XMITONE
        """

        self.time = P_XMITONETIME(conn, module_id, port_id)
        """The time at which the latest packet was transmitted using the P_XMITONE` command.

        :type: P_XMITONETIME
        """


class TxConfiguration:
    """L23 port TX configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_TXMODE(conn, module_id, port_id)
        """L23 port TX mode.

        :type: P_TXMODE
        """

        self.enable = P_TXENABLE(conn, module_id, port_id)
        """Enabling L23 port TX.

        :type: P_TXENABLE
        """

        self.time_limit = P_TXTIMELIMIT(conn, module_id, port_id)
        """L23 port TX time limit.

        :type: P_TXTIMELIMIT
        """

        self.time = P_TXTIME(conn, module_id, port_id)
        """L23 port TX time.

        :type: P_TXTIME
        """

        self.prepare = P_TXPREPARE(conn, module_id, port_id)
        """Prepare L23 port for transmission.

        :type: P_TXPREPARE
        """

        self.delay = P_TXDELAY(conn, module_id, port_id)
        """L23 port TX delay.

        :type: P_TXDELAY
        """

        self.packet_limit = P_TXPACKETLIMIT(conn, module_id, port_id)
        """L23 port TX packet limit

        :type: P_TXPACKETLIMIT
        """

        self.burst_period = P_TXBURSTPERIOD(conn, module_id, port_id)
        """L23 port TX burst period.

        :type: P_TXBURSTPERIOD
        """


class TxRate:
    """L23 port TX rate"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.fraction = P_RATEFRACTION(conn, module_id, port_id)
        """L23 port rate in ppm.

        :type: P_RATEFRACTION
        """

        self.pps = P_RATEPPS(conn, module_id, port_id)
        """L23 port rate in packets per second.

        :type: P_RATEPPS
        """

        self.l2_bps = P_RATEL2BPS(conn, module_id, port_id)
        """L23 port rate in L2 bits per second.

        :type: P_RATEL2BPS
        """


class MacControl:
    """MAC control configuration
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.address = P_MACADDRESS(conn, module_id, port_id)
        """MAC address configuration. This attribute allows the user to configure the MAC address for the port.

        :type: P_MACADDRESS
        """

        self.autotrain = P_AUTOTRAIN(conn, module_id, port_id)
        """Interval between MAC auto training packets. This attribute allows the user to configure the interval at which MAC auto training packets are sent. Auto training packets are used to optimize the performance of the MAC layer and to ensure proper communication between devices.

        :type: P_AUTOTRAIN
        """


class Multicast:
    """L23 port multicast configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_MULTICAST(conn, module_id, port_id)
        """L23 port multicast mode.

        :type: P_MULTICAST
        """

        self.mode_extended = P_MULTICASTEXT(conn, module_id, port_id)
        """L23 port multicast extended mode.

        :type: P_MULTICASTEXT
        """

        self.source_list = P_MCSRCLIST(conn, module_id, port_id)
        """L23 port multicast source list.

        :type: P_MCSRCLIST
        """

        self.header = P_MULTICASTHDR(conn, module_id, port_id)
        """L23 port multicast IGMP header.

        :type: P_MULTICASTHDR
        """

        self.igmpv3_group_record_bundle = P_IGMPV3_GROUP_RECORD_BUNDLE(conn, module_id, port_id)
        """Configure if a single membership report bundles multiple multicast group records to decrease the number of packets sent when using IGMPv3. This command returns <NOTVALID> when the IGMP version is not IGMPv3.

        :type: P_IGMPV3_GROUP_RECORD_BUNDLE
        """

class IPv4:
    """L23 port IPv4 configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPADDRESS(conn, module_id, port_id)
        """L23 port IPv4 address.

        :type: P_IPADDRESS
        """

        self.arp_reply = P_ARPREPLY(conn, module_id, port_id)
        """L23 port reply to ARP request.

        :type: P_ARPREPLY
        """

        self.ping_reply = P_PINGREPLY(conn, module_id, port_id)
        """L23 port reply to PING request.

        :type: P_PINGREPLY
        """


class IPv6:
    """L23 port IPv6 configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.address = P_IPV6ADDRESS(conn, module_id, port_id)
        """L23 port IPv6 address.

        :type: P_IPV6ADDRESS
        """

        self.arp_reply = P_ARPV6REPLY(conn, module_id, port_id)
        """L23 port reply to NDP Neighbor Solicitation.

        :type: P_ARPV6REPLY
        """

        self.ping_reply = P_PINGV6REPLY(conn, module_id, port_id)
        """L23 port reply to PINGv6 request.

        :type: P_PINGV6REPLY
        """

class NetConfig:
    """L23 port network interface configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mac = MacControl(conn, module_id, port_id)
        """L23 port MAC address and control.

        :type: P_IPV6ADDRESS
        """

        self.ipv4 = IPv4(conn, module_id, port_id)
        """L23 port IPv4 configuration.

        :type: IPv4
        """

        self.ipv6 = IPv6(conn, module_id, port_id)
        """L23 port IPv6 configuration.

        :type: IPv6
        """


class LatencyConfiguration:
    """L23 port latency configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.offset = P_LATENCYOFFSET(conn, module_id, port_id)
        """L23 port latency offset.

        :type: P_LATENCYOFFSET
        """

        self.mode = P_LATENCYMODE(conn, module_id, port_id)
        """L23 port latency measurement mode.

        :type: P_LATENCYMODE
        """


class Mix:
    """L23 port IMIX configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.weights = P_MIXWEIGHTS(conn, module_id, port_id)
        """L23 port IMIX weights

        :type: P_MIXWEIGHTS
        """

        self.lengths = tuple(
            P_MIXLENGTH(conn, module_id, port_id, idx)
            for idx in range(16)
        )  # TODO: need to add manager for handle specific indices only
        """L23 port IMIX lengths.

        :type: P_MIXLENGTH
        """


class Speed:
    """L23 port speed configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.current = P_SPEED(conn, module_id, port_id)
        """L23 port current speed in units of Mbps.

        :type: P_SPEED
        """

        self.reduction = P_SPEEDREDUCTION(conn, module_id, port_id)
        """L23 port speed reduction in ppm.

        :type: P_SPEEDREDUCTION
        """


class Traffic:
    """L23 port traffic generation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.state = P_TRAFFIC(conn, module_id, port_id)
        """L23 port traffic status and action.

        :type: P_TRAFFIC
        """

        self.error = P_TRAFFICERR(conn, module_id, port_id)
        """L23 port traffic error.

        :type: P_TRAFFICERR
        """
