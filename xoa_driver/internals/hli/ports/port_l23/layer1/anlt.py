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
        self.an = AutonegBasic(conn, module_id, port_id)
        """PCS/PMA auto-negotiation settings.
        
        :type: AutonegBasic
        """

        self.lt = LinkTrainBasic(conn, module_id, port_id)
        """PCS/PMA link training settings.
        
        :type: LinkTrainBasic
        """


class AutoNegAdvanced:
    """Advanced auto-negotiation configuration and status."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.statistics = PL1_AUTONEGINFO(conn, module_id, port_id, 0)
        """Statistics of auto-negotiation.

        :type: PL1_AUTONEGINFO
        """

        self.results = PL1_AUTONEG_STATUS(conn, module_id, port_id)
        """Received autoneg advertisement and negotiation results

        :type: PL1_AUTONEG_STATUS
        """

        self.abilities = PL1_AUTONEG_ABILITIES(conn, module_id, port_id)
        """Supported autoneg technical abilities, fec modes, and pause modes

        :type: PL1_AUTONEG_ABILITIES
        """

        self.advertise = PL1_AUTONEG_CONFIG(conn, module_id, port_id)
        """Autoneg advertisement configuration

        :type: PL1_AUTONEG_CONFIG
        """

        self._allow_loopback = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AN_LOOPBACK)
        """Whether the port should permit loopback during AN operations. 

        :type: PL1_CFG_TMP
        """

        self._empty_np = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AN_EMPTY_NP)
        """If the port should send Next Pages even if they are empty.

        :type: PL1_CFG_TMP
        """
    
    async def set_allow_loopback(self, allow: bool) -> None:
        """Set whether ANLT allows loopback during auto-negotiation.

        :param allow: Whether to allow loopback.
        :type allow: bool
        """
        value = 1 if allow else 0
        await self._allow_loopback.set(values=[value])

    async def get_allow_loopback(self) -> bool:
        """Get whether ANLT allows loopback during auto-negotiation.

        :return: True if loopback is allowed, False otherwise.
        """
        result = await self._allow_loopback.get()
        return bool(result.values[0])
    
    async def set_empty_np(self, enable: bool) -> None:
        """Set if the port should send Next Pages even if they are empty.

        :param enable: Whether to enable sending empty Next Pages.
        :type enable: bool
        """
        value = 1 if enable else 0
        await self._empty_np.set(values=[value])

    async def get_empty_np(self) -> bool:
        """Get if the port sends Next Pages even if they are empty.

        :return: True if sending empty Next Pages is enabled, False otherwise.
        """
        result = await self._empty_np.get()
        return bool(result.values[0])


class LinkTrainingAdvanced:
    """Advanced Link Training on serdes level"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
        self._cmd = PL1_LINKTRAIN_CMD(conn, module_id, port_id, serdes_xindex)
        """Link training command.
        
        :type: PP_LINKTRAIN
        """

        self.statistics = PL1_LINKTRAININFO(conn, module_id, port_id, serdes_xindex, 0)
        """Link training statistics.
        
        :type: PL1_LINKTRAININFO
        """

        self.results = PL1_LINKTRAIN_STATUS(conn, module_id, port_id, serdes_xindex)
        """Link training results.
        
        :type: PL1_LINKTRAIN_STATUS
        """

        self.preset1 = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET1)
        """Configure preset 1

        :type: LinkTrainingAdvancedPreset
        """

        self.preset2 = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET2)
        """Configure preset 2

        :type: LinkTrainingAdvancedPreset
        """

        self.preset3 = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET3)
        """Configure preset 3

        :type: LinkTrainingAdvancedPreset
        """

        self.preset4 = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET4)
        """Configure preset 4

        :type: LinkTrainingAdvancedPreset
        """

        self.preset5 = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.PRESET5)
        """Configure preset 5

        :type: LinkTrainingAdvancedPreset
        """

        self.preset_los = LinkTrainingAdvancedPreset(conn, module_id, port_id, serdes_xindex, enums.FreyaPresetIndex.LOS)
        """Configure preset LOS

        :type: LinkTrainingAdvancedPreset
        """

        self.range = LinkTrainingAdvancedRange(conn, module_id, port_id, serdes_xindex)
        """Configure Link training tap range

        :type: LinkTrainingAdvancedRange
        """

        self._initial_modulation = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.LT_INITIAL_MODULATION)
        """Link training initial modulation

        :type: PL1_CFG_TMP
        """

        self._algorithm = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.LT_TRAINING_ALGORITHM)
        """Link training algorithm

        :type: PL1_CFG_TMP
        """

    async def set_initial_modulation_nrz(self) -> None:
        """Set link training initial modulation to NRZ (PAM2).
        """
        await self._initial_modulation.set(values=[enums.LinkTrainEncoding.NRZ.value])

    async def set_initial_modulation_pam4(self) -> None:
        """Set link training initial modulation to PAM4.
        """
        await self._initial_modulation.set(values=[enums.LinkTrainEncoding.PAM4.value])

    async def set_initial_modulation_pam4precoding(self) -> None:
        """Set link training initial modulation to PAM4 with precoding.
        """
        await self._initial_modulation.set(values=[enums.LinkTrainEncoding.PAM4_WITH_PRECODING.value])


    async def get_initial_modulation(self) -> enums.LinkTrainEncoding:
        """Get link training initial modulation.

        :return: The current modulation.
        """
        result = await self._initial_modulation.get()
        return enums.LinkTrainEncoding(result.values[0])
    

    async def set_algorithm_default(self) -> None:
        """Set link training algorithm to default.

        The default algorithm is called Algorithm 0.

        Algorithm 0 sets a target BER to 1e-8. First, it picks the preset that provides the lowest BER. Then from the selected preset, it adjusts the coefficients to lower the BER further. During the training process, if the target BER is reached, the training will stop.

        """
        await self._algorithm.set(values=[enums.LinkTrainAlgorithm.ALG0.value])

    
    async def set_algorithm_lite(self) -> None:
        """Set link training algorithm to simple.

        The default algorithm is called Algorithm -1.

        Algorithm -1 request Preset 2, then requests an increment to c(1) and a decrement to c(0). Then the training stops regardless of the achieved BER.

        """
        await self._algorithm.set(values=[enums.LinkTrainAlgorithm.ALGN1.value])

    async def get_algorithm(self) -> enums.LinkTrainAlgorithm:
        """Get link training algorithm.

        :return: The current algorithm.
        """
        result = await self._algorithm.get()
        return enums.LinkTrainAlgorithm(result.values[0])

    async def send_cmd_nop(self) -> None:
        """Send NOP command.
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_NOP, arg=0)

    async def send_cmd_inc(self, coeff: enums.LinkTrainCoeffs) -> None:
        """Send Inc Coeffcient request command.

        :param coeff: The coefficient to increment.
        :type coeff: enums.LinkTrainCoeffs
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_INC, arg=coeff.value)

    async def send_cmd_dec(self, coeff: enums.LinkTrainCoeffs) -> None:
        """Send Dec Coeffcient request command.

        :param coeff: The coefficient to decrement.
        :type coeff: enums.LinkTrainCoeffs
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_DEC, arg=coeff.value)

    async def send_cmd_preset(self, preset: enums.LinkTrainPresets) -> None:
        """Send Preset request command.

        :param preset: The preset to request.
        :type preset: enums.LinkTrainPresets
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_INC, arg=preset.value)

    async def send_cmd_modulation(self, modulation: enums.LinkTrainEncoding) -> None:
        """Send Modulation request command.

        :param modulation: The modulation to request.
        :type modulation: enums.LinkTrainEncoding
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_ENCODING, arg=modulation.value)

    async def send_cmd_trained(self) -> None:
        """Send Trained command.
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_LOCAL_TRAINED, arg=0)

    async def send_cmd_no_equalization(self) -> None:
        """Send No Equalization command.

        Ask the remote port to set the coeff to NO_EQ.
        """
        await self._cmd.set(cmd=enums.LinkTrainCmd.CMD_NO_EQ, arg=0)

    async def get_cmd_result_flag(self) -> Tuple[enums.LinkTrainCmd, enums.LinkTrainCmdResults, enums.LinkTrainCmdFlags]:
        """Get the last sent link training command and its results and flags.

        :return: A tuple containing the last command and its argument.

            - The first element is the LinkTrainCmd enum representing the last command sent.
            - The second element is the LinkTrainCmdResults enum representing the result of the command.
            - The third element is the LinkTrainCmdFlags enum representing any flags associated with the command.
        
        :rtype: Tuple[enums.LinkTrainCmd, enums.LinkTrainCmdResults, enums.LinkTrainCmdFlags]
        """
        resp = await self._cmd.get()
        cmd = enums.LinkTrainCmd(resp.cmd)
        result = enums.LinkTrainCmdResults(resp.result)
        flag = enums.LinkTrainCmdFlags(resp.flags)

        return cmd, result, flag

class AnltAdvanced:
    """Advanced port-level anlt. For per-serdes configuration and status, use serdes[x]
    """
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.an = AutoNegAdvanced(conn, module_id, port_id)
        """Autoneg config and status

        :type: AutoNegAdvanced
        """

        self.ctrl = PL1_ANLT(conn, module_id, port_id)
        """ANLT control

        :type: PL1_ANLT
        """

        self.lt_config = PL1_LINKTRAIN_CONFIG(conn, module_id, port_id)
        """Port-level Link Training config

        :type: PL1_LINKTRAIN_CONFIG
        """

        self.log = PL1_LOG(conn, module_id, port_id)
        """Advanced ANLT protocol trace log

        :type: PL1_LOG
        """

        self._autorestart = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.AUTO_LINK_RECOVERY)
        """ANLT Autorestart

        :type: PL1_CFG_TMP
        """

        self._strict_mode = PL1_CFG_TMP(conn, module_id, port_id, 0, enums.Layer1ConfigType.ANLT_STRICT_MODE)
        """ANLT strict mode. In strict mode, errored framed will be ignored.

        :type: PL1_CFG_TMP
        """

    async def set_autorestart(self, restart_link_down: bool, restart_lt_failure: bool) -> None:
        """Set ANLT autorestart configuration.

        :param restart_link_down: Whether to restart ANLT when link goes down.
        :param restart_lt_failure: Whether to restart ANLT when link training fails.
        """
        value = 0
        if restart_link_down:
            value |= 0x01
        if restart_lt_failure:
            value |= 0x02
        await self._autorestart.set(values=[value])

    async def get_autorestart(self) -> Tuple[bool, bool]:
        """Get ANLT autorestart configuration.

        :return: A tuple containing two booleans:
            - The first boolean indicates whether ANLT restarts when link goes down.
            - The second boolean indicates whether ANLT restarts when link training fails.
        """
        result = await self._autorestart.get()
        value = result.values[0]
        restart_link_down = bool(value & 0x01)
        restart_lt_failure = bool(value & 0x02)
        return restart_link_down, restart_lt_failure
    
    async def set_strict_mode(self, enable: bool) -> None:
        """Set ANLT strict mode. In strict mode, errored framed will be ignored.

        :param enable: Whether to enable strict mode.
        """
        value = 1 if enable else 0
        await self._strict_mode.set(values=[value])


    async def get_strict_mode(self) -> bool:
        """Get ANLT strict mode status.

        :return: True if strict mode is enabled, False otherwise.
        """
        result = await self._strict_mode.get()
        return bool(result.values[0])


class LinkTrainingAdvancedPreset:
    """Advanced Link Training Preset"""

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

class LinkTrainingAdvancedRangeTap:
    """Advanced Link Training Range Tap"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int, tap_index: enums.FreyaTapIndex) -> None:
    
        self.native = PL1_LT_PHYTXEQ_RANGE(conn, module_id, port_id, serdes_xindex, tap_index)
        """Tap range native values. (only for Freya)

        :type: PL1_LT_PHYTXEQ_RANGE
        """

        self.ieee = PL1_LT_PHYTXEQ_RANGE_COEFF(conn, module_id, port_id, serdes_xindex, tap_index)
        """Tap range IEEE coefficient values. (only for Freya)

        :type: PL1_LT_PHYTXEQ_RANGE_COEFF
        """

class LinkTrainingAdvancedRange:
    """Advanced Link Training Range"""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, serdes_xindex: int) -> None:
    
        self.pre = LinkTrainingAdvancedRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP0)
        """Pre tap range and response. (only for Freya)

        :type: LinkTrainingAdvancedRangeTap
        """       

        self.main = LinkTrainingAdvancedRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP1)
        """Main tap range and response. (only for Freya)

        :type: LinkTrainingAdvancedRangeTap
        """  

        self.post = LinkTrainingAdvancedRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP2)
        """Post tap range and response. (only for Freya)

        :type: LinkTrainingAdvancedRangeTap
        """ 

        self.pre2 = LinkTrainingAdvancedRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP3)
        """Pre2 tap range and response. (only for Freya)

        :type: LinkTrainingAdvancedRangeTap
        """ 

        self.pre3 = LinkTrainingAdvancedRangeTap(conn, module_id, port_id, serdes_xindex, enums.FreyaTapIndex.TAP4)
        """Pre3 tap range and response. (only for Freya)

        :type: LinkTrainingAdvancedRangeTap
        """ 
