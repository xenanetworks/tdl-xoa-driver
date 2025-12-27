#: Other types which are used by ports or as a parameter to attribute set method.

"""Other types used in Xena test ports."""

from .internals.core.token import Token
from .internals.core.transporter.protocol.payload.types import Hex
from .internals.commands.subtypes import (
    ArpEntry,
    NdpEntry,
    DhcpEntry,
    GroupAddressElem,
    VlanTag,
    QueueStatsElem,
)

# indices types
from .internals.hli.indices.connection_group.cg import ConnectionGroupIdx as ConnectionGroup
from .internals.hli.indices.filter.base_filter import BaseFilterIdx as BasePortFilter
from .internals.hli.indices.filter.genuine_filter import GenuineFilterIdx as GenuinePortFilter
from .internals.hli.indices.length_term import LengthTermIdx as LengthTerm
from .internals.hli.indices.match_term import MatchTermIdx as MatchTerm
from .internals.hli.indices.port_dataset import PortDatasetIdx as PortDataset
from .internals.hli.indices.streams.base_stream import BaseStreamIdx as BaseStream
from .internals.hli.indices.streams.genuine_stream import GenuineStreamIdx as GenuineStream
from .internals.hli.ports.port_l23.chimera.port_emulation import CFlow as ImpairmentFlow
from .internals.hli.ports.port_l23.chimera.filter_definition.general import ModeBasic as BasicImpairmentFlowFilter
from .internals.hli.ports.port_l23.chimera.filter_definition.general import ModeExtended as ExtendedImpairmentFlowFilter
from xoa_driver.internals.hli.indices.macsecscs.genuine_macsecsc import GenuineMacSecTxScIdx, GenuineMacSecRxScIdx


__all__ = (
    "Token",
    "Hex",
    "ArpEntry",
    "NdpEntry",
    "DhcpEntry",
    "GroupAddressElem",
    "VlanTag",
    "QueueStatsElem",
    "ConnectionGroup",
    "BasePortFilter",
    "GenuinePortFilter",
    "LengthTerm",
    "MatchTerm",
    "PortDataset",
    "BaseStream",
    "GenuineStream",
    "ImpairmentFlow",
    "BasicImpairmentFlowFilter",
    "ExtendedImpairmentFlowFilter",
    "GenuineMacSecTxScIdx",
    "GenuineMacSecRxScIdx",
)
