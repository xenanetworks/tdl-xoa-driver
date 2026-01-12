import functools
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_MACSEC_RX_ENABLE
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.hli.indices.macsecscs.genuine_macsecsc import GenuineMacSecTxScIdx, GenuineMacSecRxScIdx

MacSecTxScIndices = idx_mgr.IndexManager[GenuineMacSecTxScIdx]
MacSecRxScIndices = idx_mgr.IndexManager[GenuineMacSecRxScIdx]

class MacSec:
    """MACsec configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.txscs: MacSecTxScIndices = idx_mgr.IndexManager(
            conn,
            GenuineMacSecTxScIdx,
            module_id,
            port_id
        )
        """MACSec TX SC index manager.

        :type: MacSecTxScIndices
        """

        self.rxscs: MacSecRxScIndices = idx_mgr.IndexManager(
            conn,
            GenuineMacSecRxScIdx,
            module_id,
            port_id
        )
        """MACSec RX SC index manager.

        :type: MacSecRxScIndices
        """

        self.decode = P_MACSEC_RX_ENABLE(conn, module_id, port_id)
        """L23 port MACSec RX enable.

        :type: P_MACSEC_RX_ENABLE        
        """

        on_macsec_rx_enable_change = functools.partialmethod(utils.on_event, P_MACSEC_RX_ENABLE)
        """Register a callback to the event that the port MACsec RX enable status changes."""
        