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

    """Create stream on port and set LLR desire"""
    # Create a stream on the port and set the LLR desire of the stream to LLR-eligible.
    stream = await port.streams.create()
    await stream.uec.llr.desire.set_llr_eligible()

    """Get LLR statistics"""
    # Get LLR CtlOS Tx statistics
    resp = await port.uec.ctlos.stats.tx.get()
    resp.llr_init_cnt
    resp.llr_init_echo_cnt
    resp.llr_ack_cnt
    resp.llr_nack_cnt
    resp.llr_init_seq
    resp.llr_init_data
    resp.llr_init_echo_seq
    resp.llr_init_echo_data

    # Get LLR CtlOS Rx statistics
    resp = await port.uec.ctlos.stats.rx.get()
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