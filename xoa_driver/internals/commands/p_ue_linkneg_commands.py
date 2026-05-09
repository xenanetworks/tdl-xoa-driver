"""Port Ultra Ethernet Link Negotiation Commands"""
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
    XmpLong,
    XmpSequence,
    XmpStr,
    Hex,
    XmpJson
)

from .enums import (
    UecCtlosClearDirection,
)

@register_command
@dataclass
class P_UE_LINKNEG_OPTIONS:
    """
    This command selects which LLDP agent to use for UE Link Negotiation Options, and configures the desired LLR-W (local) setting. After the set operation, the UE Link Negotiation Options TLV will be added to the LLDPDU (if it is not already present in the LLDPDU) or replace the existing one (if Options TLV was previously added in LLDP configurataion).

    The UE Link Negotiation Options TLV is used to discover and configure advanced UE link capabilities. Currently, the Options TLV is used to advertise the following UEC Link features:

      * Link Layer Retry (LLR): Provides link level re-transmissions for packets with errors.

    .. note::

        In Link Negotiation for LLR, the R/W access of the four flags are:

        * LLR-W (local): RW
        * LLR-W (remote): RO
        * LLR-E (local): RO
        * LLR-E (remote): RO

        When Link Negotiation is enabled on a LLDP agent, the only configurable parameter is ``LLR-W (local)``. To read ``LLR-W (remote)``, use ``P_UE_LINKNEG_OPTIONS_STATUS``. To read ``LLR-E (local)`` and ``LLR-E (remote)``, use ``P_UE_LLR_MODE``

    To disable Link Negotation for UE Link Options, send the command with no parameters. This will remove the Options TLV from the LLDPDU and disable Link Negotiation for UE Link Options.
    """

    code: typing.ClassVar[int] = 1016
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        lldp_agent_index: int = field(XmpByte())
        """integer, The LLDP agent index to use for advertising the advanced UE link capabilities. An LLDP agent must be created and configured separately using the LLDP commands before it can be used with this command. Values: 0 to 7."""

        llr_wanted_local: int = field(XmpByte())
        """integer, Indicates whether the local port wants LLR.

        - ``NO = 0``: The port does not want to use LLR.
        - ``RSVD1 = 1``: Reserved value.
        - ``RSVD2 = 2``: Reserved value.
        - ``BI = 3``: port wants bi-directional LLR (it both sends and receives).

        """

    class SetDataAttr(RequestBodyStruct):
        lldp_agent_index: int = field(XmpByte())
        """integer, The LLDP agent index to use for advertising the advanced UE link capabilities. An LLDP agent must be created and configured separately using the LLDP commands before it can be used with this command. Values: 0 to 7."""

        llr_wanted_local: int = field(XmpByte())
        """integer, Indicates whether the local port wants LLR.

        - ``NO = 0``: The port does not want to use LLR.
        - ``RSVD1 = 1``: Reserved value.
        - ``RSVD2 = 2``: Reserved value.
        - ``BI = 3``: port wants bi-directional LLR (it both sends and receives).

        """

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the port.

        :return: the description of the port
        :rtype: P_UE_LINKNEG_OPTIONS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, lldp_agent_index: int, llr_wanted_local: int) -> Token[None]:
        """Set the UE Link Negotiation Options.

        :param lldp_agent_index: The LLDP agent index to use for advertising the advanced UE link capabilities. Values: 0 to 7.
        :type lldp_agent_index: int
        :param llr_wanted_local: Indicates whether the local port wants LLR. Values: 0 (NO), 1 (RSVD1), 2 (RSVD2), 3 (BI)
        :type llr_wanted_local: int
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, lldp_agent_index=lldp_agent_index, llr_wanted_local=llr_wanted_local))


@register_command
@dataclass
class P_UE_LINKNEG_OPTIONS_STATUS:
    """
    Read ``LLR-W (local)`` and ``LLR-W (remote)`` of the port, which indicates whether the local and remote ports want to use LLR. This command is for read-only purposes and does not change any configuration or behavior of the LLR.
    """

    code: typing.ClassVar[int] = 1029
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        llr_wanted_local: int = field(XmpByte())
        """integer, Indicates whether the local port wants LLR.

        - ``NO = 0``: The port does not want to use LLR.
        - ``RSVD1 = 1``: Reserved value.
        - ``RSVD2 = 2``: Reserved value.
        - ``BI = 3``: port wants bi-directional LLR (it both sends and receives).

        """

        llr_wanted_remote: int = field(XmpByte())
        """integer, Indicates whether the remote port wants LLR.

        - ``NO = 0``: The port does not want to use LLR.
        - ``RSVD1 = 1``: Reserved value.
        - ``RSVD2 = 2``: Reserved value.
        - ``BI = 3``: port wants bi-directional LLR (it both sends and receives).

        """

    def get(self) -> Token[GetDataAttr]:
        """Get the current UE link negotiation options status.

        :return: the current UE link negotiation options status
        :rtype: P_UE_LINKNEG_OPTIONS_STATUS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))


__all__ = [
    "P_UE_LINKNEG_OPTIONS",
    "P_UE_LINKNEG_OPTIONS_STATUS",
]