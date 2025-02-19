Test Resource Management
=================================

If you are new to Xena testers, this section will help you understand the basics of test resource management. :term:`Test resources <Test resource>` can be the chassis itself, a test module on the chassis or a test port on a module.

This section describes:

* :term:`Test resource` hierarchy.
* :term:`Test resource` management principle.

Test Resource Hierarchy
------------------------------------

Xena tester has the following hierarchical structure.

::

    ---------------------
    |  Tester            |
    ---------------------
        |
        |   -----------------------
        |---|   TG Module         |
        |   -----------------------
        |        |
        |        |    ------------------- 
        |        |----|  TG Port        | 
        |        |    ------------------- 
        |        |        |
        |        |        |    ************************* 
        |        |        |----|  Port Statistics      | 
        |        |        |    ************************* 
        |        |        |    ************************* 
        |        |        |----|  Stream               | 
        |        |        |    ************************* 
        |        |        |        |
        |        |        |        |    **********************  
        |        |        |        |----|  Filter            | 
        |        |        |        |    **********************  
        |        |        |        |    **********************  
        |        |        |        |----|  Modifier          | 
        |        |        |        |    ********************** 
        |        |        |        |    **********************  
        |        |        |        |----|  Histogram         | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Length Term       | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Match Term        | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Test Payload      | 
        |        |        |        |    ********************** 
        |        |        |        |    ********************** 
        |        |        |        |----|  Stream Statistics | 
        |        |        |        |    **********************
        |        |        |        |    
        |
        |   -------------------------
        |---|  Impairment Module    |
        |   -------------------------
        |        |
        |        |    ----------------------
        |        |----|  Impairment Port   | 
        |        |    ----------------------
        |        |        |
        |        |        |    ************************* 
        |        |        |----|  Port Statistics      | 
        |        |        |    ************************* 
        |        |        |    *************************
        |        |        |----|  Flow                 | 
        |        |        |    *************************
        |        |        |        |
        |        |        |        |    ****************************
        |        |        |        |----|  Filter                  | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Impairment Config       | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Impairment Distribution | 
        |        |        |        |    ****************************
        |        |        |        |    ****************************
        |        |        |        |----|  Flow Statistics         | 
        |        |        |        |    ****************************
        |        |        |        |    

Tester, Module, and Port are hardware resources that correspond to the hardware configuration. They cannot be created or deleted. Everything below Port is virtual resources that can be created, deleted, and configured as needed.


Management Principle
-----------------------------------

Xena testers support multiple simultaneous connections from any mixture of Xena clients, such as the `XenaManager <https://xenanetworks.com/product/xenamanager/>`_, scripting clients, etc. As soon as a client has successfully established a connection to the chassis, any :term:`test resource` can be inspected. But in order to change the :term:`test resource` configuration, the resource must first be reserved by the client.

To management :term:`test resources<test resource>`, i.e., read, write, create, delete, you must follow the principles below:

1. To do ``set`` (create/update/delete) on a :term:`test resource`, i.e. *tester*, *module*, or *port*, you must reserve the resource under your username.
2. To do ``get`` (read) on a :term:`test resource`, you don't need to reserve.
3. To reserve a tester, you must make sure **all the modules and ports are either released or under your ownership**.
4. To reserve a module, you must make sure **all the ports are either released or under your ownership**.

.. important::

    Starting traffic using ``C_TRAFFIC`` of ``C_TRAFFICSYNC`` does **NOT** require chassis reservation but port reservation, although their command prefix is ``C_`` and categorized as chassis-level commands.
