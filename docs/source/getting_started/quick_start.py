################################################################
#
#                   QUICK START
#
# What this script example does:
# 1. Connect to a tester
# 2. Reserve a port as TX and another one as RX
# 3. Configure TX port
# 4. Configure a stream on the TX port
# 5. Start traffic on the TX port
# 6. Wait for 10 seconds
# 7. Collect statistics on the TX port
# 8. Collect statistics on the RX port
# 9. Release the ports
# 10. Disconnect from the chassis
#
################################################################

import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver.hlfuncs import mgmt, headers
from xoa_driver.misc import Hex
import ipaddress
import logging

#---------------------------
# GLOBAL PARAMS
#---------------------------
CHASSIS_IP = "demo.xenanetworks.com"
USERNAME = "quick_start"
PORT1 = "0/0"
PORT2 = "0/1"

async def my_awesome_func(chassis: str, username: str, port_str1: str, port_str2: str):
    # configure basic logger
    logging.basicConfig(
        format="%(asctime)s  %(message)s",
        level=logging.DEBUG,
        handlers=[
            logging.FileHandler(filename="test.log", mode="a"),
            logging.StreamHandler()]
        )
    
    # Establish connection to a Valkyrie tester using Python context manager
    # The connection will be automatically terminated when it is out of the block
    async with testers.L23Tester(host=chassis, username=username, password="xena", port=22606, enable_logging=False) as tester:
        logging.info(f"===================================")
        logging.info(f"{'Connect to chassis:':<20}{chassis}")
        logging.info(f"{'Username:':<20}{username}")

        # Access modules on the tester
        _mid1 = int(port_str1.split("/")[0])
        _pid1 = int(port_str1.split("/")[1])
        _mid2 = int(port_str2.split("/")[0])
        _pid2 = int(port_str2.split("/")[1])
        module_obj1 = tester.modules.obtain(_mid1)
        module_obj2 = tester.modules.obtain(_mid2)

        if isinstance(module_obj1, modules.E100ChimeraModule):
            return None # commands which used in this example are not supported by Chimera Module
        if isinstance(module_obj2, modules.E100ChimeraModule):
            return None # commands which used in this example are not supported by Chimera Module

        # Get the port on module as TX port
        tx_port = module_obj1.ports.obtain(_pid1)

        # Get the port on module as RX port
        rx_port = module_obj2.ports.obtain(_pid2)

        # Forcibly reserve the ports and reset
        await mgmt.reserve_port(tx_port, reset=True)
        await mgmt.reserve_port(rx_port, reset=True)

        await asyncio.sleep(2)

        #################################################
        #           TX Port Configuration               #
        #################################################
        # Simple batch configure the TX port
        await utils.apply(
            tx_port.comment.set(comment="this is tx port"),
            tx_port.ifg.set(min_byte_count=20),
            tx_port.loop_back.set(mode=enums.LoopbackMode.NONE),
            tx_port.tx_config.packet_limit.set(packet_count_limit=1_000_000),
            tx_port.tx_config.enable.set(on_off=enums.OnOff.ON),
            tx_port.net_config.mac_address.set(mac_address=Hex("BBBBBBBBBBBB")),
            tx_port.net_config.ipv4.address.set(
                ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
                subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
                gateway=ipaddress.IPv4Address("10.10.10.1"),
                wild=ipaddress.IPv4Address("0.0.0.0")),
            # for more port configuration, please go to https://docs.xenanetworks.com/projects/xoa-python-api
        )

        #################################################
        #           Stream Configuration                #
        #################################################

        # Create a stream on the port
        # Stream index is automatically assigned
        my_stream = await tx_port.streams.create()
        stream_index = my_stream.idx
        logging.info(f"TX stream index: {stream_index}")

        eth = headers.Ethernet()
        eth.dst_mac = "aaaa.aaaa.aaaa"
        eth.src_mac = "bbbb.bbbb.bbbb"
        eth.ethertype = headers.EtherType.VLAN
        vlan = headers.VLAN()
        vlan.id = 100
        vlan.type = headers.EtherType.IPv4
        ip = headers.IPV4()
        ip.proto = headers.IPProtocol.NONE
        ip.src = "10.10.10.10"
        ip.dst = "11.11.11.11"
        ip.total_length = 1000 - int(len(str(eth))/2) - int(len(str(vlan))/2) - 4

        # Simple batch configure the stream on the TX port
        await utils.apply(
            my_stream.tpld_id.set(test_payload_identifier=0),
            my_stream.enable.set_on(),
            my_stream.comment.set(comment="this is a stream"),
            my_stream.payload.content.set(payload_type=enums.PayloadType.PATTERN, hex_data=Hex("DEAD")),
            my_stream.rate.pps.set(stream_rate_pps=100_000),
            my_stream.packet.length.set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000),
            my_stream.packet.header.protocol.set(segments=[
                enums.ProtocolOption.ETHERNET,
                enums.ProtocolOption.VLAN,
                enums.ProtocolOption.IP]),
            my_stream.packet.header.data.set(hex_data=Hex(str(eth)+str(vlan)+str(ip)))
            # for more stream configuration, please go to https://docs.xenanetworks.com/projects/xoa-python-api
        )

        #################################################
        #               Traffic Control                 #
        #################################################

        # Batch clear statistics on TX and RX ports
        await asyncio.gather(
            tx_port.statistics.tx.clear.set(),
            tx_port.statistics.rx.clear.set(),
            rx_port.statistics.tx.clear.set(),
            rx_port.statistics.rx.clear.set()
        )
        
        # Start traffic on the TX port
        await tx_port.traffic.state.set_start()

        # Test duration 10 seconds
        await asyncio.sleep(10)

        # Stop traffic on the TX port
        await tx_port.traffic.state.set_stop()

        # Wait 2 seconds for the counters to finish
        await asyncio.sleep(2)

        #################################################
        #                  Statistics                   #
        #################################################

        # Query TX statistics
        tx_total, tx_stream = await utils.apply(
            # port level statistics
            tx_port.statistics.tx.total.get(),

            # stream level statistics
            # let the resource manager tell you the stream index so you don't have to remember it
            tx_port.statistics.tx.obtain_from_stream(my_stream).get()
        )
        logging.info(f"Total TX byte count since cleared: {tx_total.byte_count_since_cleared}")
        logging.info(f"Total TX packet count since cleared: {tx_total.packet_count_since_cleared}")
        logging.info(f"Stream {my_stream.idx} TX byte count since cleared: {tx_stream.byte_count_since_cleared}")
        logging.info(f"Stream {my_stream.idx} TX packet count since cleared: {tx_stream.packet_count_since_cleared}")

        # if you have forgot what TPLD ID assigned to a stream, you can query it
        resp = await my_stream.tpld_id.get()
        tpld_id = resp.test_payload_identifier

        received_tplds = await rx_port.statistics.rx.obtain_available_tplds()
        for i in received_tplds:
            logging.info(f"RX TPLD index: {i}")

        # then access the RX stat object
        rx_stats_obj = rx_port.statistics.rx.access_tpld(tpld_id)

        # then query each stats of a TPLD ID
        rx_total, rx_traffic, rx_latency, rx_jitter, rx_error = await utils.apply(
            # port level statistics
            rx_port.statistics.rx.total.get(),

            # tpld level traffic stats
            rx_stats_obj.traffic.get(),

            # tpld level latency stats
            rx_stats_obj.latency.get(),

            # tpld level jitter stats
            rx_stats_obj.jitter.get(),

            # tpld level error stats
            rx_stats_obj.errors.get()
        )

        logging.info(f"Total RX byte count since cleared: {rx_total.byte_count_since_cleared}")
        logging.info(f"Total RX packet count since cleared: {rx_total.packet_count_since_cleared}")
        logging.info(f"TPLD {tpld_id} RX byte count since cleared: {rx_traffic.byte_count_since_cleared}")
        logging.info(f"TPLD {tpld_id} RX packet count since cleared: {rx_traffic.packet_count_since_cleared}")
        logging.info(f"TPLD {tpld_id} RX min latency: {rx_latency.min_val}")
        logging.info(f"TPLD {tpld_id} RX max latency: {rx_latency.max_val}")
        logging.info(f"TPLD {tpld_id} RX avg latency: {rx_latency.avg_val}")
        logging.info(f"TPLD {tpld_id} RX min jitter: {rx_jitter.min_val}")
        logging.info(f"TPLD {tpld_id} RX max jitter: {rx_jitter.max_val}")
        logging.info(f"TPLD {tpld_id} RX avg jitter: {rx_jitter.avg_val}")
        logging.info(f"TPLD {tpld_id} RX Lost Packets: {rx_error.non_incre_seq_event_count}")
        logging.info(f"TPLD {tpld_id} RX Misordered: {rx_error.swapped_seq_misorder_event_count}")
        logging.info(f"TPLD {tpld_id} RX Payload Errors: {rx_error.non_incre_payload_packet_count}")

        #################################################
        #                  Release                      #
        #################################################
        # Release the ports
        await mgmt.release_ports(tx_port, rx_port)

async def main():
    stop_event = asyncio.Event()
    try:
        await my_awesome_func(
            chassis=CHASSIS_IP,
            username=USERNAME,
            port_str1=PORT1,
            port_str2=PORT2
        )
    except KeyboardInterrupt:
        stop_event.set()


if __name__ == "__main__":
    asyncio.run(main())
