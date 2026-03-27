from xoa_driver import hlfuncs
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
    if not isinstance(module, modules.Z800FreyaModule):
        return

    # [ports]
    """Get Port Object"""
    port = module.ports.obtain(0)

    # [LLDP]
    if isinstance(port, ports.Z800FreyaPort):

        """Create LLDP Agent Object"""
        # Create a LLDP agent representing the LLDP agent on the port.
        lldp_agent = await port.lldp.agents.create()

        """Obtain One or Multiple LLDP Agent Objects"""
        # Obtain already existing LLDP agent object(s) using agent indices.
        lldp_agent = port.lldp.agents.obtain(0)
        lldp_agents = port.lldp.agents.obtain_multiple(*[0,1,2])

        """Sync Existing LLDP Agents from Port to Script"""
        await port.lldp.agents.server_sync()

        """Get LLDP Agent index"""
        lldp_agent.idx

        """Get LLDP Agent's module and port index"""
        lldp_agent.kind.module_id
        lldp_agent.kind.port_id

        """Remove LLDP Agent by Index"""
        # Remove a LLDP agent from the port by its index.
        await port.lldp.agents.remove(position_idx=0)

        """Remove LLDP Agent by Removing the Object"""
        # Remove a LLDP agent from the port by removing the LLDP agent object.
        await lldp_agent.delete()

        """Configure a LLDP Agent time parameters"""
        # Configure the LLDP agent time parameters, including reinit delay, tx interval, tx hold multiplier, and tx delay.
        await lldp_agent.config.set(
            reinit_delay=2,
            tx_interval=5,
            tx_hold_multiplier=4,
            tx_delay=2)
        resp = await lldp_agent.config.get()

        """Configure a LLDP Agent frame header"""
        # Configure the LLDP agent's frame header
        # Here we use the hlfuncs.headers.Ethernet class to create an Ethernet header, and then set the destination MAC address, source MAC address, and ethertype for the LLDP frame header.
        eth = hlfuncs.headers.Ethernet()
        eth.dst_mac = "0180.c200.000e"
        eth.src_mac = "00:11:22:33:44:55"
        eth.ethertype = 0x88cc
        await lldp_agent.header.set(header=Hex(str(eth)))
        resp = await lldp_agent.header.get()

        """Configure a LLDP Agent LLDPDU"""
        # Configure a LLDP agent's LLDPDU, which is the payload of the LLDP frame.
        # HLAPI doesn't have a specific class for LLDPDU, so we can directly set the LLDPDU using a hexadecimal string.
        await lldp_agent.lldpdu.set(Hex("020704000130f9ada0040405312f31060200780000"))
        resp = await lldp_agent.lldpdu.get()

        """Control the LLDP Agent's operation mode"""
        # Control the LLDP agent's operation mode
        await lldp_agent.opmode.set_disable()
        await lldp_agent.opmode.set_tx_only()
        await lldp_agent.opmode.set_rx_only()
        await lldp_agent.opmode.set_tx_rx()
        resp = await lldp_agent.opmode.get()

        """Get LLDP statistics from the port"""
        resp = await port.lldp.statistics.get()

        """Get LLDP neighbor information"""
        resp = await port.lldp.neighbors.get()

        """Clear LLDP counters"""
        await port.lldp.clear.clear_all()
        await port.lldp.clear.clear_neighbor()
        await port.lldp.clear.clear_stats()
        await port.lldp.clear.clear_none()

    # [end]