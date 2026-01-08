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

    
    """Module Reservation"""
    # Reserve or release the module.
    await module.reservation.set_release()
    await module.reservation.set_relinquish()
    await module.reservation.set_reserve()
    resp_obj = await module.reservation.get()
    
    """Module Reserved By"""
    # Get the current reservation status of the module.
    resp_obj = await module.reserved_by.get()


    """Module Capabilities"""
    # Get the module capabilities information.
    resp_obj = await module.capabilities.get()


    """Module Name"""
    # The name of the module, as it appears at various places in the user interface.
    resp_obj = await module.name.get()


    """Module Description"""
    # A text description of the module.
    await module.comment.set(comment="description")
    resp_obj = await module.comment.get()


    """Legacy Model"""
    # Get the legacy model of the module, e.g. "MFREYA-800G-4S-1P"
    resp_obj = await module.model.get()


    """Module Revision"""
    # Get the hardware revision of the module, e.g. "Freya-800G-1S-1P [a]"
    resp_obj = await module.revision.get()


    """Module Serial Number"""
    # Get the serial number of the module.
    resp_obj = await module.serial_number.get()


    """Firmware Version"""
    # Get the firmware version of the module.
    resp_obj = await module.version_number.get()


    """Module Port Count"""
    # Get the number of ports on the module.
    resp_obj = await module.port_count.get()


    """Module Status"""
    # Get the temperature status of the module.
    resp_obj = await module.status.get()


    """Supported Configurations"""
    # Get the supported media configurations of the module.
    resp_obj = await module.supported_configs.get()


    """Module Media Configuration"""
    # The media configuration of the module.
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP_1600)
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP_1600_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD800)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD800_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP800)
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP800_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP112)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP112_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP28_NRZ)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP28_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP56_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD_NRZ)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP112)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP28)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP56)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFPDD)
    await module.config.media.set(media_config=enums.MediaConfigurationType.BASE_T1)
    await module.config.media.set(media_config=enums.MediaConfigurationType.BASE_T1S)
    resp_obj = await module.config.media.get()

    
    """Module Port Speed Configuration"""
    # The port speed configuration of the module.
    await module.config.port_speed.set(portspeed_list=[1, 800_000])
    await module.config.port_speed.set(portspeed_list=[2, 400_000, 400_000])
    await module.config.port_speed.set(portspeed_list=[4, 200_000, 200_000, 200_000, 200_000])
    await module.config.port_speed.set(portspeed_list=[8, 100_000, 100_000, 100_000, 100_000, 100_000, 100_000, 100_000, 100_000])
    resp_obj = await module.config.port_speed.get()

    """TX Clock Filter Loop Bandwidth"""
    # Set or get the TX clock filter loop bandwidth.
    await module.advanced_timing.clock_tx.filter.set_bw103hz()
    await module.advanced_timing.clock_tx.filter.set_bw1683hz()
    await module.advanced_timing.clock_tx.filter.set_bw207hz()
    await module.advanced_timing.clock_tx.filter.set_bw416hz()
    await module.advanced_timing.clock_tx.filter.set_bw7019hz()
    resp_obj = await module.advanced_timing.clock_tx.filter.get()


    """TX Clock Source"""
    # Set or get the TX clock source.
    await module.advanced_timing.clock_tx.source.set_modulelocalclock()
    await module.advanced_timing.clock_tx.source.set_p0rxclk()
    await module.advanced_timing.clock_tx.source.set_p1rxclk()
    await module.advanced_timing.clock_tx.source.set_p2rxclk()
    await module.advanced_timing.clock_tx.source.set_p3rxclk()
    await module.advanced_timing.clock_tx.source.set_p4rxclk()
    await module.advanced_timing.clock_tx.source.set_p5rxclk()
    await module.advanced_timing.clock_tx.source.set_p6rxclk()
    await module.advanced_timing.clock_tx.source.set_p7rxclk()
    resp_obj = await module.advanced_timing.clock_tx.source.get()


    """TX Clock Status"""
    # Get the TX clock status.
    resp_obj = await module.advanced_timing.clock_tx.status.get()


    """SMA Status"""
    # Get the SMA status.
    resp_obj = await module.advanced_timing.sma.status.get()


    """SMA Input"""
    # Set or get the SMA input.
    await module.advanced_timing.sma.input.set_notused()
    await module.advanced_timing.sma.input.set_tx10mhz()
    await module.advanced_timing.sma.input.set_tx2mhz()
    resp_obj = await module.advanced_timing.sma.input.get()


    """SMA Output"""
    # Set or get the SMA output.
    await module.advanced_timing.sma.output.set_disabled()
    await module.advanced_timing.sma.output.set_p0rxclk()
    await module.advanced_timing.sma.output.set_p0rxclk2mhz()
    await module.advanced_timing.sma.output.set_p0sof()
    await module.advanced_timing.sma.output.set_p1rxclk()
    await module.advanced_timing.sma.output.set_p1rxclk2mhz()
    await module.advanced_timing.sma.output.set_p1sof()
    await module.advanced_timing.sma.output.set_passthrough()
    await module.advanced_timing.sma.output.set_ref10mhz()
    await module.advanced_timing.sma.output.set_ref125mhz()
    await module.advanced_timing.sma.output.set_ref156mhz()
    await module.advanced_timing.sma.output.set_ref2mhz()
    await module.advanced_timing.sma.output.set_ts_pps()
    resp_obj = await module.advanced_timing.sma.output.get()


    """Local Clock Adjust"""
    # Set or get the local clock adjustment in parts per billion (ppb).
    await module.timing.clock_local_adjust.set(ppb=10)
    resp_obj = await module.timing.clock_local_adjust.get()


    """Clock Sync Status"""
    # Get the clock synchronization status.
    resp_obj = await module.timing.clock_sync_status.get()


    """Clock Source"""
    # Set or get the clock source.
    await module.timing.source.set_chassis()
    await module.timing.source.set_external()
    await module.timing.source.set_module()
    resp_obj = await module.timing.source.get()


    # [Z800 Freya and Z1600 Edun Specific APIs]
    if isinstance(module, modules.Z800FreyaModule) or isinstance(module, modules.Z1600EdunModule):

        """Clock PPM Sweep Configuration"""
        # Set or get the clock PPM sweep configuration.
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.NONE, ppb_step=10, step_delay=10, max_ppb=10, loops=1)
        await module.clock_sweep.config.set(mode=enums.PPMSweepMode.TRIANGLE, ppb_step=10, step_delay=10, max_ppb=10, loops=1)
        resp_obj = await module.clock_sweep.config.get()

        """Clock PPM Sweep Status"""
        # Get the clock PPM sweep status.
        resp_obj = await module.clock_sweep.status.get()
    

    # [E100 Chimera Specific APIs]
    if isinstance(module, modules.E100ChimeraModule):
        
        """Chimera - Bypass Mode"""
        # Set or get the module bypass mode.
        await module.emulator_bypass_mode.set_on()
        await module.emulator_bypass_mode.set_off()
        resp_obj = await module.emulator_bypass_mode.get()

        """Chimera - Latency Mode"""
        # Set or get the module latency mode.
        await module.latency_mode.set_normal()
        await module.latency_mode.set_extended()
        resp_obj = await module.latency_mode.get()

        """Chimera - TX Clock Source"""
        # Set or get the TX clock source.
        await module.tx_clock.source.set_modulelocalclock()
        await module.tx_clock.source.set_p0rxclk()
        await module.tx_clock.source.set_p1rxclk()
        await module.tx_clock.source.set_p2rxclk()
        await module.tx_clock.source.set_p3rxclk()
        await module.tx_clock.source.set_p4rxclk()
        await module.tx_clock.source.set_p5rxclk()
        await module.tx_clock.source.set_p6rxclk()
        await module.tx_clock.source.set_p7rxclk()
        resp_obj = await module.tx_clock.source.get()

        """Chimera - TX Clock Status"""
        # Get the TX clock status.
        resp_obj = await module.tx_clock.status.get()

    # [end]