``p_ue_commands`` module
=================================

This module contains the **L23 port classes (UE)** that deal with basic information about, and configuration of L23 test ports. The L23 port command names all have the form ``P_UE_<xxx>`` and require a module index id and a port index id. In general, port commands cannot be changed while traffic is on. Additionally, every stream must be disabled before changing parameters that affect the bandwidth of the port.


Port Commands - Ultra Ethernet
------------------------------

.. automodule:: xoa_driver.internals.commands.p_ue_commands
    :members:
    :no-undoc-members:
    :exclude-members: __init__

