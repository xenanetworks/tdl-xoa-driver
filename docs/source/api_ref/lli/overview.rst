Overview
=========================

``lli`` package contains XOA low-level API classes. The names of the low-level command classes are the same as the the commands in `XOA CLI <https://docs.xenanetworks.com/projects/tdl-xoa-cli/en/latest/>`_. This makes it easy for you to understand and use the APIs if you are already familiar with XOA CLI.

.. code-block:: python

    import asyncio
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection

    # Establish connection to the tester
    handler = TransportationHandler(enable_logging=False)
    await establish_connection(handler, host="10.10.10.10", port=22606)

    # Log on and set owner for the tester
    await cmd.C_LOGON(handler).set("xena")
    await cmd.C_OWNER(handler).set("username")

    # Get the version string of the Test Module 0
    resp = await cmd.M_VERSIONSTR(handler, 0).get()
    print(resp.version_str)

    # Start traffic on Test Port 0/0
    await cmd.P_TRAFFIC(handler, 0, 0,).set(on_off=enums.StartOrStop.START)

.. important::

    XOA high-level API is the recommended way to interact with the tester as it handles connection keep-alive and index management automatically.

    If you still choose to use the low-level API, you need to be aware of the additional responsibilities it entails.

    * You need to **manage the connection keep-alive manually**.
    * You need to **manage index management manually**.
    * You need to **handle the creation and deletion of stream indices, filter indices, modifier indices, etc. manually**.


Syntax and Notations
-----------------------

``lli`` package aims to be semantic in function naming to avoid expectation conflict, as well as avoiding methods that can return values of different types. 

The key rule is: **one method, one action**. The following notations are used throughout this chapter.


:<prefix>:
    
    A group of commands that manage the resources of the same kind but still stays at the same level as others. 
    
    ``C_`` for chassis level commands, ``P_`` for port level commands, etc. For example, ``P_SPEEDSELECTION`` and ``P_SPEEDS_SUPPORTED`` are in the ``P_`` category.

:<cmd_name>:
    
    The name of the command. Commands of the same access level, which access or modify parameters of the same kind, are grouped under one command group as shown in the example below.

:<conn_handler>:
    
    The connection handler object that represents the connection to the tester. 
    
    You can create a connection handler by using ``establish_connection`` function.

:<indices>:
    
    Represents *stream indices*, *connection group indices*, *filter indices*, etc.

:<method>:
    
    There are only two types of methods for each command, ``get`` and/or ``set``. 
    
    ``get`` is used to query values, status, configuration of the command. 
    
    ``set`` is the change or configure the parameters of the command.

    To use ``get`` and ``set`` methods, you need to use ``await`` because they are all made asynchronous.


Import Modules
-------------------------

To create a test script using low-level API, you first need to import the necessary modules. Then you need to make an async function to hold your test script code.

Here is an example of how to do it:

.. code-block:: python

    import asyncio
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums
    from xoa_driver import utils


Establish Connection
-------------------------

After importing the necessary modules, you need to establish a connection to the tester. Create a ``TransportationHandler`` object first, which represents the connection to the tester. 

Then use the ``establish_connection`` function to connect to the tester. You need to provide the tester's IP address and port number (default is 22606) as parameters.

.. code-block:: python

    import asyncio
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums
    from xoa_driver import utils

    # Establish connection to the tester
    handler = TransportationHandler(enable_logging=False)
    await establish_connection(handler, host="10.10.10.10", port=22606)


Use Low-Level APIs
-------------------------

Once the connection is established, you need to gain access to the tester using the ``C_LOGON`` and ``C_OWNER`` commands. You need to provide the username and password for authentication.

Now you can send low-level commands to the tester using the command classes in the ``commands`` module. Each command class corresponds to a specific command in XOA CLI.

Create an instance of the command class by providing the ``TransportationHandler`` object and any necessary indices as parameters. Then use the ``get`` and ``set`` methods to query or modify the command's parameters.

.. code-block:: python

    import asyncio
    from xoa_driver import utils
    from xoa_driver.lli import commands as cmd
    from xoa_driver.lli import TransportationHandler
    from xoa_driver.lli import establish_connection
    from xoa_driver import enums

    # Establish connection to the tester
    handler = TransportationHandler(enable_logging=False)
    await establish_connection(handler, host="10.10.10.10", port=22606)

    # Log on and set owner for the tester
    await cmd.C_LOGON(handler).set("xena")
    await cmd.C_OWNER(handler).set("username")

    # Reserve Port 0/0
    resp = await cmd.P_RESERVATION(handler, 0 , 0).get()
    if resp.status == enums.ReservedStatus.RESERVED_BY_OTHER:
        await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RELINQUISH)
    if resp.status == enums.ReservedStatus.RESERVED_BY_YOU:
        await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RELEASE)
    await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RESERVE)

    # Change description for Port 0/0
    await cmd.P_COMMENT(handler, 0, 0).set(comment="My Port")

    # Create Stream 0 on Port 0/0
    await cmd.PS_CREATE(handler, 0, 0, 0).set()

    # Configure Stream 0 on Port 0/0
    await cmd.PS_PACKETLENGTH(handler, 0, 0, 0).set(length_type=enums.LengthType.FIXED, min_val=1000, max_val=1000)

    # Start traffic on Port 0/0
    await cmd.P_TRAFFIC(handler, 0, 0,).set(on_off=enums.StartOrStop.START)
    
    # Stop traffic on Port 0/0
    await cmd.P_TRAFFIC(handler, 0, 0,).set(on_off=enums.StartOrStop.STOP)

    # Get statistics for Stream 0 on Port 0/0
    await cmd.PT_STREAM(handler, 0, 0, 0).get()

    # Release port
    await cmd.P_RESERVATION(handler, 0, 0).set(enums.ReservedAction.RELEASE)


Close Connection
-------------------------
After you have finished sending commands to the tester, you need to log off and close the connection using the ``C_LOGOFF`` command.

.. code-block:: python

    ...

    # Log off and close connection
    await cmd.C_LOGOFF(handler).set()
    handler.close()



