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
    if not isinstance(module, modules.E100ChimeraModule):
        return

    # [chimera ports]
    """Get Port Object"""
    port = module.ports.obtain(0)

    """Link Flap and PMA Error Injection"""
    await port.pcs_pma.link_flap.params.set(duration=100, period=1000, repetition=0)
    await port.pcs_pma.link_flap.enable.set_on()
    await port.pcs_pma.link_flap.enable.set_off()

    await port.pcs_pma.pma_error_inject.params.set(duration=100, period=1000, repetition=0, coeff=100, exp=-4)
    await port.pcs_pma.pma_error_inject.enable.set_on()
    await port.pcs_pma.pma_error_inject.enable.set_off()

    """Enable/Disable Impairment on the Port"""
    # Enable impairment on the port.
    await port.emulate.set_off()
    await port.emulate.set_on()
    resp = await port.emulate.get()

    """TPLD Mode Configuration"""
    # Set TPLD mode
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.NORMAL)
    await port.emulation.tpld_mode.set(mode=enums.TPLDMode.MICRO)
    resp = await port.emulation.tpld_mode.get()

    # [chimera flows]
    """Basic and Extended Flow Filter Configuration"""
    # Configure flow's basic filter on a port
    # Configure flow properties
    flow = port.emulation.flows[1]

    await flow.comment.set(comment="Flow description")
    
    resp = await flow.comment.get()
    resp.comment

    # Initializing the shadow copy of the filter.
    await flow.shadow_filter.initiating.set()

    # Configure shadow filter to BASIC mode
    await flow.shadow_filter.use_basic_mode()
    
    # Query the mode of the filter (either basic or extended)
    filter = await flow.shadow_filter.get_mode()

    if isinstance(filter, misc.BasicImpairmentFlowFilter):
        #------------------
        # Ethernet subfilter
        #------------------
        # Use and configure basic-mode shadow filter's Ethernet subfilter
        await utils.apply(
            filter.ethernet.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.ethernet.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.ethernet.src_address.set(use=enums.OnOff.ON, value=Hex("AAAAAAAAAAAA"), mask=Hex("FFFFFFFFFFFF")),
            filter.ethernet.dest_address.set(use=enums.OnOff.ON, value=Hex("BBBBBBBBBBBB"), mask=Hex("FFFFFFFFFFFF"))
        )

        #------------------
        # Layer 2+ subfilter
        #------------------
        # Not use basic-mode shadow filter's Layer 2+ subfilter
        await filter.l2plus_use.set(use=enums.L2PlusPresent.NA)

        # Use and configure basic-mode shadow filter's Layer2+ subfilter (One VLAN tag)
        await utils.apply(
            filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN1),
            filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.vlan.inner.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF")),
            filter.vlan.inner.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07")),
        )
        # Use and configure basic-mode shadow filter's Layer2+ subfilter (Two VLAN tag)
        await utils.apply(
            filter.l2plus_use.set(use=enums.L2PlusPresent.VLAN2),
            filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.vlan.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.vlan.inner.tag.set(use=enums.OnOff.ON, value=1234, mask=Hex("0FFF")),
            filter.vlan.inner.pcp.set(use=enums.OnOff.OFF, value=3, mask=Hex("07")),
            filter.vlan.outer.tag.set(use=enums.OnOff.ON, value=2345, mask=Hex("0FFF")),
            filter.vlan.outer.pcp.set(use=enums.OnOff.OFF, value=0, mask=Hex("07")),
        )
        # Use and configure basic-mode shadow filter's Layer2+ subfilter (MPLS)
        await utils.apply(
            filter.l2plus_use.set(use=enums.L2PlusPresent.MPLS),
            filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.mpls.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.mpls.label.set(use=enums.OnOff.ON, value=1000, mask=Hex("FFFFF")),
            filter.mpls.toc.set(use=enums.OnOff.ON, value=0, mask=Hex("07")),
        )

        #------------------
        # Layer 3 subfilter
        #------------------
        # Not use basic-mode shadow filter's Layer 3 subfilter
        await filter.l3_use.set(use=enums.L3Present.NA)
        # Use and configure basic-mode shadow filter's Layer 3 subfilter (IPv4)
        await utils.apply(
            filter.l3_use.set(use=enums.L3Present.IP4),
            filter.ip.v4.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.ip.v4.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.ip.v4.src_address.set(use=enums.OnOff.ON, value=ipaddress.IPv4Address("10.0.0.2"), mask=Hex("FFFFFFFF")),
            filter.ip.v4.dest_address.set(use=enums.OnOff.ON, value=ipaddress.IPv4Address("10.0.0.2"), mask=Hex("FFFFFFFF")),
            filter.ip.v4.dscp.set(use=enums.OnOff.ON, value=0, mask=Hex("FC")),
        )
        # Use and configure basic-mode shadow filter's Layer 3 subfilter (IPv6)
        await utils.apply(
            filter.l3_use.set(use=enums.L3Present.IP6),
            filter.ip.v6.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.ip.v6.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.ip.v6.src_address.set(use=enums.OnOff.ON, value=ipaddress.IPv6Address("2001::2"), mask=Hex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")),
            filter.ip.v6.dest_address.set(use=enums.OnOff.ON, value=ipaddress.IPv6Address("2002::2"), mask=Hex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF")),
            filter.ip.v6.traffic_class.set(use=enums.OnOff.ON, value=0, mask=Hex("FC")),
        )

        #------------------
        # Layer 4 subfilter
        #------------------
        # Use and configure basic-mode shadow filter's Layer 4 subfilter (TCP)
        await utils.apply(
            filter.tcp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.tcp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.tcp.src_port.set(use=enums.OnOff.ON, value=1234, mask=Hex("FFFF")),
            filter.tcp.dest_port.set(use=enums.OnOff.ON, value=80, mask=Hex("FFFF")),
        )
        # Use and configure basic-mode shadow filter's Layer 4 subfilter (UDP)
        await utils.apply(
            filter.udp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.udp.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.udp.src_port.set(use=enums.OnOff.ON, value=1234, mask=Hex("FFFF")),
            filter.udp.dest_port.set(use=enums.OnOff.ON, value=80, mask=Hex("FFFF")),
        )

        #------------------
        # Layer Xena subfilter
        #------------------
        await utils.apply(
            filter.tpld.settings.set(action=enums.InfoAction.EXCLUDE),
            filter.tpld.settings.set(action=enums.InfoAction.INCLUDE),
            filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.ON, id = 2),
            filter.tpld.test_payload_filters_config[0].set(use=enums.OnOff.OFF, id = 2),
            filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.ON, id = 4),
            filter.tpld.test_payload_filters_config[1].set(use=enums.OnOff.OFF, id = 4),
            filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.ON, id = 6),
            filter.tpld.test_payload_filters_config[2].set(use=enums.OnOff.OFF, id = 6),
            filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.ON, id = 8),
            filter.tpld.test_payload_filters_config[3].set(use=enums.OnOff.OFF, id = 8),
            filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.ON, id = 10),
            filter.tpld.test_payload_filters_config[4].set(use=enums.OnOff.OFF, id = 10),
            filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.ON, id = 20),
            filter.tpld.test_payload_filters_config[5].set(use=enums.OnOff.OFF, id = 20),
            filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.ON, id = 40),
            filter.tpld.test_payload_filters_config[6].set(use=enums.OnOff.OFF, id = 40),
            filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.ON, id = 60),
            filter.tpld.test_payload_filters_config[7].set(use=enums.OnOff.OFF, id = 60),
            filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.ON, id = 80),
            filter.tpld.test_payload_filters_config[8].set(use=enums.OnOff.OFF, id = 80),
            filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.ON, id = 100),
            filter.tpld.test_payload_filters_config[9].set(use=enums.OnOff.OFF, id = 100),
            filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.ON, id = 102),
            filter.tpld.test_payload_filters_config[10].set(use=enums.OnOff.OFF, id = 102),
            filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.ON, id = 104),
            filter.tpld.test_payload_filters_config[11].set(use=enums.OnOff.OFF, id = 104),
            filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.ON, id = 106),
            filter.tpld.test_payload_filters_config[12].set(use=enums.OnOff.OFF, id = 106),
            filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.ON, id = 108),
            filter.tpld.test_payload_filters_config[13].set(use=enums.OnOff.OFF, id = 108),
            filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.ON, id = 110),
            filter.tpld.test_payload_filters_config[14].set(use=enums.OnOff.OFF, id = 110),
            filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.ON, id = 200),
            filter.tpld.test_payload_filters_config[15].set(use=enums.OnOff.OFF, id = 200),
        )

        #------------------
        # Layer Any subfilter
        #------------------
        await utils.apply(
            filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.EXCLUDE),
            filter.any.settings.set(use=enums.FilterUse.AND, action=enums.InfoAction.INCLUDE),
            filter.any.config.set(position=0, value=Hex("112233445566"), mask=Hex("112233445566"))
        )

    # Apply the filter so the configuration data in the shadow copy is committed to the working copy automatically.
    await flow.shadow_filter.enable.set_off()
    await flow.shadow_filter.enable.set_on()
    await flow.shadow_filter.apply.set()

    # Configure flow's extended filter on a port
    # Configure flow properties
    flow = port.emulation.flows[1]
    await flow.comment.set("Flow description")

    # Initializing the shadow copy of the filter.
    await flow.shadow_filter.initiating.set()

    # Configure shadow filter to EXTENDED mode
    await flow.shadow_filter.use_extended_mode()

    # Query the mode of the filter (either basic or extended)
    filter = await flow.shadow_filter.get_mode()

    if isinstance(filter, misc.ExtendedImpairmentFlowFilter):

        await filter.use_segments(
            enums.ProtocolOption.VLAN
            )
        protocol_segments = await filter.get_protocol_segments()
        await protocol_segments[0].value.set(value=Hex("AAAAAAAAAAAABBBBBBBBBBBB8100"))
        await protocol_segments[0].mask.set(masks=Hex("0000000000000000000000000000"))
        await protocol_segments[1].value.set(value=Hex("0064FFFF"))
        await protocol_segments[1].mask.set(masks=Hex("00000000"))


    """Impairment Distribution Configuration for Different Impairment Types"""
    # Configure impairment - Drop
    # Fixed Burst distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.fixed_burst.set(burst_size=5),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=5), #repeat (duration = 1, period = x)
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=0), #one shot
    )

    # Random Burst distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.random_burst.set(minimum=1, maximum=10, probability=10_000),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Fixed Rate distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.fixed_rate.set(probability=10_000),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Bit Error Rate distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.bit_error_rate.set(coef=1, exp=1),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Random Rate distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.random_rate.set(probability=10_000),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gilbert Elliot distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Uniform distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.uniform.set(minimum=1, maximum=1),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gaussian distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.gaussian.set(mean=1, std_deviation=1),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Poisson distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.poisson.set(mean=9),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gamma distribution for impairment Drop
    await utils.apply(
        flow.impairment_distribution.drop_type_config.gamma.set(shape=1, scale=1),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Custom distribution for impairment Drop
    data_x=[0, 1] * 256
    await port.custom_distributions.assign(0)
    await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
    await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
    await utils.apply(
        flow.impairment_distribution.drop_type_config.custom.set(cust_id=0),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=1, period=1),
        flow.impairment_distribution.drop_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Set distribution and start impairment Drop
    await flow.impairment_distribution.drop_type_config.enable.set_on()
    await flow.impairment_distribution.drop_type_config.enable.set_off()
    
    
    # Configure impairment - Misordering
    # Fixed Burst distribution for impairment Misordering
    # dist = distributions.misordering.FixedBurst(burst_size=1)
    # dist.repeat(period=5)
    # dist.one_shot()

    # Fixed Burst distribution for impairment Misordering
    await utils.apply(
        flow.impairment_distribution.misorder_type_config.fixed_burst.set(burst_size=5),
        flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=5), #repeat
        flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=0), #one shot
    )

    # Fixed Rate distribution for impairment Misordering
    await utils.apply(
        flow.impairment_distribution.misorder_type_config.fixed_rate.set(probability=10_000),
        flow.impairment_distribution.misorder_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.misorder_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Set distribution and start impairment Misordering
    await flow.misordering.set(depth=1)
    await flow.impairment_distribution.misorder_type_config.enable.set_on()
    await flow.impairment_distribution.misorder_type_config.enable.set_off()


    # Configure impairment - Latency & Jitter
    # Fixed Burst distribution for impairment Latency & Jitter
    await flow.impairment_distribution.latency_jitter_type_config.constant_delay.set(delay=100)

    # Random Burst distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.accumulate_and_burst.set(delay=1300),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=1, period=0), #one shot
    )

    # Step distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.step.set(low=1300, high=77000),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )
    await flow.impairment_distribution.corruption_type_config.off.set()

    # Uniform distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.uniform.set(minimum=1, maximum=1),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gaussian distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.gaussian.set(mean=1, std_deviation=1),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )

    resp = await flow.latency_range.get()
    resp.min
    resp.max
    

    # Poisson distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.poisson.set(mean=1),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gamma distribution for impairment Latency & Jitter
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.gamma.set(shape=1, scale=1),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Custom distribution for impairment Latency & Jitter
    data_x=[0, 1] * 256
    await port.custom_distributions.assign(0)
    await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
    await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
    await utils.apply(
        flow.impairment_distribution.latency_jitter_type_config.custom.set(cust_id=0),
        flow.impairment_distribution.latency_jitter_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Set distribution and start impairment Latency & Jitter
    await flow.impairment_distribution.latency_jitter_type_config.enable.set_on()
    await flow.impairment_distribution.latency_jitter_type_config.enable.set_off()


    # Configure impairment - Duplication
    # Fixed Burst distribution for impairment Duplication
    # dist.one_shot()
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.fixed_burst.set(burst_size=1300),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=0), #one shot
    )

    # Random Burst distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.random_burst.set(minimum=1, maximum=1, probability=10_0000),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Fixed Rate distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.fixed_rate.set(probability=10_000),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Bit Error Rate distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.bit_error_rate.set(coef=1, exp=1),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Random Rate distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.random_rate.set(probability=10_000),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gilbert Elliot distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Uniform distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.uniform.set(minimum=1, maximum=1),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gaussian distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.gaussian.set(mean=1, std_deviation=1),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Poisson distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.poisson.set(mean=9),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gamma distribution for impairment Duplication
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.gamma.set(shape=1, scale=1),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Custom distribution for impairment Duplication
    data_x=[0, 1] * 256
    await port.custom_distributions.assign(0)
    await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
    await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
    await utils.apply(
        flow.impairment_distribution.duplication_type_config.custom.set(cust_id=0),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=1, period=1),
        flow.impairment_distribution.duplication_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Set distribution and start impairment Duplication
    await flow.impairment_distribution.duplication_type_config.enable.set_on()
    await flow.impairment_distribution.duplication_type_config.enable.set_off()


    # Configure impairment - Corruption
    # Fixed Burst distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.fixed_burst.set(burst_size=1300),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), #repeat (duration = 1, period = x)
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=0), #one shot
    )
    # Random Burst distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.random_burst.set(minimum=1, maximum=1, probability=10_0000),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Fixed Rate distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.fixed_rate.set(probability=10_000),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Bit Error Rate distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.bit_error_rate.set(coef=1, exp=1),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Random Rate distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.random_rate.set(probability=10_000),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gilbert Elliot distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.ge.set(good_state_prob=0, good_state_trans_prob=0, bad_state_prob=0, bad_state_trans_prob=0),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Uniform distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.uniform.set(minimum=1, maximum=1),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gaussian distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.gaussian.set(mean=1, std_deviation=1),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),# repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Poisson distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.poisson.set(mean=9),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Gamma distribution for impairment Corruption
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.gamma.set(shape=1, scale=1),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1), # repeat pattern
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )


    # Custom distribution for impairment Corruption
    data_x=[0, 1] * 256
    await port.custom_distributions.assign(0)
    await port.custom_distributions[0].comment.set(comment="Example Custom Distribution")
    await port.custom_distributions[0].definition.set(linear=enums.OnOff.OFF, symmetric=enums.OnOff.OFF, entry_count=len(data_x), data_x=data_x)
    await utils.apply(
        flow.impairment_distribution.corruption_type_config.custom.set(cust_id=0),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=1, period=1),
        flow.impairment_distribution.corruption_type_config.schedule.set(duration=0, period=0), #continuous
    )

    # Set distribution and start impairment Corruption
    await flow.corruption.set(corruption_type=enums.CorruptionType.OFF)
    await flow.corruption.set(corruption_type=enums.CorruptionType.ETH)
    await flow.corruption.set(corruption_type=enums.CorruptionType.IP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.TCP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.UDP)
    await flow.corruption.set(corruption_type=enums.CorruptionType.BER)
    await flow.impairment_distribution.corruption_type_config.enable.set_on()
    await flow.impairment_distribution.corruption_type_config.enable.set_off()

    await flow.impairment_distribution.corruption_type_config.enable.set_on()

    resp = await flow.impairment_distribution.corruption_type_config.one_shot_status.get()
    resp.one_shot_status


    # Configure bandwidth control - Policer
    await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000)
    await flow.bandwidth_control.policer.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000)


    # Configure bandwidth control - Shaper
    # Set and start bandwidth control Shaper
    await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L1, cir=10_000, cbs=1_000, buffer_size=1_000)
    await flow.bandwidth_control.shaper.set(on_off=enums.OnOff.ON, mode=enums.PolicerMode.L2, cir=10_000, cbs=1_000, buffer_size=1_000)


    """Per-Flow Impairment Statistics"""
    # Flow Rx statistics
    rx_total = await flow.statistics.rx.total.get()
    rx_total.byte_count
    rx_total.packet_count
    rx_total.l2_bps
    rx_total.pps

    # Flow Tx statistics
    tx_total = await flow.statistics.tx.total.get()
    tx_total.byte_count
    tx_total.packet_count
    tx_total.l2_bps
    tx_total.pps

    # Flow overall statistics
    flow_drop_total = await flow.statistics.total.drop_packets.get()
    flow_drop_total.pkt_drop_count_total
    flow_drop_total.pkt_drop_count_programmed
    flow_drop_total.pkt_drop_count_bandwidth
    flow_drop_total.pkt_drop_count_other
    flow_drop_total.pkt_drop_ratio_total
    flow_drop_total.pkt_drop_ratio_programmed
    flow_drop_total.pkt_drop_ratio_bandwidth
    flow_drop_total.pkt_drop_ratio_other

    # Flow corrupted statistics
    flow_corrupted_total = await flow.statistics.total.corrupted_packets.get()
    flow_corrupted_total.fcs_corrupted_pkt_count
    flow_corrupted_total.fcs_corrupted_pkt_ratio
    flow_corrupted_total.ip_corrupted_pkt_count
    flow_corrupted_total.ip_corrupted_pkt_ratio
    flow_corrupted_total.tcp_corrupted_pkt_count
    flow_corrupted_total.tcp_corrupted_pkt_ratio
    flow_corrupted_total.total_corrupted_pkt_count
    flow_corrupted_total.total_corrupted_pkt_ratio
    flow_corrupted_total.udp_corrupted_pkt_count
    flow_corrupted_total.udp_corrupted_pkt_ratio

    # Flow latency and jitter statistics
    flow_delayed_total = await flow.statistics.total.latency_packets.get()
    flow_delayed_total.pkt_count
    flow_delayed_total.ratio

    flow_jittered_total = await flow.statistics.total.jittered_packets.get()
    flow_jittered_total.pkt_count
    flow_jittered_total.ratio

    # Flow duplication and misordering statistics
    flow_duplicated_total = await flow.statistics.total.duplicated_packets.get()
    flow_duplicated_total.pkt_count
    flow_duplicated_total.ratio

    flow_misordered_total = await flow.statistics.total.mis_ordered_packets.get()
    flow_misordered_total.pkt_count
    flow_misordered_total.ratio

    # Clear flow statistics
    await flow.statistics.tx.clear.set()
    await flow.statistics.rx.clear.set()
    await flow.statistics.clear.set()
    

    """Per-Port Impairment Statistics"""
    # Port statistics
    # Port drop statistics
    port_drop = await port.emulation.statistics.drop.get()
    port_drop.pkt_drop_count_total
    port_drop.pkt_drop_count_programmed
    port_drop.pkt_drop_count_bandwidth
    port_drop.pkt_drop_count_other
    port_drop.pkt_drop_ratio_total
    port_drop.pkt_drop_ratio_programmed
    port_drop.pkt_drop_ratio_bandwidth
    port_drop.pkt_drop_ratio_other

    # Port corrupt statistics
    port_corrupted = await port.emulation.statistics.corrupted.get()
    port_corrupted.fcs_corrupted_pkt_count
    port_corrupted.fcs_corrupted_pkt_ratio
    port_corrupted.ip_corrupted_pkt_count
    port_corrupted.ip_corrupted_pkt_ratio
    port_corrupted.tcp_corrupted_pkt_count
    port_corrupted.tcp_corrupted_pkt_ratio
    port_corrupted.total_corrupted_pkt_count
    port_corrupted.total_corrupted_pkt_ratio
    port_corrupted.udp_corrupted_pkt_count
    port_corrupted.udp_corrupted_pkt_ratio

    # Port latency and jitter statistics
    port_delayed = await port.emulation.statistics.latency.get()
    port_delayed.pkt_count
    port_delayed.ratio

    port_jittered = await port.emulation.statistics.jittered.get()
    port_jittered.pkt_count
    port_jittered.ratio

    # Port duplication and misordering statistics
    port_duplicated = await port.emulation.statistics.duplicated.get()
    port_duplicated.pkt_count
    port_duplicated.ratio

    port_misordered = await port.emulation.statistics.mis_ordered.get()
    port_misordered.pkt_count
    port_misordered.ratio

    # Clear port statistics
    await port.emulation.clear.set()

    # [end]