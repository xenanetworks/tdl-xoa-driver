from typing import (
    TYPE_CHECKING,
    List,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_UE_LLR_MODE,
    P_UE_LLR_RX_STATS,
    P_UE_LLR_TX_STATS,
    PR_CLEAR,
    PT_CLEAR,
    P_UE_LLR_REPLAY,
    P_UE_LLR_BEHAVIOR,
    P_UE_LLR_INIT,
    P_UE_LLR_INIT_ECHO,
    P_UE_LLR_ACKNACK,
    P_UE_LLR_INJECT_ERR,
    P_UE_LLR_POISONFCS,
    P_UE_LLR_INIT_ECHO_CHK,
    P_UE_LLR_TXFSM_STATE,
    P_UE_LLR_RXFSM_STATE,
    P_UE_LLR_STATUS,
)

class UecLlr:
    """UE LLR Link Layer Retry"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.mode = P_UE_LLR_MODE(conn, module_id, port_id)
        """Get or set the LLR mode of the port.

        :type: P_UE_LLR_MODE
        """

        self.statistics = UecLlrStats(conn, module_id, port_id)
        """UE LLR statistics.

        :type: UecLlrStats
        """
        
        self.status = P_UE_LLR_STATUS(conn, module_id, port_id)
        """UE LLR status. Indicates the link status pertaining to LLR-eligible frames.
        
        :type: P_UE_LLR_STATUS
        """
        
        self.configuration = UecLlrConfig(conn, module_id, port_id)
        """UE LLR configuration.
        
        :type: UecLlrConfig
        """
        
        self.fsm = UecLlrFsm(conn, module_id, port_id)
        """UE LLR FSM status.
        
        :type: UecLlrFsm
        """
        
        self.err_inject = UecLlrErrorInjection(conn, module_id, port_id)
        """UE LLR error injection.
        
        :type: UecLlrErrorInjection
        """
        

class UecLlrStats:
    """UE LLR (Link Layer Retry) statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.rx = P_UE_LLR_RX_STATS(conn, module_id, port_id)
        """UE LLR Rx statistics.

        :type: P_UE_LLR_RX_STATS
        """

        self.tx = P_UE_LLR_TX_STATS(conn, module_id, port_id)
        """UE LLR Tx statistics.

        :type: P_UE_LLR_TX_STATS
        """

        self.clear_tx = PT_CLEAR(conn, module_id, port_id)
        """Clear UE LLR Tx counters in the specified direction(s).
        
        This command also clears L2/L3 Tx traffic statistics of the port.

        :type: PT_CLEAR
        """

        self.clear_rx = PR_CLEAR(conn, module_id, port_id)
        """Clear UE LLR Rx counters in the specified direction(s).

        This command also clears L2/L3 Rx traffic statistics of the port.

        :type: PR_CLEAR
        """
        

class UecLlrConfig:
    """UE LLR (Link Layer Retry) configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.replay = P_UE_LLR_REPLAY(conn, module_id, port_id)
        """UE LLR replay configuration.

        :type: P_UE_LLR_REPLAY
        """
        
        self.behavior = P_UE_LLR_BEHAVIOR(conn, module_id, port_id)
        """UE LLR Tx behavior configuration for state INIT and FLUSH, and LLR replay failure.
        
        :type: P_UE_LLR_BEHAVIOR
        """
        
        self.llr_init = P_UE_LLR_INIT(conn, module_id, port_id)
        """Configures the LLR INIT transmission parameters of the port.

        :type: P_UE_LLR_INIT
        """
        
        self.llr_init_echo = P_UE_LLR_INIT_ECHO(conn, module_id, port_id)
        """Configures the LLR INIT_ECHO transmission parameters of the port.
        
        :type: P_UE_LLR_INIT_ECHO
        """
        
        self.llr_init_echo_chk = P_UE_LLR_INIT_ECHO_CHK(conn, module_id, port_id)
        """Configures the validation of the LLR INIT_ECHO sequence number and data of the port.
        
        :type: P_UE_LLR_INIT_ECHO_CHK
        """
        
        self.llr_acknack = P_UE_LLR_ACKNACK(conn, module_id, port_id)
        """Configures the LLR ACKNACK transmission parameters of the port.
        
        :type: P_UE_LLR_ACKNACK
        """
        

class UecLlrFsm:
    """UE LLR FSM status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.tx = P_UE_LLR_TXFSM_STATE(conn, module_id, port_id)
        """UE LLR Tx FSM state.

        :type: P_UE_LLR_TXFSM_STATE
        """

        self.rx = P_UE_LLR_RXFSM_STATE(conn, module_id, port_id)
        """UE LLR Rx FSM state.

        :type: P_UE_LLR_RXFSM_STATE
        """
        

class UecLlrErrorInjectionConfig:
    """UE LLR error injection configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.poison_fcs = P_UE_LLR_POISONFCS(conn, module_id, port_id)
        """Configures the poison FCS pattern used by the LLR TX error injection of the port.

        :type: P_UE_LLR_POISONFCS
        """

        
class UecLlrErrorInjection:
    """UE LLR error injection"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.configuration = UecLlrErrorInjectionConfig(conn, module_id, port_id)
        """UE LLR error injection configuration.

        :type: UecLlrErrorInjectionConfig
        """

        self.inject = P_UE_LLR_INJECT_ERR(conn, module_id, port_id)
        """UE LLR error injection control.

        :type: P_UE_LLR_INJECT_ERR
        """