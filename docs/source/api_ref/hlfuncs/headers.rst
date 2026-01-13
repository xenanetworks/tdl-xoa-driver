``headers`` module
=================================================

The ``headers`` module provides a simple way to edit the value of a header in a packet. The purpose of this module is to provide a simple interface for modifying the value of a header in a packet. The module provides a function that takes a packet and a header name as input and returns the modified packet with the new value for the specified header.

The module is designed to be used in conjunction with the HLAPI ``stream.packet.header.data.set()`` function. Without this module the user would have to manually set the hex value of the header in the packet. This module simplifies that process by providing a simple interface for modifying the value of a header in a packet.

.. code-block:: python

    eth = headers.Ethernet()
    eth.src_mac = aaaa.aaaa.0005
    eth.dst_mac = bbbb.bbbb.0005
    eth.ethertype = headers.EtherType.NONE
    print(str(eth))
    # Output will be: BBBBBBBB0005AAAAAAAA0005FFFF
    stream.packet.header.data.set(hex_data=Hex(str(eth)))


.. currentmodule:: xoa_driver.hlfuncs.headers

.. autosummary::

    IPV4
    IPV6
    UDP
    TCP
    PTP
    eCPRIGeneralDataTransfer
    DHCPV4
    DHCPOptionMessageType
    DHCPOptionClientIdentifier
    DHCPOptionRequestedIP
    DHCPOptionParamRequestList
    DHCPOptionPad
    DHCPOptionEnd
    MACControlPFC
    MACControlPause
    BTH
    RETH
    AETH
    RDETH
    DETH
    IB
    MPLS

Module Contents
-----------------

.. automodule:: xoa_driver.hlfuncs.headers
    :members:
    :show-inheritance:
    :no-undoc-members:
    :member-order: bysource
