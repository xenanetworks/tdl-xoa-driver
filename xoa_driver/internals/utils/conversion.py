from typing import Union, Set
from xoa_driver.internals.core.transporter.protocol.payload.types import XmpHex
from xoa_driver.internals.commands.enums import AutoNegTecAbility


class AutoNegTecAbilityHex(XmpHex):
    """Auto Neg Technical Abilities Hex wrapper class for protocol compatibility."""

    def __init__(self, value: Union[str, "AutoNegTecAbility", Set["AutoNegTecAbility"]] = "0x0000000000000000") -> None:
        super().__init__(size=8)
        if isinstance(value, set):
            # Convert set of enums to hex string by OR-ing their values
            combined = 0
            for ability in value:
                combined |= ability.value
            self._hex_string: str = "0x" + format(combined, '016X')
        elif isinstance(value, AutoNegTecAbility):
            # Convert enum to hex string
            self._hex_string = "0x" + format(value.value, '016X')
        else:
            # Handle hex string input
            hex_string = value
            if hex_string.lower().startswith("0x"):
                hex_string = hex_string[2:]
            self._hex_string = "0x" + hex_string.upper().zfill(16)

    @classmethod
    def from_abilities(cls, abilities: Set["AutoNegTecAbility"]) -> "AutoNegTecAbilityHex":
        """Create an AutoNegTecAbilityHex from a set of AutoNegTecAbility enums.

        Args:
            abilities: A set of AutoNegTecAbility enum values to combine.

        Returns:
            A new AutoNegTecAbilityHex with the combined bit flags.

        Example:
            >>> from xoa_driver.enums import AutoNegTecAbility
            >>> from xoa_driver.internals.commands.utils import AutoNegTecAbilityHex
            >>> abilities = {AutoNegTecAbility.IEEE_100GBASE_KR4, AutoNegTecAbility.IEEE_100GBASE_CR4}
            >>> hex_obj = AutoNegTecAbilityHex.from_abilities(abilities)
            >>> print(hex_obj.hex_string)
            0x0000000000000C00
        """
        return cls(abilities)

    def to_abilities(self) -> Set["AutoNegTecAbility"]:
        """Convert this AutoNegTecAbilityHex to a set of AutoNegTecAbility enums.

        Returns:
            A set of AutoNegTecAbility enum values representing all set bits.

        Example:
            >>> from xoa_driver.internals.commands.utils import AutoNegTecAbilityHex
            >>> hex_obj = AutoNegTecAbilityHex("0x0000000000000C00")
            >>> abilities = hex_obj.to_abilities()
            >>> for ability in sorted(abilities, key=lambda x: x.value):
            ...     print(ability.name)
            IEEE_100GBASE_KR4
            IEEE_100GBASE_CR4
        """
        int_value = int(self._hex_string, 16)
        abilities: Set[AutoNegTecAbility] = set()
        for ability in AutoNegTecAbility:
            if int_value & ability.value:
                abilities.add(ability)
        return abilities

    def to_enum(self) -> "AutoNegTecAbility":
        """Convert this AutoNegTecAbilityHex to an AutoNegTecAbility enum.

        Returns:
            The corresponding AutoNegTecAbility enum value.

        Raises:
            ValueError: If the hex value doesn't correspond to a valid AutoNegTecAbility.
        """
        int_value = int(self._hex_string, 16)
        return AutoNegTecAbility(int_value)

    @property
    def hex_string(self) -> str:
        """Get the hex string value (with 0x prefix)."""
        return self._hex_string

    @hex_string.setter
    def hex_string(self, val: str) -> None:
        """Set the hex string value."""
        if val.lower().startswith("0x"):
            val = val[2:]
        self._hex_string = "0x" + val.upper().zfill(16)

    def to_int(self) -> int:
        """Convert the hex string to an integer."""
        return int(self._hex_string, 16)


