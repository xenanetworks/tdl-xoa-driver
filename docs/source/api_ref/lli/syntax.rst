Syntax and Notations
=======================

``lli`` package aims to be semantic in function naming to avoid expectation conflict, as well as avoiding methods that can return values of different types. The key rule is: **one method, one action**. The following notations are used throughout this chapter.


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
