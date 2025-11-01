import asyncio
from xoa_driver import testers, modules, ports
from .xoa_cli_manager import XOACLIManager
from typing import Optional, Callable, Union, List, Dict, Any

async def save_port_config(tester: testers.L23Tester, port: ports.GenericL23Port, path: str) -> str:
    
    tester_ip = tester.info.host
    resp = await tester.password.get()
    tester_password = resp.password
    port_index = f"{port.kind.module_id}/{port.kind.port_id}"
    
    # Connect to the tester on tcp port 22611
    xm = XOACLIManager(host=tester_ip, debug=False, halt_on_error=False)

    # Log on and set username
    xm.logon_set_owner(tester_password)

    resp = xm.get_port_full_config(port_index)
    return resp



