#: All available test port types.

import typing

from xoa_driver.internals.hli.ports.chimera import *
from xoa_driver.internals.hli.ports.odin import *
from xoa_driver.internals.hli.ports.loki import *
from xoa_driver.internals.hli.ports.thor import *
from xoa_driver.internals.hli.ports.freya import *
from xoa_driver.internals.hli.ports.vulcan import *

GenericPortL23 = typing.Union[
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

GenericPortNE = typing.Union[
    "PChi100G5S2P",
    "PChi100G5S2P_b",
    "PChi40G2S2P",
]

GenericPortL47 = typing.Union[
    "PVulcan28PE10G",
    "PVulcan28PE10GCU",
    "PVulcan28PE25G",
    "PVulcan28PE40G",
]

GenericPortAny = typing.Union[
    "PortL23Base",
    "PortL47Base",
    "PortNEBase",
    "GenericPortL23",
    "GenericPortNE",
    "GenericPortL47",
]

__all__ = (
    "PortL23Base",
    "PortL47Base",
    "PortNEBase",

    "GenericPortAny",
    "GenericPortL23",
    "GenericPortNE",
    "GenericPortL47",
    
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

    "PChi100G5S2P",
    "PChi100G5S2P_b",
    "PChi40G2S2P",

    "PVulcan28PE10G",
    "PVulcan28PE10GCU",
    "PVulcan28PE25G",
    "PVulcan28PE40G",
)
