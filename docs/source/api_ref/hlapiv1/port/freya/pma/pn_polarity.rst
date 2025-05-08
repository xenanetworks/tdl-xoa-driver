P/N Polarity
=========================

In a SERDES link, you transmit data at high speeds over differential pairs. Each pair has two signals:

* P (positive)
* N (negative)

Normally, the transmitter sends the differential signal correctly: when the P is high, N is low, and vice versa.
However, in real hardware, especially during PCB design or cable assembly, sometimes the P and N wires get accidentally swapped.

You can enable the P/N polarity swap of a SERDES in PMA tab in XenaManager, as shown in the screenshot below. By default, the RX and TX P/N polarity swap is off.

P/N Polarity Swap TX
--------------------

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PNSWAP_TX`

.. code-block:: python

    await port.l1.serdes[0].pma.pn_swap_tx.set(on_off=enums.OnOff.ON)
    await port.l1.serdes[0].pma.pn_swap_tx.set_on()
    await port.l1.serdes[0].pma.pn_swap_tx.set(on_off=enums.OnOff.OFF)
    await port.l1.serdes[0].pma.pn_swap_tx.set_off()

    resp = await port.l1.serdes[0].pma.pn_swap_tx.get()
    resp.on_off


P/N Polarity Swap RX
--------------------

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.pl1_commands.PL1_PNSWAP_RX`

.. code-block:: python

    await port.l1.serdes[0].pma.pn_swap_rx.set(on_off=enums.OnOff.ON)
    await port.l1.serdes[0].pma.pn_swap_rx.set_on()
    await port.l1.serdes[0].pma.pn_swap_rx.set(on_off=enums.OnOff.OFF)
    await port.l1.serdes[0].pma.pn_swap_rx.set_off()

    resp = await port.l1.serdes[0].pma.pn_swap_rx.get()
    resp.on_off