HL Module Management
=====================

.. currentmodule:: xoa_driver.hlfuncs.mgmt

The following high-level functions help you manage test modules.

Reserve/Release Module
---------------------------

.. autofunction:: reserve_module

.. autofunction:: release_module

Access Module Object
---------------------------

.. autofunction:: get_module

.. autofunction:: get_modules

Module Supported Media
---------------------------

.. autofunction:: get_module_supported_media


Module Configuration
---------------------------

.. autofunction:: set_module_config

.. autofunction:: set_module_media_config

.. autofunction:: set_module_port_config

.. note::
    
    If you use `set_module_config`, you don't need to call `set_module_media_config` and `set_module_port_config` separately, as `set_module_config` already includes both functionalities.


Module End-of-Life Information
-------------------------------

.. autofunction:: get_module_eol_date

.. autofunction:: get_module_eol_days


Module Cage Insertion Information
-------------------------------------

.. autofunction:: get_module_cage_insertion_count