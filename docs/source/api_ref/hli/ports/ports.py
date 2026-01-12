import asyncio
from xoa_driver import testers, modules, ports, enums, utils, misc
from xoa_driver.hlfuncs import * 
from xoa_driver.misc import Hex, ArpEntry, NdpEntry
import ipaddress

async def my_awesome_func(stop_event: asyncio.Event):

    # [testers]
    """Connect Chassis"""
    # Create a tester object representing a chassis 
    # and connect to the chassis at IP address 10.10.10.
    tester = await testers.L23Tester(
        host="10.10.10.10",
        username="my_name",
        password="xena",
        enable_logging=False)
    
    
    # [modules]
    """Get Module Object"""
    # Obtain a module object representing the module installed in slot 0.
    module = tester.modules.obtain(0)

    # [Check module type]
    if isinstance(module, modules.E100ChimeraModule):
        return

    # [ports]
    """Get Port Object"""
    # Obtain a port object representing port 0 on module.
    port = module.ports.obtain(0)


    # [Check port type]
    if isinstance(port, ports.PortChimera):
        return

    """RESERVATION"""
    """Port Reservation"""
    # Reserve or release the port.
    await port.reservation.set_release()
    await port.reservation.set_relinquish()
    await port.reservation.set_reserve()
    resp_obj = await port.reservation.get()

    
    """Port Reserved By"""
    # Get the current reservation status of the port.
    resp_obj = await port.reserved_by.get()


    """IDENTIFICATION"""
    """Port Description"""
    # A text description of the port.
    await port.comment.set(comment="description")
    resp_obj = await port.comment.get()


    # [Interface Name]
    # The interface name of the port.
    resp_obj = await port.interface.get()


    """CONTROL"""
    """Reset Port"""
    # Reset the port. This will clear the port configuration, statistics, and any ongoing traffic.
    await port.reset.set()


    """Flash Port LEDs"""
    # Make the port LED flash on and off with a 1-second interval.
    await port.flash.set_on()
    await port.flash.set_off()
    resp_obj = await port.flash.get()


    """TX CONTROL"""
    """Sync Status"""
    # Get the port synchronization status.
    resp_obj = await port.sync_status.get()


    """TX Output"""
    # Enable or disable the port transmitter.
    await port.tx_config.enable.set_on()
    await port.tx_config.enable.set_off()
    resp_obj = await port.tx_config.enable.get()


    """Tx Time Limit"""
    # Set or get the transmit time limit.
    await port.tx_config.time_limit.set(microseconds=1_000_000)
    resp_obj = await port.tx_config.time_limit.get()


    """Tx Packet Limit"""
    # Set or get the transmit packet limit.
    await port.tx_config.packet_limit.set(packet_count_limit=1_000_000)
    resp_obj = await port.tx_config.packet_limit.get()


    """Tx Time Elapsed"""
    # Get the elapsed transmit time.
    await port.tx_config.time.get()


    """Tx Delay"""
    # Set or get the transmit delay.
    await port.tx_config.delay.get()


    """Tx Prepare"""
    # Prepare the port for transmission.
    await port.tx_config.prepare.set()

    
    """Tx Start/Stop"""
    # Start or stop traffic on the port.
    await port.traffic.state.set_start()
    await port.traffic.state.set_stop()
    resp_obj = await port.traffic.state.get()


    """Traffic Error"""
    # Get the traffic error status.
    resp_obj = await port.traffic.error.get()


    """Transmit Manual Packet"""
    # Transmit a single manually specified packet.
    await port.tx_single_pkt.send.set(hex_data=Hex("00112233445566778899AABB080045000028000100004006B1E6C0A80001C0A80002"))


    """Transmit Manual Packet Time"""
    # Get the time taken to transmit a single manually specified packet.
    resp_obj = await port.tx_single_pkt.time.get()


    """Dynamic Traffic"""
    # Enable or disable dynamic traffic on the port.
    # When dynamic traffic is enabled, you can adjust traffic rate while the port is transmitting.
    await port.dynamic.set_off()
    await port.dynamic.set_on()
    resp_obj = await port.dynamic.get()


    """TX PROFILE"""
    """Rate Fraction"""
    # Set or get the transmit rate as a fraction of line rate in parts per million (ppm).
    await port.rate.fraction.set(port_rate_ppm=1_000_000)
    resp_obj = await port.rate.fraction.get()


    """Rate L2 Bits Per Second"""
    # Set or get the transmit rate in bits per second at Layer 2.
    await port.rate.l2_bps.set(port_rate_bps=1_000_000)
    resp_obj = await port.rate.l2_bps.get()


    """Rate Frames Per Second"""
    # Set or get the transmit rate in frames per second.
    await port.rate.pps.set(port_rate_pps=10_000)
    resp_obj = await port.rate.pps.get()


    """TX Mode"""
    # Set or get the transmit mode.
    await port.tx_config.mode.set_normal()
    await port.tx_config.mode.set_burst()
    await port.tx_config.mode.set_sequential()
    await port.tx_config.mode.set_strictuniform()
    resp_obj = await port.tx_config.mode.get()


    """Burst Period"""
    # Set or get the burst period in milliseconds.
    await port.tx_config.burst_period.set(burst_period=100)
    resp_obj = await port.tx_config.burst_period.get()



    """BASIC LAYER-1 CONTROL"""
    """Inter-frame Gap"""
    # Set or get the inter-frame gap minimum byte count.
    await port.interframe_gap.set(min_byte_count=20)
    resp_obj = await port.interframe_gap.get()


    """Speed Mode Selection"""
    # Set or get the speed mode selection.
    await port.speed.mode.selection.set_auto()
    await port.speed.mode.selection.set_f10m()
    await port.speed.mode.selection.set_f10m100m()
    await port.speed.mode.selection.set_f10mhdx()
    await port.speed.mode.selection.set_f100m()
    await port.speed.mode.selection.set_f100m1g()
    await port.speed.mode.selection.set_f100m1g10g()
    await port.speed.mode.selection.set_f100m1g2500m()
    await port.speed.mode.selection.set_f100mhdx()
    await port.speed.mode.selection.set_f1g()
    await port.speed.mode.selection.set_f2500m()
    await port.speed.mode.selection.set_f5g()
    await port.speed.mode.selection.set_f10g()
    await port.speed.mode.selection.set_f40g()
    await port.speed.mode.selection.set_f100g()
    resp_obj = await port.speed.mode.selection.get()


    """Supported Speed Modes"""
    resp_obj = await port.speed.mode.supported.get()


    """Current Speed"""
    resp_obj = await port.speed.current.get()


    """Speed Reduction"""
    await port.speed.reduction.set(ppm=100)
    resp_obj = await port.speed.reduction.get()


    """Optical Rx Power"""
    resp_obj = await port.status.get()


    """LAYER-2 CONTROL"""
    """MAC Address"""
    await port.net_config.mac_address.set(mac_address=Hex("000000000000"))
    resp_obj = await port.net_config.mac_address.get()


    """Auto MAC Training"""
    await port.autotrain.set(interval=1)
    resp_obj = await port.autotrain.get()


    """PAUSE and PFC"""
    await port.pause.set_on()
    await port.pause.set_off()
    resp_obj = await port.pause.get()

    await port.pfc_enable.set(
        cos_0=enums.OnOff.ON,
        cos_1=enums.OnOff.OFF,
        cos_2=enums.OnOff.ON,
        cos_3=enums.OnOff.OFF,
        cos_4=enums.OnOff.ON,
        cos_5=enums.OnOff.OFF,
        cos_6=enums.OnOff.ON,
        cos_7=enums.OnOff.OFF,
        )
    resp_obj = await port.pfc_enable.get()

    
    """Gap Monitor"""
    await port.gap_monitor.set(start=100, stop=10)
    resp_obj = await port.gap_monitor.get()


    """PAYLOAD CONFIGURATION"""
    """Checksum Offset"""
    await port.checksum.set(offset=14)
    resp_obj = await port.checksum.get()


    """Random Seed"""
    await port.random_seed.set(seed=1)
    resp_obj = await port.random_seed.get()


    """Maximum Header Length"""
    await port.max_header_length.set(max_header_length=56)
    resp_obj = await port.max_header_length.get()


    """IMIX Weights"""
    await port.mix.weights.set(
        weight_56_bytes=0,
        weight_60_bytes=0,
        weight_64_bytes=70,
        weight_70_bytes=15,
        weight_78_bytes=15,
        weight_92_bytes=0,
        weight_256_bytes=0,
        weight_496_bytes=0,
        weight_512_bytes=0,
        weight_570_bytes=0,
        weight_576_bytes=0,
        weight_594_bytes=0,
        weight_1438_bytes=0,
        weight_1518_bytes=0,
        weight_9216_bytes=0,
        weight_16360_bytes=0)
    resp_obj = await port.mix.weights.get()


    """IMIX Lengths"""
    await port.mix.lengths[0].set(frame_size=56)
    await port.mix.lengths[1].set(frame_size=60)
    await port.mix.lengths[14].set(frame_size=9216)
    await port.mix.lengths[15].set(frame_size=16360)

    resp_obj = await port.mix.lengths[0].get()
    resp_obj = await port.mix.lengths[1].get()
    resp_obj = await port.mix.lengths[14].get()
    resp_obj = await port.mix.lengths[15].get()


    """Payload Mode"""
    await port.payload_mode.set_normal()
    await port.payload_mode.set_extpl()
    await port.payload_mode.set_cdf()
    resp_obj = await port.payload_mode.get()


    """TPLD Mode"""
    await port.tpld_mode.set_normal()
    await port.tpld_mode.set_micro()
    resp_obj = await port.tpld_mode.get()


    """LOOPBACK"""
    """Loopback Modes"""
    await port.loop_back.set_none()
    await port.loop_back.set_l1rx2tx()
    await port.loop_back.set_l2rx2tx()
    await port.loop_back.set_l3rx2tx()
    await port.loop_back.set_port2port()
    await port.loop_back.set_txoff2rx()
    await port.loop_back.set_txon2rx()
    resp_obj = await port.loop_back.get()


    """LATENCY CONFIG"""
    """Latency Mode"""
    await port.latency_config.mode.set_first2first()
    await port.latency_config.mode.set_first2last()
    await port.latency_config.mode.set_last2first()
    await port.latency_config.mode.set_last2last()
    resp_obj = await port.latency_config.mode.get()


    """Latency Offset"""
    await port.latency_config.offset.set(offset=5)
    resp_obj = await port.latency_config.offset.get()


    """IPV4 CONFIGURATION"""
    """IPv4: Address"""
    await port.net_config.ipv4.address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.1.1"),
        wild=ipaddress.IPv4Address("0.0.0.0"))
    resp_obj = await port.net_config.ipv4.address.get()


    """IPv4: Reply to ARP"""
    await port.net_config.ipv4.arp_reply.set_on()
    await port.net_config.ipv4.arp_reply.set_off()
    resp_obj = await port.net_config.ipv4.arp_reply.get()


    """IPv4: Reply to Ping"""
    await port.net_config.ipv4.ping_reply.set_on()
    await port.net_config.ipv4.ping_reply.set_off()
    resp_obj = await port.net_config.ipv4.ping_reply.get()

    
    """IPV6 CONFIGURATION"""
    """IPv6: Address"""
    await port.net_config.ipv6.address.set(
        ipv6_address=ipaddress.IPv6Address("fc00::0002"),
        gateway=ipaddress.IPv6Address("fc00::0001"),
        subnet_prefix=7,
        wildcard_prefix=0
    )
    resp_obj = await port.net_config.ipv6.address.get()


    """IPv6: Reply to NDP"""
    await port.net_config.ipv6.arp_reply.set_on()
    await port.net_config.ipv6.arp_reply.set_off()
    resp_obj = await port.net_config.ipv6.arp_reply.get()


    """IPv6: Reply to IPv6 Ping"""
    await port.net_config.ipv6.ping_reply.set_on()
    await port.net_config.ipv6.ping_reply.set_off()
    resp_obj = await port.net_config.ipv6.ping_reply.get()


    """ARP/NDP TABLES"""
    """IPv4: ARP Table"""
    arp_entry = ArpEntry(
        ipv4_address=ipaddress.IPv4Address("12.12.12.12"), 
        prefix=24, 
        patched_mac=enums.OnOff.OFF,
        mac_address=Hex("FFEEDDCCBBAA"))
    await port.arp_rx_table.set(entries=[arp_entry])
    resp_obj = await port.arp_rx_table.get()


    """IPv6: NDP Table"""
    ndp_entry = NdpEntry(
        ipv6_address=ipaddress.IPv6Address("fc00::1234"), 
        prefix=64, 
        patched_mac=enums.OnOff.OFF,
        mac_address=Hex("AABBCCDDEEFF"))
    await port.ndp_rx_table.set(entries=[ndp_entry])
    resp_obj = await port.ndp_rx_table.get()


    """IPV4 MULTICAST CONFIGURATION"""
    """IPv4: Multicast"""
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.JOIN,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.LEAVE,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.OFF,
        second_count=10)
    await port.multicast.mode.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastOperation.ON,
        second_count=10)

    resp_obj = await port.multicast.mode.get()

    """IPv4: Multicast Advanced, IGMPv3"""
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.EXCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.INCLUDE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV3
    )


    """IPv4: Multicast Advanced, IGMPv2"""
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.JOIN,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.LEAVE_TO_ALL,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GENERAL_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.GROUP_QUERY,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.ON,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    await port.multicast.mode_extended.set(
        ipv4_multicast_addresses=[],
        operation=enums.MulticastExtOperation.OFF,
        second_count=10,
        igmp_version=enums.IGMPVersion.IGMPV2
    )
    resp_obj = await port.multicast.mode_extended.get()


    """IPv4: Multicast Source List"""
    await port.multicast.source_list.set(ipv4_addresses=[])
    resp_obj = await port.multicast.source_list.get()


    """IPv4: Multicast Header"""
    await port.multicast.header.set(header_count=1, header_format=enums.MulticastHeaderFormat.VLAN, tag=10, pcp=0, dei=enums.OnOff.OFF)
    await port.multicast.header.set(header_count=0, header_format=enums.MulticastHeaderFormat.NOHDR, tag=10, pcp=0, dei=enums.OnOff.OFF)
    resp_obj = await port.multicast.header.get()


    """UnAvailable Time (UAT) Mode"""
    # Only applicable in Xena1564 test suite. 
    # This API enables the UAT detection on the port in Xena1564 test suite.
    await port.uat.mode.set(mode=enums.OnOff.ON, delay=500)
    await port.uat.mode.set(mode=enums.OnOff.OFF, delay=500)
    resp = await port.uat.mode.get()


    """UAT Frame Loss Ratio"""
    # Only applicable in Xena1564 test suite. 
    # This API specifies the Frame Loss Ratio threshold used to classify a 
    # one-second interval as a Severely Errored Second (SES). 
    # In accordance with Xena1564, Unavailable Time (UAT) is declared after 
    # the occurrence of 10 consecutive SES intervals.
    resp = await port.uat.frame_loss_ratio.get()


    """UAT Status"""
    # Only applicable in Xena1564 test suite.
    # This API retrieves the current UAT status of the port.
    resp = await port.statistics.rx.uat.status.get()


    """UAT Time"""
    # Only applicable in Xena1564 test suite.
    # This API retrieves the total Unavailable Time (UAT) in seconds since the last reset.
    resp = await port.statistics.rx.uat.time.get()



    """PACKET CAPTURE"""
    """Capture Trigger Criteria"""
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FULL, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.ON, start_criteria_filter=0, stop_criteria=enums.StopTrigger.USERSTOP, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FCSERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FCSERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.PLDERR, start_criteria_filter=0, stop_criteria=enums.StopTrigger.PLDERR, stop_criteria_filter=0)
    await port.capturer.trigger.set(start_criteria=enums.StartTrigger.FILTER, start_criteria_filter=0, stop_criteria=enums.StopTrigger.FILTER, stop_criteria_filter=0)

    resp_obj = await port.capturer.trigger.get()


    """Frame to Keep"""
    await port.capturer.keep.set(kind=enums.PacketType.ALL, index=0, byte_count=-1)
    await port.capturer.keep.set(kind=enums.PacketType.FCSERR, index=0, byte_count=-1)
    await port.capturer.keep.set(kind=enums.PacketType.NOTPLD, index=0, byte_count=-1)
    await port.capturer.keep.set(kind=enums.PacketType.PLDERR, index=0, byte_count=-1)
    await port.capturer.keep.set(kind=enums.PacketType.TPLD, index=5, byte_count=-1) # TPLD == 5
    await port.capturer.keep.set(kind=enums.PacketType.FILTER, index=2, byte_count=-1) # Filter index == 2
    resp_obj = await port.capturer.keep.get()


    """Capture State"""
    await port.capturer.state.set_start()
    await port.capturer.state.set_stop()
    resp_obj = await port.capturer.state.get()


    """Capture Start Time, Status"""
    resp_obj = await port.capturer.stats.get()


    """Read Captured Packets"""
    pkts = await port.capturer.obtain_captured()
    for i in range(len(pkts)):
        resp_obj = await pkts[i].packet.get()
        print(f"Packet content # {i}: {resp_obj.hex_data}")


    """PORT FILTER"""
    """Create Filter"""
    filter = await port.filters.create()

    """Obtain One or Multiple Already Existing Filters"""
    filter = port.filters.obtain(key=0)
    filters = port.filters.obtain_multiple(*[0,1,2])

    """Sync Existing Filters from Port"""
    await port.filters.server_sync()

    """Remove Filter using Index"""
    await port.filters.remove(position_idx=0)

    """Remove Filter using Object"""
    await filter.delete()

    """Get filter index"""
    filter.idx

    """Get filter's module and port index"""
    filter.kind.module_id
    filter.kind.port_id

    """Filter - Enable"""
    await filter.enable.set_on()
    await filter.enable.set_off()
    resp = await filter.enable.get()

    """Filter - Description"""
    await filter.comment.set(comment="this is a comment")
    resp = await filter.comment.get()

    """Filter - Condition"""
    await filter.condition.set(and_expression_0=0, and_not_expression_0=0, and_expression_1=1, and_not_expression_1=0, and_expression_2=0, and_expression_3=0)
    resp = await filter.condition.get()

    """Filter - String Representation"""
    await filter.string.set(string_name="this is name")
    resp = await filter.string.get()


    """PORT LENGTH TERMS"""
    """Create Length Term"""
    length_term = await port.length_terms.create()
    
    """Obtain One or Multiple Already Existing Length Terms"""
    length_term = port.length_terms.obtain(key=0)
    length_terms = port.length_terms.obtain_multiple(*[0,1,2])

    """Remove Length Term using Index"""
    await port.length_terms.remove(position_idx=0)

    """Remove Length Term using Object"""
    await length_term.delete()

    """Get length term index"""
    length_term.idx

    """Get length term's module and port index"""
    length_term.kind.module_id
    length_term.kind.port_id

    """Sync Existing Length Terms from Port"""
    await port.length_terms.server_sync()

    """Configure Length Term - Length Value"""
    await length_term.length.set(
        length_check_type=enums.LengthCheckType.AT_MOST,
        size=100)
    await length_term.length.set(
        length_check_type=enums.LengthCheckType.AT_LEAST,
        size=100)
    resp = await length_term.length.get()


    """PORT MATCH TERMS"""
    """Create Match Term"""
    match_term = await port.match_terms.create()
    
    """Obtain One or Multiple Already Existing Match Terms"""
    match_term = port.match_terms.obtain(key=0)
    match_terms = port.match_terms.obtain_multiple(*[0,1,2])

    """Remove Match Term using Index"""
    await port.match_terms.remove(position_idx=0)

    """Remove Match Term using Object"""
    await match_term.delete()

    """Get match term index"""
    match_term.idx

    """Get match term's module and port index"""
    match_term.kind.module_id
    match_term.kind.port_id

    """Sync Existing Match Terms from Port"""
    await port.match_terms.server_sync()

    """Configure Match Term - Match Value"""
    await match_term.match.set(mask=Hex("FF"), value=Hex("00"))
    resp = await match_term.match.get()

    """Configure Match Term - Position"""
    await match_term.position.set(byte_offset=0)
    resp = await match_term.position.get()

    """Configure Match Term - Protocol Segments"""
    await match_term.protocol.set(segments=[enums.ProtocolOption.VLAN])
    resp = await match_term.protocol.get()


    """PORT HISTOGRAM"""
    """Create Histogram"""
    histogram = await port.datasets.create()
    
    """Obtain One or Multiple Already Existing Histograms"""
    histogram = port.datasets.obtain(key=0)
    histograms = port.datasets.obtain_multiple(*[0,1,2])

    """Get histogram index"""
    histogram.idx

    """Get histogram's module and port index"""
    histogram.kind.module_id
    histogram.kind.port_id

    """Sync Existing Histograms from Port"""
    await port.datasets.server_sync()

    """Remove Histogram using index"""
    await port.datasets.remove(position_idx=0)

    """Remove Histogram using object"""
    await histogram.delete()

    """Enable Histogram"""
    await histogram.enable.set_on()
    await histogram.enable.set_off()
    resp = await histogram.enable.get()

    """Configure Histogram - Data Source"""
    await histogram.source.set(
        source_type=enums.SourceType.TX_IFG,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await histogram.source.set(
        source_type=enums.SourceType.TX_LEN,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await histogram.source.set(
        source_type=enums.SourceType.RX_IFG,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await histogram.source.set(
        source_type=enums.SourceType.RX_LEN,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await histogram.source.set(
        source_type=enums.SourceType.RX_LATENCY,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    await histogram.source.set(
        source_type=enums.SourceType.RX_JITTER,
        which_packets=enums.PacketDetailSelection.ALL,
        identity=0
    )
    resp = await histogram.source.get()

    """Configure Histogram - Bucket Range"""
    await histogram.range.set(
        start=1, #first value going into the second bucket
        step=1, # the span of each middle bucket: (1) 1,2,4,8,16,32,64,128,256,512 (bytes, non-latency histograms).(2) 16,32,64,128,...,1048576,2097152 (nanoseconds, latency histograms).
        bucket_count=10 # the total number of buckets
    )
    resp = await histogram.range.get()

    """Get Histogram Samples"""
    resp = await histogram.samples.get()


    """PORT STATISTICS"""
    """Port Error Counter"""
    resp = await port.errors_count.get()


    """TX STATISTICS"""
    """Clear Tx Statistics"""
    # Clear all the transmit statistics for a port.
    await port.statistics.tx.clear.set()


    """Total Tx Traffic Counters"""
    # Obtains statistics concerning all the packets 
    # transmitted on the port.
    # Includes: bytes transmitted since cleared, 
    # packets transmitted since cleared, 
    # bits per second, 
    # packets per second.
    resp = await port.statistics.tx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """Tx Non-TPLD Traffic Counter"""
    # Obtains statistics concerning the packets without 
    # a test payload transmitted on the port.
    # Includes: bytes transmitted since cleared, 
    # packets transmitted since cleared, 
    # bits per second, 
    # packets per second.
    resp = await port.statistics.tx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """Extra Tx Counters"""
    # Obtains additional statistics for packets 
    # transmitted on the port.
    # Includes: transmitted ARP Requests, 
    # transmitted ARP Replies, 
    # transmitted IPv4 ICMP Echo Requests, 
    # transmitted IPv4 ICMP Echo Replies, 
    # transmitted FCS error packets,
    # transmitted sequence error packets,
    # transmitted misordered error packets,
    # transmitted payload error packets,
    # transmitted TPLD error packets,
    # transmitted MAC training frames,
    # transmitted IGMP Join packets.
    resp = await port.statistics.tx.extra.get()
    resp.tx_arp_request_count
    resp.tx_arp_reply_count
    resp.tx_ping_request_count
    resp.tx_ping_reply_count
    resp.tx_fcs_inj_count
    resp.tx_seq_inj_count
    resp.tx_mis_inj_count
    resp.tx_pld_inj_count
    resp.tx_tpld_inj_count
    resp.tx_mac_train_count
    resp.tx_igmp_join_count


    """Tx Traffic Counters Per Stream Index"""
    # Obtains statistics concerning the packets of 
    # a specific stream transmitted on the port.
    resp = await port.statistics.tx.obtain_from_stream(stream=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """RX STATISTICS"""
    """Clear Rx Statistics"""
    # Clear all the receive statistics for a port.
    await port.statistics.rx.clear.set()


    """Calibrate Rx Latency"""
    # Calibrate the latency calculation for packets received on the port. 
    # The lowest detected latency value (across all Test Payload IDs) 
    # will be set as the new base.
    await port.statistics.rx.calibrate.set()


    """Total Rx Traffic Counters"""
    # Obtains statistics concerning all the packets received on the port.
    # Includes: bytes received since cleared, 
    # packets received since cleared, 
    # bits per second, 
    # packets per second.
    resp = await port.statistics.rx.total.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """Rx Non-TPLD Traffic Counter"""
    # Obtains statistics concerning the packets without 
    # a test payload received on the port.
    # Includes: bytes received since cleared, 
    # packets received since cleared, 
    # bits per second, 
    # packets per second.
    resp = await port.statistics.rx.no_tpld.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """Rx PFC Counters"""
    # Obtains statistics of received 
    # Priority Flow Control (PFC) packets on the port.
    resp = await port.statistics.rx.pfc_stats.get()
    resp.packet_count
    resp.quanta_pri_0
    resp.quanta_pri_1
    resp.quanta_pri_2
    resp.quanta_pri_3
    resp.quanta_pri_4
    resp.quanta_pri_5
    resp.quanta_pri_6
    resp.quanta_pri_7


    """Extra Rx Counters"""
    # Obtains statistics concerning special errors 
    # received on the port since received statistics were cleared.
    # Includes: received ARP Requests, 
    # received ARP Replies, 
    # received IPv4 ICMP Echo Requests, 
    # received IPv4 ICMP Echo Replies, 
    # received FCS error packets,
    # received PAUSE frames,
    # received gap count,
    # received gap duration.
    resp = await port.statistics.rx.extra.get()
    resp.fcs_error_count
    resp.pause_frame_count
    resp.gap_count
    resp.gap_duration
    resp.pause_frame_count
    resp.rx_arp_reply_count
    resp.rx_arp_request_count
    resp.rx_ping_reply_count
    resp.rx_ping_request_count


    """Received TPLDs"""
    # Obtain the set of test payload IDs observed 
    # among the received packets since receive statistics were cleared. 
    # Traffic statistics for these test payload streams 
    # will have non-zero byte and packet count.
    rx_tplds = await port.statistics.rx.obtain_available_tplds()


    """Rx Error Counters Per TPLD"""
    # Obtains statistics concerning errors in the packets 
    # with a particular test payload id received on the port.
    resp = await port.statistics.rx.access_tpld(tpld_id=0).errors.get()
    resp.packet_loss_by_seq
    resp.payload_err_packets
    resp.misorder_by_seq


    """Rx Latency Counter Per TPLD"""
    # Obtains statistics concerning the latency 
    # experienced by the packets with a particular 
    # test payload id received on the port. 
    resp = await port.statistics.rx.access_tpld(tpld_id=0).latency.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val


    """Rx Jitter Counter Per TPLD"""
    # Obtains statistics concerning the jitter 
    # experienced by the packets with a particular 
    # test payload id received on the port. 
    resp = await port.statistics.rx.access_tpld(tpld_id=0).jitter.get()
    resp.avg_last_sec
    resp.max_last_sec
    resp.min_last_sec
    resp.avg_val
    resp.max_val
    resp.min_val


    """Rx Traffic Counters Per TPLD"""
    # Obtains traffic statistics concerning the packets 
    # with a particular test payload identifier received 
    # on the port.
    resp = await port.statistics.rx.access_tpld(tpld_id=0).traffic.get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    """Rx Filtered Traffic Counters"""
    # Obtains statistics concerning the packets 
    # satisfying the condition of a particular 
    # filter for the port.
    resp = await port.statistics.rx.obtain_filter_statistics(filter=0).get()
    resp.byte_count_since_cleared
    resp.packet_count_since_cleared
    resp.bit_count_last_sec
    resp.packet_count_last_sec


    # [Z01s/Z01sx Odin Specific APIs]
    # [MDI/MDIX]
    if isinstance(port, ports.POdin1G3S6P) or isinstance(port, ports.POdin1G3S6P_b) or isinstance(port, ports.POdin1G3S6PE):

        """MDI/MDIX Mode"""
        await port.mdix_mode.set_auto()
        await port.mdix_mode.set_mdi()
        await port.mdix_mode.set_mdix()
        resp_obj = await port.mdix_mode.get()


    # [Z01t Odin Specific APIs]
    # [BroadR Reach]
    if isinstance(port, ports.POdin1G3S6PT1RJ45):

        """BroadR Reach Configuration"""
        await port.brr.mode.set_master()
        await port.brr.mode.set_slave()
        resp_obj = await port.brr.mode.get()

        """BroadR Reach Status"""
        resp_obj = await port.brr.status.get()


    
    # [Z10r Odin Specific APIs]
    if isinstance(port, ports.POdin10G5S6PCU) or isinstance(port, ports.POdin10G5S6PCU_b):

        # [Energy Efficient Ethernet (EEE)]
        """ENERGY EFFICIENT ETHERNET (EEE) CONFIGURATION"""
        """EEE- Capabilities"""
        resp_obj = await port.eee.capabilities.get()


        """EEE - Partner Capabilities"""
        resp_obj = await port.eee.partner_capabilities.get()


        """EEE - Control"""
        await port.eee.enable.set_off()
        await port.eee.enable.set_on()
        resp_obj = await port.eee.enable.get()


        """EEE - Low Power TX Mode"""
        await port.eee.mode.set_off()
        await port.eee.mode.set_on()
        resp_obj = await port.eee.mode.get()


        """EEE - RX Power"""
        resp_obj = await port.eee.rx_power.get()


        """EEE - SNR Margin"""
        resp_obj = await port.eee.snr_margin.get()


        """EEE - Status"""
        resp_obj = await port.eee.status.get()

    
    if isinstance(port, ports.POdin10G6S6P_a):

        # [Runt Frame Handling]
        """Runt Frame Handling"""
        # Runt - RX Length
        await port.runt.rx_length.set(runt_length=40)
        resp_obj = await port.runt.rx_length.get()

        # Runt - TX Length
        await port.runt.tx_length.set(runt_length=40)
        resp_obj = await port.runt.tx_length.get()

        # Runt - Length Error
        resp_obj = await port.runt.has_length_errors.get()


        # [Preamble Handling]
        """Preamble Handling"""
        # RX Preamble Insert
        await port.preamble.rx_insert.set(on_off=enums.OnOff.ON)
        await port.preamble.rx_insert.set(on_off=enums.OnOff.OFF)
        resp_obj = await port.preamble.rx_insert.get()

        # TX Preamble Removal   
        await port.preamble.tx_remove.set(on_off=enums.OnOff.ON)
        await port.preamble.tx_remove.set(on_off=enums.OnOff.OFF)
        resp_obj = await port.preamble.tx_remove.get()


    if isinstance(port, ports.PLoki100G5S4P_a):

        """MACSEC CONFIGURATION"""
        """MACsec - Tx SCs"""
        await port.macsec.txscs.create()



    # [Layer-1 Advanced Features]
    # [Z100 Loki, Z400 Thor, Z800 Freya, Z1600 Edun Specific APIs]
    if isinstance(port, ports.Z100LokiPort) or isinstance(port, ports.Z400ThorPort) or isinstance(port, ports.Z800FreyaPort) or isinstance(port, ports.Z1600EdunPort):

        """LINK FLAP"""
        """Link Flap - Configuration"""
        await port.layer1.impairment.link_flap.params.set(duration=10, period=20, repetition=0)
        resp_obj = await port.layer1.impairment.link_flap.params.get()


        """Link Flap - Control"""
        await port.layer1.impairment.link_flap.enable.set_on()
        await port.layer1.impairment.link_flap.enable.set_off()
        resp_obj = await port.layer1.impairment.link_flap.enable.get()


        """PMA ERROR INJECTION"""
        """PMA Error Insertion - Configuration"""
        await port.layer1.impairment.pma_error_inject.params.set(duration=10, period=20, repetition=0, coeff=1, exp=-6)
        resp_obj = await port.layer1.impairment.pma_error_inject.params.get()


        """PMA Error Insertion - Control"""
        await port.layer1.impairment.pma_error_inject.enable.set_on()
        await port.layer1.impairment.pma_error_inject.enable.set_off()
        resp_obj = await port.layer1.impairment.pma_error_inject.enable.get()


        """RS FAULT"""
        """RS Fault - Signaling"""
        await port.layer1.rs_fault.signaling.set_disabled()
        await port.layer1.rs_fault.signaling.set_force_local()
        await port.layer1.rs_fault.signaling.set_force_remote()
        await port.layer1.rs_fault.signaling.set_normal()
        resp_obj = await port.layer1.rs_fault.signaling.get()


        """RS Fault - Status"""
        resp_obj = await port.layer1.rs_fault.status.get()



        """PCS/FEC"""
        """FEC Mode"""
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.RS_FEC)
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.RS_FEC_KP)
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.RS_FEC_KR)
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.FC_FEC)
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.OFF)
        await port.layer1.pcs_fec.fec_mode.set(mode=enums.FECMode.ON)
        resp_obj = await port.layer1.pcs_fec.fec_mode.get()


        """PCS TX Configuration - Skew"""
        await port.layer1.pcs_fec.lane[0].tx_config.set(virt_lane_index=0, skew=0)


        """PCS RX Status - Skew"""
        resp_obj = await port.layer1.pcs_fec.lane[0].rx_status.status.get()


        """PCS Lane BER and Error Counters"""
        resp_obj = await port.layer1.pcs_fec.lane[0].rx_status.errors.get()


        """PCS Header Lock & Align Lock"""
        resp_obj = await port.layer1.pcs_fec.lane[0].rx_status.lock.get()


        """Clear Counters"""
        await port.layer1.pcs_fec.clear.set()


        """FEC Symbol Error Distribution Status"""
        resp_obj = await port.layer1.pcs_fec.fec_symbol_status.fec_status.get()


        """FEC Symbol Total Status"""
        # Total Codewords
        # Corrected Codewords
        # Uncorrectable Codewords
        # Corrected Symbols
        # Pre-FEC BER
        # Post-FEC BER
        resp_obj = await port.layer1.pcs_fec.fec_symbol_status.total_status.get()


        """Error Counters"""
        # Total Alarms, LOS Errors, Alignment Errors, BIP Errors, FEC Errors, Header Errors, Higher Layer Errors, PCS Errors, Valid Mask
        resp_obj = await port.layer1.pcs_fec.alarms.errors.get()


        """PRBS PATTERN GENERATION"""
        """PRBS Configuration"""
        await port.layer1.prbs_config.set(prbs_inserted_type=enums.PRBSInsertedType.PHY_LINE, polynomial=enums.PRBSPolynomial.PRBS31, invert=enums.PRBSInvertState.NON_INVERTED, statistics_mode=enums.PRBSStatisticsMode.ACCUMULATIVE)
        resp_obj = await port.layer1.prbs_config.get()


        """PRBS Control"""
        await port.layer1.serdes[0].prbs.control.set_on()
        await port.layer1.serdes[0].prbs.control.set_off()
        resp_obj = await port.layer1.serdes[0].prbs.control.get()


        """PRBS Bit Error and Lock Status"""
        resp_obj = await port.layer1.serdes[0].prbs.status.get()
        

        # [Z800 Freya, Z1600 Edun Specific APIs]
        if isinstance(port, ports.Z800FreyaPort) or isinstance(port, ports.Z1600EdunPort):
            
            """GRAY CODING AND PRECODING"""
            # [Z800 Freya, Z1600 Edun Specific APIs]
            """Gray Coding - Configuration"""
            await port.layer1.serdes[0].pma.graycoding.set(rx_mode=enums.GrayCodingMode.ON, rx_endianness=enums.Endianness.NORMAL, tx_mode=enums.GrayCodingMode.ON, tx_endianness=enums.Endianness.NORMAL)
            resp = await port.layer1.serdes[0].pma.graycoding.get()


            """Precoding - Configuration"""
            await port.layer1.serdes[0].pma.precoding.set(rx_mode=enums.PreCodingMode.ON, rx_endianness=enums.Endianness.NORMAL,tx_mode=enums.PreCodingMode.ON, tx_endianness=enums.Endianness.NORMAL)
            resp = await port.layer1.serdes[0].pma.precoding.get()


            """P/N POLARITY SWAP"""
            # [Z800 Freya, Z1600 Edun Specific APIs]
            """P/N Polarity - Tx/Rx Swap"""
            await port.layer1.serdes[0].pma.pn_swap_tx.set_on()
            await port.layer1.serdes[0].pma.pn_swap_tx.set_off()
            resp = await port.layer1.serdes[0].pma.pn_swap_tx.get()

            await port.layer1.serdes[0].pma.pn_swap_rx.set_on()
            await port.layer1.serdes[0].pma.pn_swap_rx.set_off()
            resp = await port.layer1.serdes[0].pma.pn_swap_rx.get()


            """PCS VARIANT"""
            # [Z800 Freya, Z1600 Edun Specific APIs]
            await port.layer1.pcs_fec.pcs_variant.set(variant=enums.FreyaPCSVariant.ETC)
            await port.layer1.pcs_fec.pcs_variant.set(variant=enums.FreyaPCSVariant.IEEE)
            resp_obj = await port.layer1.pcs_fec.pcs_variant.get()


            """FEC ERROR INSERTION"""
            # [Z800 Freya, Z1600 Edun Specific APIs]
            """FEC Error Insertion - Control"""
            await port.layer1.pcs_fec.fec_error_inject.control.set_start()
            await port.layer1.pcs_fec.fec_error_inject.control.set_stop()
            resp = await port.layer1.pcs_fec.fec_error_inject.control.get()


            """FEC Error Insertion - Codeword Error Pattern"""
            await port.layer1.pcs_fec.fec_error_inject.cycle.set(loop=0, cycle_len=8, error_len=4)
            resp = await port.layer1.pcs_fec.fec_error_inject.cycle.get()


            """FEC Error Insertion - Symbol Error Pattern"""
            await port.layer1.pcs_fec.fec_error_inject.err_symbols.set(error_sym_indices=[543, 542, 541, 50, 44, 76, 88])
            resp = await port.layer1.pcs_fec.fec_error_inject.err_symbols.get()


            """FEC Error Insertion - Bit Error Mask"""
            await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.STATIC, bitmask=Hex("000F"))
            await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.ROTATE_HIGH, bitmask=Hex("000F"))
            await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.set(mode=enums.FecCodewordBitErrorMaskMode.INC, bitmask=Hex("000F"))
            await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.set_all_bits()
            await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.set_no_bits()
            resp = await port.layer1.pcs_fec.fec_error_inject.bit_err_mask.get()


            """FEC Error Insertion - FEC Engine Control"""
            await port.layer1.pcs_fec.fec_error_inject.engine.set_all_engines()
            resp = await port.layer1.pcs_fec.fec_error_inject.engine.get()


            """FEC Error Insertion - Statistics"""
            resp = await port.layer1.pcs_fec.fec_error_inject.statistics.get()


            """FEC Error Insertion - Clear Statistics"""
            await port.layer1.pcs_fec.fec_error_inject.clear_stats.set()
        

        """AUTO-NEGOTIATION AND LINK TRAINING"""
        """Basic Auto-Negotiation and Link Training Operations"""
        # [For Z400 Thor and Z1600 Edun]
        if isinstance(port, ports.Z1600EdunPort) or isinstance(port, ports.Z400ThorPort):
            
            """Auto-Negotiation Settings"""
            ta_conf = enums.AutoNegTecAbility.IEEE_1_6TBASE_CR8_KR8 | enums.AutoNegTecAbility.IEEE_800GBASE_CR4_KR4
            ta_conf = Hex(format(ta_conf, 'X').zfill(16))

            fec_conf = enums.AutoNegFECOption.RS528 | enums.AutoNegFECOption.RS272
            fec_conf = Hex(format(fec_conf, 'X').zfill(2))

            pause_conf = enums.PauseMode.SYM_PAUSE | enums.PauseMode.ASYM_PAUSE
            pause_conf = Hex(format(pause_conf, 'X').zfill(2))

            await port.layer1.anlt.an.settings.set(
                mode=enums.AutoNegMode.ANEG_ON, 
                tec_ability=ta_conf, 
                fec_capable=fec_conf, 
                fec_requested=fec_conf, 
                pause_mode=pause_conf
                )
            resp = await port.layer1.anlt.an.settings.get()


            """Auto-Negotiation Status"""
            await port.layer1.anlt.an.status.get()


            """Link Training Settings"""
            await port.layer1.anlt.lt.settings.set(
                mode=enums.LinkTrainingMode.DISABLED, 
                pam4_frame_size=enums.PAM4FrameSize.P4K_FRAME, 
                nrz_pam4_init_cond=enums.LinkTrainingInitCondition.NO_INIT, 
                nrz_preset=enums.NRZPreset.NRZ_WITH_PRESET, 
                timeout_mode=enums.TimeoutMode.DEFAULT)
            resp = await port.layer1.anlt.lt.settings.get()


            """Link Training Status"""
            resp = await port.layer1.serdes[0].lt_status.get()

        """Advanced Auto-Negotiation and Link Training Operations"""
        # [For Z800 Freya]
        if isinstance(port, ports.Z800FreyaPort):
            
            """ANLT Auto-Restart Settings"""
            await port.layer1.anlt.set_autorestart(restart_link_down=True, restart_lt_failure=True)
            resp = await port.layer1.anlt.get_autorestart()

            """ANLT Strict Mode Settings"""
            await port.layer1.anlt.set_strict_mode(enable=False)
            resp = await port.layer1.anlt.get_strict_mode()

            """Auto-Negotiation Allow-in-Loopback Settings"""
            await port.layer1.anlt.an.set_allow_loopback(allow=True)
            resp = await port.layer1.anlt.an.get_allow_loopback()

            """Auto-Negotiation Send Empty Next Page Settings"""
            await port.layer1.anlt.an.set_empty_np(enable=True)
            resp = await port.layer1.anlt.an.get_empty_np()

            """Read Auto-Negotiation supported abilities per-port"""
            resp= await port.layer1.anlt.an.abilities.get()

            """Set Auto-Negotiation advertised abilities per-port"""
            ta_conf = enums.AutoNegTecAbility.IEEE_1_6TBASE_CR8_KR8 | enums.AutoNegTecAbility.IEEE_800GBASE_CR4_KR4
            ta_conf = Hex(format(ta_conf, 'X').zfill(16))

            fec_conf = enums.AutoNegFECOption.RS528 | enums.AutoNegFECOption.RS272
            fec_conf = Hex(format(fec_conf, 'X').zfill(2))

            pause_conf = enums.PauseMode.SYM_PAUSE | enums.PauseMode.ASYM_PAUSE
            pause_conf = Hex(format(pause_conf, 'X').zfill(2))

            await port.layer1.anlt.an.advertise.set(
                tech_abilities=ta_conf,
                fec_abilities=fec_conf,
                pause_mode=pause_conf
            )
            resp = await port.layer1.anlt.an.advertise.get()


            """Link Training Per-Serdes Algorithm Selection"""
            await port.layer1.serdes[0].lt.set_algorithm_default()
            resp = await port.layer1.serdes[0].lt.get_algorithm()

            """Link Training Per-Serdes Initial Modulation Selection"""
            await port.layer1.serdes[0].lt.set_initial_modulation_nrz()
            await port.layer1.serdes[0].lt.set_initial_modulation_pam4()
            await port.layer1.serdes[0].lt.set_initial_modulation_pam4precoding()
            resp = await port.layer1.serdes[0].lt.get_initial_modulation()

            """Link Training Per-Serdes Preset Custom Configuration"""
            # Using the native values for Preset 1
            await port.layer1.serdes[0].lt.preset1.native.set(
                response=enums.FreyaPresetResponse.ACCEPT,
                pre3=0,
                pre2=0,
                pre=0,
                main=0,
                post=0
                )
            resp = await port.layer1.serdes[0].lt.preset1.native.get()

            # Using the IEEE values for Preset 1
            await port.layer1.serdes[0].lt.preset1.ieee.set(
                response=enums.FreyaPresetResponse.ACCEPT,
                pre3=-200,
                pre2=100,
                pre=-100,
                main=507,
                post=100,
                )
            resp = await port.layer1.serdes[0].lt.preset1.ieee.get()


            # Using the level values for Preset 1
            await port.layer1.serdes[0].lt.preset1.level.set(
                response=enums.FreyaPresetResponse.ACCEPT,
                pre3=6,
                pre2=3,
                pre=2,
                main=64,
                post=3,
                )
            resp = await port.layer1.serdes[0].lt.preset1.level.get()

            """Reset Link Training Per-Serdes Preset to Default"""
            await port.layer1.serdes[0].lt.preset1.reset.set()


            """Link Training Per-Serdes Eq Range Configuration"""
            # Using native values, set the response to COEFF_AT_LIMIT when the coeff reaches the min or max
            await port.layer1.serdes[0].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=50)
            resp = await port.layer1.serdes[0].lt.range.main.native.get()

            # Using ieee values, set the response to COEFF_AT_LIMIT when the coeff reaches the min or max
            await port.layer1.serdes[0].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.COEFF_AT_LIMIT, min=0, max=50)
            resp = await port.layer1.serdes[0].lt.range.main.ieee.get()

            """Reset Link Training Per-Serdes Eq Range to Auto"""
            # When in Auto mode, the min and max values use the default values to the full range supported by the serdes, thus min and max are ignored
            await port.layer1.serdes[0].lt.range.main.native.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=0)
            await port.layer1.serdes[0].lt.range.main.ieee.set(response=enums.FreyaLinkTrainingRangeResponse.AUTO, min=0, max=0)

            """Link Training Configurationl, per-port"""
            # Using IEEE standard OOS preset
            # Enable Default Timeout Mode for Link Training Auto mode
            await port.layer1.anlt.lt_config.set(
                oos_preset=enums.FreyaOutOfSyncPreset.IEEE,
                timeout_mode=enums.TimeoutMode.DEFAULT
                )
            # Using IEEE standard OOS preset
            # Disable Timeout for Link Training Manual mode
            await port.layer1.anlt.lt_config.set(
                oos_preset=enums.FreyaOutOfSyncPreset.IEEE,
                timeout_mode=enums.TimeoutMode.DISABLED
                )
            

            """Control ANLT with various modes, per-port"""
            # Only enable Auto-Negotiation
            await port.layer1.anlt.ctrl.enable_an_only()

            # Enable Auto-Negotiation and Link Training (auto mode)
            # When Link Training is set to auto mode, the serdes will automatically select the best algorithm and initial modulation based on the negotiated capabilities
            await port.layer1.anlt.ctrl.enable_an_lt_auto()

            # Enable Auto-Negotiation and Link Training (manual mode)
            # When Link Training is set to manual mode, the serdes will use the user configured algorithm and initial modulation
            await port.layer1.anlt.ctrl.enable_an_lt_interactive()

            # Only enable Link Training (auto mode), skipping Auto-Negotiation
            await port.layer1.anlt.ctrl.enable_lt_auto_only()

            # Only enable Link Training (manual mode), skipping Auto-Negotiation
            await port.layer1.anlt.ctrl.enable_lt_interactive_only()

            # Disable both Auto-Negotiation and Link Training
            await port.layer1.anlt.ctrl.disable_anlt()

            """For Link Training in manual mode, you can send different LT commands to the remote partner, per-serdes"""
            # Send PAM4 Request
            await port.layer1.serdes[0].lt.send_cmd_modulation(modulation=enums.LinkTrainEncoding.PAM4)
            # Send PAM4Precoding Request
            await port.layer1.serdes[0].lt.send_cmd_modulation(modulation=enums.LinkTrainEncoding.PAM4_WITH_PRECODING)
            
            # Send Preset Request
            await port.layer1.serdes[0].lt.send_cmd_preset(preset=enums.LinkTrainPresets.PRESET_1)

            # Send EQ Coefficient Inc Request
            await port.layer1.serdes[0].lt.send_cmd_inc(coeff=enums.LinkTrainCoeffs.MAIN)

            # Send EQ Coefficient Dec Request
            await port.layer1.serdes[0].lt.send_cmd_dec(coeff=enums.LinkTrainCoeffs.MAIN)

            # Send No EQ
            await port.layer1.serdes[0].lt.send_cmd_no_equalization()

            # Send Trained Notification
            await port.layer1.serdes[0].lt.send_cmd_trained()

            # Check response status after sending any command
            cmd, result, flag = await port.layer1.serdes[0].lt.get_cmd_result_flag()


            """ANLT Statistics, Result and Status"""
            # Get Auto-Negotiation results
            resp = await port.layer1.anlt.an.results.get()

            # Get Auto-Negotiation statistics
            resp = await port.layer1.anlt.an.statistics.get()

            # Get Link Training results, per-serdes
            resp = await port.layer1.serdes[0].lt.results.get()

            # Get Link Training statistics, per-serdes
            resp = await port.layer1.serdes[0].lt.statistics.get()

        
        """SIGNAL INTEGRITY SAMPLE READING"""
        # Only for Freya and Edun Modules
        if isinstance(port, ports.Z800FreyaPort) or isinstance(port, ports.Z1600EdunPort):
            
            """Signal Integrity Sample Read - Control"""
            await port.layer1.serdes[0].siv.control.set(opcode=enums.Layer1Opcode.START_SCAN)

            """Signal Integrity Sample Read - Data"""
            resp = await port.layer1.serdes[0].siv.data.get()



        """HOST TX/RX EQUALIZATION CONFIGURATION"""
        # For Loki Modules
        if isinstance(port, ports.Z100LokiPort):
            # Tx Equalizer Settings
            await port.layer1.serdes[0].medium.tx_equalizer.set(tap_values=[0, 60, 0])

            # Rx Equalizer Settings
            await port.layer1.serdes[0].medium.rx_equalizer.set(auto=1, ctle=5, reserved=0)
        
        # For Thor Modules
        if isinstance(port, ports.Z400ThorPort):
            # Tx Equalizer Settings
            await port.layer1.serdes[0].medium.tx_equalizer.set(tap_values=[0, 60, 0, 0, 0])

            # Rx Equalizer Settings
            await port.layer1.serdes[0].medium.rx_equalizer.set(auto=1, ctle=5, reserved=0)

        # For Freya Modules
        if isinstance(port, ports.Z800FreyaPort):
            # Tx Equalizer Settings
            await port.layer1.serdes[0].medium.tx.native.set(tap_values=[0, 60, 0, 0, 0, 0])

            # Rx Equalizer Settings, either in Auto, Manual, or Freeze
            await port.layer1.serdes[0].medium.rx.config.agc.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            await port.layer1.serdes[0].medium.rx.config.cdr.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            await port.layer1.serdes[0].medium.rx.config.ctle_high.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            await port.layer1.serdes[0].medium.rx.config.ctle_low.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            await port.layer1.serdes[0].medium.rx.config.dfe.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            await port.layer1.serdes[0].medium.rx.config.oc.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            # Post-FFE 1-23
            await port.layer1.serdes[0].medium.rx.config.post_ffe_1.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)
            # Pre-FFE 1-8
            await port.layer1.serdes[0].medium.rx.config.pre_ffe_1.set(mode=enums.RxEqExtCapMode.MANUAL, value=5)

        # For Edun Modules
        if isinstance(port, ports.Z1600EdunPort):
            # Tx Equalizer Settings
            await port.layer1.serdes[0].medium.tx.ieee.set(tap_values=[0, 60, 0, 0, 0, 0, 0])

            # Rx Equalizer Settings


    # [Transceiver Management]
    """TRANSCEIVER MANAGEMENT"""
    """Read / Write"""
    # Provides read and write access to the
    # register interface supported by the transceiver.
    await port.transceiver.access_rw(page_address=0, register_address=0).set(value=Hex("FF"))
    
    resp = await port.transceiver.access_rw(page_address=0, register_address=0).get()


    """Sequential Read & Write"""
    # I2C sequential access to a transceiver's register.
    # When invoked, the ``<byte_count>`` number of bytes will be 
    # read or written in one I2C transaction, in which the 
    # ``<value>`` is read or written with only a single register 
    # address setup. A subsequent invocation will perform a second 
    # I2C transaction in the same manner.
    await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).set(value=Hex("00FF00FF"))
    
    resp = await port.transceiver.access_rw_seq(page_address=0, register_address=0, byte_count=4).get()


    """Sequential Read & Write (Banked)"""
    # I2C sequential access to a transceiver's register 
    # with bank selection.
    await port.transceiver.access_rw_seq_bank(bank_address=1, page_address=0x9F, register_address=200, byte_count=1).set(value=Hex("00"))
    
    resp = await port.transceiver.access_rw_seq_bank(bank_address=1, page_address=0x9F, register_address=200, byte_count=1).get()


    """MII Access"""
    # Provides access to the register interface supported 
    # by the media-independent interface (MII) transceiver. 
    await port.transceiver.access_mii(register_address=0).set(value=Hex("00"))
    
    resp = await port.transceiver.access_mii(register_address=0).get()
    

    """I2C Configuration"""
    # Configures the I2C interface parameters
    await port.transceiver.i2c_config.set(frequency=100)


    """Tx/Rx Laser Power"""
    # Reading of the optical power level of the Tx/Rx signal
    resp = await port.transceiver.laser_power.tx_laser_power.get()
    resp.nanowatts

    resp = await port.transceiver.laser_power.rx_laser_power.get()
    resp.nanowatts


    """Get CDB Instances Supported"""
    # Return the supported CDB instances from the CMIS transceiver
    await port.transceiver.cmis.cdb_instances_supported.get()


    """CMIS CDB"""
    # See hlfuncs.cmis.cdb module for CMIS CDB APIs


    # [end]