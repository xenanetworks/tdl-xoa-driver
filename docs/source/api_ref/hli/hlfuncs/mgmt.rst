``mgmt`` - Resource management functions 
==========================================

The ``mgmt`` module offers functions for managing test chassis, modules, and ports.


.. currentmodule:: xoa_driver.hlfuncs.mgmt

Chassis Reservation and System Uptime
-------------------------------------

.. autosummary::

    reserve_tester
    release_tester
    get_chassis_sys_uptime


Obtain Module Instance
----------------------

.. autosummary::

    obtain_modules_by_ids
    obtain_module_by_id
    obtain_module_by_port_id

Module Reservation
------------------

.. autosummary::

    reserve_modules
    release_modules


Module Configuration
---------------------

.. autosummary::

    get_module_supported_configs
    set_module_configs
    set_module_config


Module Warranty Checking 
------------------------

.. autosummary::

    get_module_eol_date
    get_module_eol_days

Module Cage Count and Insertions
--------------------------------

.. autosummary::

    get_cage_insertions
    get_cage_count


Port Object from ID
-------------------

.. autosummary::

    obtain_ports_by_ids
    obtain_port_by_id


Port Reservation and Stream Removal
-----------------------------------

.. autosummary::

    reserve_ports
    release_ports
    reset_ports
    remove_streams

Module Contents
-----------------

.. automodule:: xoa_driver.hlfuncs.mgmt
    :members:
    :show-inheritance:
    :undoc-members:
    :member-order: bysource