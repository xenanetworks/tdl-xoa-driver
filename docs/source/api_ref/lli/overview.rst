Overview
=========================

``lli`` package contains low-level API classes, giving you the direct control of the tester.

The names of the low-level command classes are the same as the the CLI commands in :term:`XOA CLI`. This makes it easy for you to understand and use ``lli`` if you are already familiar with XOA CLI.


Import Modules
-------------------------

To create a test script using low-level API, you first need to import the necessary modules. Then you need to make an async function to hold your test script code.

Here is an example of how to do it:

.. code-block:: python

    import asyncio
    from xoa_driver import utils
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums

    async def low_level():
        # Your test script code goes here
        pass


Establish Connection
-------------------------

After importing the necessary modules, you need to establish a connection to the tester. Create a ``TransportationHandler`` object first, which represents the connection to the tester. Then use the ``establish_connection`` function to connect to the tester. You need to provide the tester's IP address and port number (default is 22606) as parameters.

Once the connection is established, you need to gain access to the tester using the ``C_LOGON`` and ``C_OWNER`` commands. You need to provide the username and password for authentication.

.. code-block:: python

    import asyncio
    from xoa_driver import utils
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums

    async def low_level():
        # Establish connection to the tester
        handler = TransportationHandler(enable_logging=False)
        await establish_connection(handler, host="10.10.10.10", port=22606)
        await utils.apply(
            cmd.C_LOGON(handler).set("xena"),
            cmd.C_OWNER(handler).set(username),
        )

Send Commands
-------------------------

Now you can send low-level commands to the tester using the command classes in the ``commands`` module. Each command class corresponds to a specific command in XOA CLI. You can create an instance of the command class by providing the ``TransportationHandler`` object and any necessary indices as parameters. Then you can use the ``get`` and ``set`` methods to query or modify the command's parameters.

.. code-block:: python

    import asyncio
    from xoa_driver import utils
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums

    async def low_level():
        # Establish connection to the tester
        handler = TransportationHandler(enable_logging=False)
        await establish_connection(handler, host="10.10.10.10", port=22606)
        await utils.apply(
            cmd.C_LOGON(handler).set("xena"),
            cmd.C_OWNER(handler).set(username),
        )

        # Send low-level commands
        module_id = 0
        port_id = 0
        stream_id = 0

        # Reserve port 
        resp = await cmd.P_RESERVATION(handler, module_id , port_id).get()
        if resp.status == enums.ReservedStatus.RESERVED_BY_OTHER:
            await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELINQUISH)
        if resp.status == enums.ReservedStatus.RESERVED_BY_YOU:
            await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELEASE)
        await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RESERVE)

        # Set comment for port
        await cmd.P_COMMENT(handler, module_id, port_id).set(comment="My Port")

        # Create a stream on port
        await cmd.PS_CREATE(handler, module_id, port_id, stream_id).set()
        await cmd.PS_PACKETLENGTH(handler, module_id, port_id, stream_id).set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000)

        # Start traffic on port
        await cmd.P_TRAFFIC(handler, module_id, port_id,).set(on_off=enums.StartOrStop.START)
        
        # Stop traffic on port
        await cmd.P_TRAFFIC(handler, module_id, port_id,).set(on_off=enums.StartOrStop.STOP)

        # Get stream statistics
        await cmd.PT_STREAM(handler, module_id, port_id, stream_id).get()

        # Release port
        await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELEASE)

Close Connection
-------------------------
After you have finished sending commands to the tester, you need to log off and close the connection using the ``C_LOGOFF`` command.

.. code-block:: python

    import asyncio
    from xoa_driver import utils
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums

    async def low_level():
        # Establish connection to the tester
        handler = TransportationHandler(enable_logging=False)
        await establish_connection(handler, host="10.10.10.10", port=22606)
        await utils.apply(
            cmd.C_LOGON(handler).set("xena"),
            cmd.C_OWNER(handler).set(username),
        )

        # Send low-level commands
        module_id = 0
        port_id = 0
        stream_id = 0

        # Reserve port 
        resp = await cmd.P_RESERVATION(handler, module_id , port_id).get()
        if resp.status == enums.ReservedStatus.RESERVED_BY_OTHER:
            await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELINQUISH)
        if resp.status == enums.ReservedStatus.RESERVED_BY_YOU:
            await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELEASE)
        await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RESERVE)

        # Set comment for port
        await cmd.P_COMMENT(handler, module_id, port_id).set(comment="My Port")

        # Create a stream on port
        await cmd.PS_CREATE(handler, module_id, port_id, stream_id).set()
        await cmd.PS_PACKETLENGTH(handler, module_id, port_id, stream_id).set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000)

        # Start traffic on port
        await cmd.P_TRAFFIC(handler, module_id, port_id,).set(on_off=enums.StartOrStop.START)
        
        # Stop traffic on port
        await cmd.P_TRAFFIC(handler, module_id, port_id,).set(on_off=enums.StartOrStop.STOP)

        # Get stream statistics
        await cmd.PT_STREAM(handler, module_id, port_id, stream_id).get()

        # Release port
        await cmd.P_RESERVATION(handler, module_id, port_id).set(enums.ReservedAction.RELEASE)

        # Log off and close connection
        await cmd.C_LOGOFF(handler).set()
        handler.close()


.. important:: 
    
    The trade-off using ``lli`` directly is that you need to handle the connection keep-alive in your code (no *auto connection keep-alive* feature) and you need to handle the creation and deletion of stream indices, filter indices, modifier indices, etc. (no *auto index management* feature). This means there will be more lines of code in your test scripts.


