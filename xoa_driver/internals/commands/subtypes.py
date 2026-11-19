"""Subtypes"""
import ipaddress
from dataclasses import dataclass

from xoa_driver.internals.core.transporter.protocol.payload import (
    field,
    XmpByte,
    XmpShort,
    XmpInt,
    XmpLong,
    XmpMacAddress,
    XmpIPv4Address,
    Hex,
)
from .enums import (
    IsEnabled,
    L1CGMIICaptureTriggerType,
    OnOff,
    VlanType
)


@dataclass
class ArpEntry:
    ipv4_address: ipaddress.IPv4Address
    """The IP address to match to the Target IP address in the ARP requests"""

    prefix: int
    """The IP prefix used for address matching."""

    patched_mac: OnOff
    """If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix"""

    mac_address: Hex
    """The target MAC address to return in the ARP reply. If set t to all-zero, the port MAC address will be used."""


@dataclass
class NdpEntry:
    ipv6_address: ipaddress.IPv6Address
    """The IP address to match to the Target IP address in the NDP Neighbor Solicitation"""

    prefix: int
    """The IP prefix used for address matching."""

    patched_mac: OnOff
    """If on, the target MAC address will be patched with the part of the IP address that is not masked by the prefix"""

    mac_address: Hex
    """The target MAC address to return in the NDP Neighbor Advertisement. If set t to all-zero, the port MAC address will be used."""

@dataclass
class DhcpEntry:
    ipv4_address:       ipaddress.IPv4Address = field(XmpIPv4Address())  # provided IP address by DHCP Server
    subnet_mask:        ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Subnet mask by DHCP Server
    braodcast_address:  ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Broadcast address by DHCP Server
    defaultgw:          ipaddress.IPv4Address = field(XmpIPv4Address())  # provided Default GW by DHCP Server
    lease_time:         int                   = field(XmpInt())          # provided Lease Time by DHCP Server
    mac_address:        Hex                   = field(XmpMacAddress())   # The client source mac address that this DHCP request blongs to

@dataclass
class GroupAddressElem:
    def __init__(self, ip_address, subnet_mask, mac_address):
        self.ipv4_address = ip_address
        self.subnet_mask = subnet_mask
        self.mac_address = mac_address
        
    
    
    ipv4_address:   ipaddress.IPv4Address = field(XmpIPv4Address()) # Ip address
    subnet_mask:    ipaddress.IPv4Address = field(XmpIPv4Address()) # Subne Mask
    mac_address:    Hex                   = field(XmpMacAddress())  # Mac Address

    
@dataclass
class VlanTag:
    def __init__(self, tci, type):
        self.tci = tci
        self.type = type
    
    tci: int        =   field(XmpShort())  # 
    type: VlanType  =   field(XmpByte())  # Subne Mask
    
@dataclass
class QueueStatsElem:
    rx_bytes:   int = field(XmpLong())  # Total Received Bytes
    rx_packets: int = field(XmpLong())  # Total Received Packets
    tx_bytes:   int = field(XmpLong())  # Total Sent Bytes
    tx_packets: int = field(XmpLong())  # Total Sent Packets

@dataclass
class L1CGMIICodeword:
    data: int = field(XmpLong(signed=False))  # CGMII codeword data
    ctrl: int = field(XmpByte(signed=False))  # CGMII codeword control. 1 bit for each byte in the data field.


@dataclass
class L1CGMIICaptureSubscriptionType:
    enabled: IsEnabled = field(XmpByte())
    """Indicates whether the Layer-1 CGMII capture subscription is enabled."""

    trigger_type: L1CGMIICaptureTriggerType = field(XmpByte())
    """The type of the Layer-1 CGMII capture trigger."""

_CGMII_CONTROL_SYMBOLS = {0x07: 'I', 0x06: 'LI', 0xFB: 'S', 0xFD: 'T', 0xFE: 'E', 0x9C: 'Q', 0x5C: 'C'}

def cgmii_codeword_str(codeword: L1CGMIICodeword, sep: str = "", traditional=False) -> str:
    """Show the 8 lanes of a CGMII codeword by symbol name, lane 0 (the most significant byte of ``data``) first.

    Control characters are /I/ idle, /LI/ low power idle, /S/ start, /T/ terminate, /E/ error,
    /Q/ sequence ordered set and /C/ UEC CtlOS. Any other control character shows its value, e.g. /0x1C/.
    Data is /D/, except 0x55 and 0xD5 after an /S/ in the same codeword, which are /P/ (preamble) and /F/ (SFD).

    :param codeword: the CGMII codeword
    :type codeword: L1CGMIICodeword
    :param sep: the text between the symbols
    :type sep: str
    :return: the symbols, e.g. ``SPPPPPPF``
    :rtype: str
    """
    symbols = []
    after_start = False
    for lane in range(8):
        byte = (codeword.data >> (56 - 8 * lane)) & 0xFF
        if (codeword.ctrl >> (7 - lane)) & 1:
            symbol = _CGMII_CONTROL_SYMBOLS.get(byte, f'0x{byte:02X}')
            after_start = byte == 0xFB
        elif after_start and byte == 0x55:
            symbol = 'P'
        elif after_start and byte == 0xD5:
            symbol = 'F'
        else:
            symbol = 'D'
        symbols.append(f'/{symbol}/' if traditional else symbol)
    return sep.join(symbols)
