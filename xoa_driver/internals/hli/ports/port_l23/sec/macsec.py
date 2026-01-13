import functools
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    P_MACSEC_RX_ENABLE,
    P_MACSEC_TX_STATS,
    P_MACSEC_TX_CLEAR,
    P_MACSEC_RX_STATS,
    P_MACSEC_RX_CLEAR,
)
from xoa_driver.internals.utils import attributes as utils
from xoa_driver.internals.utils.indices import index_manager as idx_mgr
from xoa_driver.internals.hli.indices.macsecscs.genuine_macsecsc import GenuineMacSecTxScIdx, GenuineMacSecRxScIdx

MacSecTxScIndices = idx_mgr.IndexManager[GenuineMacSecTxScIdx]
MacSecRxScIndices = idx_mgr.IndexManager[GenuineMacSecRxScIdx]

class MACSecTxStats:
    """MACSec TX SC Statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.total = P_MACSEC_TX_STATS(conn, module_id, port_id)
        """Port's total MACsec TX statistics

        :type: P_MACSEC_TX_STATS
        """

        self.clear = P_MACSEC_TX_CLEAR(conn, module_id, port_id)
        """Clear Port's MACsec TX statistics

        :type: P_MACSEC_TX_CLEAR
        """

class MACSecRxStats:
    """MACSec RX SC Statistics"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.total = P_MACSEC_RX_STATS(conn, module_id, port_id)
        """Port's total MACsec RX statistics

        :type: P_MACSEC_RX_STATS
        """

        self.clear = P_MACSEC_RX_CLEAR(conn, module_id, port_id)
        """Clear Port's MACsec RX statistics

        :type: P_MACSEC_RX_CLEAR
        """

class MacSecPortStats:
    """MACSec Port Statistics"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.tx = MACSecTxStats(conn, module_id, port_id)
        """L23 port's MACsec TX statistics.

        :type: MACSecTxStats
        """

        self.rx = MACSecRxStats(conn, module_id, port_id)
        """L23 port's MACsec RX statistics.

        :type: MACSecRxStats
        """


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

        self.statistics = MacSecPortStats(conn, module_id, port_id)
        """L23 port MACSec statistics.
        
        :type: MacSecPortStats
        """

        on_macsec_rx_enable_change = functools.partialmethod(utils.on_event, P_MACSEC_RX_ENABLE)
        """Register a callback to the event that the port MACsec RX enable status changes."""
        