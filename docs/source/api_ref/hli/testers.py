import asyncio

from xoa_driver import testers
from xoa_driver import modules
from xoa_driver import ports
from xoa_driver import enums
from xoa_driver import utils
from xoa_driver import misc
from xoa_driver.hlfuncs import mgmt
from xoa_driver.misc import Hex
from xoa_driver.lli import commands
import ipaddress


async def my_awesome_func(stop_event: asyncio.Event):

    #################################################
    #                   Tester                      #
    #################################################
    tester = await testers.L23Tester(
        host="10.10.10.10",
        username="my_name",
        password="xena",
        enable_logging=False)
    
    # Shutdown/Restart
    await tester.down.set(operation=enums.ChassisShutdownAction.POWER_OFF)
    await tester.down.set_poweroff()
    await tester.down.set(operation=enums.ChassisShutdownAction.RESTART)
    await tester.down.set_restart()

    # Flash
    await tester.flash.set(on_off=enums.OnOff.OFF)
    await tester.flash.set_off()
    await tester.flash.set(on_off=enums.OnOff.ON)
    await tester.flash.set_on()

    resp = await tester.flash.get()
    resp.on_off

    # Debug Log
    resp = await tester.debug_log.get()
    resp.data
    resp.message_length

    # IP Address
    await tester.management_interface.ip_address.set(
        ipv4_address=ipaddress.IPv4Address("10.10.10.10"),
        subnet_mask=ipaddress.IPv4Address("255.255.255.0"),
        gateway=ipaddress.IPv4Address("10.10.10.1"))
    
    resp = await tester.management_interface.ip_address.get()
    resp.ipv4_address
    resp.subnet_mask
    resp.gateway

    # MAC Address
    resp = await tester.management_interface.macaddress.get()
    resp.mac_address

    # Hostname
    await tester.management_interface.hostname.set(hostname="name")

    resp = await tester.management_interface.hostname.get()
    resp.hostname

    # DHCP
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.ON)
    await tester.management_interface.dhcp.set_on()
    await tester.management_interface.dhcp.set(on_off=enums.OnOff.OFF)
    await tester.management_interface.dhcp.set_off()

    resp = await tester.management_interface.dhcp.get()
    resp.on_off

    # Capabilities
    resp = await tester.capabilities.get()
    resp.version
    resp.max_name_len
    resp.max_comment_len
    resp.max_password_len
    resp.max_ext_rate
    resp.max_session_count
    resp.max_chain_depth
    resp.max_module_count
    resp.max_protocol_count
    resp.can_stream_based_arp
    resp.can_sync_traffic_start
    resp.can_read_log_files
    resp.can_par_module_upgrade
    resp.can_upgrade_timekeeper
    resp.can_custom_defaults
    resp.max_owner_name_length
    resp.can_read_temperatures
    resp.can_latency_f2f

    # Name
    await tester.name.set(chassis_name="name")

    resp = await tester.name.get()
    resp.chassis_name

    # Password
    await tester.password.set(password="xena")

    resp = await tester.password.get()
    resp.password

    # Description
    await tester.comment.set(comment="description")
    
    resp = await tester.comment.get()
    resp.comment

    # Model
    resp = await tester.model.get()
    resp.model

    # Serial Number
    resp = await tester.serial_no.get()
    resp.serial_number

    # Firmware Version
    resp = await tester.version_no.get()
    resp.chassis_major_version
    resp.pci_driver_version

    resp = await tester.version_no_minor.get()
    resp.chassis_minor_version
    resp.reserved_1
    resp.reserved_2

    # Build String
    resp = await tester.build_string.get()
    resp.build_string

    # Reservation
    await tester.reservation.set(operation=enums.ReservedAction.RELEASE)
    await tester.reservation.set_release()
    await tester.reservation.set(operation=enums.ReservedAction.RELINQUISH)
    await tester.reservation.set_relinquish()
    await tester.reservation.set(operation=enums.ReservedAction.RESERVE)
    await tester.reservation.set_reserve()

    resp = await tester.reservation.get()
    resp.operation

    # Reserved By
    resp = await tester.reserved_by.get()
    resp.username

    # Information
    # The following are pre-fetched in cache when connection is established, thus no need to use await

    tester.session.owner_name
    tester.session.keepalive
    tester.session.pwd
    tester.session.is_online
    tester.session.sessions_info
    tester.session.timeout
    tester.is_released()
    tester.is_reserved_by_me()

    # Logoff
    await tester.session.logoff()

    # Time
    resp = await tester.time.get()
    resp.local_time

    # TimeKeeper Configuration
    await tester.time_keeper.config_file.set(config_file="filename")
    
    resp = await tester.time_keeper.config_file.get()
    resp.config_file

    # TimeKeeper GPS State
    resp = await tester.time_keeper.gps_state.get()
    resp.status

    # TimeKeeper License File
    await tester.time_keeper.license_file.set(license_content="")
    
    resp = await tester.time_keeper.license_file.get()
    resp.license_content

    # TimeKeeper License State
    resp = await tester.time_keeper.license_state.get()
    resp.license_errors
    resp.license_file_state
    resp.license_type

    # TimeKeeper Status
    resp = await tester.time_keeper.status.get()
    resp.status_string

    resp = await tester.time_keeper.status_extended.get()
    resp.status_string

    # Chassis Traffic
    await tester.traffic.set(on_off=enums.OnOff.ON, module_ports=[0,0,0,1])
    await tester.traffic.set(on_off=enums.OnOff.OFF, module_ports=[0,0,0,1])
    await tester.traffic.set_on(module_ports=[0,0,0,1])
    await tester.traffic.set_off(module_ports=[0,0,0,1])

    # Synchronized Chassis Traffic
    await tester.traffic_sync.set(on_off=enums.OnOff.ON, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set(on_off=enums.OnOff.OFF, timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_on(timestamp=1234567, module_ports=[0,0,0,1])
    await tester.traffic_sync.set_off(timestamp=1234567, module_ports=[0,0,0,1])
