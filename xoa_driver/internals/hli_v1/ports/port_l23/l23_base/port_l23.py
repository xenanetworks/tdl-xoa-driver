import functools
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import *
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.hli_v1.ports import base_port
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.hli_v1.indices.streams.genuine_stream import GenuineStreamIdx
from xoa_driver.internals.hli_v1.indices.filter.genuine_filter import GenuineFilterIdx
from xoa_driver.internals.hli_v1.indices.port_dataset import PortDatasetIdx
from xoa_driver.internals.state_storage import ports_state
from xoa_driver.internals.hli_v1.indices.length_term import LengthTermIdx
from xoa_driver.internals.hli_v1.indices.match_term import MatchTermIdx
from xoa_driver.internals.hli_v1.indices.macsecscs.genuine_macsecsc import GenuineMacSecTxScIdx, GenuineMacSecRxScIdx

from .port_capture import PortCapture
from .port_statistics_rx import PortReceptionStatistics
from .port_statistics_tx import PortTransmissionStatistics
from .port_layer1 import PortLayer1

LengthTermIndices = idx_mgr.IndexManager[LengthTermIdx]
MatchTermIndices = idx_mgr.IndexManager[MatchTermIdx]
StreamIndices = idx_mgr.IndexManager[GenuineStreamIdx]
FilterIndices = idx_mgr.IndexManager[GenuineFilterIdx]
PortDatasetIndices = idx_mgr.IndexManager[PortDatasetIdx]
MacSecTxScIndices = idx_mgr.IndexManager[GenuineMacSecTxScIdx]
MacSecRxScIndices = idx_mgr.IndexManager[GenuineMacSecRxScIdx]

from xoa_driver.internals.hli_v1.ports.port_l23.l23_base.port_layer1 import PortLayer1

class TxSinglePacket:
    """L23 port single-packet transmission"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.send = P_XMITONE(conn, module_id, port_id)
        """Send one packet from the L23 port without a stream config.

        :type: P_XMITONE
        """

        self.time = P_XMITONETIME(conn, module_id, port_id)
        """The time at which the latest packet was transmitted using the P_XMITONE command.

        :type: P_XMITONETIME
        """


class TxControl:
    """L23 port TX control"""

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

        self.elapsed_time = P_TXTIME(conn, module_id, port_id)
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

        self.single_pkt = TxSinglePacket(conn, module_id, port_id)
        """L23 port single-packet TX configuration.

        :type: TxSinglePacket
        """


class TrafficRate:
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


class IMix:
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


class FlowControl:
    """L23 port flow control config"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.pause = P_PAUSE(conn, module_id, port_id)
        """L23 port response to Ethernet PAUSE frames.

        :type: P_PAUSE
        """

        self.pfc = P_PFCENABLE(conn, module_id, port_id)
        """L23 port Ethernet Priority Flow Control (PFC).

        :type: P_PFCENABLE
        """



class Speed:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.selection = P_SPEEDSELECTION(conn, module_id, port_id)
        """L23 port speed mode selection.

        :type: P_SPEEDSELECTION
        """

        self.supported = P_SPEEDS_SUPPORTED(conn, module_id, port_id)
        """L23 port's supported speed modes.

        :type: P_SPEEDS_SUPPORTED
        """

        self.current = P_SPEED(conn, module_id, port_id)
        """L23 port current speed in units of Mbps.

        :type: P_SPEED
        """

        self.reduction = P_SPEEDREDUCTION(conn, module_id, port_id)
        """L23 port speed reduction in ppm.

        :type: P_SPEEDREDUCTION
        """


class UnavailableTime:
    """UnAvailable Time"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = P_UAT_MODE(conn, module_id, port_id)
        """L23 port's Unavailable Time mode.

        :type: P_UAT_MODE
        """

        self.frame_loss_ratio = P_UAT_FLR(conn, module_id, port_id)
        """L23 port's Frame Loss Ratio for UAT.

        :type: P_UAT_FLR
        """


class Statistics:
    """L23 port statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.rx = PortReceptionStatistics(conn, module_id, port_id)
        """L23 port's RX statistics."""

        self.tx = PortTransmissionStatistics(conn, module_id, port_id)
        """L23 port's TX statistics."""


class MacControl:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.address = P_MACADDRESS(conn, module_id, port_id)
        """L23 port MAC address.

        :type: P_MACADDRESS
        """

        self.autotrain = P_AUTOTRAIN(conn, module_id, port_id)
        """L23 port interval between auto training packets.

        :type: P_AUTOTRAIN
        """


class EnergyEfficientEthernet:
    """L23 port low power mode."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.enable = P_LPENABLE(conn, module_id, port_id)
        """Energy Efficiency Ethernet.
        
        :type: P_LPENABLE
        """

        self.mode = P_LPTXMODE(conn, module_id, port_id)
        """Low power TX mode.
        
        :type: P_LPTXMODE
        """
        self.status = P_LPSTATUS(conn, module_id, port_id)
        """Low power status.
        
        :type: P_LPSTATUS
        """

        self.partner_capabilities = P_LPPARTNERAUTONEG(conn, module_id, port_id)
        """EEE capabilities advertised during auto-negotiation by the far side.
        
        :type: P_LPPARTNERAUTONEG
        """

        self.snr_margin = P_LPSNRMARGIN(conn, module_id, port_id)
        """SNR margin on the four link channels by the PHY.
        
        :type: P_LPSNRMARGIN
        """

        self.rx_power = P_LPRXPOWER(conn, module_id, port_id)
        """RX power recorded during training for the four channels.
        
        :type: P_LPRXPOWER
        """

        self.capabilities = P_LPSUPPORT(conn, module_id, port_id)
        """EEE capabilities of the port.
        
        :type: P_LPSUPPORT
        """


class Runt:
    """Runt settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_length = P_TXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's TX runt length.
        
        :type: P_TXRUNTLENGTH
        """

        self.rx_length = P_RXRUNTLENGTH(conn, module_id, port_id)
        """L23 port's RX runt length.
        
        :type: P_RXRUNTLENGTH
        """

        self.has_length_errors = P_RXRUNTLEN_ERRS(conn, module_id, port_id)
        """L23 port's RX runt length errors..
        
        :type: P_RXRUNTLEN_ERRS
        """


class Preamble:
    """Preamble settings."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx_remove = P_TXPREAMBLE_REMOVE(conn, module_id, port_id)
        """L23 port's removal of preamble from outgoing packets.
        
        :type: P_TXPREAMBLE_REMOVE
        """

        self.rx_insert = P_RXPREAMBLE_INSERT(conn, module_id, port_id)
        """L23 port's insertion of preamble into incoming packets.
        
        :type: P_RXPREAMBLE_INSERT
        """


class PortL23(base_port.BasePort[ports_state.PortL23LocalState]):
    """L23 port basic configuration."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)

        self._local_states = ports_state.PortL23LocalState()

        self.streams: StreamIndices = idx_mgr.IndexManager(
            conn,
            GenuineStreamIdx,
            module_id,
            port_id
        )
        """L23 port stream index manager.

        :type: StreamIndices
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

        self.filters: FilterIndices = idx_mgr.IndexManager(
            conn,
            GenuineFilterIdx,
            module_id,
            port_id
        )
        """L23 port filter index manager.

        :type: FilterIndices
        """

        self.datasets: PortDatasetIndices = idx_mgr.IndexManager(
            conn,
            PortDatasetIdx,
            module_id,
            port_id
        )
        """L23 port histogram index manager.

        :type: PortDatasetIndices
        """

        self.macsec_txscs: MacSecTxScIndices = idx_mgr.IndexManager(
            conn,
            GenuineMacSecTxScIdx,
            module_id,
            port_id
        )
        """L23 port MACSec TX SC index manager.

        :type: MacSecTxScIndices
        """

        self.macsec_rxscs: MacSecRxScIndices = idx_mgr.IndexManager(
            conn,
            GenuineMacSecRxScIdx,
            module_id,
            port_id
        )
        """L23 port MACSec RX SC index manager.

        :type: MacSecRxScIndices
        """

        self.capabilities = P_CAPABILITIES(conn, module_id, port_id)
        """L23 port capabilities.

        :type: P_CAPABILITIES
        """

        self.capabilities_ext = P_CAPABILITIES_EXT(conn, module_id, port_id)
        """L23 port capabilities ext.

        :type: P_CAPABILITIES_EXT
        """

        

        self.loopback = P_LOOPBACK(conn, module_id, port_id)
        """L23 port loopback mode.

        :type: P_LOOPBACK
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

        self.imix = IMix(conn, module_id, port_id)
        """L23 port IMIX configuration.

        :type: Mix
        """

        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        """L23 port latency configuration.

        self.latency_config = LatencyConfiguration(conn, module_id, port_id)
        :type:
        """

        self.rate = TrafficRate(conn, module_id, port_id)
        """L23 port rate.

        :type: Rate
        """

        self.tx_control = TxControl(conn, module_id, port_id)
        """L23 port TX control.

        :type: TxControl
        """

        self.multicast = Multicast(conn, module_id, port_id)
        """L23 port multicast configuration.

        :type: Multicast
        """

        self.mac = MacControl(conn, module_id, port_id)
        """L23 port MAC configuration.
        
        :type: MacControl
        """

        self.ipv4 = IPv4(conn, module_id, port_id)
        """L23 port IPv4 address configuration.
        """

        self.ipv6 = IPv6(conn, module_id, port_id)
        """L23 port IPv6 address configuration.
        """

        self.local_states = ports_state.PortL23LocalState()
        """L23 port local states.

        :type: PortL23LocalState
        """

        

        self.used_tpld_ids = P_USED_TPLDID(conn, module_id, port_id)
        """TG port's used TPLD IDs.

        :type: P_USED_TPLDID
        """

        self.flash = P_FLASH(conn, module_id, port_id)
        """L23 port flashes.

        :type: P_FLASH
        """

        self.status = P_STATUS(conn, module_id, port_id)
        """L23 port's received optical signal level'.

        :type: P_STATUS
        """

        self.fec_mode = PP_FECMODE(conn, module_id, port_id)
        """L23 port FEC mode.

        :type: PP_FECMODE
        """

        self.speed = Speed(conn, module_id, port_id)
        """L23 port speed configuration.

        :type: GenuineSpeed
        """

        self.uat = UnavailableTime(conn, module_id, port_id)
        """L23 port UnAvailable Time configuration.

        :type: UnAvailableTime
        """

        

        self.statistics = Statistics(conn, module_id, port_id)
        """L23 port statistics.

        :type: PortStatistics
        """

        self.macsec_rx = P_MACSEC_RX_ENABLE(conn, module_id, port_id)
        """L23 port MACSec RX enable.

        :type: P_MACSEC_RX_ENABLE        
        """

        self.mdix_mode = P_MDIXMODE(conn, module_id, port_id)
        """L23 port's MDI/MDIX mode.
        
        :type: P_MDIXMODE
        """

        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """L23 port's auto-negotiation selection.
        
        :type: P_AUTONEGSELECTION
        """

        self.eee = EnergyEfficientEthernet(conn, module_id, port_id)
        """L23 port Low Power mode settings.
        
        :type: LowPowerMode
        """

        self.runt = Runt(conn, module_id, port_id)
        """Runt settings."""

        self.preamble = Preamble(conn, module_id, port_id)
        """Preamble settiNgs."""

        self.dynamic = P_DYNAMIC(conn, module_id, port_id)
        """L23 port's dynamic traffic change.
        
        :type: P_DYNAMIC
        """

        self.brr_mode = P_BRRMODE(conn, module_id, port_id)
        """BRR mode.
        
        :type: P_BRRMODE
        """
        self.brr_status = P_BRRSTATUS(conn, module_id, port_id)
        """Actual BRR status.
        
        :type: P_BRRSTATUS
        """
        
        

    @property
    def info(self) -> ports_state.PortL23LocalState:
        return self._local_states

    async def _setup(self):
        await self._local_states.initiate(self)
        self._local_states.register_subscriptions(self)
        self.l1 = PortLayer1(self._conn, self)
        return self

    on_speed_change = functools.partialmethod(utils.on_event, P_SPEED)
    """Register a callback to the event that the port's speed changes."""

    on_traffic_change = functools.partialmethod(utils.on_event, P_TRAFFIC)
    """Register a callback to the event that the port's traffic status changes."""

    on_speed_selection_change = functools.partialmethod(utils.on_event, P_SPEEDSELECTION)
    """Register a callback to the event that the port's speed mode changes."""

    on_macsec_rx_enable_change = functools.partialmethod(utils.on_event, P_MACSEC_RX_ENABLE)
    """Register a callback to the event that the port MACsec RX enable status changes."""

    on_dynamic_change = functools.partialmethod(utils.on_event, P_DYNAMIC)
    """Register a callback to the event that the port's dynamic traffic setting changes."""
