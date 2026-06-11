"""Port Commands - MACsec"""
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
    XmpLong,
    XmpShort,
    XmpMacAddress,
    XmpSequence,
    XmpStr,
    Hex,
    XmpJson,
)
from .enums import (
    OnOff,
    MACSecSCIMode,
    MACSecCipherSuite,
    # MACSecVLANMode,
    MACSecRekeyMode,
    MACSecEncryptionMode,
    MACSecPNMode,
)



@register_command
@dataclass
class P_MACSEC_TXSC_CREATE:
    """
    Create a TX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 505
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a TX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))
    

@register_command
@dataclass
class P_MACSEC_TXSC_INDICES:
    """
    Create multiple TX SCs or query the existing TX SCs on the port.
    """

    code: typing.ClassVar[int] = 506
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        txsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of TX SCs on the port."""

    class SetDataAttr(RequestBodyStruct):
        txsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of TX SCs on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the full list of which TX SCs are defined for a port.

        :return: the sub-indices of TX SCs on the port
        :rtype: P_MACSEC_TXSC_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, txsc_indices: typing.List[int]) -> Token[None]:
        """Creates a new empty TX SC for each value that is not already in use, and deletes each TX SC that is not mentioned in the list.

        :param txsc_indices: the sub-indices of TX SCs on the port
        :type txsc_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, txsc_indices=txsc_indices))


@register_command
@dataclass
class P_MACSEC_TXSC_DELETE:
    """
    Delete a TX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 530
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete a TX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))


@register_command
@dataclass
class P_MACSEC_TXSC_CONF_OFFSET:
    """
    The confidentiality offset of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 510
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, the TX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, the TX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    def get(self) -> Token[GetDataAttr]:
        """Get the TX Secure Channel (SC) offset on the port.

        :return: the TX Secure Channel (SC) offset on the port
        :rtype: P_MACSEC_TXSC_CONF_OFFSET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, offset: int) -> Token[None]:
        """Set the TX Secure Channel (SC) offset on the port.

        :param offset: the TX Secure Channel (SC) offset
        :type offset: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], offset=offset))
    

@register_command
@dataclass
class P_MACSEC_TXSC_DESCR:
    """
    The description of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 507
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the TX Secure Channel (SC)."""

    class SetDataAttr(RequestBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the TX Secure Channel (SC)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the TX Secure Channel (SC) on the port.

        :return: the description of the TX Secure Channel (SC) on the port
        :rtype: P_MACSEC_TXSC_DESCR.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, description: str) -> Token[None]:
        """Set the description of the TX Secure Channel (SC) on the port.

        :param description: the description of the TX Secure Channel (SC)
        :type description: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], description=description))
    

@register_command
@dataclass
class P_MACSEC_TXSC_SCI_MODE:
    """
    The mode of the port’s TX SCI in MACsec.

    """

    code: typing.ClassVar[int] = 513
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecSCIMode = field(XmpByte())
        """coded byte, the mode of the port’s TX SCI in MACsec."""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecSCIMode = field(XmpByte())
        """coded byte, the mode of the port’s TX SCI in MACsec."""

    def get(self) -> Token[GetDataAttr]:
        """Get the mode of the port’s TX SCI in MACsec.

        :return: the mode of the port’s TX SCI in MACsec.
        :rtype: P_MACSEC_TXSC_SCI_MODE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecSCIMode) -> Token[None]:
        """Set the mode of the port’s TX SCI in MACsec.

        :param mode: the mode of the port’s TX SCI in MACsec.
        :type mode: MACSecSCIMode
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))

    set_end_station = functools.partialmethod(set, MACSecSCIMode.END_STATION)
    """Set SCI Mode to END STATION.
    """

    set_with_sci = functools.partialmethod(set, MACSecSCIMode.WITH_SCI)
    """Set SCI Mode to WITH SCI.
    """

    # set_no_sci = functools.partialmethod(set, MACSecSCIMode.NO_SCI)
    # """Set SCI Mode to NO SCI.
    # """


@register_command
@dataclass
class P_MACSEC_TXSC_SCI:
    """
    The SCI of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 508
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s TX SC."""

    class SetDataAttr(RequestBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s TX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SCI of the port’s TX SC.

        :return: the SCI of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_SCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, sci: Hex) -> Token[None]:
        """Set the SCI of the port’s TX SC.

        :param sci: The SCI of the port’s TX SC.
        :type sci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], sci=sci))
    

@register_command
@dataclass
class P_MACSEC_TXSC_CIPHERSUITE:
    """
    The cipher suite of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 509
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s TX SC."""

    class SetDataAttr(RequestBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s TX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the cipher suite of the port’s TX SC.

        :return: the cipher suite of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_CIPHERSUITE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, cipher_suite: MACSecCipherSuite) -> Token[None]:
        """Set the cipher suite of the port’s TX SC.

        :param cipher_suite: the cipher suite of the port’s TX SC.
        :type cipher_suite: MACSecCipherSuite
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], cipher_suite=cipher_suite))

    set_gcm_aes_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_128)
    """Set cipher suite to GCM_AES_128.
    """

    set_gcm_aes_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_256)
    """Set cipher suite to GCM_AES_256.
    """

    set_gcm_aes_xpn_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_128)
    """Set cipher suite to GCM_AES_XPN_128.
    """

    set_gcm_aes_xpn_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_256)
    """Set cipher suite to GCM_AES_XPN_256.
    """


@register_command
@dataclass
class P_MACSEC_TXSC_STARTING_PN:
    """
    The starting PN number of the port’s TX SC uses.
    """

    code: typing.ClassVar[int] = 514
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        starting_pn: int = field(XmpLong())
        """integer, the starting PN number. Default to 1, maximum 2^64. Allowed to be 0."""

        mode: MACSecPNMode = field(XmpByte())
        """byte, defining how to continue the TX PN after the start-traffic. Default to CONTINUOUS."""

    class SetDataAttr(RequestBodyStruct):
        starting_pn: int = field(XmpLong())
        """integer, the starting PN number. Default to 1, maximum 2^64. Allowed to be 0."""

        mode: MACSecPNMode = field(XmpByte())
        """byte, defining how to continue the TX PN after the start-traffic. Default to CONTINUOUS."""

    def get(self) -> Token[GetDataAttr]:
        """Get the starting PN number. Default to 1, maximum 2^64. Allowed to be 0.

        :return: the starting PN number. Default to 1, maximum 2^64.
        :rtype: P_MACSEC_TXSC_STARTING_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, starting_pn: int, mode: MACSecPNMode) -> Token[None]:
        """Set the starting PN number. Default to 1, maximum 2^64. Allowed to be 0.

        :param starting_pn: the starting PN number. Default to 1, maximum 2^64.
        :type starting_pn: int
        :param mode: defining how to continue the TX PN after the start-traffic.
        :type mode: MACSecPNMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], starting_pn=starting_pn, mode=mode))
    

# @register_command
# @dataclass
# class P_MACSEC_TXSC_VLAN_MODE:
#     """
#     The VLAN mode of the port’s TX SC.
    
#         * VLAN encrypted: The original MACsec header format encoded the 802.1Q tag as part of the encrypted payload, thus hiding it from the public Ethernet transport.
        
#         * VLAN in clear text (WAN MACsec): With 802.1Q tag in the clear, the 802.1Q tag is encoded outside the 802.1AE encryption header, exposing the tag to the private and public Ethernet transport.

#     """

#     code: typing.ClassVar[int] = 511
#     pushed: typing.ClassVar[bool] = False

#     _connection: 'interfaces.IConnection'
#     _module: int
#     _port: int
#     _txsc_index: int

#     class GetDataAttr(ResponseBodyStruct):
#         mode: MACSecVLANMode = field(XmpByte())
#         """integer, the VLAN mode. Default to ENCRYPTED."""

#     class SetDataAttr(RequestBodyStruct):
#         mode: MACSecVLANMode = field(XmpByte())
#         """integer, the VLAN mode. Default to ENCRYPTEDC."""

#     def get(self) -> Token[GetDataAttr]:
#         """Get the VLAN mode.

#         :return: the VLAN mode.
#         :rtype: P_MACSEC_TXSC_VLAN_MODE.GetDataAttr
#         """
#         return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

#     def set(self, mode: MACSecVLANMode) -> Token[None]:
#         """Set the VLAN mode.

#         :param mode: the VLAN mode.
#         :type mode: MACSecVLANMode
#         """
#         return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))
    
#     set_encrypted = functools.partialmethod(set, MACSecVLANMode.ENCRYPTED)
#     """Set VLAN mode to ENCRYPTED.
#     """

#     set_clear_text = functools.partialmethod(set, MACSecVLANMode.CLEAR_TEXT)
#     """Set VLAN mode to CLEAR_TEXT.
#     """


@register_command
@dataclass
class P_MACSEC_TXSC_REKEY_MODE:
    """
    The rekey mode of the port’s TX SC defines when to switch to the next SAK.
    """

    code: typing.ClassVar[int] = 515
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecRekeyMode = field(XmpByte())
        """byte, the rekey mode of the port’s TX SC"""

        value: int = field(XmpInt())
        """integer, defines the packet number that triggers the rekey. This value will be ignored if the mode is set to PN_EXHAUSTION"""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecRekeyMode = field(XmpByte())
        """byte, the rekey mode of the port’s TX SC"""

        value: int = field(XmpInt())
        """integer, defines the packet number that triggers the rekey. This value will be ignored if the mode is set to PN_EXHAUSTION"""

    def get(self) -> Token[GetDataAttr]:
        """Get the rekey mode of the port’s TX SC

        :return: the rekey mode of the port’s TX SC
        :rtype: P_MACSEC_TXSC_REKEY_MODE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecRekeyMode, value: int) -> Token[None]:
        """Set the rekey mode.

        :param mode: the rekey mode.
        :type mode: MACSecRekeyMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode, value=value))


@register_command
@dataclass
class P_MACSEC_TXSC_ENCRYPT:
    """
    The encryption mode of the port’s TX SC.
    """

    code: typing.ClassVar[int] = 512
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        mode: MACSecEncryptionMode = field(XmpByte())
        """byte, the encryption mode of the port’s TX SC"""

    class SetDataAttr(RequestBodyStruct):
        mode: MACSecEncryptionMode = field(XmpByte())
        """byte, the encryption mode of the port’s TX SC"""

    def get(self) -> Token[GetDataAttr]:
        """Get the encryption mode of the port’s TX SC

        :return: the encryption mode of the port’s TX SC
        :rtype: P_MACSEC_TXSC_ENCRYPT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, mode: MACSecEncryptionMode) -> Token[None]:
        """Set the encryption mode.

        :param mode: the encryption mode.
        :type mode: MACSecEncryptionMode
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], mode=mode))
    
    set_encrypt_integrity = functools.partialmethod(set, MACSecEncryptionMode.ENCRYPT_INTEGRITY)
    """Set encryption mode to encryption and integrity.
    """

    set_integrity_only = functools.partialmethod(set, MACSecEncryptionMode.INTEGRITY_ONLY)
    """Set encryption mode to integrity only.
    """

@register_command
@dataclass
class P_MACSEC_TXSC_SAK_VALUE:
    """
    Configure the value of a SAK key on the port’s TX SC.
    """

    code: typing.ClassVar[int] = 534
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int
    _sak_key_index: int

    class GetDataAttr(ResponseBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    class SetDataAttr(RequestBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SAK key.

        :return: the the SAK key.
        :rtype: P_MACSEC_TXSC_SAK_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index, self._sak_key_index]))

    def set(self, sak_key_value: Hex) -> Token[None]:
        """Set the SAK key.

        :param sak_key_value: the SAK key.
        :type sak_key_value: Hex
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index, self._sak_key_index], sak_key_value=sak_key_value))
    

@register_command
@dataclass
class P_MACSEC_TXSC_XPN_SSCI:
    """
    The XPN Short SCI of the port's TX SC when XPN cipher suite is in use.
    """

    code: typing.ClassVar[int] = 540
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        xpn_ssci: Hex = field(XmpHex(size=4))
        """hex 4 bytes, The XPN Short SCI of the port's TX SC when XPN cipher suite is in use"""

    class SetDataAttr(RequestBodyStruct):
        xpn_ssci: Hex = field(XmpHex(size=4))
        """hex 4 bytes, The XPN Short SCI of the port's TX SC when XPN cipher suite is in use"""

    def get(self) -> Token[GetDataAttr]:
        """Get the XPN Short SCI of the port's TX SC when XPN cipher suite is in use

        :return: the SCI of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_XPN_SSCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, xpn_ssci: Hex) -> Token[None]:
        """Set the XPN Short SCI of the port's TX SC when XPN cipher suite is in use

        :param xpn_ssci: the XPN Short SCI of the port's TX SC when XPN cipher suite is in use
        :type xpn_ssci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], xpn_ssci=xpn_ssci))
    

@register_command
@dataclass
class P_MACSEC_TXSC_XPN_SALT:
    """
    The XPN salt of the port's TX SC when XPN cipher suite is in use.
    """

    code: typing.ClassVar[int] = 541
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        xpn_salt: Hex = field(XmpHex(size=12))
        """hex 12 bytes, XPN salt of the port's TX SC when XPN cipher suite is in use."""

    class SetDataAttr(RequestBodyStruct):
        xpn_salt: Hex = field(XmpHex(size=12))
        """hex 12 bytes, XPN salt of the port's TX SC when XPN cipher suite is in use."""

    def get(self) -> Token[GetDataAttr]:
        """Get XPN salt of the port's TX SC when XPN cipher suite is in use.

        :return: the SCI of the port’s TX SC.
        :rtype: P_MACSEC_TXSC_XPN_SALT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, xpn_salt: Hex) -> Token[None]:
        """Set XPN salt of the port's TX SC when XPN cipher suite is in use.

        :param xpn_salt: XPN salt of the port's TX SC when XPN cipher suite is in use.
        :type xpn_salt: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], xpn_salt=xpn_salt))
    

@register_command
@dataclass
class P_MACSEC_RXSC_CREATE:
    """
    Create a RX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 518
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Create a RX Secure Channel (SC) on the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RXSC_INDICES:
    """
    Create multiple RX SCs or query the existing RX SCs on the port.
    """

    code: typing.ClassVar[int] = 519
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        rxsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of RX SCs on the port."""

    class SetDataAttr(RequestBodyStruct):
        rxsc_indices: typing.List[int] = field(XmpSequence(types_chunk=[XmpInt()]))
        """list of integers, the sub-indices of RX SCs on the port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the full list of which RX SCs are defined for a port.

        :return: the sub-indices of RX SCs on the port
        :rtype: P_MACSEC_RXSC_INDICES.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, rxsc_indices: typing.List[int]) -> Token[None]:
        """Creates a new empty RX SC for each value that is not already in use, and deletes each RX SC that is not mentioned in the list.

        :param rxsc_indices: the sub-indices of RX SCs on the port
        :type rxsc_indices: typing.List[int]
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, rxsc_indices=rxsc_indices))
    

@register_command
@dataclass
class P_MACSEC_RXSC_DELETE:
    """
    Delete a RX Secure Channel (SC) on the port.
    """

    code: typing.ClassVar[int] = 531
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Delete a RX Secure Channel (SC) on the port.
        """
        
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RXSC_DESCR:
    """
    The description of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 520
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the RX Secure Channel (SC)."""

    class SetDataAttr(RequestBodyStruct):
        description: str = field(XmpStr())
        """string, the description of the RX Secure Channel (SC)."""

    def get(self) -> Token[GetDataAttr]:
        """Get the description of the RX Secure Channel (SC) on the port.

        :return: the description of the RX Secure Channel (SC) on the port
        :rtype: P_MACSEC_RXSC_DESCR.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, description: str) -> Token[None]:
        """Set the description of the RX Secure Channel (SC) on the port.

        :param description: the description of the RX Secure Channel (SC)
        :type description: str
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], description=description))
    

@register_command
@dataclass
class P_MACSEC_RXSC_SCI:
    """
    The SCI of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 523
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s RX SC."""

    class SetDataAttr(RequestBodyStruct):
        sci: Hex = field(XmpHex(size=8))
        """hex 8 bytes, the SCI of the port’s RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SCI of the port’s RX SC.

        :return: the SCI of the port’s RX SC.
        :rtype: P_MACSEC_RXSC_SCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, sci: Hex) -> Token[None]:
        """Set the SCI of the port’s RX SC.

        :param sci: The SCI of the port’s RX SC.
        :type sci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], sci=sci))
    

@register_command
@dataclass
class P_MACSEC_RXSC_CONF_OFFSET:
    """
    The confidentiality offset of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 522
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        offset: int = field(XmpInt())
        """integer, the RX Secure Channel (SC) offset. Allowed values are 0, 30, and 50."""

    class SetDataAttr(RequestBodyStruct):
        offset: int = field(XmpInt())
        """integer, the RX Secure Channel (SC) offset. Allowed values are 0, 30, and 50"""

    def get(self) -> Token[GetDataAttr]:
        """Get the RX Secure Channel (SC) offset on the port.

        :return: the RX Secure Channel (SC) offset on the port
        :rtype: P_MACSEC_RXSC_CONF_OFFSET.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, offset: int) -> Token[None]:
        """Set the RX Secure Channel (SC) offset on the port.

        :param offset: the RX Secure Channel (SC) offset
        :type offset: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], offset=offset))
    

@register_command
@dataclass
class P_MACSEC_RXSC_CIPHERSUITE:
    """
    The cipher suite of the port’s RX SC.
    """

    code: typing.ClassVar[int] = 521
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s RX SC."""

    class SetDataAttr(RequestBodyStruct):
        cipher_suite: MACSecCipherSuite = field(XmpByte())
        """coded byte, the cipher suite of the port’s RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the cipher suite of the port’s RX SC.

        :return: the cipher suite of the port’s RX SC.
        :rtype: P_MACSEC_RXSC_CIPHERSUITE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, cipher_suite: MACSecCipherSuite) -> Token[None]:
        """Set the cipher suite of the port’s RX SC.

        :param cipher_suite: the cipher suite of the port’s RX SC.
        :type cipher_suite: MACSecCipherSuite
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], cipher_suite=cipher_suite))

    set_gcm_aes_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_128)
    """Set cipher suite to GCM_AES_128.
    """

    set_gcm_aes_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_256)
    """Set cipher suite to GCM_AES_256.
    """

    set_gcm_aes_xpn_128 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_128)
    """Set cipher suite to GCM_AES_XPN_128.
    """

    set_gcm_aes_xpn_256 = functools.partialmethod(set, MACSecCipherSuite.GCM_AES_XPN_256)
    """Set cipher suite to GCM_AES_XPN_256.
    """

@register_command
@dataclass
class P_MACSEC_RXSC_LOWEST_PN:
    """
    The lowest PN number of the port’s RX SC expects to receive.
    """

    code: typing.ClassVar[int] = 511
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        lowest_pn: Hex = field(XmpHex(size=8))
        """hex, The lowest PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""

    class SetDataAttr(RequestBodyStruct):
        lowest_pn: Hex = field(XmpHex(size=8))
        """hex, The lowest PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""


    def get(self) -> Token[GetDataAttr]:
        """Get the lowest PN number of the port’s RX SC expects to receive

        :return: the lowest PN number of the port’s RX SC expects to receive
        :rtype: P_MACSEC_RXSC_LOWEST_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, lowest_pn: int) -> Token[None]:
        """Set the lowest PN number of the port’s RX SC expects to receive

        :param lowest_pn: The lowest PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64.
        :type lowest_pn: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], lowest_pn=lowest_pn))


@register_command
@dataclass
class P_MACSEC_RXSC_TPLDID:
    """
    Associate a TPLD ID with the RX SC.
    """

    code: typing.ClassVar[int] = 535
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        tpld_id: int = field(XmpInt())
        """integer, the TPLD ID to associate with the RX SC."""

    class SetDataAttr(RequestBodyStruct):
        tpld_id: int = field(XmpInt())
        """integer, the TPLD ID to associate with the RX SC."""

    def get(self) -> Token[GetDataAttr]:
        """Get the TPLD ID to associate with the RX SC.

        :return: the TPLD ID to associate with the RX SC.
        :rtype: P_MACSEC_RXSC_TPLDID.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, tpld_id: int) -> Token[None]:
        """Set the TPLD ID to associate with the RX SC.

        :param tpld_id: the TPLD ID to associate with the RX SC.
        :type tpld_id: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], tpld_id=tpld_id))
    

@register_command
@dataclass
class P_MACSEC_RXSC_SAK_VALUE:
    """
    Configure the value of a SAK key on the port’s RX SC.
    """

    code: typing.ClassVar[int] = 542
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int
    _sak_key_index: int

    class GetDataAttr(ResponseBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    class SetDataAttr(RequestBodyStruct):
        sak_key_value: Hex = field(XmpHex())
        """integer, the SAK key. Default to all-zero. Allowed to be empty."""

    def get(self) -> Token[GetDataAttr]:
        """Get the SAK key.

        :return: the the SAK key.
        :rtype: P_MACSEC_RXSC_SAK_VALUE.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index, self._sak_key_index]))

    def set(self, sak_key_value: Hex) -> Token[None]:
        """Set the SAK key.

        :param sak_key_value: the SAK key.
        :type sak_key_value: Hex
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index, self._sak_key_index], sak_key_value=sak_key_value))
    

@register_command
@dataclass
class P_MACSEC_RXSC_XPN_SSCI:
    """
    The XPN Short SCI of the port's RX SC when XPN cipher suite is in use.
    """

    code: typing.ClassVar[int] = 544
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        xpn_ssci: Hex = field(XmpHex(size=4))
        """hex 4 bytes, The XPN Short SCI of the port's RX SC when XPN cipher suite is in use"""

    class SetDataAttr(RequestBodyStruct):
        xpn_ssci: Hex = field(XmpHex(size=4))
        """hex 4 bytes, The XPN Short SCI of the port's RX SC when XPN cipher suite is in use"""

    def get(self) -> Token[GetDataAttr]:
        """Get the XPN Short SCI of the port's RX SC when XPN cipher suite is in use

        :return: the SCI of the port’s RX SC.
        :rtype: P_MACSEC_RXSC_XPN_SSCI.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, xpn_ssci: Hex) -> Token[None]:
        """Set the XPN Short SCI of the port's RX SC when XPN cipher suite is in use

        :param xpn_ssci: the XPN Short SCI of the port's RX SC when XPN cipher suite is in use
        :type xpn_ssci: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], xpn_ssci=xpn_ssci))
    

@register_command
@dataclass
class P_MACSEC_RXSC_XPN_SALT:
    """
    The XPN salt of the port's RX SC when XPN cipher suite is in use.
    """

    code: typing.ClassVar[int] = 546
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        xpn_salt: Hex = field(XmpHex(size=12))
        """hex 12 bytes, XPN salt of the port's RX SC when XPN cipher suite is in use."""

    class SetDataAttr(RequestBodyStruct):
        xpn_salt: Hex = field(XmpHex(size=12))
        """hex 12 bytes, XPN salt of the port's RX SC when XPN cipher suite is in use."""

    def get(self) -> Token[GetDataAttr]:
        """Get XPN salt of the port's RX SC when XPN cipher suite is in use.

        :return: the SCI of the port’s RX SC.
        :rtype: P_MACSEC_TXSC_XPN_SALT.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, xpn_salt: Hex) -> Token[None]:
        """Set XPN salt of the port's RX SC when XPN cipher suite is in use.

        :param xpn_salt: XPN salt of the port's RX SC when XPN cipher suite is in use.
        :type xpn_salt: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], xpn_salt=xpn_salt))


@register_command
@dataclass
class P_MACSEC_TX_STATS:
    """
    Port-level MACsec TX counters
    """

    code: typing.ClassVar[int] = 517
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted since last cleared."""
        total_protected_only_bits: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bits transmitted by the port since cleared."""
        total_protected_only_bytes: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bytes transmitted by the port since cleared."""
        total_encrypted_bits: int = field(XmpLong())
        """long integer, the number of encrypted bits transmitted by the port since cleared, excluding the bytes in the Confidentiality Offset."""
        total_encrypted_bytes: int = field(XmpLong())
        """long integer, the number of encrypted bytes transmitted by the port since cleared, excluding the bytes in the Confidentiality Offset."""


    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec TX counters

        :return: port-level MACsec TX counters
        :rtype: P_MACSEC_TX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class P_MACSEC_TXSC_STATS:
    """
    SC/stream-level MACsec TX counters.
    """

    code: typing.ClassVar[int] = 528
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, the number of MACsec L2 bits transmitted since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, the number of MACsec L2 bytes transmitted since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, the number of MACsec frames transmitted since last cleared."""
        total_protected_only_bits: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bits transmitted since cleared."""
        total_protected_only_bytes: int = field(XmpLong())
        """long integer, the number of protected-only (non-encrypted) bytes transmitted since cleared."""
        total_encrypted_bits: int = field(XmpLong())
        """long integer, the number of encrypted bits transmitted since cleared, excluding the bytes in the Confidentiality Offset."""
        total_encrypted_bytes: int = field(XmpLong())
        """long integer, the number of encrypted bytes transmitted since cleared, excluding the bytes in the Confidentiality Offset."""


    def get(self) -> Token[GetDataAttr]:
        """Get SC/stream-level MACsec TX counters.

        :return: SC/stream-level MACsec TX counters.
        :rtype: P_MACSEC_TXSC_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))
    

@register_command
@dataclass
class P_MACSEC_TX_CLEAR:
    """
    Clear the MACsec TX counters of the port.
    """

    code: typing.ClassVar[int] = 516
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear the MACsec TX counters of the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    


@register_command
@dataclass
class P_MACSEC_RX_STATS:
    """
    Port-level MACsec RX counters
    """

    code: typing.ClassVar[int] = 525
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, number of MACsec frames received of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, number of MACsec frames received since last cleared."""
        total_ok_frames: int = field(XmpLong())
        """long integer, the number of good MACsec frames received since cleared."""
        total_delayed_frames: int = field(XmpLong())
        """long integer, the number of frames with the PN lower than the minmum expected since cleared."""
        total_icv_check_failed_frames: int = field(XmpLong())
        """long integer, the number of frames with ICV check failed recevied since cleared."""

    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec RX counters

        :return: port-level MACsec RX counters
        :rtype: P_MACSEC_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))



@register_command
@dataclass
class P_MACSEC_RXSC_STATS:
    """
    SC/stream-level MACsec RX counters
    """

    code: typing.ClassVar[int] = 529
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        bits_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received of the previous second."""
        bytes_sec: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received of the previous second."""
        frames_sec: int = field(XmpLong())
        """long integer, number of MACsec frames received of the previous second."""
        total_bits: int = field(XmpLong())
        """long integer, number of MACsec L2 bits received since last cleared."""
        total_bytes: int = field(XmpLong())
        """long integer, number of MACsec L2 bytes received since last cleared."""
        total_frames: int = field(XmpLong())
        """long integer, number of MACsec frames received since last cleared."""
        total_ok_frames: int = field(XmpLong())
        """long integer, the number of good MACsec frames received since cleared."""
        total_delayed_frames: int = field(XmpLong())
        """long integer, the number of frames with the PN lower than the minmum expected since cleared."""
        total_icv_check_failed_frames: int = field(XmpLong())
        """long integer, the number of frames with ICV check failed recevied since cleared."""


    def get(self) -> Token[GetDataAttr]:
        """Get port-level MACsec RX counters

        :return: port-level MACsec RX counters
        :rtype: P_MACSEC_RX_STATS.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RX_CLEAR:
    """
    Clear the MACsec RX counters of the port.
    """

    code: typing.ClassVar[int] = 524
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class SetDataAttr(RequestBodyStruct):
        pass

    def set(self) -> Token[None]:
        """Clear the MACsec RX counters of the port.
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port))
    

@register_command
@dataclass
class P_MACSEC_RX_ENABLE:
    """
    This will enable/disable the MACSec functionality on the RX side. With it ON, the RX port will try to decode the received packets. If it is OFF, the port will not try to decode any received packets.
    """

    code: typing.ClassVar[int] = 545
    pushed: typing.ClassVar[bool] = True

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int

    class GetDataAttr(ResponseBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, enable or disable MACsec on the RX port."""

    class SetDataAttr(RequestBodyStruct):
        on_off: OnOff = field(XmpByte())
        """coded byte, enable or disable MACsec on the RX port."""

    def get(self) -> Token[GetDataAttr]:
        """Get the RX port MACSec state.

        :return: the RX port MACSec stat
        :rtype: PS_MACSEC_ENABLE.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port))

    def set(self, on_off: OnOff) -> Token[None]:
        """Set the RX port MACSec stat.

        :param on_off: the RX port MACSec stat
        :type on_off: OnOff
        """

        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, on_off=on_off))

    set_off = functools.partialmethod(set, OnOff.OFF)
    """Disable the RX port MACSec.
    """

    set_on = functools.partialmethod(set, OnOff.ON)
    """Enable the RX port MACSec.
    """


@register_command
@dataclass
class P_MACSEC_RXSC_AN:
    """
    RX SC's next AN
    """

    code: typing.ClassVar[int] = 550
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        next_an: int = field(XmpInt())
        """integer, the next AN"""

    def get(self) -> Token[GetDataAttr]:
        """Get RX SC's next AN

        :return: RX SC's next AN
        :rtype: P_MACSEC_RXSC_AN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))
    

@register_command
@dataclass
class P_MACSEC_RXSC_NEXT_PN:
    """
    The next PN number of the port’s RX SC expects to receive.
    """

    code: typing.ClassVar[int] = 548
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        next_pn: Hex = field(XmpHex(size=8))
        """hex, The next PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""

    class SetDataAttr(RequestBodyStruct):
        next_pn: Hex = field(XmpHex(size=8))
        """hex, The next PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""


    def get(self) -> Token[GetDataAttr]:
        """Get the next PN number of the port’s RX SC expects to receive

        :return: the next PN number of the port’s RX SC expects to receive
        :rtype: P_MACSEC_RXSC_NEXT_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))

    def set(self, value: int) -> Token[None]:
        """Set the next PN number of the port’s RX SC expects to receive

        :param value: The next PN number of the port’s RX SC expects to receive. Default to 1, maximum 2^64.
        :type value: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._rxsc_index], value=value))
    

@register_command
@dataclass
class P_MACSEC_TXSC_NEXT_PN:
    """
    The next PN number of the port’s TX SC expects to receive.
    """

    code: typing.ClassVar[int] = 547
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        next_pn: Hex = field(XmpHex(size=8))
        """hex, The next PN number of the port’s TX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""
    class SetDataAttr(RequestBodyStruct):
        next_pn: Hex = field(XmpHex(size=8))
        """hex, The next PN number of the port’s TX SC expects to receive. Default to 1, maximum 2^64. Allowed to be 0."""

    def get(self) -> Token[GetDataAttr]:
        """Get the next PN number of the port’s TX SC expects to receive

        NextPN is a monotonically incrementing 32 or 64 bit counter that is never zero. 

        :return: the next PN number of the port’s TX SC expects to receive
        :rtype: P_MACSEC_TXSC_NEXT_PN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, next_pn: int) -> Token[None]:
        """Set the next PN number of the port’s TX SC expects to receive

        NextPN is a monotonically incrementing 32 or 64 bit counter that is never zero. 

        :param next_pn: The next PN number of the port’s TX SC expects to receive. Default to 1, maximum 2^64.
        :type next_pn: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], next_pn=next_pn))
    


@register_command
@dataclass
class P_MACSEC_RXSC_PN:
    """
    RX SC's next PN
    """

    code: typing.ClassVar[int] = 551
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _rxsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        pn: Hex = field(XmpHex(size=8))
        """hex, 8-byte long, the latest recovered PN for the Rx SC"""

    def get(self) -> Token[GetDataAttr]:
        """Get RX SC's next PN
        
        :return: RX SC's next PN
        :rtype: P_MACSEC_RXSC_PN.GetDataAttr
        """

        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._rxsc_index]))


@register_command
@dataclass
class P_MACSEC_TXSC_NEXT_AN:
    """
    The next AN number of the port’s TX SC expects to receive.
    """

    code: typing.ClassVar[int] = 549
    pushed: typing.ClassVar[bool] = False

    _connection: 'interfaces.IConnection'
    _module: int
    _port: int
    _txsc_index: int

    class GetDataAttr(ResponseBodyStruct):
        next_an: int = field(XmpInt())
        """integer, The next AN number of the port’s TX SC expects to receive.  Allowed to be 0."""

    class SetDataAttr(RequestBodyStruct):
        next_an: int = field(XmpInt())
        """integer, The next AN number of the port’s TX SC expects to receive.  Allowed to be 0."""
    
    def get(self) -> Token[GetDataAttr]:
        """Get the next AN number of the port’s TX SC expects to receive

        :return: the next AN number of the port’s TX SC expects to receive
        :rtype: P_MACSEC_TXSC_NEXT_AN.GetDataAttr
        """
        return Token(self._connection, build_get_request(self, module=self._module, port=self._port, indices=[self._txsc_index]))

    def set(self, next_an: int) -> Token[None]:
        """Set the next AN number of the port’s TX SC expects to receive

        :param next_an: The next AN number of the port’s TX SC expects to receive. 
        :type next_an: int
        """
        return Token(self._connection, build_set_request(self, module=self._module, port=self._port, indices=[self._txsc_index], next_an=next_an))




__all__ = [
    "P_MACSEC_TXSC_CREATE",
    "P_MACSEC_TXSC_INDICES",
    "P_MACSEC_TXSC_DELETE",
    "P_MACSEC_TXSC_CONF_OFFSET",
    "P_MACSEC_TXSC_DESCR",
    "P_MACSEC_TXSC_SCI_MODE",
    "P_MACSEC_TXSC_SCI",
    "P_MACSEC_TXSC_CIPHERSUITE",
    "P_MACSEC_TXSC_STARTING_PN",
    "P_MACSEC_TXSC_REKEY_MODE",
    "P_MACSEC_TXSC_ENCRYPT",
    "P_MACSEC_TXSC_SAK_VALUE",
    "P_MACSEC_TXSC_XPN_SSCI",
    "P_MACSEC_TXSC_XPN_SALT",
    "P_MACSEC_RXSC_CREATE",
    "P_MACSEC_RXSC_INDICES",
    "P_MACSEC_RXSC_DELETE",
    "P_MACSEC_RXSC_DESCR",
    "P_MACSEC_RXSC_SCI",
    "P_MACSEC_RXSC_CONF_OFFSET",
    "P_MACSEC_RXSC_CIPHERSUITE",
    "P_MACSEC_RXSC_LOWEST_PN",
    "P_MACSEC_RXSC_TPLDID",
    "P_MACSEC_RXSC_SAK_VALUE",
    "P_MACSEC_RXSC_XPN_SSCI",
    "P_MACSEC_RXSC_XPN_SALT",
    "P_MACSEC_TX_STATS",
    "P_MACSEC_TXSC_STATS",
    "P_MACSEC_TX_CLEAR",
    "P_MACSEC_RX_STATS",
    "P_MACSEC_RXSC_STATS",
    "P_MACSEC_RX_CLEAR",
    "P_MACSEC_RX_ENABLE",
    "P_MACSEC_RXSC_AN",
    "P_MACSEC_RXSC_NEXT_PN",
    "P_MACSEC_TXSC_NEXT_PN",
    "P_MACSEC_RXSC_PN",
    "P_MACSEC_TXSC_NEXT_AN",
]