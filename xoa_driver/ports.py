#: All available test port types.
import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

import typing

from .internals.hli_v1.ports.port_l47.port_l47 import PortL47
from .internals.hli_v1.ports.port_l23.chimera_base.port_chimera import PortChimera
from .internals.hli_v1.ports.port_l23.l23_base.port_l23 import PortL23

from xoa_driver.internals.hli_v1.ports.port_l23.chimera import *
from xoa_driver.internals.hli_v1.ports.port_l23.odin import *
from xoa_driver.internals.hli_v1.ports.port_l23.loki import *
from xoa_driver.internals.hli_v1.ports.port_l23.thor import *
from xoa_driver.internals.hli_v1.ports.port_l23.freya import *

GenericL23Port = typing.Union[
    "POdin1G3S2PT",
    "POdin1G3S6P",
    "POdin1G3S6P_b",
    "POdin1G3S6PE",
    "POdin1G3S6PT1RJ45",
    "POdin1G4S4PCombi",
    "POdin1G4S4PCombi_b",
    "POdin5G4S6PCU",
    "POdin10G1S2P",
    "POdin10G1S2P_b",
    "POdin10G1S2P_c",
    "POdin10G1S2P_d",
    "POdin10G1S2PT",
    "POdin10G1S6P",
    "POdin10G1S6P_b",
    "POdin10G1S12P",
    "POdin10G3S2PCU",
    "POdin10G3S6PCU",
    "POdin10G4S2PCombi",
    "POdin10G4S2PCombi_b",
    "POdin10G5S6PCU",
    "POdin10G5S6PCU_b",
    "POdin10G6S6P_a",
    "POdin40G2S2P",
    "POdin40G2S2PB",
    "POdin100G3S1P",

    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G3S1PB",
    "PLoki100G3S1PB_b",
    "PLoki100G5S1P",
    "PLoki100G5S2P",

    "PThor100G5S4P",
    "PThor400G7S1P",
    "PThor400G7S1PLE",
    "PThor400G7S1P_b",
    "PThor400G7S1P_c",
    "PThor400G7S1P_d",

    "PFreya800G1S1P_a",
    "PFreya800G1S1P_b",
    "PFreya800G1S1POSFP_a",
    "PFreya800G1S1POSFP_b",
    "PFreya800G4S1P_a",
    "PFreya800G4S1P_b",
    "PFreya800G4S1P_c",
    "PFreya800G4S1P_d",
    "PFreya800G4S1P_e",
    "PFreya800G4S1P_f",
    "PFreya800G4S1POSFP_a",
    "PFreya800G4S1POSFP_b",
    "PFreya800G4S1POSFP_c",
    "PFreya800G4S1POSFP_d",
    "PFreya800G4S1POSFP_e",
    "PFreya800G4S1POSFP_f",
]

GenericChimeraPort = typing.Union[
    "PChi100G5S2P",
    "PChi100G5S2P_b",
    "PChi40G2S2P",
]

GenericAnyPort = typing.Union[
    "PortL47",
    "PortChimera",
    "GenericL23Port",
]

__all__ = (
    "GenericL23Port",
    "PortL47",
    "PortChimera",
    "GenericAnyPort",
    "POdin1G3S2PT",
    "POdin1G3S6P",
    "POdin1G3S6P_b",
    "POdin1G3S6PE",
    "POdin1G3S6PT1RJ45",
    "POdin1G4S4PCombi",
    "POdin1G4S4PCombi_b",
    "POdin5G4S6PCU",
    "POdin10G1S2P",
    "POdin10G1S2P_b",
    "POdin10G1S2P_c",
    "POdin10G1S2P_d",
    "POdin10G1S2PT",
    "POdin10G1S6P",
    "POdin10G1S6P_b",
    "POdin10G1S12P",
    "POdin10G3S2PCU",
    "POdin10G3S6PCU",
    "POdin10G4S2PCombi",
    "POdin10G4S2PCombi_b",
    "POdin10G5S6PCU",
    "POdin10G5S6PCU_b",
    "POdin10G6S6P_a",
    "POdin40G2S2P",
    "POdin40G2S2PB",
    "POdin100G3S1P",

    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G3S1PB",
    "PLoki100G3S1PB_b",
    "PLoki100G5S1P",
    "PLoki100G5S2P",

    "PThor100G5S4P",
    "PThor400G7S1P",
    "PThor400G7S1PLE",
    "PThor400G7S1P_b",
    "PThor400G7S1P_c",
    "PThor400G7S1P_d",

    "PFreya800G1S1P_a",
    "PFreya800G1S1P_b",
    "PFreya800G1S1POSFP_a",
    "PFreya800G1S1POSFP_b",
    "PFreya800G4S1P_a",
    "PFreya800G4S1P_b",
    "PFreya800G4S1P_c",
    "PFreya800G4S1P_d",
    "PFreya800G4S1P_e",
    "PFreya800G4S1P_f",
    "PFreya800G4S1POSFP_a",
    "PFreya800G4S1POSFP_b",
    "PFreya800G4S1POSFP_c",
    "PFreya800G4S1POSFP_d",
    "PFreya800G4S1POSFP_e",
    "PFreya800G4S1POSFP_f",
)
