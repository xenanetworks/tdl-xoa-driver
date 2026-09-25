from xoa_driver.internals.hli.indices.lldp import lldp_agent
from xoa_driver import hlfuncs, headers
import asyncio
from xoa_driver import testers, modules, ports, enums, utils, misc
from xoa_driver.hlfuncs import * 


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
    if not isinstance(module, modules.Z800FreyaModule | modules.Z1600EdunModule):
        return

    # [ports]
    """Get Port Object"""
    port = module.ports.obtain(0)

    """CBFC mode - manual configuration"""
    # Manually set the port's CBFC mode
    await port.uec.cbfc.mode.enable_rx_only()
    await port.uec.cbfc.mode.enable_tx_only()
    await port.uec.cbfc.mode.enable_both()
    await port.uec.cbfc.mode.disable_both()
    
    response = await port.uec.cbfc.mode.get()
    response.rx_mode
    response.tx_mode
    
    """CBFC link message configuration"""
    # CC_Update message header configuration for negative testing
    await port.uec.cbfc.cc_update.header.set(
        dmac="001122334455", 
        smac="001122334455", 
        ethertype="88B5", 
        opcode="FFFE", 
        cid="FA7ACB"
        )
    response = await port.uec.cbfc.cc_update.header.get()
    response.dmac
    response.smac
    response.ethertype
    response.opcode
    response.cid
    
    # CC_Update timer configuration
    await port.uec.cbfc.cc_update.timer.set(
        cc_msg_timer = 5
    )
    response = await port.uec.cbfc.cc_update.timer.get()
    response.cc_msg_timer
    
    
    # CF_Update timer configuration
    await port.uec.cbfc.cf_update.timer.set(
        cf_min_timer = 800,
        cf_max_timer = 16384
    )
    response = await port.uec.cbfc.cf_update.timer.get()
    response.cf_min_timer
    response.cf_max_timer
    
    """CBFC VC configuration"""
    # Local Receiver Staged
    await port.uec.cbfc.vc_local_rx_staged.numvcs.set(num_vcs=4)
    await port.uec.cbfc.vc_local_rx_staged.link_config.set(
        credit_size=64,
        credit_limit_method=enums.UecCbfcCreditLimitMethod.TOTAL,
        total_credit_limit=524287,
        packet_overhead=0
    )
    i = 0
    await port.uec.cbfc.vc_local_rx_staged.vc[i].type.set_best_effort()
    await port.uec.cbfc.vc_local_rx_staged.vc[i].type.set_lossless()
    await port.uec.cbfc.vc_local_rx_staged.vc[i].config.set(
        credit_limit=524287, 
        mapping=enums.UecCbfcVcMapping.VLAN, 
        mask_pcp_dei="F", value_pcp_dei="F", 
        mask_dscp="3F", value_dscp="3F",
        handle=0
    )
        
    # Local Sender Staged
    await port.uec.cbfc.vc_local_tx_staged.numvcs.set(num_vcs=4)
    await port.uec.cbfc.vc_local_tx_staged.link_config.set(
        credit_size=64,
        credit_limit_method=enums.UecCbfcCreditLimitMethod.TOTAL,
        total_credit_limit=524287,
        packet_overhead=0
    )
    i = 0
    await port.uec.cbfc.vc_local_tx_staged.vc[i].type.set_best_effort()
    await port.uec.cbfc.vc_local_tx_staged.vc[i].type.set_lossless()
    await port.uec.cbfc.vc_local_tx_staged.vc[i].config.set(
        credit_limit=524287, 
        mapping=enums.UecCbfcVcMapping.VLAN, 
        mask_pcp_dei="F", value_pcp_dei="F", 
        mask_dscp="3F", value_dscp="3F",
        handle=0
    )
        
    # Apply the Local Receiver Staged to Active
    await port.uec.cbfc.apply.local_rx()

    # Apply the Local Sender Staged to Active
    await port.uec.cbfc.apply.local_tx()
    
    """Streams-to-VCs Mapping"""
    # Create streams on the port
    stream_0 = await port.streams.create()
    await stream_0.packet.length.set_fixed(64, 64)
    await stream_0.packet.header.protocol.set(
        segments = [enums.ProtocolOption.ETHERNET,
                    enums.ProtocolOption.VLAN]
    )
    eth = headers.Ethernet()
    vlan = headers.VLAN()
    eth.dst_mac = "0000.0000.0000"
    eth.src_mac = "0000.0000.0001"
    eth.ethertype = headers.EtherType.VLAN
    vlan.pcp = 7
    vlan.dei = 1
    await stream_0.packet.header.data.set(hex_data=str(eth)+str(vlan))
    
    # Map the created stream to a VC
    await stream_0.uec.cbfc.vc_mapping.set(vc_index=[0])
    
    # Remove the mapping of the stream
    await stream_0.uec.cbfc.vc_mapping.remove_mapping()
    
    """CBFC link message statistics"""
    # CBFC CC_Update Statistics (Rx)
    response = await port.uec.cbfc.statistics.port.rx.get()
    response.cc_update_count
    response.cc_update_interval_avg
    response.cc_update_interval_max
    response.cc_update_interval_min
    
    # CBFC CC_Update Statistics (Tx)
    response = await port.uec.cbfc.statistics.port.tx.get()
    response.cc_update_count
    response.cc_update_interval_avg
    response.cc_update_interval_max
    response.cc_update_interval_min
    
    # CBFC CF_Update Statistics (Rx)
    response = await port.uec.ctlos.statistics.rx.get()
    response.cbfc_cf_update_cnt
    
    # CBFC CF_Update Statistics (Tx)
    response = await port.uec.ctlos.statistics.tx.get()
    response.cbfc_cf_update_cnt
    
    """CBFC VC traffic statistics"""
    # CBFC VC Traffic Statistics (Rx)
    response = await port.uec.cbfc.statistics.vc[0].rx.get()
    response.bits_last_sec
    response.bytes_last_sec
    response.pkts_last_sec
    response.bytes_total
    response.pkts_total
    response.credits_consumed
    response.credits_freed

    # CBFC VC Traffic Statistics (Tx)
    response = await port.uec.cbfc.statistics.vc[0].tx.get()
    response.bits_last_sec
    response.bytes_last_sec
    response.pkts_last_sec
    response.bytes_total
    response.pkts_total
    response.credits_consumed
    response.credits_freed
    
    """CBFC Error Statistics"""
    # CBFC Error Statistics (Rx)
    response = await port.uec.cbfc.statistics.error.rx.get()
    response.lost_credits
    response.cc_update_bad_cid
    response.cc_update_bad_opcode
    response.cc_update_unknown_msg_type
    
    
    """CBFC Error Injection"""
    # Configure CC_Update credit increment
    await port.uec.cbfc.error_injection.cc_update_inc_config.set(vc_index=0, credit_increment=100)
    
    # Inject CBFC errors
    await port.uec.cbfc.error_injection.inject.cc_update_inc()
    await port.uec.cbfc.error_injection.inject.cc_update_bad_fcs()
    await port.uec.cbfc.error_injection.inject.cc_update_poisoned_fcs()
    
    """CBFC statistics clear"""
    # Clear CBFC statistics
    await port.uec.cbfc.statistics.clear.clear_rx()
    await port.uec.cbfc.statistics.clear.clear_tx()
    await port.uec.cbfc.statistics.clear.clear_all()
    await port.uec.cbfc.statistics.clear.clear_none()
    
    """Check streams mapped to Tx VC"""
    # Get the stream indices mapped to a Tx VC
    response = await port.uec.cbfc.vc_local_tx_active.vc[0].stream_indices.get()
    response.stream_indices
    
    
    # [end]