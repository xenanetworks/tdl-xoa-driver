################################################################
#
#                   XOA LOW-LEVEL API
#
# This script shows you how to use the low-level API
#
################################################################

import asyncio
from xoa_driver import utils
from xoa_driver.lli import commands as cmd
from xoa_driver.lli import TransportationHandler
from xoa_driver.lli import establish_connection
from xoa_driver import enums

CHASSIS_ADDR = "demo.xenanetworks.com"
USERNAME = "lli_example"
TCP_PORT = 22606
PORT_ID = "0/0"
STREAM_ID = 0
TPLD_ID = 0

async def main(chassis: str, username: str, tcp_port: int, port_id: str, stream_id: int, tpld_id: int, stop_event: asyncio.Event):
    # Connect to chassis                            
    handler = TransportationHandler(enable_logging=False)
    await establish_connection(handler, host=chassis, port=tcp_port)
    await utils.apply(
        cmd.C_LOGON(handler).set("xena"),
        cmd.C_OWNER(handler).set(username),
    )

    # module id and port id
    _mid = int(port_id.split("/")[0])
    _pid = int(port_id.split("/")[1])

    # Reserve port 
    resp = await cmd.P_RESERVATION(handler, _mid, _pid).get()
    if resp.status == enums.ReservedStatus.RESERVED_BY_OTHER:
        await cmd.P_RESERVATION(handler, _mid, _pid).set(enums.ReservedAction.RELINQUISH)
    if resp.status == enums.ReservedStatus.RESERVED_BY_YOU:
        await cmd.P_RESERVATION(handler, _mid, _pid).set(enums.ReservedAction.RELEASE)
    await cmd.P_RESERVATION(handler, _mid, _pid).set(enums.ReservedAction.RESERVE)

    # Set comment for port
    await cmd.P_COMMENT(handler, _mid, _pid).set(comment="My Port")
    
    # Set port into loopback mode, so the traffic sent on the port is looped back to itself
    await cmd.P_LOOPBACK(handler, _mid, _pid).set(loopback=enums.LoopbackMode.TXOFF2RX)

    # Create a stream on port
    await cmd.PS_CREATE(handler, _mid, _pid, stream_id).set()
    
    # Set packet length for the stream to 1000 bytes
    await cmd.PS_PACKETLENGTH(handler,_mid, _pid, stream_id).set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000)
    
    # Set test payload identifier for the stream to 0
    await cmd.PS_TPLDID(handler, _mid, _pid, stream_id).set(test_payload_identifier=tpld_id)

    # Clear stats
    await cmd.PT_CLEAR(handler, _mid, _pid).set()
    await cmd.PR_CLEAR(handler, _mid, _pid).set()
    
    # Start traffic on port
    await cmd.P_TRAFFIC(handler, _mid, _pid,).set(on_off=enums.StartOrStop.START)
    
    # Wait for some time to let the traffic flow
    await asyncio.sleep(5)
    
    # Stop traffic on port
    await cmd.P_TRAFFIC(handler, _mid, _pid,).set(on_off=enums.StartOrStop.STOP)
    
    # Collect stream Tx traffic statistics
    resp = await cmd.PT_STREAM(handler, _mid, _pid, stream_id).get()
    print(resp)
    
    # Collect stream Rx traffic statistics
    resp = await cmd.PR_TPLDTRAFFIC(handler, _mid, _pid, tpld_id).get()
    print(resp)

    # Release port
    await cmd.P_RESERVATION(handler, _mid, _pid).set(enums.ReservedAction.RELEASE)
    
    # Log off and close connection
    await cmd.C_LOGOFF(handler).set()
    handler.close()


if __name__ == "__main__":
    stop_event = asyncio.Event()
    try:
        asyncio.run(main(
            chassis=CHASSIS_ADDR,
            username=USERNAME,
            tcp_port=TCP_PORT,
            port_id=PORT_ID,
            stream_id=STREAM_ID,
            tpld_id=TPLD_ID,
            stop_event=stop_event
        ))
    except KeyboardInterrupt:
        stop_event.set()