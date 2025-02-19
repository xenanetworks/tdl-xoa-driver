#: All available test port types.


import typing

from xoa_driver.internals.hli_v2.ports.port_l47.main import PortL47

from xoa_driver.internals.hli_v2.ports.port_l23.port_l23ve import PortL23VE
from xoa_driver.internals.hli_v2.ports.port_l23.chimera.port_chimera import (
    PortChimera,
    PChi100G5S2P,
    PChi100G5S2P_b,
    PChi40G2S2P,
)

from xoa_driver.internals.hli_v2.ports.port_l23.bases.port_l23 import BasePortL23
from xoa_driver.internals.hli_v2.ports.port_l23.family_combi import (
    POdin1G4S4PCombi,
    POdin1G4S4PCombi_b,
    POdin10G4S2PCombi,
    POdin10G4S2PCombi_b,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_d import (
    POdin1G3S2PT,
    POdin1G3S6P,
    POdin1G3S6P_b,
    POdin1G3S6PE,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_e import (
    POdin5G4S6PCU,
    POdin10G3S2PCU,
    POdin10G3S6PCU,
    POdin10G5S6PCU,
    POdin10G5S6PCU_b,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_f import (
    POdin10G1S2P,
    POdin10G1S2P_b,
    POdin10G1S2P_c,
    POdin10G1S2P_d,
    POdin10G1S2PT,
    POdin10G1S6P,
    POdin10G1S6P_b,
    POdin10G1S12P,
    POdin40G2S2P,
    POdin40G2S2PB,
    POdin10G6S6P_a,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_g import (
    PLoki100G3S1P,
    PLoki100G3S1P_b,
    PLoki100G3S1PSE,
    PLoki100G3S1PB,
    PLoki100G3S1PB_b,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_h import (
    PLoki100G5S1P,
    POdin100G3S1P,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_i import PLoki100G5S2P
from xoa_driver.internals.hli_v2.ports.port_l23.family_j import PThor100G5S4P
from xoa_driver.internals.hli_v2.ports.port_l23.family_k import (
    PThor400G7S1P,
    PThor400G7S1PLE,
)
from xoa_driver.internals.hli_v2.ports.port_l23.family_l import (
    PThor400G7S1P_b,
    PThor400G7S1P_c,
    PThor400G7S1P_d,
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_l1 import (
    PFreya800G1S1P_a,
    PFreya800G1S1P_b,
    PFreya800G1S1POSFP_a,
    PFreya800G1S1POSFP_b,
    PFreya800G4S1P_a,
    PFreya800G4S1P_b,
    PFreya800G4S1P_c,
    PFreya800G4S1P_d,
    PFreya800G4S1P_e,
    PFreya800G4S1P_f,
    PFreya800G4S1POSFP_a,
    PFreya800G4S1POSFP_b,
    PFreya800G4S1POSFP_c,
    PFreya800G4S1POSFP_d,
    PFreya800G4S1POSFP_e,
    PFreya800G4S1POSFP_f,    
)

from xoa_driver.internals.hli_v2.ports.port_l23.family_m import POdin1G3S6PT1RJ45

GenericL23Port = typing.Union[
    "POdin1G3S6P",
    "POdin1G3S6P_b",
    "POdin1G3S6PE",
    "POdin1G3S2PT",
    "POdin5G4S6PCU",
    "POdin10G5S6PCU",
    "POdin10G5S6PCU_b",
    "POdin10G3S6PCU",
    "POdin10G3S2PCU",
    "POdin10G1S2P",
    "POdin10G1S2P_b",
    "POdin10G1S2P_c",
    "POdin10G1S6P",
    "POdin10G1S6P_b",
    "POdin10G1S2PT",
    "POdin10G1S2P_d",
    "POdin10G1S12P",
    "POdin40G2S2P",
    "POdin40G2S2PB",
    "POdin100G3S1P",
    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G3S1PB",
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
    "POdin1G3S6PT1RJ45",
    "POdin1G4S4PCombi",
    "POdin1G4S4PCombi_b",
    "POdin10G4S2PCombi",
    "POdin10G4S2PCombi_b",
    "POdin10G6S6P_a",
    "PLoki100G3S1PB_b",
]

GenericAnyPort = typing.Union[
    GenericL23Port,
    "PortL47",
    "PortL23VE",
    "PortChimera",
    "PChi100G5S2P",
    "PChi100G5S2P_b",
    "PChi40G2S2P",
]

__all__ = (
    "BasePortL23",
    "PortL47",
    "PortL23VE",
    "GenericL23Port",
    "GenericAnyPort",
    "PortChimera",
    "PChi100G5S2P",
    "PChi100G5S2P_b",
    "PChi40G2S2P",
    "POdin1G3S6P",
    "POdin1G3S6P_b",
    "POdin1G3S6PE",
    "POdin1G3S2PT",
    "POdin5G4S6PCU",
    "POdin10G5S6PCU",
    "POdin10G5S6PCU_b",
    "POdin10G3S6PCU",
    "POdin10G3S2PCU",
    "POdin10G1S2P",
    "POdin10G1S2P_b",
    "POdin10G1S2P_c",
    "POdin10G1S6P",
    "POdin10G1S6P_b",
    "POdin10G1S2PT",
    "POdin10G1S2P_d",
    "POdin10G1S12P",
    "POdin40G2S2P",
    "POdin40G2S2PB",
    "POdin100G3S1P",
    "POdin1G3S6PT1RJ45",
    "POdin1G4S4PCombi",
    "POdin1G4S4PCombi_b",
    "POdin10G4S2PCombi",
    "POdin10G4S2PCombi_b",
    "POdin10G6S6P_a",
    "PLoki100G3S1P",
    "PLoki100G3S1P_b",
    "PLoki100G3S1PSE",
    "PLoki100G3S1PB",
    "PLoki100G5S1P",
    "PLoki100G5S2P",
    "PLoki100G3S1PB_b",
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
