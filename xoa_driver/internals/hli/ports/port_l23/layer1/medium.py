from typing import (
    TYPE_CHECKING,
    Tuple,
)
from typing import Self
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_PHYTXEQ,
    PP_PHYRETUNE,
    PP_PHYAUTOTUNE,
    PP_PHYRXEQ,
    PL1_PHYTXEQ_LEVEL,
    PL1_PHYTXEQ_COEFF,
    PL1_PHYTXEQ,
    PP_PHYRXEQ_EXT,
    PP_PHYRXEQSTATUS_EXT,
    P_EDUN_RX_STATUS,
)
from xoa_driver import enums

class BasicMedium:
    """L23 high-speed port SerDes PHY configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx_equalizer = PP_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        """Equalizer settings of the on-board PHY in the TX direction.

        :type: PP_PHYTXEQ
        """

        self.rx_equalizer = PP_PHYRXEQ(conn, module_id, port_id, serdes_xindex)
        """Equalizer settings of the on-board PHY in the RX direction.

        :type: PP_PHYRXEQ
        """

        self.retune = PP_PHYRETUNE(conn, module_id, port_id, serdes_xindex)
        """Retuning of the PHY.

        :type: PP_PHYRETUNE
        """

        self.autotune = PP_PHYAUTOTUNE(conn, module_id, port_id, serdes_xindex)
        """Autotune of the PHY.

        :type: PP_PHYAUTOTUNE
        """

class FreyaTxTap:
    """Freya Tx Tap"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.native = PL1_PHYTXEQ(conn, module_id, port_id, serdes_xindex)
        """TX tap native value. (only for Freya)

        :type: PL1_PHYTXEQ
        """

        self.level = PL1_PHYTXEQ_LEVEL(conn, module_id, port_id, serdes_xindex)
        """TX tap mV/dB value. (only for Freya)

        :type: PL1_PHYTXEQ_LEVEL
        """

        self.ieee = PL1_PHYTXEQ_COEFF(conn, module_id, port_id, serdes_xindex)
        """TX tap IEEE coefficient value. (only for Freya)

        :type: PL1_PHYTXEQ_COEFF
        """

class EdunTxTap(FreyaTxTap):
    """Edun Tx Tap
    """
    pass

class FreyaRxTapConfig:
    """Freya Rx Tap Configuration"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.ctle_low = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_LOW)
        """RX tap CTLE LOW. (only for Freya)
        """

        self.ctle_high = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_HIGH)
        """RX tap CTLE HIGH. (only for Freya)
        """

        self.agc = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.AGC)
        """RX tap Automatic Gain Control. (only for Freya)
        """

        self.oc = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.OC)
        """RX tap Offset Cancellation. (only for Freya)
        """

        self.cdr = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CDR)
        """RX tap Clock and Data Recovery. (only for Freya)
        """

        self.pre_ffe_1 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_1)
        """RX tap Pre Feed-Forward Equalizer #1. (only for Freya)
        """

        self.pre_ffe_2 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_2)
        """RX tap Pre Feed-Forward Equalizer #2. (only for Freya)
        """

        self.pre_ffe_3 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_3)
        """RX tap Pre Feed-Forward Equalizer #3. (only for Freya)
        """

        self.pre_ffe_4 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_4)
        """RX tap Pre Feed-Forward Equalizer #4. (only for Freya)
        """

        self.pre_ffe_5 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_5)
        """RX tap Pre Feed-Forward Equalizer #5. (only for Freya)
        """

        self.pre_ffe_6 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_6)
        """RX tap Pre Feed-Forward Equalizer #6. (only for Freya)
        """

        self.pre_ffe_7 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_7)
        """RX tap Pre Feed-Forward Equalizer #7. (only for Freya)
        """

        self.pre_ffe_8 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_8)
        """RX tap Pre Feed-Forward Equalizer #8. (only for Freya)
        """

        self.dfe = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.DFE)
        """RX tap Decision Feedback Equalization. (only for Freya)
        """

        self.post_ffe_1 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_1)
        """RX tap Post Feed-Forward Equalizer #1. (only for Freya)
        """

        self.post_ffe_2 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_2)
        """RX tap Post Feed-Forward Equalizer #2. (only for Freya)
        """

        self.post_ffe_3 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_3)
        """RX tap Post Feed-Forward Equalizer #3. (only for Freya)
        """

        self.post_ffe_4 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_4)
        """RX tap Post Feed-Forward Equalizer #4. (only for Freya)
        """

        self.post_ffe_5 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_5)
        """RX tap Post Feed-Forward Equalizer #5. (only for Freya)
        """

        self.post_ffe_6 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_6)
        """RX tap Post Feed-Forward Equalizer #6. (only for Freya)
        """

        self.post_ffe_7 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_7)
        """RX tap Post Feed-Forward Equalizer #7. (only for Freya)
        """

        self.post_ffe_8 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_8)
        """RX tap Post Feed-Forward Equalizer #8. (only for Freya)
        """

        self.post_ffe_9 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_9)
        """RX tap Post Feed-Forward Equalizer #9. (only for Freya)
        """

        self.post_ffe_10 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_10)
        """RX tap Post Feed-Forward Equalizer #10. (only for Freya)
        """

        self.post_ffe_11 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_11)
        """RX tap Post Feed-Forward Equalizer #11. (only for Freya)
        """

        self.post_ffe_12 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_12)
        """RX tap Post Feed-Forward Equalizer #12. (only for Freya)
        """

        self.post_ffe_13 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #13. (only for Freya)
        """

        self.post_ffe_14 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_14)
        """RX tap Post Feed-Forward Equalizer #14. (only for Freya)
        """

        self.post_ffe_15 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_15)
        """RX tap Post Feed-Forward Equalizer #15. (only for Freya)
        """

        self.post_ffe_16 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_16)
        """RX tap Post Feed-Forward Equalizer #16. (only for Freya)
        """

        self.post_ffe_17 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_17)
        """RX tap Post Feed-Forward Equalizer #17. (only for Freya)
        """

        self.post_ffe_18 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_18)
        """RX tap Post Feed-Forward Equalizer #18. (only for Freya)
        """

        self.post_ffe_19 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_19)
        """RX tap Post Feed-Forward Equalizer #19. (only for Freya)
        """

        self.post_ffe_20 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_20)
        """RX tap Post Feed-Forward Equalizer #20. (only for Freya)
        """

        self.post_ffe_21 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_21)
        """RX tap Post Feed-Forward Equalizer #21. (only for Freya)
        """

        self.post_ffe_22 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_22)
        """RX tap Post Feed-Forward Equalizer #22. (only for Freya)
        """

        self.post_ffe_23 = PP_PHYRXEQ_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #23. (only for Freya)
        """

class FreyaRxTapStatus:
    """Freya Rx Tap Status"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.ctle_low = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_LOW)
        """RX tap CTLE LOW. (only for Freya)
        """

        self.ctle_high = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CTLE_HIGH)
        """RX tap CTLE HIGH. (only for Freya)
        """

        self.agc = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.AGC)
        """RX tap Automatic Gain Control. (only for Freya)
        """

        self.oc = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.OC)
        """RX tap Offset Cancellation. (only for Freya)
        """

        self.cdr = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.CDR)
        """RX tap Clock and Data Recovery. (only for Freya)
        """

        self.pre_ffe_1 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_1)
        """RX tap Pre Feed-Forward Equalizer #1. (only for Freya)
        """

        self.pre_ffe_2 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_2)
        """RX tap Pre Feed-Forward Equalizer #2. (only for Freya)
        """

        self.pre_ffe_3 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_3)
        """RX tap Pre Feed-Forward Equalizer #3. (only for Freya)
        """

        self.pre_ffe_4 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_4)
        """RX tap Pre Feed-Forward Equalizer #4. (only for Freya)
        """

        self.pre_ffe_5 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_5)
        """RX tap Pre Feed-Forward Equalizer #5. (only for Freya)
        """

        self.pre_ffe_6 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_6)
        """RX tap Pre Feed-Forward Equalizer #6. (only for Freya)
        """

        self.pre_ffe_7 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_7)
        """RX tap Pre Feed-Forward Equalizer #7. (only for Freya)
        """

        self.pre_ffe_8 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.PRE_FFE_8)
        """RX tap Pre Feed-Forward Equalizer #8. (only for Freya)
        """

        self.dfe = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.DFE)
        """RX tap Decision Feedback Equalization. (only for Freya)
        """

        self.post_ffe_1 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_1)
        """RX tap Post Feed-Forward Equalizer #1. (only for Freya)
        """

        self.post_ffe_2 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_2)
        """RX tap Post Feed-Forward Equalizer #2. (only for Freya)
        """

        self.post_ffe_3 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_3)
        """RX tap Post Feed-Forward Equalizer #3. (only for Freya)
        """

        self.post_ffe_4 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_4)
        """RX tap Post Feed-Forward Equalizer #4. (only for Freya)
        """

        self.post_ffe_5 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_5)
        """RX tap Post Feed-Forward Equalizer #5. (only for Freya)
        """

        self.post_ffe_6 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_6)
        """RX tap Post Feed-Forward Equalizer #6. (only for Freya)
        """

        self.post_ffe_7 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_7)
        """RX tap Post Feed-Forward Equalizer #7. (only for Freya)
        """

        self.post_ffe_8 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_8)
        """RX tap Post Feed-Forward Equalizer #8. (only for Freya)
        """

        self.post_ffe_9 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_9)
        """RX tap Post Feed-Forward Equalizer #9. (only for Freya)
        """

        self.post_ffe_10 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_10)
        """RX tap Post Feed-Forward Equalizer #10. (only for Freya)
        """

        self.post_ffe_11 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_11)
        """RX tap Post Feed-Forward Equalizer #11. (only for Freya)
        """

        self.post_ffe_12 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_12)
        """RX tap Post Feed-Forward Equalizer #12. (only for Freya)
        """

        self.post_ffe_13 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #13. (only for Freya)
        """

        self.post_ffe_14 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_14)
        """RX tap Post Feed-Forward Equalizer #14. (only for Freya)
        """

        self.post_ffe_15 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_15)
        """RX tap Post Feed-Forward Equalizer #15. (only for Freya)
        """

        self.post_ffe_16 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_16)
        """RX tap Post Feed-Forward Equalizer #16. (only for Freya)
        """

        self.post_ffe_17 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_17)
        """RX tap Post Feed-Forward Equalizer #17. (only for Freya)
        """

        self.post_ffe_18 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_18)
        """RX tap Post Feed-Forward Equalizer #18. (only for Freya)
        """

        self.post_ffe_19 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_19)
        """RX tap Post Feed-Forward Equalizer #19. (only for Freya)
        """

        self.post_ffe_20 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_20)
        """RX tap Post Feed-Forward Equalizer #20. (only for Freya)
        """

        self.post_ffe_21 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_21)
        """RX tap Post Feed-Forward Equalizer #21. (only for Freya)
        """

        self.post_ffe_22 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_22)
        """RX tap Post Feed-Forward Equalizer #22. (only for Freya)
        """

        self.post_ffe_23 = PP_PHYRXEQSTATUS_EXT(conn, module_id, port_id, serdes_xindex, enums.RxEqExtCap.POST_FFE_13)
        """RX tap Post Feed-Forward Equalizer #23. (only for Freya)
        """

class FreyaRxTap:
    """Freya Rx tap
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.config = FreyaRxTapConfig(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap configuration
        """
        self.status = FreyaRxTapStatus(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap status
        """

class EdunRxTap:
    """Edun Rx Tap
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.status = P_EDUN_RX_STATUS(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap status
        """

class FreyaMedium:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx = FreyaTxTap(conn, module_id, port_id, serdes_xindex)
        """Freya Tx tap
        """
        self.rx = FreyaRxTap(conn, module_id, port_id, serdes_xindex)
        """Freya Rx tap
        """
        
class EdunMedium:
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.tx = EdunTxTap(conn, module_id, port_id, serdes_xindex)
        """Edun Tx tap
        """
        self.rx = EdunRxTap(conn, module_id, port_id, serdes_xindex)
        """Edun Rx tap
        """
