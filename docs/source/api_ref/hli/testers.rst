``testers`` module
=========================

.. literalinclude:: testers.py
    :language: python


.. currentmodule:: xoa_driver.testers.l23_tester

``xoa_driver.testers`` includes tester APIs for all testers.

.. code-block:: python

    import asyncio
    from xoa_driver import testers, enums

.. autoclass:: xoa_driver.testers.l23_tester.L23Tester
    :members:
    :undoc-members:
    :show-inheritance:


Connect to Chassis
-------------------------

.. code-block:: python

    tester = await testers.L23Tester(
        host="10.10.10.10",
        username="my_name",
        password="xena",
        enable_logging=False)

Disconnect from Chassis
-----------------------------

.. code-block:: python

    await tester.session.logoff()


Shutdown/Restart
-------------------------

Shuts down the chassis, and either restarts it in a clean state or leaves it powered off.

.. code-block:: python

    await tester.down.set()

Flash LED
-------------------------

Make all the test port LEDs flash on and off with a 1-second interval. This is helpful if you have multiple chassis mounted side by side and you need to identify a specific one.

.. code-block:: python

    await tester.flash.set()
    await tester.flash.get()


