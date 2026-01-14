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

from ..trafficgen.capture import PortCapture
from ..trafficgen.tgen import *

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]


class BasePortL23(base_port.BasePort[ports_state.PortL23LocalState]):
    """L23 port layout which is relevant to all L23 ports."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """L23 Port capabilities

        :type: P_CAPABILITIES
        """

        self.capabilities_ext = P_CAPABILITIES_EXT(conn, module_id, port_id)
        """L23 port capabilities ext.

        :type: P_CAPABILITIES_EXT
        """

        self.pause = P_PAUSE(conn, module_id, port_id)
        """L23 port response to Ethernet PAUSE frames.

        :type: P_PAUSE
        """

        self.loopback = P_LOOPBACK(conn, module_id, port_id)
        """L23 port loopback mode.

        :type: P_LOOPBACK
        """

        self.errors_count = P_ERRORS(conn, module_id, port_id)
        """L23 port errors.

        :type: P_ERRORS
        """

        self.interframe_gap = P_INTERFRAMEGAP(conn, module_id, port_id)
        """L23 port interframe gap.

        :type: P_INTERFRAMEGAP
        """

        self.max_header_length = P_MAXHEADERLENGTH(conn, module_id, port_id)
        """L23 port maximum header length.

        :type: P_MAXHEADERLENGTH
        """

        self.tpld_mode = P_TPLDMODE(conn, module_id, port_id)
        """L23 port test payload mode.

        :type: P_TPLDMODE
        """

        self.pfc_enable = P_PFCENABLE(conn, module_id, port_id)
        """L23 port Ethernet Priority Flow Control (PFC).

        :type: P_PFCENABLE
        """

        self.random_seed = P_RANDOMSEED(conn, module_id, port_id)
        """L23 port seed value.

        :type: P_RANDOMSEED
        """

        self.payload_mode = P_PAYLOADMODE(conn, module_id, port_id)
        """L23 port payload mode.

        :type: P_PAYLOADMODE
        """

        self.gap_monitor = P_GAPMONITOR(conn, module_id, port_id)
        """L23 port gap monitor.

        :type: P_GAPMONITOR
        """

        self.checksum = P_CHECKSUM(conn, module_id, port_id)
        """L23 port extra payload integrity checksum.

        :type: P_CHECKSUM
        """

        self.arp_rx_table = P_ARPRXTABLE(conn, module_id, port_id)
        """L23 port ARP table.

        :type: P_ARPRXTABLE
        """

        self.ndp_rx_table = P_NDPRXTABLE(conn, module_id, port_id)
        """L23 port NDP table.

        :type: P_NDPRXTABLE
        """

        self.capturer = PortCapture(conn, module_id, port_id)
        """L23 port capturer configuration.

        :type: PortCapture
        """

        self.speed = Speed(conn, module_id, port_id)
        """L23 port speed configuration.

        :type: Speed
        """

        self.traffic = Traffic(conn, module_id, port_id)
        """L23 port traffic configuration.

        :type: Traffic
        """

        self.mix = Mix(conn, module_id, port_id)
        """L23 port IMIX configuration.

        :type: Mix
        """

        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        """L23 port latency configuration.

        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        :type:
        """

        self.rate = TxRate(conn, module_id, port_id)
        """L23 port rate.

        :type: Rate
        """

        self.tx_config = TxConfiguration(conn, module_id, port_id)
        """L23 port TX configuration.

        :type: TxConfiguration
        """

        self.tx_single_pkt = TxSinglePacket(conn, module_id, port_id)
        """L23 port single-packet TX configuration.

        :type: TxSinglePacket
        """

        self.multicast = Multicast(conn, module_id, port_id)
        """L23 port multicast configuration.

        :type: Multicast
        """

        self.net_config = NetConfig(conn, module_id, port_id)
        """L23 port network configuration, including MAC and IP addresses.

        :type: NetConfig
        """


        self.local_states = ports_state.PortL23LocalState()
        """L23 port local states.

        :type: PortL23LocalState
        """

        self.length_terms: LengthTermIndices = idx_mgr.IndexManager(
            conn,
            LengthTermIdx,
            module_id,
            port_id
        )
        """L23 port's length term index manager.

        :type: LengthTermIndices
        """

        self.match_terms: MatchTermIndices = idx_mgr.IndexManager(
            conn,
            MatchTermIdx,
            module_id,
            port_id
        )
        """L23 port's match term index manager.

        :type: MatchTermIndices
        """

        self.used_tpld_ids = P_USED_TPLDID(conn, module_id, port_id)
        """TG port's used TPLD IDs.

        :type: P_USED_TPLDID
        """

    on_speed_change = functools.partialmethod(utils.on_event, P_SPEED)
    """Register a callback to the event that the port's speed changes."""

    on_traffic_change = functools.partialmethod(utils.on_event, P_TRAFFIC)
    """Register a callback to the event that the port's traffic status changes."""
