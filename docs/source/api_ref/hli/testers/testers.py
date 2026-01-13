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

    """Disconnect Chassis"""
    # Disconnect from the chassis.
    await tester.session.logoff()

    """Shutdown/Restart Chassis"""
    # Shuts down the chassis, and either restarts it 
    # in a clean state or leaves it powered off.
    await tester.down.set_poweroff()
    await tester.down.set_restart()

    """Reserve/Release Chassis"""
    # Reserve or release the chassis.
    await tester.reservation.set_release()
    await tester.reservation.set_relinquish()
    await tester.reservation.set_reserve()
    resp_obj = await tester.reservation.get()

    """Reservation Status"""
    # Get the current reservation status of the chassis.
    resp_obj = await tester.reserved_by.get()

    """Flash LEDs"""
    # Make all the test port LEDs flash on and off with a 1-second interval.
    # This is helpful if you have multiple chassis mounted side by side and you need to identify a specific one.
    await tester.flash.set_off()
    await tester.flash.set_on()
    resp_obj = await tester.flash.get()

    """Management IP Address"""
    # The management IP address of the chassis management port.
    await tester.management_interface.ip_address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.10.1"))
    resp_obj = await tester.management_interface.ip_address.get()

    """Management MAC Address"""
    # Get the MAC address for the chassis management port.
    resp_obj = await tester.management_interface.macaddress.get()
    
    """Management Hostname"""
    # Get or set the chassis hostname used when DHCP is enabled.
    await tester.management_interface.hostname.set(hostname="name")
    resp_obj = await tester.management_interface.hostname.get()

    """Management DHCP"""
    # Controls whether the chassis will use DHCP 
    # to get the management IP address.
    await tester.management_interface.dhcp.set_on()
    await tester.management_interface.dhcp.set_off()
    resp_obj = await tester.management_interface.dhcp.get()

    """Capabilities"""
    # Get the chassis capabilities information.
    resp_obj = await tester.capabilities.get()
    
    """Chassis Name"""
    # The name of the chassis, as it appears at various places in the user interface.
    # The name is also used to distinguish the various chassis contained within a testbed, 
    # and in files containing the configuration for an entire test case.
    await tester.name.set(chassis_name="name")
    resp_obj = await tester.name.get()

    """Chassis Password"""
    # The password of the chassis must be provided 
    # when logging on to the chassis.
    await tester.password.set(password="xena")
    resp_obj = await tester.password.get()

    """Chassis Description"""
    # A text description of the chassis.
    await tester.comment.set(comment="description")
    resp_obj = await tester.comment.get()

    """Chassis Model"""
    # The model of the chassis.
    resp_obj = await tester.model.get()

    """Chassis Serial Number"""
    # The serial number of the chassis.
    resp_obj = await tester.serial_no.get()

    """Chassis Build String"""
    resp_obj = await tester.build_string.get()
    
    """Chassis Version String"""
    # Returns the currently running chassis software version.
    resp_obj = await tester.version_str.get()
    
    """Used TPLD IDs"""
    # Get the used TPLD IDs in the chassis.
    resp_obj = await tester.used_tpld_ids.get()
    
    """Chassis Time"""
    # Get the chassis local time.
    resp_obj = await tester.time.get()

    """Synchronized Port Traffic"""
    # Synchronous traffic control for multiple ports on the same chassis.
    await tester.traffic.set_on(module_ports=[0,0,0,1])
    await tester.traffic.set_off(module_ports=[0,0,0,1])
    
    """Synchronized Chassis Traffic"""
    # Synchronous traffic control for multiple ports on different chassis.
    # This requires all involved chassis to have their internal clocks synchronized.
    await tester.traffic_sync.set_on(timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_off(timestamp=1234567, module_ports=[0,0,0,1])

    # [end]