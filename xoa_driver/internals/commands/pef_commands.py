from __future__ import annotations
from dataclasses import dataclass
import ipaddress
import typing
import functools

from xoa_driver.internals.core.builders import (
    build_get_request,
    build_set_request
)
from xoa_driver.internals.core import interfaces
from xoa_driver.internals.core.token import Token
from xoa_driver.internals.core.transporter.registry import register_command
from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    RequestBodyStruct,
    ResponseBodyStruct,
    XmpByte,
    XmpHex,
    XmpInt,
    XmpIPv4Address,
    XmpIPv6Address,
    XmpSequence,
    Hex,
)
from .enums import (
    OnOff,
    YesNo,
    ProtocolOption,
    FilterUse,
    InfoAction,
    L2PlusPresent,
    L3Present,
    FilterMode,
    FilterType,
    FilterVlanType,
)


@register_command
@dataclass
class PEF_INIT:
    """
    Prepares for setting up a filter definition.  When called, all filter
    definitions in the shadow-set which are not applied are discarded and replaced
    with the default values (DEFAULT).

    .. note::

        There are 2 register copies used to configure the filters:

            (1) ``Shadow-copy (type value = 0)`` temporary copy configured by sever.
                Values stored in ``shadow-copy`` have no immediate effect on the flow filters. PEF_APPLY will pass the values from the ``shadow-copy`` to the ``working-copy``.

            (2) ``Working-copy (type value = 1)`` reflects what is currently used for filtering in the FPGA.
                ``Working-copy`` cannot be written directly. Only ``shadow-copy`` allows direct write.

            (3) All ``set`` actions are performed on ``shadow-copy`` ONLY.

            (4) Only when PEF_APPLY is called, ``working-copy`` and FPGA are updated with values from the ``shadow-copy``.
    """

    code: typing.ClassVar[int] = 1700
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Setting up a filter definition.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PEF_APPLY:
    """
    Applies filter definitions from "shadow-copy" to "working-copy". This
    also pushes these settings to the FPGA.
    """

    code: typing.ClassVar[int] = 1701
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Applies filter definitions from "shadow-copy" to "working-copy"."""

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PEF_ENABLE:
    """
    Defines if filtering is enabled for the flow.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1702
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        state: OnOff = field(XmpByte())
        """coded byte, specifies the state of the filter."""

    class SetDataAttr(RequestBodyStruct):
        state: OnOff = field(XmpByte())
        """coded byte, specifies the state of the filter."""

    def get(self) -> Token[GetDataAttr]:
        """Get if filtering is enabled for the flow.

        :return: filter state
        :rtype: PEF_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, state: OnOff) -> Token[None]:
        """Set the filter state.

        :param state: state of the filter
        :type state: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], state=state))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Set the filter state to OFF.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Set the filter state to ON.
    """


@register_command
@dataclass
class PEF_ETHSETTINGS:
    """
    Defines what filter action is performed on the Ethernet header.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1703
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of Ethernet information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of Ethernet information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of Ethernet information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of Ethernet information."""

    def get(self) -> Token[GetDataAttr]:
        """Get the filter action settings on Ethernet header.

        :return: Filter setting
        :rtype: PEF_ETHSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set the filter action settings on Ethernet header.

        :param use: specifies if Ethernet information is expected
        :type use: FilterUse
        :param action: specifies the use of Ethernet information.
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_ETHSRCADDR:
    """
    Defines the Ethernet Source Address settings for the Ethernet filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1704
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of Ethernet Source Address information."""
        value: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000."""
        mask: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF."""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of Ethernet Source Address information."""
        value: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000."""
        mask: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF."""

    def get(self) -> Token[GetDataAttr]:
        """Get the Ethernet Source Address settings for the Ethernet filter.

        :return: the Ethernet Source Address settings for the Ethernet filter
        :rtype: PEF_ETHSRCADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: Hex, mask: Hex) -> Token[None]:
        """Set the Ethernet Source Address settings for the Ethernet filter.

        :param use: specifies the use of Ethernet Source Address information
        :type use: OnOff
        :param value: specifying the six bytes of the address. Default value: 0x000000000000.
        :type value: Hex
        :param mask: specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF.
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Ethernet Source Address is not used for the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """Ethernet Source Address is used for the filter."""


@register_command
@dataclass
class PEF_ETHDESTADDR:
    """
    Defines the Ethernet Destination Address settings for the Ethernet filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1705
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of Ethernet information"""
        value: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000"""
        mask: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of Ethernet information"""
        value: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the six bytes of the address. Default value: 0x000000000000"""
        mask: Hex = field(XmpHex(size=6))
        """six hex bytes, specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the Ethernet Destination Address settings for the Ethernet filter.

        :return: the Ethernet Destination Address settings for the Ethernet filter.
        :rtype: PEF_ETHDESTADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: Hex, mask: Hex) -> Token[None]:
        """Set the Ethernet Destination Address settings for the Ethernet filter.

        :param use: specifies the use of Ethernet Destination Address information
        :type use: OnOff
        :param value: specifying the six bytes of the address. Default value: 0x000000000000
        :type value: Hex
        :param mask: specifying the mask corresponding to the address. Default value: 0xFFFFFFFFFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Ethernet Destination Address is not used for the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """Ethernet Destination Address is used for the filter."""


@register_command
@dataclass
class PEF_L2PUSE:
    """
    Defines what Layer 2+ protocols that are present and may be used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1706
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: L2PlusPresent = field(XmpByte())
        """coded byte, specifies the presence of Layer 2+ protocols."""

    class SetDataAttr(RequestBodyStruct):
        use: L2PlusPresent = field(XmpByte())
        """coded byte, specifies the presence of Layer 2+ protocols."""

    def get(self) -> Token[GetDataAttr]:
        """Get the Layer 2+ protocols settings for the filter.

        :return: the Layer 2+ protocols settings for the filter
        :rtype: PEF_L2PUSE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: L2PlusPresent) -> Token[None]:
        """Set the Layer 2+ protocols settings for the filter.

        :param use:  specifies the presence of Layer 2+ protocols.
        :type use: L2PlusPresent
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use))

    set_na = functools.partialmethod(set, L2PlusPresent.NA)
    """Set the presence of Layer 2+ protocols to NA."""

    set_vlan1 = functools.partialmethod(set, L2PlusPresent.VLAN1)
    """Set the presence of Layer 2+ protocols to one VLAN Tag."""

    set_vlan2 = functools.partialmethod(set, L2PlusPresent.VLAN2)
    """Set the presence of Layer 2+ protocols to two VLAN Tags."""

    set_mpls = functools.partialmethod(set, L2PlusPresent.MPLS)
    """Set the presence of Layer 2+ protocols to MPLS."""


@register_command
@dataclass
class PEF_VLANSETTINGS:
    """
    Defines what filter action is performed on the VLAN header.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1707
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies if VLAN information is expected."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the use of VLAN information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies if VLAN information is expected."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the use of VLAN information."""

    def get(self) -> Token[GetDataAttr]:
        """Get filter action settings on VLAN header.

        :return: filter action settings on VLAN header
        :rtype: PEF_VLANSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set filter action settings on VLAN header.

        :param use: specifies if VLAN information is expected
        :type use: FilterUse
        :param action: specifies the action of VLAN information
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_VLANTAG:
    """
    Basic mode only. Defines the VLAN TAG settings for the VLAN filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1708
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType
    _vlan_type: FilterVlanType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of VLAN information"""
        value: int = field(XmpInt())
        """decimal digits, specifying the 12 bit value of the tag. Default value: 0."""
        mask: Hex = field(XmpHex(size=2))
        """two hex digits, specifying the 12 bit value of the tag. Default value: 0x0FFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of VLAN information"""
        value: int = field(XmpInt())
        """decimal digits, specifying the 12 bit value of the tag. Default value: 0."""
        mask: Hex = field(XmpHex(size=2))
        """two hex digits, specifying the 12 bit value of the tag. Default value: 0x0FFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the VLAN TAG settings for the VLAN filter.

        :return: the VLAN TAG settings for the VLAN filter
        :rtype: PEF_VLANTAG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._vlan_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set the VLAN TAG settings for the VLAN filter.

        :param use: specifies the use of VLAN TAG information
        :type use: OnOff
        :param value: specifying the 12 bit value of the tag. Default value: 0.
        :type value: int
        :param mask: specifying the 12 bit value of the tag. Default value: 0x0FFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._vlan_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """VLAN TAG is not used for the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """VLAN TAG is used for the filter."""


@register_command
@dataclass
class PEF_VLANPCP:
    """
    Basic mode only. Defines the VLAN PCP settings for the VLAN filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1709
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType
    _vlan_type: FilterVlanType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of VLAN information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the PCP. Default value: 0 (Range: 0 to 7)"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the 8 bit value mask. Default value: 0x07"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of VLAN information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the PCP. Default value: 0 (Range: 0 to 7)"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the 8 bit value mask. Default value: 0x07"""

    def get(self) -> Token[GetDataAttr]:
        """Get the VLAN PCP settings for the VLAN filter.

        :return: the VLAN PCP settings for the VLAN filter
        :rtype: PEF_VLANPCP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._vlan_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set the VLAN PCP settings for the VLAN filter.

        :param use: specifies the use of VLAN PCP information
        :type use: OnOff
        :param value: specifying the value of the PCP. Default value: 0 (Range: 0 to 7)
        :type value: int
        :param mask: specifying the 8 bit value mask. Default value: 0x07
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._vlan_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """VLAN PCP is not used for the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """VLAN PCP is used for the filter."""


@register_command
@dataclass
class PEF_MPLSSETTINGS:
    """
    Basic mode only. Defines what filter action is performed on the MPLS header.
    """

    code: typing.ClassVar[int] = 1710
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of MPLS information"""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action on MPLS information"""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of MPLS information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action on MPLS information"""

    def get(self) -> Token[GetDataAttr]:
        """Get the filter action settings on the MPLS header.

        :return: the filter action settings on the MPLS header
        :rtype: PEF_MPLSSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set the filter action settings on the MPLS header.

        :param use: specifies the use of MPLS information
        :type use: FilterUse
        :param action: specifies specifies if MPLS information is expected
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_MPLSLABEL:
    """
    Basic mode only. Defines the MPLS label settings for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1711
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of MPLS information."""
        value: int = field(XmpInt())
        """integer, specifying the 20 bit value of the label. Default value: 0."""
        mask: Hex = field(XmpHex(size=3))
        """three hex bytes, specifying the 20 bit value of the label. Default value: 0x0FFFFF,"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of MPLS information."""
        value: int = field(XmpInt())
        """integer, specifying the 20 bit value of the label. Default value: 0."""
        mask: Hex = field(XmpHex(size=3))
        """three hex bytes, specifying the 20 bit value of the label. Default value: 0x0FFFFF,"""

    def get(self) -> Token[GetDataAttr]:
        """Get the MPLS label settings for the filter.

        :return: the MPLS label settings for the filter
        :rtype: PEF_MPLSLABEL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set the MPLS label settings for the filter.

        :param use: specifies the use of MPLS label information.
        :type use: OnOff
        :param value: specifying the 20-bit value of the label. Default value: 0.
        :type value: int
        :param mask: specifying the 20-bit value of the label. Default value: 0x0FFFFF,
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """The MPLS label is not used by the filter"""

    set_on = functools.partialmethod(set, OnOff.ON)
    """The MPLS label is used by the filter"""


@register_command
@dataclass
class PEF_MPLSTOC:
    """
    Basic mode only. Defines the MPLS TOC settings for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1712
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of MPLS TOC information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7)."""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask for the value of the MPLS TOC. Default value: 0x07"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of MPLS TOC information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7)."""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask for the value of the MPLS TOC. Default value: 0x07"""

    def get(self) -> Token[GetDataAttr]:
        """Get the MPLS TOC settings for the filter.

        :return: the MPLS TOC settings for the filter
        :rtype: PEF_MPLSTOC.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set the MPLS TOC settings for the filter.

        :param use: specifies the use of MPLS TOC information
        :type use: OnOff
        :param value: specifying the value of the MPLS TOC. Default value: 0 (Range: 0 to 7).
        :type value: int
        :param mask: specifying the filter mask for the value of the MPLS TOC. Default value: 0x07
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """The MPLS TOC is not used by the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """The MPLS TOC is used by the filter."""


@register_command
@dataclass
class PEF_L3USE:
    """
    Basic mode only. Defines what Layer 3 protocols that are present and may be used
    for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1713
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: L3Present = field(XmpByte())
        """coded byte, specifies the presence of Layer 3 protocols:"""

    class SetDataAttr(RequestBodyStruct):
        use: L3Present = field(XmpByte())
        """coded byte, specifies the presence of Layer 3 protocols:"""

    def get(self) -> Token[GetDataAttr]:
        """Get Layer 3 protocols settings for the filter.

        :return: Layer 3 protocols settings for the filter.
        :rtype: PEF_L3USE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: L3Present) -> Token[None]:
        """Set Layer 3 protocols settings for the filter.

        :param use: specifies the presence of Layer 3 protocols
        :type use: L3Present
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use))

    set_na = functools.partialmethod(set, L3Present.NA)
    """Set Layer 3 protocol presence to NA."""

    set_ip4 = functools.partialmethod(set, L3Present.IP4)
    """Set Layer 3 protocol presence to IPv4."""

    set_ip6 = functools.partialmethod(set, L3Present.IP6)
    """Set Layer 3 protocol presence to IPv6."""


@register_command
@dataclass
class PEF_IPV4SETTINGS:
    """
    Basic mode only. Defines what filter action is performed on the IPv4 header.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1714
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of IPv4 information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of IPv4 information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of IPv4 information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of IPv4 information."""

    def get(self) -> Token[GetDataAttr]:
        """Get the filter action settings on IPv4 header.

        :return: the filter action settings on IPv4 header
        :rtype: PEF_IPV4SETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set the filter action settings on IPv4 header.

        :param use: specifies the use of IPv4 information
        :type use: FilterUse
        :param action: specifies the action of IPv4 information
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_IPV4SRCADDR:
    """
    Basic mode only. Defines the IPv4 Source Address settings for the IPv4 filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1715
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 Source Address."""
        value: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, specifying the four bytes of the address. Default value: 0.0.0.0"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 Source Address."""
        value: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, specifying the four bytes of the address. Default value: 0.0.0.0"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv4 Source Address settings for the IPv4 filter.

        :return: the IPv4 Source Address settings for the IPv4 filter
        :rtype: PEF_IPV4SRCADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: ipaddress.IPv4Address, mask: Hex) -> Token[None]:
        """Set the IPv4 Source Address settings for the IPv4 filter.

        :param use: specifies the use of IPv4 Source Address information
        :type use: OnOff
        :param value: specifying the four bytes of the address. Default value: 0.0.0.0
        :type value: ipaddress.IPv4Address
        :param mask: specifying the filter mask of the value. Default value: 0xFFFFFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv4 Source Address is not used by the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv4 Source Address is used by the filter."""


@register_command
@dataclass
class PEF_IPV4DESTADDR:
    """
    Basic mode only. Defines the IPv4 Destination Address settings for the IPv4 filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1716
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 Destination Address."""
        value: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, specifying the four bytes of the address. Default value: 0.0.0.0"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 Destination Address."""
        value: ipaddress.IPv4Address = field(XmpIPv4Address())
        """address, specifying the four bytes of the address. Default value: 0.0.0.0"""
        mask: Hex = field(XmpHex(size=4))
        """four hex bytes, specifying the filter mask of the value. Default value: 0xFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv4 Destination Address settings for the IPv4 filter.

        :return: the IPv4 Destination Address settings for the IPv4 filter
        :rtype: PEF_IPV4DESTADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: ipaddress.IPv4Address, mask: Hex) -> Token[None]:
        """Set the IPv4 Destination Address settings for the IPv4 filter.

        :param use: specifies the use of IPv4 Destination Address information
        :type use: OnOff
        :param value: specifying the four bytes of the address. Default value: 0.0.0.0
        :type value: ipaddress.IPv4Address
        :param mask: specifying the filter mask of the value. Default value: 0xFFFFFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv4 Destination Address is not used by the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv4 Destination Address is used by the filter."""


@register_command
@dataclass
class PEF_IPV4DSCP:
    """
    Basic mode only. Defines if IPv4 DSCP/TOS settings used for the IPv4 filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1717
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default value: 0"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv4 information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default value: 0"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC"""

    def get(self) -> Token[GetDataAttr]:
        """Get IPv4 DSCP/TOS settings for the filter.

        :return: IPv4 DSCP/TOS settings for the filter.
        :rtype: PEF_IPV4DSCP.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set IPv4 DSCP/TOS settings for the filter.

        :param use: specifies the use of IPv4 DSCP/TOS information.
        :type use: OnOff
        :param value: specifying the value of the IPv4 DSCP/TOS in the upper 6 bits. value[7:2] = DSCP/TOS, value[1:0] = reserved (must be zero). Default value: 0
        :type value: int
        :param mask: specifying the filter mask of the value in the upper 6 bits. mask[7:2] = DSCP/TOS mask, mask[1:0] = reserved (must be zero). Default value: 0xFC
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv4 DSCP/TOS is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv4 DSCP/TOS is used in the filter."""


@register_command
@dataclass
class PEF_IPV6SETTINGS:
    """
    Basic mode only. Defines what filter action is performed on the IPv6 header.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1718
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of IPv6 information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of IPv6 information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of IPv6 information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of IPv6 information."""

    def get(self) -> Token[GetDataAttr]:
        """Get filter action settings on the IPv6 header.

        :return: specifies the use of IPv6 header
        :rtype: PEF_IPV6SETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set filter action settings on the IPv6 header.

        :param use: specifies the use of IPv6 header
        :type use: FilterUse
        :param action: specifies the action of IPv6 header
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_IPV6SRCADDR:
    """
    Basic mode only. Defines the IPv6 Source Address settings for the IPv6 filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1719
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 Source Address."""
        value: ipaddress.IPv6Address = field(XmpIPv6Address())
        """16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000"""
        mask: Hex = field(XmpHex(size=16))
        """16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 Source Address."""
        value: ipaddress.IPv6Address = field(XmpIPv6Address())
        """16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000"""
        mask: Hex = field(XmpHex(size=16))
        """16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv6 Source Address settings for the IPv6 filter.

        :return: the IPv6 Source Address settings for the IPv6 filter
        :rtype: PEF_IPV6SRCADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: ipaddress.IPv6Address, mask: Hex) -> Token[None]:
        """Set the IPv6 Source Address settings for the IPv6 filter.

        :param use: specifies the use of IPv6 Source Address information
        :type use: OnOff
        :param value: specifying the address. Default : 0x00000000000000000000000000000000
        :type value: ipaddress.IPv6Address
        :param mask: specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv6 Source Address is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv6 Source Address is used in the filter."""


@register_command
@dataclass
class PEF_IPV6DESTADDR:
    """
    Basic mode only. Defines the IPv6 Destination Address settings for the IPv6 filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1720
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 Destination Address."""
        value: ipaddress.IPv6Address = field(XmpIPv6Address())
        """16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000"""
        mask: Hex = field(XmpHex(size=16))
        """16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 Destination Address."""
        value: ipaddress.IPv6Address = field(XmpIPv6Address())
        """16 hex bytes, specifying the address. Default : 0x00000000000000000000000000000000"""
        mask: Hex = field(XmpHex(size=16))
        """16 hex bytes, specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the IPv6 Destination Address settings for the IPv6 filter.

        :return: IPv6 Destination Address settings for the IPv6 filter
        :rtype: PEF_IPV6DESTADDR.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: ipaddress.IPv6Address, mask: Hex) -> Token[None]:
        """Set the IPv6 Destination Address settings for the IPv6 filter.

        :param use:  specifies the use of IPv6 Destination Address information
        :type use: OnOff
        :param value: specifying the address. Default : 0x00000000000000000000000000000000
        :type value: ipaddress.IPv6Address
        :param mask: specifying the six first bytes of the address. Default value: 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv6 Destination Address is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv6 Destination Address is used in the filter."""


@register_command
@dataclass
class PEF_IPV6TC:
    """
    Basic mode only. Defines the IPv6 Traffic Class settings used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1721
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of IPv6 information."""
        value: int = field(XmpByte())
        """byte, specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0"""
        mask: Hex = field(XmpHex(size=1))
        """hex byte, specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC"""

    def get(self) -> Token[GetDataAttr]:
        """Get IPv6 Traffic Class settings used for the filter.

        :return: IPv6 Traffic Class settings used for the filter
        :rtype: PEF_IPV6TC.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set IPv6 Traffic Class settings used for the filter.

        :param use: specifies the use of the IPv6 Traffic Class information.
        :type use: OnOff
        :param value: specifying the value of the IPv6 Traffic Class in the upper 6 bits. value[7:2] = IPv6 Traffic Class. value[1:0] = reserved (must be zero). Default value: 0
        :type value: int
        :param mask: specifying the filter mask for the value in the upper 6 bits. mask[7:2] = IPv6 Traffic Class mask. mask[1:0] = reserved (must be zero). Default value: 0xFC
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """IPv6 Traffic Class is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """IPv6 Traffic Class is used in the filter."""


@register_command
@dataclass
class PEF_UDPSETTINGS:
    """
    Basic mode only. Controls if UDP packet information is used for flow filtering.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1722
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of UDP information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies action use of UDP information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of UDP information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of UDP information."""

    def get(self) -> Token[GetDataAttr]:
        """Get filter settings on the UDP header.

        :return: filter action settings on the UDP header
        :rtype: PEF_UDPSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set filter settings on the UDP header.

        :param use: specifies the use of UDP information.
        :type use: FilterUse
        :param action: specifies the action of UDP information.
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_UDPSRCPORT:
    """
    Basic mode only. Defines UDP Source Port settings used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``

    """

    code: typing.ClassVar[int] = 1723
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of UDP Source Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the UDP Source Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of UDP Source Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the UDP Source Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get UDP Source Port settings used for the filter.

        :return: UDP Source Port settings used for the filter.
        :rtype: PEF_UDPSRCPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set UDP Source Port settings used for the filter.

        :param use: specifies the use of UDP Source Port information
        :type use: OnOff
        :param value: specifying the value of the UDP Source Port. Default value: 0
        :type value: int
        :param mask: specifying the filter mask for the value. Default value: 0xFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """UDP Source Port is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """UDP Source Port is used in the filter."""


@register_command
@dataclass
class PEF_UDPDESTPORT:
    """
    Basic mode only. Defines UDP Destination Port settings used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.
    """

    code: typing.ClassVar[int] = 1724
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of UDP Destination Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the UDP Destination Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of UDP Destination Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the UDP Destination Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get UDP Destination Port settings used for the filter.

        :return: UDP Destination Port settings used for the filter.
        :rtype: PEF_UDPDESTPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set UDP Destination Port settings used for the filter.

        :param use: specifies the use of UDP Destination Port information
        :type use: OnOff
        :param value: specifying the value of the UDP Destination Port. Default value: 0
        :type value: int
        :param mask: specifying the filter mask for the value. Default value: 0xFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """UDP Destination Port is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """UDP Destination Port is used in the filter."""


@register_command
@dataclass
class PEF_TCPSETTINGS:
    """
    Basic mode only. Defines if filtering on TCP information is used for flow
    filtering.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1725
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of TCP information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of TCP information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of TCP information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of TCP information."""

    def get(self) -> Token[GetDataAttr]:
        """Get filter action settings on the TCP header.

        :return: filter action settings on the TCP header.
        :rtype: PEF_TCPSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set filter action settings on the TCP header.

        :param use: specifies the use of TCP information.
        :type use: FilterUse
        :param action: specifies the action of TCP information.
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_TCPSRCPORT:
    """
    Basic mode only. Defines TCP Source Port settings used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1726
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TCP Source Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the TCP Source Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TCP Source Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the TCP Source Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get TCP Source Port settings used for the filter.

        :return: TCP Source Port settings used for the filter.
        :rtype: PEF_TCPSRCPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set TCP Source Port settings used for the filter.

        :param use:  specifies the use of TCP Source Port information
        :type use: OnOff
        :param value: specifies the value of the TCP Source Port. Default value: 0
        :type value: int
        :param mask: specifies the filter mask for the value. Default value: 0xFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """TCP Source Port is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """TCP Source Port is used in the filter."""


@register_command
@dataclass
class PEF_TCPDESTPORT:
    """
    Basic mode only. Defines TCP Destination Port settings used for the filter.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1727
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TCP Destination Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the TCP Destination Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TCP Destination Port information"""
        value: int = field(XmpInt())
        """integer , specifying the value of the TCP Destination Port. Default value: 0"""
        mask: Hex = field(XmpHex(size=2))
        """two hex bytes , specifying the filter mask for the value. Default value: 0xFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get TCP Destination Port settings used for the filter.

        :return: TCP Destination Port settings used for the filter.
        :rtype: PEF_TCPDESTPORT.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: OnOff, value: int, mask: Hex) -> Token[None]:
        """Set TCP Destination Port settings used for the filter.

        :param use: specifies the use of TCP Destination Port information
        :type use: OnOff
        :param value: specifies the value of the TCP Destination Port. Default value: 0
        :type value: int
        :param mask: specifies the filter mask for the value. Default value: 0xFFFF
        :type mask: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, value=value, mask=mask))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """TCP Destination Port is not used in the filter."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """TCP Destination Port is used in the filter."""


@register_command
@dataclass
class PEF_ANYSETTINGS:
    """
    Basic mode only. Defines if filtering on ANY field in a packet is used for flow filtering.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1728
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of ANY field information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of ANY field information."""

    class SetDataAttr(RequestBodyStruct):
        use: FilterUse = field(XmpByte())
        """coded byte, specifies the use of ANY field information."""
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of ANY field information."""

    def get(self) -> Token[GetDataAttr]:
        """Get the settings of filtering state on ANY field in a packet.

        :return: settings of filtering state on ANY field in a packet.
        :rtype: PEF_ANYSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, use: FilterUse, action: InfoAction) -> Token[None]:
        """Set the settings of filtering state on ANY field in a packet.

        :param use: specifies the use of ANY field information.
        :type use: FilterUse
        :param action:  specifies the action of ANY field information.
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], use=use, action=action))


@register_command
@dataclass
class PEF_ANYCONFIG:
    """
    Basic mode only. Defines the ANY field filter configuration. The "ANY field"
    filter will match 6 consecutive bytes in the incoming packets at a programmable
    offset. Applying a mask, allows to only filter based on selected bits within the
    6 bytes.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1729
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        position: int = field(XmpByte())
        """byte, specifies the start position of the ANY field. Default value: 0, Range:0-127"""
        value: Hex = field(XmpHex(size=6))
        """6 hex bytes, specifying the six bytes of the field. Default value: 0x000000000000"""
        mask: Hex = field(XmpHex(size=6))
        """6 hex bytes, specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF"""

    class SetDataAttr(RequestBodyStruct):
        position: int = field(XmpByte())
        """byte, specifies the start position of the ANY field. Default value: 0, Range:0-127"""
        value: Hex = field(XmpHex(size=6))
        """6 hex bytes, specifying the six bytes of the field. Default value: 0x000000000000"""
        mask: Hex = field(XmpHex(size=6))
        """6 hex bytes, specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF"""

    def get(self) -> Token[GetDataAttr]:
        """Get the ANY field filter configuration.

        :return: the ANY field filter configuration
        :rtype: PEF_ANYCONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, position: int, value: Hex, mask: Hex) -> Token[None]:
        """Set the ANY field filter configuration

        :param position: specifies the start position of the ANY field. Default value: 0, Range:0-127
        :type position: int
        :param value: specifying the six bytes of the field. Default value: 0x000000000000
        :type value: str
        :param mask: specifying the six bytes of the field. Default value: 0xFFFFFFFFFFFF
        :type mask: str
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], position=position, value=value, mask=mask))


@register_command
@dataclass
class PEF_TPLDSETTINGS:
    """
    Defines if filtering on TPLD field in a packet is used for flow filtering. The
    TPLD filter allows filtering based on the Xena TPLD ID. The TPLD
    ID is meta data, which can be inserted into the Ethernet packets by Xena traffic
    generators. For each flow filter, can the filter be based on 16 TPLD ID values.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1730
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of TPLD information."""

    class SetDataAttr(RequestBodyStruct):
        action: InfoAction = field(XmpByte())
        """coded byte, specifies the action of TPLD information."""

    def get(self) -> Token[GetDataAttr]:
        """Get the settings of filtering on TPLD field in a packet.

        :return: the settings of filtering on TPLD field in a packet.
        :rtype: PEF_TPLDSETTINGS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, action: InfoAction) -> Token[None]:
        """Set the settings of filtering on TPLD field in a packet.

        :param action: specifies the action of TPLD information.
        :type action: InfoAction
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], action=action))


@register_command
@dataclass
class PEF_TPLDCONFIG:
    """
    Defines the TPLD filter configuration. There are only 16 TPLD filter, thus the index values are from 0 to 15.

    .. note::

        For SET, the only allowed ``_filter_type`` is ``shadow-copy``.

    """

    code: typing.ClassVar[int] = 1731
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType
    _test_payload_filter_index: int

    class GetDataAttr(ResponseBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TPLD field information."""
        id: int = field(XmpInt())
        """int, specifies the TPLD ID. Range: 0-2015, Default value: 0"""

    class SetDataAttr(RequestBodyStruct):
        use: OnOff = field(XmpByte())
        """coded byte, specifies the use of TPLD field information."""
        id: int = field(XmpInt())
        """int, specifies the TPLD ID. Range: 0-2015, Default value: 0"""

    def get(self) -> Token[GetDataAttr]:
        """Get the TPLD filter configuration.

        :return: the use of TPLD field information, and the TPLD ID. Range: 0-2015, Default value: 0
        :rtype: PEF_TPLDCONFIG.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._test_payload_filter_index]))

    def set(self, use: OnOff, id: int) -> Token[None]:
        """Set the TPLD filter configuration.

        :param use: specifies the use of TPLD field information
        :type use: OnOff
        :param id: specifies the TPLD ID. Range: 0-2015, Default value: 0
        :type id: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type, self._test_payload_filter_index], use=use, id=id))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """The TPLD information is not used."""

    set_on = functools.partialmethod(set, OnOff.ON)
    """The TPLD information is used."""


@register_command
@dataclass
class PEF_ISSHADOWDIRTY:
    """
    Get shadow filter status (if shadow is in sync with working copy or not).
    """

    code: typing.ClassVar[int] = 1734
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class GetDataAttr(ResponseBodyStruct):
        is_in_sync: YesNo = field(XmpByte())
        """coded byte, if shadow is in sync with working copy or not."""

    def get(self) -> Token[GetDataAttr]:
        """Get shadow filter status.

        :return: if shadow is in sync with working copy or not.
        :rtype: PEF_ISSHADOWDIRTY.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PEF_CANCEL:
    """Undo updates to shadow filter settings, sets dirty false."""

    code: typing.ClassVar[int] = 1735
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Undo updates to shadow filter settings, sets dirty false.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex]))


@register_command
@dataclass
class PEF_VALUE:
    """
    This command is valid only for ``Extended filter mode`` (check :class:`PEF_MODE`).

    Defines the byte values that can be matched if selected by :class:`PEF_MASK`.

    If ``<protocol_segment_index> = 0`` the maximum number of match value
    bytes that can be set is determined by the total length of the protocol segments
    specified with PEF_PROTOCOL.

    E.g. if PEF_PROTOCOL is set to ETHERNET then only
    12 bytes can be set. In order to set the full 128 bytes, either specify a
    detailed protocol segment list, or use the raw protocol segment type. This specifies 12 + 116 = 128 bytes.

    If ``<protocol_segment_index> != 0`` only the bytes covered by that segment are manipulated,
    so if PEF_PROTOCOL is set to ``ETHERNET VLAN ETHERTYPE eCPRI`` then ``<protocol_segment_index> = 4`` selects the 8
    bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18.

    For ``set`` command where fewer value bytes are provided than specified by the protocol segment, those unspecified bytes are set to zero.

    The ``get`` command always returns the number of bytes specified by the protocol segment.
    """

    code: typing.ClassVar[int] = 1777
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType
    _protocol_segment_index: int

    class GetDataAttr(ResponseBodyStruct):
        value: Hex = field(XmpHex())
        """list of hex bytes, the raw bytes comprising the packet header."""

    class SetDataAttr(RequestBodyStruct):
        value: Hex = field(XmpHex())
        """list of hex bytes, the raw bytes comprising the packet header."""

    def get(self) -> Token[GetDataAttr]:
        """Get the byte values that can be matched if selected by :class:`PEF_MASK`.

        :return: the byte values that can be matched if selected by :class:`PEF_MASK`
        :rtype: PEF_VALUE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, value: Hex) -> Token[None]:
        """Set the byte values that can be matched if selected by :class:`PEF_MASK`.

        :param value: the raw bytes comprising the packet header
        :type value: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], value=value))


@register_command
@dataclass
class PEF_MASK:
    """
    This command is valid only for ``Extended filter mode`` (check :class:`PEF_MODE`).

    Defines the mask byte values that select the values specified by :class:`PEF_VALUE`.

    For a chosen ``<protocol_segment_index>`` the first byte in the value masks the
    first byte of the corresponding :class:`PEF_VALUE` and so on.

    If ``<protocol_segment_index> = 0`` the maximum number of match value
    bytes that can be set is determined by the total length of the protocol segments
    specified with PEF_PROTOCOL`.

    E.g. if PEF_PROTOCOL is set to ETHERNET then only
    12 bytes can be set. In order to set the full 128 bytes, either specify a
    detailed protocol segment list, or use the raw protocol segment type. This specifies 12 + 116 = 128 bytes.

    If ``<protocol_segment_index> != 0`` only the bytes covered by that segment are manipulated,
    so if PEF_PROTOCOL is set to ``ETHERNET VLAN ETHERTYPE eCPRI`` then ``<protocol_segment_index> = 4`` selects the 8
    bytes of the eCPRI header starting at byte position (12 + 2 + 4) = 18.

    ``get/set`` semantics are similar to :class:`PEF_VALUE`.
    """

    code: typing.ClassVar[int] = 1778
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType
    _protocol_segment_index: int

    class GetDataAttr(ResponseBodyStruct):
        masks: Hex = field(XmpHex())

    class SetDataAttr(RequestBodyStruct):
        masks: Hex = field(XmpHex())

    def get(self) -> Token[GetDataAttr]:
        """Get the mask byte values that select the values specified by :class:`PEF_VALUE`.

        :return: the mask byte values that select the values specified by :class:`PEF_VALUE`.
        :rtype: PEF_MASK.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, masks: Hex) -> Token[None]:
        """Set the mask byte values that select the values specified by :class:`PEF_VALUE``.

        :param masks: mask byte values
        :type masks: Hex
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], masks=masks))


@register_command
@dataclass
class PEF_PROTOCOL:
    """
    This command is valid only for ``Extended filter mode`` (check :class:`PEF_MODE`).

    Defines the sequence of protocol segments that can be
    matched. The total length of the specified segments cannot exceed 128 bytes. If
    an existing sequence of segments is changed (using PEF_PROTOCOL) the underlying
    value and mask bytes remain unchanged, even though the semantics of those bytes
    may have changed. However, if the total length, in bytes, of the segments is
    reduced, then the excess bytes of value and mask are set to zero. I.e. to update
    an existing filter, you must first correct the list of segments (using
    PEF_PROTOCOL) and subsequently update the filtering value (using :class:`PEF_VALUE`) and filtering mask (:class:`PEF_MASK`).
    """

    code: typing.ClassVar[int] = 1779
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        segment_list: typing.List[ProtocolOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of bytes, specifying the list of protocol segment types in the order they are expected in a frame. First segment type must be ETHERNET;
        the following can be chosen freely.
        """

    class SetDataAttr(RequestBodyStruct):
        segment_list: typing.List[ProtocolOption] = field(XmpSequence(types_chunk=[XmpByte()]))
        """list of bytes, specifying the list of protocol segment types in the order they are expected in a frame. First segment type must be ETHERNET;
        the following can be chosen freely.
        """

    def get(self) -> Token[GetDataAttr]:
        """Get the sequence of protocol segments that can be matched.

        :return: the sequence of protocol segments that can be matched.
        :rtype: PEF_PROTOCOL.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, segment_list: typing.List[ProtocolOption]) -> Token[None]:
        """Set the sequence of protocol segments that can be matched.

        :param segment_list: specifying the list of protocol segment types in the order they are expected in a frame.
            First segment type must be ``ETHERNET``; the following can be chosen freely.
        :type segment_list: typing.List[ProtocolOption]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], segment_list=segment_list))


@register_command
@dataclass
class PEF_MODE:
    """Control the filter mode."""

    code: typing.ClassVar[int] = 1780
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _flow_xindex: int
    _filter_type: FilterType

    class GetDataAttr(ResponseBodyStruct):
        mode: FilterMode = field(XmpByte())
        """integer, the mode of the filter."""

    class SetDataAttr(RequestBodyStruct):
        mode: FilterMode = field(XmpByte())
        """integer, the mode of the filter."""

    def get(self) -> Token[GetDataAttr]:
        """Get the filter mode.

        :return: the filter mode
        :rtype: PEF_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type]))

    def set(self, mode: FilterMode) -> Token[None]:
        """Set the filter mode.

        :param mode: the mode of the filter.
        :type sid: FlowMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._flow_xindex, self._filter_type], mode=mode))

    set_basic = functools.partialmethod(set, FilterMode.BASIC)
    """Set the filter mode to Basic."""

    set_extended = functools.partialmethod(set, FilterMode.EXTENDED)
    """Set the filter mode to Extended."""
