Configuration
=========================

Media Configuration
-------------------
For the test modules that support media configuration (check :class:`~xoa_driver.internals.commands.m_commands.M_CAPABILITIES`), this command sets the desired media type (front port).

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_MEDIA`

.. code-block:: python

    # Media Configuration
    await module.config.media.set(media_config=enums.MediaConfigurationType.BASE_T1)
    await module.config.media.set(media_config=enums.MediaConfigurationType.BASE_T1S)
    await module.config.media.set(media_config=enums.MediaConfigurationType.CFP)
    await module.config.media.set(media_config=enums.MediaConfigurationType.CFP4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.CXP)
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP800)
    await module.config.media.set(media_config=enums.MediaConfigurationType.OSFP800_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP112)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP112_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP28_NRZ)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP28_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFP56_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD_NRZ)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD_PAM4)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD800)
    await module.config.media.set(media_config=enums.MediaConfigurationType.QSFPDD800_ANLT)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP112)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP28)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFP56)
    await module.config.media.set(media_config=enums.MediaConfigurationType.SFPDD)

    resp = await module.config.media.get()
    resp.media_config

Supported Configuration
------------------------
Shows the supported configurations by a module, including the supported media configurations and their corresponding port configurations. 

The structure of the returned value is
``[ <cage_type> <available_speed_count> [<ports_per_speed> <speed>] ]``.
``[<ports_per_speed> <speed>]`` is repeated until all speeds supported by the ``<cage_type>`` has been listed.
``[<cage_type> <available_speed_count>]`` is repeated for all cage types on the module including the related ``<ports_per_speed> <speed>`` information.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_MEDIASUPPORT`

.. code-block:: python

    resp = await module.supported_configs.get()
    resp.media_info_list


Port Configuration
------------------
This property defines the current number of ports and the speed of each of them
on a test module. 

.. note::

    ``<portspeed_list>`` is a list of integers, where the first element is the number of ports followed by a number of port speeds in Mbps.

    The number of port speeds equals the value of the number of ports.
    
    For example if the configuration is 4x25G, ``<portspeed_list>`` will be ``[4, 25000, 25000, 25000, 25000]``.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_CFPCONFIGEXT`

.. code-block:: python

    # Port Configuration
    await module.config.port_speed.set(portspeed_list=[1, 800000])
    await module.config.port_speed.set(portspeed_list=[2, 400000, 400000])
    await module.config.port_speed.set(portspeed_list=[4, 200000, 200000, 200000, 200000])
    await module.config.port_speed.set(portspeed_list=[8, 100000, 100000, 100000, 100000, 100000, 100000, 100000, 100000])

    resp = await module.config.port_speed.get()
    resp.portspeed_list


Configuration Status
--------------------
Show the test module configuration status when the user has configured the test module to a different configuration than the one it is currently running.

Corresponding low-level API class: :class:`~xoa_driver.internals.commands.m_commands.M_RECONFIG_STATUS`

.. code-block:: python

    # Module Configuration Status

    resp = await module.config.status.get()
    resp.status
    resp.progress