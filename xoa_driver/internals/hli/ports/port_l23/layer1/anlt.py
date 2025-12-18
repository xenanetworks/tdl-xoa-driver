from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
from xoa_driver.internals.commands import (
    PP_AUTONEG,
    PP_AUTONEGSTATUS,
    PP_LINKTRAIN,
    PL1_AUTONEGINFO,
    PL1_LINKTRAININFO,
    PL1_LOG,
    PL1_CFG_TMP,
    PL1_LINKTRAIN_CMD,
    PL1_AUTONEG_STATUS,
    PL1_AUTONEG_ABILITIES,
    PL1_AUTONEG_CONFIG,
    PL1_ANLT,
    PL1_LINKTRAIN_CONFIG,
    PL1_LINKTRAIN_STATUS,
    PL1_LT_PHYTXEQ_RANGE,
    PL1_LT_PHYTXEQ_RANGE_COEFF,
    PL1_PRESET_CONFIG,
    PL1_PRESET_CONFIG_COEFF,
    PL1_PRESET_CONFIG_LEVEL,
    PL1_PRESET_RESET,
)
from xoa_driver import enums


class AutonegBasic:
    """Basic auto-negotiation"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.settings = PP_AUTONEG(conn, module_id, port_id)
        """Auto-negotiation settings of the PHY.
        
        :type: PP_AUTONEG
        """

        self.status = PP_AUTONEGSTATUS(conn, module_id, port_id)
        """Status of auto-negotiation settings of the PHY.
        
        :type: PP_AUTONEGSTATUS
        """


class LinkTrainBasic:
    """Basic link training"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.settings = PP_LINKTRAIN(conn, module_id, port_id)
        """Link training settings.
        
        :type: PP_LINKTRAIN
        """


class AnltBasic:
    """Basic ANLT settings"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.autoneg = AutonegBasic(conn, module_id, port_id)
        """PCS/PMA auto-negotiation settings.
        
        :type: AutonegBasic
        """

        self.link_training = LinkTrainBasic(conn, module_id, port_id)
        """PCS/PMA link training settings.
        
        :type: LinkTrainBasic
        """


class FreyaAutoNeg:
    """Freya Autoneg"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.info = PL1_AUTONEGINFO(conn, module_id, port_id, 0)
        """Autoneg info

        :type: PL1_AUTONEGINFO
        """

        self.status = PL1_AUTONEG_STATUS(conn, module_id, port_id)
        """Autoneg status

        :type: PL1_AUTONEG_STATUS
        """

        self.abilities = PL1_AUTONEG_ABILITIES(conn, module_id, port_id)
        """Autoneg abilities

        :type: PL1_AUTONEG_ABILITIES
        """

        self.config = PL1_AUTONEG_CONFIG(conn, module_id, port_id)
        """Autoneg configuration

        :type: PL1_AUTONEG_CONFIG
        """

class FreyaLinkTraining:
    """Freya Link Training on serdes level"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self.cmd = PL1_LINKTRAIN_CMD(conn, module_id, port_id, serdes_xindex)
        """Link training command.
        
        :type: PP_LINKTRAIN
        """

        self.info = PL1_LINKTRAININFO(conn, module_id, port_id, serdes_xindex, 0)
        """Link training info.
        
        :type: PL1_LINKTRAININFO
        """

        self.status = PL1_LINKTRAIN_STATUS(conn, module_id, port_id, serdes_xindex)
        """Link training status.
        
        :type: PL1_LINKTRAIN_STATUS
        """

        self.preset1 = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET1)
        """Link training preset 1

        :rtype: FreyaLinkTrainingPreset
        """

        self.preset2 = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET2)
        """Link training preset 2

        :rtype: FreyaLinkTrainingPreset
        """

        self.preset3 = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET3)
        """Link training preset 3

        :rtype: FreyaLinkTrainingPreset
        """

        self.preset4 = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET4)
        """Link training preset 4

        :rtype: FreyaLinkTrainingPreset
        """

        self.preset5 = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET5)
        """Link training preset 5

        :rtype: FreyaLinkTrainingPreset
        """

        self.preset_los = FreyaLinkTrainingPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.LOS)
        """Link training preset LOS

        :rtype: FreyaLinkTrainingPreset
        """

        self.range = FreyaLinkTrainingRange(conn, module_id, port_id, serdes_xindex)
        """Link training tap range

        :rtype: FreyaLinkTrainingRange
        """

        self.initial_modulation = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.LT_INITIAL_MODULATION)
        """Link training initial modulation

        :rtype: PL1_CFG_TMP
        """

        self.algorithm = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.LT_TRAINING_ALGORITHM)
        """Link training algorithm

        :rtype: PL1_CFG_TMP
        """

        self.strict_mode = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.ANLT_STRICT_MODE)
        """ANLT strict mode. In strict mode, errored framed will be ignored.

        :rtype: PL1_CFG_TMP
        """

class FreyaAnlt:
    """Freya port-level anlt. For per-serdes configuration and status, use serdes[x]
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.an = FreyaAutoNeg(conn, module_id, port_id)
        """Autoneg config and status
        """
        self.ctrl = PL1_ANLT(conn, module_id, port_id)
        """ANLT control
        """
        self.lt_config = PL1_LINKTRAIN_CONFIG(conn, module_id, port_id)
        """Port-level Link Training config
        """
        self.log = PL1_LOG(conn, module_id, port_id)
        """ANLT log
        """
        self.autorestart = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AUTO_LINK_RECOVERY)
        """ANLT Autorestart
        """
        self.allow_an_loopback = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AN_LOOPBACK)
        """ANLT Autorestart
        """
        self.send_empty_np = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AN_EMPTY_NP)
        """If the port should send Next Pages if they are empty.
        """

class FreyaLinkTrainingPreset:
    """Freya Link Training Preset"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int, preset_index: enums.FreyaPresetIndex) -> None:
    
        self.native = PL1_PRESET_CONFIG(conn, module_id, port_id, serdes_xindex, preset_index)
        """Preset native values. (only for Freya)

        :type: PL1_PRESET_CONFIG
        """

        self.ieee = PL1_PRESET_CONFIG_COEFF(conn, module_id, port_id, serdes_xindex, preset_index)
        """Preset IEEE coefficient values. (only for Freya)

        :type: PL1_PRESET_CONFIG_COEFF
        """

        self.level = PL1_PRESET_CONFIG_LEVEL(conn, module_id, port_id, serdes_xindex, preset_index)
        """Preset mV/dB values. (only for Freya)

        :type: PL1_PRESET_CONFIG_LEVEL
        """

        self.reset = PL1_PRESET_RESET(conn, module_id, port_id, serdes_xindex, preset_index)
        """Reset preset to default. (only for Freya)

        :type: PL1_PRESET_RESET
        """

class FreyaLinkTrainingRangeTap:
    """Freya Link Training Range Tap"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int, tap_index: enums.FreyaTapIndex) -> None:
    
        self.native = PL1_LT_PHYTXEQ_RANGE(conn, module_id, port_id, serdes_xindex, tap_index)
        """Tap range native values. (only for Freya)

        :type: PL1_LT_PHYTXEQ_RANGE
        """

        self.ieee = PL1_LT_PHYTXEQ_RANGE_COEFF(conn, module_id, port_id, serdes_xindex, tap_index)
        """Tap range IEEE coefficient values. (only for Freya)

        :type: PL1_LT_PHYTXEQ_RANGE_COEFF
        """

class FreyaLinkTrainingRange:
    """Freya Link Training Range"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
    
        self.pre = FreyaLinkTrainingRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP0)
        """Pre tap range and response. (only for Freya)

        :type: FreyaLinkTrainingRangeTap
        """       

        self.main = FreyaLinkTrainingRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP1)
        """Main tap range and response. (only for Freya)

        :type: FreyaLinkTrainingRangeTap
        """  

        self.post = FreyaLinkTrainingRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP2)
        """Post tap range and response. (only for Freya)

        :type: FreyaLinkTrainingRangeTap
        """ 

        self.pre2 = FreyaLinkTrainingRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP3)
        """Pre2 tap range and response. (only for Freya)

        :type: FreyaLinkTrainingRangeTap
        """ 

        self.pre3 = FreyaLinkTrainingRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP4)
        """Pre3 tap range and response. (only for Freya)

        :type: FreyaLinkTrainingRangeTap
        """ 
