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

    # [streams]
    """Create Stream Object"""
    # Create a stream object representing a specific stream on the port.
    stream = await port.streams.create()


    """Obtain One or Multiple Stream Objects"""
    # Obtain already existing stream object(s) using stream indices.
    stream = port.streams.obtain(0)
    streams = port.streams.obtain_multiple(*[0,1,2])


    """Sync Existing Streams from Port"""
    await port.streams.server_sync()


    """Get stream index"""
    stream.idx


    """Get stream's module and port index"""
    stream.kind.module_id
    stream.kind.port_id


    """Remove Stream by Index"""
    # Remove a stream object from the port.
    await port.streams.remove(position_idx=0)


    """Remove Stream by Removing Stream Object"""
    # Remove a stream object from the port.
    await stream.delete()


    """Description"""
    await stream.comment.set(comment="description")
    resp = await stream.comment.get()


    """Test Payload ID"""
    # The identifier of the test payloads inserted 
    # into packets transmitted for a stream. 
    # A value of -1 disables test payloads for the stream. 
    await stream.tpld_id.set(test_payload_identifier=0)
    resp = await stream.tpld_id.get()


    """Enable/Disable Stream"""
    # This property determines if a stream contributes 
    # outgoing packets for a port. The value can be 
    # toggled between ON and SUPPRESS while traffic is enabled 
    # at the port level. 
    # Streams in the OFF state cannot be set to any other value 
    # while traffic is enabled. 
    # The sum of the rates of all enabled or suppressed streams 
    # must not exceed the effective port rate.
    await stream.enable.set_off()
    await stream.enable.set_on()
    await stream.enable.set_suppress()
    resp = await stream.enable.get()


    """Stream Rate Configuration"""
    # The rate of the traffic transmitted for a stream 
    # expressed in millionths of the effective rate for 
    # the port. 
    await stream.rate.fraction.set(stream_rate_ppm=1_000_000)
    resp = await stream.rate.fraction.get()

    # The rate of the traffic transmitted for a stream 
    # expressed in packets per second.
    await stream.rate.pps.set(stream_rate_pps=1_000)
    resp = await stream.rate.pps.get()

    # The rate of the traffic transmitted for a stream, 
    # expressed in units of bits-per-second at layer-2, 
    # thus including the Ethernet header but excluding the 
    # inter-frame gap.
    await stream.rate.l2bps.set(l2_bps=1_000_000)
    resp = await stream.rate.l2bps.get()


    """Stream Packet Limit"""
    # The total number of packets to be transmitted for a stream. 
    # A value of 0 indicates that there is no limit to the 
    # number of packets transmitted for the stream.
    await stream.packet.limit.set(packet_count=1_000)
    resp = await stream.packet.limit.get()


    """Burst Size and Density"""
    # The burstiness of the traffic transmitted for a 
    # stream, expressed in terms of the number of packets 
    # in each burst, and how densely they are packed together.
    await stream.burst.burstiness.set(size=20, density=80)
    resp = await stream.burst.burstiness.get()


    """Inter Burst/Packet Gap"""
    # When the port is in in Burst TX mode, this command 
    # defines the gap between packets in a burst 
    # (inter-packet gap) and the gap after a burst defined 
    # in one stream stops until a burst defined in the next 
    # stream starts (inter-burst gap).
    await stream.burst.gap.set(inter_packet_gap=30, inter_burst_gap=30)
    resp = await stream.burst.gap.get()


    """Priority Flow"""
    # Set and get the Priority Flow Control (PFC) Cos 
    # value of a stream.
    await stream.priority_flow.set(cos=enums.PFCMode.ZERO)
    await stream.priority_flow.set(cos=enums.PFCMode.ONE)
    await stream.priority_flow.set(cos=enums.PFCMode.TWO)
    await stream.priority_flow.set(cos=enums.PFCMode.THREE)
    await stream.priority_flow.set(cos=enums.PFCMode.FOUR)
    await stream.priority_flow.set(cos=enums.PFCMode.FIVE)
    await stream.priority_flow.set(cos=enums.PFCMode.SIX)
    await stream.priority_flow.set(cos=enums.PFCMode.SEVEN)
    await stream.priority_flow.set(cos=enums.PFCMode.VLAN_PCP)
    resp = await stream.priority_flow.get()


    """Packet Size Configuration"""
    # The length distribution of the packets transmitted for 
    # a stream. The length of the packets transmitted for a 
    # stream can be varied from packet to packet, according 
    # to a choice of distributions within a specified min...
    # max range.
    await stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=64, max_val=64)
    await stream.packet.length.set(length_type=enums.LengthType.INCREMENTING, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.BUTTERFLY, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.RANDOM, min_val=64, max_val=1500)
    await stream.packet.length.set(length_type=enums.LengthType.MIX, min_val=64, max_val=64)

    resp = await stream.packet.length.get()
    resp.length_type


    """Packet Auto Size"""
    # Adjust the packet length distribution 
    # of the stream.
    await stream.packet.auto_adjust.set()


    """Packet Header Configuration"""
    # Header Protocol Segments
    await stream.packet.header.protocol.set(
        segments=[
            enums.ProtocolOption.ETHERNET,
            enums.ProtocolOption.VLAN,
            enums.ProtocolOption.IP,
            enums.ProtocolOption.UDP
            ])
    resp = await stream.packet.header.protocol.get()

    # Header Values
    # Use hlfuncs.headers to build packet headers for the stream.
    eth = headers.Ethernet()
    eth.src_mac = "aaaa.aaaa.0005"
    eth.dst_mac = "bbbb.bbbb.0005"
    eth.ethertype = headers.EtherType.VLAN

    vlan = headers.VLAN()
    vlan.pri = 3
    vlan.dei = 0
    vlan.id = 100
    vlan.type = headers.EtherType.IPv4

    ipv4 = headers.IPV4()
    ipv4.src = "1.1.1.5"
    ipv4.dst = "2.2.2.5"
    ipv4.proto = headers.IPProtocol.UDP

    udp = headers.UDP()
    udp.src_port = 5005
    udp.dst_port = 6006
    udp.length = 0

    await stream.packet.header.data.set(hex_data=Hex(str(eth) + str(vlan) + str(ipv4) + str(udp)))
    resp = await stream.packet.header.data.get()

    # Alternatively, you can also use raw hex data.
    await stream.packet.header.data.set(hex_data=Hex("bbbbbbbbbbbbaaaaaaaabbbb8100006408004500002e000100004011f9b201010105020202050505060"))
    resp = await stream.packet.header.data.get()


    """Payload Type"""
    # The payload content of the packets transmitted for 
    # a stream. The payload portion of a packet starts 
    # after the header and continues up until the test 
    # payload or the frame checksum. 

    # Pattern string in hex, min = 1 byte, max = 18 bytes
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("000102030405060708090A0B0C0D0E0FDEAD"))
    await stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("F5"))

    # Patter string ignored for non-pattern types
    await stream.payload.content.set(payload_type=enums.PayloadType.INC16, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.INC8, hex_data=Hex("F5"))
    await stream.payload.content.set_inc_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC8, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_byte("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.DEC16, hex_data=Hex("F5"))
    await stream.payload.content.set_dec_word("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.PRBS, hex_data=Hex("F5"))
    await stream.payload.content.set_prbs("00")
    await stream.payload.content.set(payload_type=enums.PayloadType.RANDOM, hex_data=Hex("F5"))
    await stream.payload.content.set_random("00")

    resp = await stream.payload.content.get()


    """Extended Payload"""
    # This API allows the definition of a much larger (up to MTU) payload buffer for each stream. The extended payload will be inserted immediately after the end of the protocol segment area.

    # To use this API, the port must be in Extended 
    # Payload Mode. This mode is set at the port level
    # using await port.payload_mode.set_extpl()

    await stream.payload.extended.set(hex_data=Hex("00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF00110022FF"))    
    resp = await stream.payload.extended.get()


    """Custom Data Field"""
    # To use CDF API, the port must be in Custom Data Field Mode. This mode is set at the port level
    # using await port.payload_mode.set_cdf()

    # CDF Offset
    # The CDF offset for the stream is the location in 
    # the stream data packets where the various CDF data 
    # will be inserted. All fields for a given stream 
    # uses the same offset value. 
    await stream.cdf.offset.set(offset=1)
    resp = await stream.cdf.offset.get()

    # CDF Count
    # Controls the number of custom data fields 
    # available for each stream. You can set a different 
    # number of fields for each stream.
    await stream.cdf.count.set(cdf_count=1)
    resp = await stream.cdf.count.get()

    # CDF Data
    # Controls the actual field data for a single field. It is possible to define fields with different data lengths for each stream. If the length of a data field exceeds (packet length - CDF offset) defined for the stream the field data will be truncated when transmitted.
    await stream.cdf.data(0).set(hex_data=Hex("AABBCCDD"))
    resp = await stream.cdf.data(0).get()


    """IPv4 Gateway Address"""
    # An IPv4 gateway configuration specified for the stream.
    await stream.gateway.ipv4.set(gateway=ipaddress.IPv4Address("10.10.10.1"))
    resp = await stream.gateway.ipv4.get()


    """IPv6 Gateway Address"""
    # An IPv6 gateway configuration specified for the stream.
    await stream.gateway.ipv6.set(gateway=ipaddress.IPv6Address("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
    resp = await stream.gateway.ipv6.get()


    """ARP Resolve Peer Address"""
    # Generates an outgoing ARP request on the test port. 
    # The packet header for the stream must contain an IP 
    # protocol segment, and the destination IP address is 
    # used in the ARP request.
    resp = await stream.request.arp.get()
    resp.mac_address


    """PING Check IP Peer"""
    # Generates an outgoing ping request using the ICMP 
    # protocol on the test port. The packet header for 
    # the stream must contain an IP protocol segment, 
    # with valid source and destination IP addresses. 
    resp = await stream.request.ping.get()
    resp.delay
    resp.time_to_live


    """FCS Error Injection"""
    # Force a frame checksum error in one of the packets 
    # currently being transmitted from a stream. 
    await stream.inject_err.frame_checksum.set()


    """Misorder Error Injection"""
    # Force a misorder error by swapping the test payload 
    # sequence numbers in two of the packets currently 
    # being transmitted from a stream. 
    await stream.inject_err.misorder.set()


    """Payload Integrity Error Injection"""
    # Force a payload integrity error in one of the 
    #  packets currently being transmitted from a stream. 
    # Payload integrity validation is only available for 
    # incrementing payloads, and the error is created by 
    # changing a byte from the incrementing sequence. 
    await stream.inject_err.payload_integrity.set()


    """Sequence Error Injection"""
    # Force a sequence error by skipping a test payload 
    # sequence number in one of the packets currently 
    # being transmitted from a stream.
    await stream.inject_err.sequence.set()


    """Test Payload Error Injection"""
    # Force a test payload error in one of the packets 
    # currently being transmitted from a stream. This 
    # means that the test payload will not be recognized 
    # at the receiving port, so it will be counted as a 
    # no-test-payload packet, and there will be a lost 
    # packet for the stream.
    await stream.inject_err.test_payload.set()


    """MODIFIERS"""
    """16/24-bit modifier"""

    """Create modifier"""
    await stream.packet.header.modifiers.configure(number=1)

    """Clear modifiers"""
    await stream.packet.header.modifiers.clear()

    """Obtain modifier object"""
    # Must create modifiers before obtain.
    modifier = stream.packet.header.modifiers.obtain(idx=0)

    """Modifier Range Configuration"""
    # Range specification for a packet modifier for a 
    # stream header, specifying which values the modifier 
    # should take on. This applies only to incrementing 
    # and decrementing modifiers; random modifiers always 
    # produce every possible bit pattern.
    await modifier.range.set(min_val=0, step=10, max_val=9)
    resp = await modifier.range.get()
    resp.min_val
    resp.max_val
    resp.step

    """Modifier Position, Action, Mask"""
    # A packet modifier for a stream header. The headers 
    # of each packet transmitted for the stream will be 
    # varied according to the modifier specification. 
    # This command requires two sub-indices, one for the 
    # stream and one for the modifier.

    # A modifier is positioned at a fixed place in the 
    # header, selects a number of consecutive bits 
    # starting from that position, and applies an action 
    # to those bits in each packet. Packets can be 
    # repeated so that a certain number of identical 
    # packets are transmitted before applying the next 
    # modification.
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.INC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.DEC, repetition=1)
    await modifier.specification.set(position=0, mask=Hex("FFFF0000"), action=enums.ModifierAction.RANDOM, repetition=1)
    
    resp = await modifier.specification.get()
    resp.action
    resp.mask
    resp.position
    resp.repetition

    """Endianness"""
    # Network byte order is Big Endian, where the MSB is 
    # assigned with the smallest address. Xena’s modifier 
    # (16-bit, 24-bit, or 32-bit) inc/dec mode is default 
    # to BIG, which inc/dec starts from the LSB (the 
    # largest address). The user can set the mode to 
    # LITTLE, which the modifier inc/dec starts from the 
    # MSB (the smallest address)
    await modifier.endian.set(mode=enums.ModifierEndianness.BIG)
    await modifier.endian.set(mode=enums.ModifierEndianness.LITTLE)    
    resp = await modifier.endian.get()


    """32-bit modifier"""
    """Create modifier"""
    await stream.packet.header.modifiers_extended.configure(number=1)

    """Clear modifiers"""
    await stream.packet.header.modifiers_extended.clear()

    """Obtain modifier object"""
    # Must create modifiers before obtain.
    modifier_ext = stream.packet.header.modifiers_extended.obtain(idx=0)

    """Modifier Range Configuration"""
    await modifier_ext.range.set(min_val=0, step=1, max_val=100)
    
    resp = await modifier_ext.range.get()
    resp.max_val
    resp.min_val
    resp.step

    """Modifier Position, Action, Mask"""
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.INC, repetition=1)
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.DEC, repetition=1)
    await modifier_ext.specification.set(position=0, mask=Hex("FFFFFFFF"), action=enums.ModifierAction.RANDOM, repetition=1)

    resp = await modifier_ext.specification.get()
    resp.action
    resp.mask
    resp.position
    resp.repetition

    # [end]

