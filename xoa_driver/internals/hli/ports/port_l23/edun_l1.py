from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PRECODING,
    PP_GRAYCODING,
    PL1_PHYTXEQ_LEVEL,
    PL1_PHYTXEQ_COEFF,
    PL1_PCS_VARIANT,
    PL1_PHYTXEQ,
    PL1_CWE_CYCLE,
    PL1_CWE_ERR_SYM_INDICES,
    PL1_CWE_BIT_ERR_MASK,
    PL1_CWE_FEC_ENGINE,
    PL1_CWE_FEC_STATS,
    PL1_CWE_CONTROL,
    PL1_CWE_FEC_STATS_CLEAR,
    PP_PRBSTYPE,
    PL1_PNSWAP_RX,
    PL1_PNSWAP_TX,
    PP_AUTONEG,
    PP_AUTONEGSTATUS,
    PP_LINKTRAIN,
)
from .pcs_pma_ghijkl import (
    Prbs,
)
from xoa_driver import enums

class EdunPMA:
    """Edun PMA"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.precoding = PP_PRECODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Pre-Coding Configurations.

        :type: PP_PRECODING
        """

        self.graycoding = PP_GRAYCODING(conn, module_id, port_id, serdes_xindex)
        """GET/SET Gray-Coding Configurations.

        :type: PP_GRAYCODING
        """

        self.pn_swap_rx = PL1_PNSWAP_RX(conn, module_id, port_id, serdes_xindex)
        """GET/SET PN-Swap RX Configurations. 

        :type: PL1_PNSWAP_RX
        """

        self.pn_swap_tx = PL1_PNSWAP_TX(conn, module_id, port_id, serdes_xindex)
        """GET/SET PN-Swap TX Configurations.
        
        :type: PL1_PNSWAP_TX
        """

class EdunTxTap:
    """Edun Tx Tap"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.native = PL1_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        """TX tap native value. (only for Edun)

        :type: PL1_PHYTXEQ
        """

        self.level = PL1_PHYTXEQ_LEVEL(conn, module_id, port_id, serdes_xindex)
        """TX tap mV/dB value. (only for Edun)

        :type: PL1_PHYTXEQ_LEVEL
        """

        self.ieee = PL1_PHYTXEQ_COEFF(conn, module_id, port_id, serdes_xindex)
        """TX tap IEEE coefficient value. (only for Edun)

        :type: PL1_PHYTXEQ_COEFF
        """

# class EdunRxTap:
#     """Edun Rx tap
#     """
    # def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
    #     self.status = P_EDUN_RX_STATUS(conn, module_id, port_id, serdes_xindex)
    #     """Edun Rx tap status
    #     """

class EdunMedium:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx = EdunTxTap(conn, module_id, port_id, serdes_xindex)
        """Edun Tx tap
        """
        # self.rx = EdunRxTap(conn, module_id, port_id, serdes_xindex)
        # """Edun Rx tap
        # """

class SerDesEdun:
    """L23 high-speed port SerDes configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:

        self.prbs = Prbs(conn, module_id, port_id, serdes_xindex)
        """PRBS
        :type: Prbs
        """
        
        self.pma = EdunPMA(conn, module_id, port_id, serdes_xindex)
        """Edun PMA

        :type: EdunPMA
        """

        self.medium = EdunMedium(conn, module_id, port_id, serdes_xindex)
        """Edun medium

        :type: EdunMedium
        """

class EdunAutoneg:
    """Edun port-level autoneg. For per-serdes configuration and status, use serdes[x]
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.config = PP_AUTONEG(conn, module_id, port_id)
        """Autoneg config and status
        """
        self.status = PP_AUTONEGSTATUS(conn, module_id, port_id)
        """Autoneg status
        """

class EdunFecCodewordErrorInject:
    """Edun FEC Codeword Error Injection
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.cycle = PL1_CWE_CYCLE(conn, module_id, port_id)
        """FEC codeword error injection cycle.
        """
        self.err_symbols = PL1_CWE_ERR_SYM_INDICES(conn, module_id, port_id)
        """The positions of the errored symbols in errored codewords.
        """
        self.bit_err_mask = PL1_CWE_BIT_ERR_MASK(conn, module_id, port_id)
        """The bit error mask for the errored symbols.
        """
        self.engine = PL1_CWE_FEC_ENGINE(conn, module_id, port_id)
        """The FEC engines to use.
        """
        self.statistics = PL1_CWE_FEC_STATS(conn, module_id, port_id)
        """FEC error injection statistics
        """
        self.clear_stats = PL1_CWE_FEC_STATS_CLEAR(conn, module_id, port_id)
        """Clear FEC codeword injection stats
        """
        self.control = PL1_CWE_CONTROL(conn, module_id, port_id)
        """Control the FEC codeword error injection
        """

class Layer1:
    def __init__(self, conn: "itf.IConnection", port) -> None:
        self.serdes: Tuple[SerDesEdun, ...] = tuple(
                SerDesEdun(conn, *port.kind, serdes_xindex=idx)
                for idx in range(port.info.capabilities.serdes_count)
                )
        self.autoneg = EdunAutoneg(conn, *port.kind)
        """Edun port-level autoneg. For per-serdes configuration and status, use serdes[x]
        """
        self.lt = PP_LINKTRAIN(conn, *port.kind)
        """Edun Link Training on serdes level

        :type: PP_LINKTRAIN
        """
        self.pcs_variant = PL1_PCS_VARIANT(conn, *port.kind)
        """PCS variant configuration
        """
        self.fec_error_inject = EdunFecCodewordErrorInject(conn, *port.kind)
        """FEC codeword error injection
        """
        self.prbs_config = PP_PRBSTYPE(conn, *port.kind)
        """PRBS configuration, including PRBS polynomial, invert mode, and statistic collection mode (for RX).
        """
