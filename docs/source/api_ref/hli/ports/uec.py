from xoa_driver.internals.hli.indices.lldp import lldp_agent
from xoa_driver import hlfuncs
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

    """LLR mode - manual configuration"""
    # Manually set the port's LLR mode
    await port.uec.llr.mode.set_on()
    await port.uec.llr.mode.set_off()
    
    """LLR mode - automatic configuration using Link Negotiation"""
    # Auto configure the port's LLR mode based on the link partner's capability using Link Negotiation
    await port.uec.linkneg.link_options.config.set(lldp_agent_index = 0, llr_wanted_local=enums.UecLinkOptionLlr.BI_WANTED)

    """LLR Replay Configuration"""
    # LLR Replay parameters
    await port.uec.llr.configuration.replay.set(
        outstanding_seq_max=524288,
        outstanding_data_max=1000,
        replay_timer_max=32767,
        replay_ct_max=127,
        pcs_lost_status_timer_max=4_000_000_000,
        data_age_timer_max=4_290_000_000
    )
    
    """LLR Transmission Behavior Configuration"""
    # LLR Transmission Behavior Configuration allows you to configure how the LLR transmitter handles protocol events, enabling flexible test scenarios and controlled validation of link behavior.

    await port.uec.llr.configuration.behavior.set(
        llr_init_behavior=enums.UecLlrBehavior.DISCARD,
        llr_flush_behavior=enums.UecLlrBehavior.BEST_EFFORT,
        re_init_on_discard=enums.YesNo.YES
    )
    
    """LLR Initialization Configuration"""
    # Tx LLR_INIT Configuration
    await port.uec.llr.configuration.llr_init.set(
        init_seq="0DADA",
        init_data="FFEE",
        min_spacing_multiplier=4
        )
    
    # Tx LLR_INIT_ECHO Configuration
    await port.uec.llr.configuration.llr_init_echo.set(
        init_seq_mode=enums.UecLlrInitEchoMode.USE_MANUAL,
        init_seq="01234",
        init_data_mode=enums.UecLlrInitEchoMode.USE_LLR_INIT_DATA,
        init_data="0000"
    )
    
    # LLR_INIT_ECHO Validation - no validation needed
    await port.uec.llr.configuration.llr_init_echo_chk.validate_none()
    
    # LLR_INIT_ECHO Validation - validate both init_seq and init_data
    await port.uec.llr.configuration.llr_init_echo_chk.validate_both()
    
    # LLR_INIT_ECHO Validation - validate init_seq only
    await port.uec.llr.configuration.llr_init_echo_chk.validate_init_seq()
    
    # LLR_INIT_ECHO Validation - validate init_data only
    await port.uec.llr.configuration.llr_init_echo_chk.validate_init_data()
    
    """Create stream on port and set LLR desire"""
    # LLR-desired stream
    stream = await port.streams.create()
    await stream.uec.llr.desire.set_llr_eligible()
    
    # LLR-not-desired stream
    await stream.uec.llr.desire.set_llr_ineligible()
    
    
    """LLR Error Injection"""
    # Sequence Drop – Causes the LLR transmitter to skip the next sequence number, simulating a lost frame
    await port.uec.llr.err_inject.inject.inject_seq_drop()
    
    # Sequence Duplicate – Causes the LLR transmitter to retransmit the previous sequence number, simulating a duplicate frame.
    await port.uec.llr.err_inject.inject.inject_seq_duplicate()
    
    # Causes the LLR transmitter to inject an invalid Frame Check Sequence (FCS) into a frame
    await port.uec.llr.err_inject.inject.inject_fcs_bad()

    
    """LLR FSM Statistics"""
    # Tx FSM Stats - current Tx FSM state & accumulated Tx FSM state time
    resp = await port.uec.llr.fsm.tx.get()
    resp.txfsm_state
    resp.ns_in_llr_off
    resp.ns_in_init
    resp.ns_in_advance
    resp.ns_in_replay
    resp.ns_in_flush
    
    # Rx FSM Stats - current Rx FSM state & accumulated Rx FSM state time
    resp = await port.uec.llr.fsm.rx.get()
    resp.rxfsm_state
    resp.ns_in_off
    resp.ns_in_send_acks
    resp.ns_in_send_nack
    resp.ns_in_nack_sent
    

    """Get LLR CtlOS and Traffic Statistics"""
    # Get LLR CtlOS Tx statistics
    resp = await port.uec.ctlos.statistics.tx.get()
    resp.llr_init_cnt
    resp.llr_init_echo_cnt
    resp.llr_ack_cnt
    resp.llr_nack_cnt
    resp.llr_init_seq
    resp.llr_init_data
    resp.llr_init_echo_seq
    resp.llr_init_echo_data

    # Get LLR CtlOS Rx statistics
    resp = await port.uec.ctlos.statistics.rx.get()
    resp.llr_init_cnt
    resp.llr_init_echo_cnt
    resp.llr_ack_cnt
    resp.llr_nack_cnt
    resp.llr_init_seq
    resp.llr_init_data
    resp.llr_init_echo_seq
    resp.llr_init_echo_data
    resp.llr_init_echo_mismatch

    # Get LLR Tx layer-2 statistics
    resp = await port.uec.llr.statistics.tx.get()
    resp.tx_llr_eligible_good_fcs
    resp.tx_llr_eligible_poisoned_fcs
    resp.tx_llr_eligible_bad_fcs
    resp.tx_llr_eligible_discard
    resp.tx_llr_ineligible_good_fcs
    resp.tx_llr_ineligible_bad_fcs
    resp.tx_llr_ineligible_total
    resp.tx_replayed

    # Get LLR Rx layer-2 statistics
    resp = await port.uec.llr.statistics.rx.get()
    resp.rx_llr_eligible_good_fcs
    resp.rx_llr_eligible_poisoned_fcs
    resp.rx_llr_eligible_bad_fcs
    resp.rx_llr_eligible_total
    resp.rx_llr_eligible_good_fcs_exp_seq
    resp.rx_llr_eligible_poisoned_fcs_exp_seq
    resp.rx_llr_eligible_bad_fcs_exp_seq
    resp.rx_llr_eligible_total_exp_seq
    resp.rx_llr_eligible_missing_seq
    resp.rx_llr_eligible_duplicate_seq
    resp.rx_llr_ineligible_good_fcs
    resp.rx_llr_ineligible_bad_fcs
    resp.rx_llr_ineligible_total

    # [end]