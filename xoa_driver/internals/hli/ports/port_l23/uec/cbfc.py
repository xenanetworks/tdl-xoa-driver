from typing import (
    TYPE_CHECKING,
    List,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_UE_CBFC_MODE,
    P_UE_CBFC_CCUPDATE_HDR,
    P_UE_CBFC_CCUPDATE_TIMER,
    P_UE_CBFC_CFUPDATE_TIMER,
    P_UE_CBFC_NUMVCS,
    P_UE_CBFC_LINK,
    P_UE_CBFC_VC_STREAMS,
    P_UE_CBFC_VC_TYPE,
    P_UE_CBFC_VC,
    P_UE_CBFC_APPLY,
    P_UE_CBFC_INJECT_ERR,
    P_UE_CBFC_CC_INC,
    P_UE_CBFC_CLEAR,
    P_UE_CBFC_TX_STATS,
    P_UE_CBFC_RX_STATS,
    P_UE_CBFC_RX_ERRORS,
    P_UE_CBFC_VC_TX_STATS,
    P_UE_CBFC_VC_RX_STATS,
)

class UecCbfc:
    """UE CBFC Credit-Based Flow Control."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.mode = P_UE_CBFC_MODE(conn, module_id, port_id)
        """UE CBFC Mode of the port.

        :type: P_UE_CBFC_MODE
        """
        
        self.ccupdate = UecCbfcCcupdate(conn, module_id, port_id)
        """UE CBFC CC_Update configuration of the port.

        :type: UecCbfcCcupdate
        """
        
        self.cfupdate = UecCbfcCfupdate(conn, module_id, port_id)
        """UE CBFC CF_Update configuration of the port.

        :type: UecCbfcCfupdate
        """
        
        self.vc_local_rx_staged = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=0)
        """UE CBFC Local RX Staged VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.vc_local_tx_staged = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=1)
        """UE CBFC Local TX Staged VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.vc_local_rx_active = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=2)
        """UE CBFC Local RX Active VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.vc_local_tx_active = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=3)
        """UE CBFC Local TX Active VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.vc_remote_tx_staged = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=4)
        """UE CBFC Remote TX Staged VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.vc_remote_rx_staged = UecCbfcConfigurationBase(conn, module_id, port_id, storage_index=5)
        """UE CBFC Remote RX Staged VC configuration of the port.

        :type: UecCbfcVcConfiguration
        """
        
        self.apply = P_UE_CBFC_APPLY(conn, module_id, port_id)
        """UE CBFC Apply staged configuration to active VC configuration of the port.

        :type: P_UE_CBFC_APPLY
        """
        

class UecCbfcCcupdate:
    """UE CBFC CC_Update configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.header = P_UE_CBFC_CCUPDATE_HDR(conn, module_id, port_id)
        """UE CBFC CC_Update Header configuration of the port.

        :type: P_UE_CBFC_CCUPDATE_HDR
        """

        self.timer = P_UE_CBFC_CCUPDATE_TIMER(conn, module_id, port_id)
        """UE CBFC CC_Update Timer configuration of the port.

        :type: P_UE_CBFC_CCUPDATE_TIMER
        """


class UecCbfcCfupdate:
    """UE CBFC CF_Update configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.timer = P_UE_CBFC_CFUPDATE_TIMER(conn, module_id, port_id)
        """UE CBFC CF_Update Timer configuration of the port.

        :type: P_UE_CBFC_CFUPDATE_TIMER
        """

        
class UecCbfcConfigurationBase:
    """CBFC VC configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, storage_index: int) -> None:

        self.numvcs = P_UE_CBFC_NUMVCS(conn, module_id, port_id, storage_index)
        """UE CBFC Number of VCs configuration of the port.

        :type: P_UE_CBFC_NUMVCS
        """
        
        self.link_config = P_UE_CBFC_LINK(conn, module_id, port_id, storage_index)
        """UE CBFC Link configuration of the port, including Credit Size, Credit Limit Method, Total Credits, and Packet Overhead.

        :type: P_UE_CBFC_LINK
        """
        
class UecCbfcLocalRxStaged(UecCbfcConfigurationBase):
    """CBFC Local RX Staged configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=0)

        self.vc: Tuple["UecCbfcPerVcConfigurationBase", ...] = tuple(
            UecCbfcPerVcConfigurationBase(conn, module_id, port_id, vc_index=idx, storage_index=0)
            for idx in range(32)
        )
        

        
class UecCbfcLocalTxStaged(UecCbfcConfigurationBase):
    """CBFC Local TX Staged configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=1)

        self.vc: Tuple["UecCbfcPerVcConfigurationBase", ...] = tuple(
            UecCbfcPerVcConfigurationBase(conn, module_id, port_id, vc_index=idx, storage_index=1)
            for idx in range(32)
        )
        
        
        
class UecCbfcLocalRxActive(UecCbfcConfigurationBase):
    """CBFC Local RX Active configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=2)

        self.vc: Tuple["UecCbfcPerVcConfigurationBase", ...] = tuple(
            UecCbfcPerVcConfigurationBase(conn, module_id, port_id, vc_index=idx, storage_index=2)
            for idx in range(32)
        )
        

        
class UecCbfcLocalTxActive(UecCbfcConfigurationBase):
    """CBFC Local TX Active configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=3)

        self.vc: Tuple["UecCbfcPerVcConfigurationTxActive", ...] = tuple(
            UecCbfcPerVcConfigurationTxActive(conn, module_id, port_id, vc_index=idx)
            for idx in range(32)
        )
        
        
class UecCbfcRemoteTxStaged(UecCbfcConfigurationBase):
    """CBFC Remote TX Staged configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=4)

        self.vc: Tuple["UecCbfcPerVcConfigurationBase", ...] = tuple(
            UecCbfcPerVcConfigurationBase(conn, module_id, port_id, vc_index=idx, storage_index=4)
            for idx in range(32)
        )
        
        
        
class UecCbfcRemoteRxStaged(UecCbfcConfigurationBase):
    """CBFC Remote RX Staged configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id, storage_index=5)

        self.vc: Tuple["UecCbfcPerVcConfigurationBase", ...] = tuple(
            UecCbfcPerVcConfigurationBase(conn, module_id, port_id, vc_index=idx, storage_index=5)
            for idx in range(32)
        )

        
        
class UecCbfcPerVcConfigurationBase:
    """CBFC per-VC configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, vc_index: int, storage_index: int) -> None:
        

        self.type = P_UE_CBFC_VC_TYPE(conn, module_id, port_id, vc_index, storage_index)
        """CBFC VC Type configuration of the port.

        :type: P_UE_CBFC_VC_TYPE
        """

        self.config = P_UE_CBFC_VC(conn, module_id, port_id, vc_index, storage_index)
        """CBFC per-VC configuration of the port.

        :type: P_UE_CBFC_VC
        """
        
class UecCbfcPerVcConfigurationTxActive(UecCbfcPerVcConfigurationBase):
    """CBFC per-VC Tx Active configuration of the port."""
    
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, vc_index: int) -> None:
        super().__init__(conn, module_id, port_id, vc_index, storage_index=3)
        
        self.stream_indices = P_UE_CBFC_VC_STREAMS(conn, module_id, port_id, vc_index)
        """CBFC Streams per-VC mapping configuration of the port.

        :type: P_UE_CBFC_VC_STREAMS
        """


class UecCbfcErrorInject:
    """CBFC Error Inject configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.cc_inc = P_UE_CBFC_CC_INC(conn, module_id, port_id)
        """CBFC CC Increment configuration of the port.

        :type: P_UE_CBFC_CC_INC
        """
        
        self.error_inject = P_UE_CBFC_INJECT_ERR(conn, module_id, port_id)
        """CBFC Error Inject configuration of the port.

        :type: P_UE_CBFC_INJECT_ERR
        """
        
class UecCbfcPortStatistics:
    """CBFC Statistics configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.tx = P_UE_CBFC_TX_STATS(conn, module_id, port_id)
        """CBFC TX Statistics configuration of the port.

        :type: P_UE_CBFC_TX_STATS
        """
        
        self.rx = P_UE_CBFC_RX_STATS(conn, module_id, port_id)
        """CBFC RX Statistics configuration of the port.

        :type: P_UE_CBFC_RX_STATS
        """
    
class UecCbfcVcStatistics:
    """CBFC per-VC Statistics configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, vc_index: int) -> None:
        
        self.tx = P_UE_CBFC_VC_TX_STATS(conn, module_id, port_id, vc_index)
        """CBFC per-VC TX Statistics configuration of the port.

        :type: P_UE_CBFC_VC_TX_STATS
        """

        self.rx = P_UE_CBFC_VC_RX_STATS(conn, module_id, port_id, vc_index)
        """CBFC per-VC RX Statistics configuration of the port.

        :type: P_UE_CBFC_VC_RX_STATS
        """
        

class UecCbfcErrorStatistics:
    """CBFC Error Statistics configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.rx = P_UE_CBFC_RX_ERRORS(conn, module_id, port_id)
        """CBFC RX Error Statistics configuration of the port.

        :type: P_UE_CBFC_RX_ERRORS
        """
        

class UecCbfcStats:
    """CBFC overall Statistics configuration of the port."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        
        self.clear = P_UE_CBFC_CLEAR(conn, module_id, port_id)
        """CBFC Clear configuration of the port.

        :type: P_UE_CBFC_CLEAR
        """
        
        self.port = UecCbfcPortStatistics(conn, module_id, port_id)
        """CBFC per-port Statistics configuration of the port.

        :type: UecCbfcPortStatistics
        """

        self.vc: Tuple["UecCbfcVcStatistics", ...] = tuple(
            UecCbfcVcStatistics(conn, module_id, port_id, vc_index=idx)
            for idx in range(32)
        )
        """CBFC per-VC Statistics configuration of the port.

        :type: Tuple["UecCbfcVcStatistics", ...]
        """
        
        self.error = UecCbfcErrorStatistics(conn, module_id, port_id)
        """CBFC Error Statistics configuration of the port.

        :type: UecCbfcErrorStatistics
        """
