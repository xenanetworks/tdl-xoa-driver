import asyncio
from xoa_driver import testers, modules, ports, enums, utils, misc
from xoa_driver.hlfuncs import * 
from xoa_driver.misc import Hex, ArpEntry, NdpEntry
import ipaddress

async def my_awesome_func(stop_event: asyncio.Event):

    # [testers]
    """Connect Chassis"""
    # Create a tester object representing a chassis 
    # and connect to the chassis at IP address 10.10.10.
    tester = await testers.L23Tester(
        host="10.10.10.10",
        username="my_name",
        password="xena",
        enable_logging=False)
    
    
    # [modules]
    """Get Module Object"""
    # Obtain a module object representing the module installed in slot 0.
    module = tester.modules.obtain(0)

    # [Check module type]
    if isinstance(module, modules.E100ChimeraModule):
        return

    # [ports]
    """Get Port Object"""
    port = module.ports.obtain(0)

    """Create a stream"""
    stream = await port.streams.create()

    # [Loki-4P Specific]
    if isinstance(port, ports.PLoki100G5S4P_a):

        """MACSEC CONFIGURATION"""
        """MACsec - Tx SCs"""
        # Create a TX Secure Channel
        txsc_obj = await port.macsec.txscs.create()

        # Tx SC Description
        await txsc_obj.config.description.set(description="This is a TX SC comment")

        # Tx SC SCI
        await txsc_obj.config.sci.set(sci=Hex("AABBCCDDEEFF0011"))

        # Tx SC Mode
        await txsc_obj.config.sci_mode.set(mode=enums.MACSecSCIMode.WITH_SCI)
        await txsc_obj.config.sci_mode.set(mode=enums.MACSecSCIMode.END_STATION)

        # Tx SC Confidentiality Offset
        await txsc_obj.config.confidentiality_offset.set(offset=0)

        # Tx SC Cipher Suite
        await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_128)

        # Tx SC Starting PN
        await txsc_obj.config.starting_pn.set(starting_pn=1, mode=enums.MACSecPNMode.RESET)

        # Tx SC ReKey Mode
        await txsc_obj.config.rekey_mode.set(mode=enums.MACSecRekeyMode.PN_EXHAUSTION, value=0)

        # Tx SC Encryption Mode
        await txsc_obj.config.encryption_mode.set(mode=enums.MACSecEncryptionMode.ENCRYPT_INTEGRITY)

        # Tx SC XPN SSCI
        await txsc_obj.config.xpn_ssci.set(xpn_ssci=Hex("000000000001"))

        # Tx SC XPN Salt
        await txsc_obj.config.xpn_salt.set(xpn_salt=Hex("AABBCCDDEEFFAABBCCDDEEFF"))

        # Tx SC Next PN
        await txsc_obj.config.next_pn.set(next_pn=1)
        resp = await txsc_obj.config.next_pn.get()

        # Tx SC Next AN
        await txsc_obj.config.next_an.set(next_an=1)
        resp = await txsc_obj.config.next_an.get()


        """MACsec - Rx SCs"""
        # Create a RX Secure Channel
        rxsc_obj = await port.macsec.rxscs.create()

        # Rx SC Description
        await rxsc_obj.config.description.set(description="This is a RX SC comment")

        # Rx SC SCI
        await rxsc_obj.config.sci.set(sci=Hex("AABBCCDDEEFF0011"))

        # Rx SC Confidentiality Offset
        await rxsc_obj.config.confidentiality_offset.set(offset=0)

        # Rx SC Cipher Suite
        await rxsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_128)

        # Rx SC Lowest PN
        await rxsc_obj.config.lowest_pn.set(lowest_pn=1)

        # Rx SC TPLD ID
        await rxsc_obj.config.tpld_id.set(tpld_id=0)

        # Rx SC XPN SSCI
        await rxsc_obj.config.xpn_ssci.set(xpn_ssci=Hex("000000000001"))

        # Rx SC XPN Salt
        await rxsc_obj.config.xpn_salt.set(xpn_salt=Hex("AABBCCDDEEFFAABBCCDDEEFF"))

        # Rx SC AN
        resp = await rxsc_obj.config.an.get()

        # RX SC Next PN
        resp = await rxsc_obj.config.next_pn.get()

        # RX SC PN
        resp = await rxsc_obj.config.pn.get()

        # Enable MACsec decode on the port
        await port.macsec.decode.set_on()
        await port.macsec.decode.set_off()

        # Assing Tx SC to the stream by Tx SC index
        await stream.macsec.assign.set(tx_sc_index=txsc_obj.kind.index_id)

        # Enable MACsec encode on the stream
        await stream.macsec.enable.set_on()

        # Collect MACsec port statistics
        await port.macsec.statistics.tx.total.get()
        await port.macsec.statistics.rx.total.get()

        # Clear MACsec port statistics
        await port.macsec.statistics.tx.clear.set()
        await port.macsec.statistics.rx.clear.set()

        # Collect MACsec TXSC/RXSC statistics for the port
        resp = await txsc_obj.stats.get()
        resp = await rxsc_obj.stats.get()

    # [end]