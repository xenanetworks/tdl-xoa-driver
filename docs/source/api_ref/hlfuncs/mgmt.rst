``mgmt`` module
===============================

The ``mgmt`` module offers high-level functions for managing test chassis, modules, and ports.


.. currentmodule:: xoa_driver.hlfuncs.mgmt

.. rubric:: Chassis Reservation and System Uptime

.. autosummary::

    reserve_tester
    release_tester
    get_chassis_sys_uptime


.. rubric:: Module Object from ID

.. autosummary::

    obtain_modules_by_ids
    obtain_module_by_id
    obtain_module_by_port_id

.. rubric:: Module Reservation

.. autosummary::

    reserve_modules
    release_modules


.. rubric:: Module Configuration

.. autosummary::

    get_module_supported_configs
    set_module_configs
    set_module_config


.. rubric:: Module Warranty Checking 

.. autosummary::

    get_module_eol_date
    get_module_eol_days

.. rubric:: Module Cage Count and Insertions

.. autosummary::

    get_cage_insertions
    get_cage_count


.. rubric:: Port Object from ID

.. autosummary::

    obtain_ports_by_ids
    obtain_port_by_id


.. rubric:: Port Reservation and Stream Removal

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