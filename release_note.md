# XOA Python API v1.6.1 Release Notes
We are excited to announce the **release of XOA Python API v1.6.1**, which brings several significant updates and improvements to enhance your experience. This version focuses on **refining the some API naming convention**, **introducing new features**, and **improving documentation** for better usability.

## 💥 Breaking Changes

### Refined Layer-1 API Naming Convention

The previous naming convention used `pcs_pma` and `l1` to represent Layer-1 functionalities, which could be confusing for users. In version 1.6.0, we have revamped the naming convention to use `layer1` as the primary attribute for accessing Layer-1 features. This change enhances code readability and makes it easier for users to locate and utilize Layer-1 functionalities.

In addtion, all ``pcs_fec`` related APIs have been moved under the ``pcs`` attribute of ``layer1`` for better organization.

**Link Flap and PMA Error Injection**
``` python
# Before v1.6 -> Now v1.6
await port.pcs_pma.link_flap -> await port.layer1.impairment.link_flap
await port.pcs_pma.pma_pulse_err_inj ->  await port.layer1.impairment.pma_error_inject
```

**PCS**
``` python
# Before v1.6 -> Now v1.6
await port.fec_mode -> await port.layer1.pcs.fec_mode
await port.pcs_pma.rx.clear -> await port.layer1.pcs.clear
await port.pcs_pma.rx.fec_status -> await port.layer1.pcs.fec_symbol_status.fec_status
await port.l1.pcs_variant -> port.layer1.pcs.pcs_variant
await port.pcs_pma.lanes[i] -> await port.layer1.pcs.lane[i]
await port.l1.fec_error_inject -> await port.layer1.pcs.fec_error_inject
```
**PRBS**
``` python
# Before v1.6 -> Now v1.6
await port.pcs_pma.prbs_config.type -> await port.layer1.prbs_config
await port.serdes[i].prbs.control -> await port.layer1.serdes[i].prbs.control
await port.serdes[i].prbs.status -> await port.layer1.serdes[i].prbs.status
```
**Equalization**
``` python
# Before v1.6 -> Now v1.6
await port_obj.l1.serdes[i].medium -> await port.layer1.serdes[i].medium
```
**PMA**
``` python
# Before v1.6 -> Now v1.6
await port.l1.serdes[0].pma -> await port.layer1.serdes[0].pma
```
**ANLT**
```python
# Before v1.6 -> Now v1.6
await port.pcs_pma.auto_neg -> await port.layer1.anlt.an
await port.pcs_pma.link_training -> await port.layer1.anlt.lt
```
**Signal Integrity View**
``` python
# Before v1.6 -> Now v1.6
await port.l1.serdes[li].medium.siv -> await port.layer1.serdes[i].siv
```

### Refined TG APIs for Better Usability

To enhance the usability of Traffic Generator (TG) APIs, we have refined several API names to make them more intuitive and easier to understand. These changes aim to improve code readability and help users quickly identify the purpose of each API.

**Port Speed Mode**
``` python
# Before v1.6 -> Now v1.6
await port.speed.mode.selection -> await port.speed.selection
await port.speed.mode.supported -> await port.speed.supported
```

**Loopback**
``` python
# Before v1.6 -> Now v1.6
await port.loop_back -> await port.loopback
```

**UAT Frame Loss Ratio**
``` python
# Before v1.6 -> Now v1.6
await port.uat.frame_loss_ratio -> await port.uat.flr
```


## 🎉 Exciting New Features

Several new features have been introduced in this release to enhance the functionality and capabilities of the XOA Python API.

**🎉 Support for Z1800 Edun Modules**
Z1800 Edun modules are now supported in the XOA Python API, enabling users to leverage the capabilities of these modules for their testing needs.

**🎉 APIs for Advanced ANLT Features**
The Freya-specific Advanced ANLT features have only been supported by `hlfuncs.anlt` module. Now we have added the object-oriented APIs for Advanced ANLT, enabling users to script ANLT protocol testing with great flexibility.

Here are some examples (More details can be found in the User Guide and API Reference Documentation):
``` python
"""ANLT Auto-Restart Settings"""
await port.layer1.anlt.set_autorestart(restart_link_down=True, restart_lt_failure=True)
resp = await port.layer1.anlt.get_autorestart()

"""ANLT Strict Mode Settings"""
await port.layer1.anlt.set_strict_mode(enable=False)
resp = await port.layer1.anlt.get_strict_mode()

"""Auto-Negotiation Allow-in-Loopback Settings"""
await port.layer1.anlt.an.set_allow_loopback(allow=True)
resp = await port.layer1.anlt.an.get_allow_loopback()

"""Auto-Negotiation Send Empty Next Page Settings"""
await port.layer1.anlt.an.set_empty_np(enable=True)
resp = await port.layer1.anlt.an.get_empty_np()

"""Link Training Per-Serdes Algorithm Selection"""
await port.layer1.serdes[0].lt.set_algorithm_default()
resp = await port.layer1.serdes[0].lt.get_algorithm()

"""Link Training Per-Serdes Initial Modulation Selection"""
await port.layer1.serdes[0].lt.set_initial_modulation_nrz()
await port.layer1.serdes[0].lt.set_initial_modulation_pam4()
await port.layer1.serdes[0].lt.set_initial_modulation_pam4precoding()
resp = await port.layer1.serdes[0].lt.get_initial_modulation()
...
```

**🎉 MACsec APIs for Loki-4P**
MACsec APIs are added to Loki-4P modules and ports. Users can now configure MACsec settings, manage security associations, and monitor MACsec statistics through the API. Here are some examples (More details can be found in the User Guide and API Reference Documentation):
``` python
# Create a TX Secure Channel
txsc_obj = await port.macsec.txscs.create()
# Set SCI and Cipher Suite for the TX Secure Channel
await txsc_obj.config.sci.set(sci=Hex("AABBCCDDEEFF0011"))
await txsc_obj.config.cipher_suite.set(cipher_suite=enums.MACSecCipherSuite.GCM_AES_128)
...
```

**🎉 More Functions for Test Resource Management**
The `hlfuncs` module has been enhanced to provide better support for test resource management. New functions have been added to facilitate the reservation, release, and management of test resources, making it easier for users to handle resource allocation in their test scripts.

* **Support Port Index Notation "x/y"**. It previously required extra parsing to obtain the module object and the port object. As port indices are commonly notated as “0/0” or “7/4”, new functions are added, allowing the use of string notations directly. Here are some examples (More details can be found in the User Guide and API Reference Documentation):
``` python
from xoa_driver.hlfuncs import mgmt

# Obtain a single port object by its ID
port_obj = mgmt.obtain_port_by_id(tester_obj, "0/0")
```

* **Do More at the Same Time.** Previously you can only change the configuration of one test module at a time. Now we have fun that can match configure the module configuration for users. Here are some examples (More details can be found in the User Guide and API Reference Documentation):
``` python
from xoa_driver.hlfuncs import mgmt
from xoa_driver import enums

# Change config of multiple modules
await mgmt.set_module_configs([
  (module_obj1, enums.MediaConfigurationType.OSFP_1600, 2, 400_000),
  (module_obj2, enums.MediaConfigurationType.QSFPDD800, 8, 100_000),
  (module_obj3, enums.MediaConfigurationType.QSFPDD800, 1, 800_000)
  ])

# Obtain multiple port objects by their IDs
port_objs = mgmt.obtain_ports_by_ids(tester_obj, ["0/0", "7/4", "3/1"])

# Reserve multiple ports
await mgmt.reserve_ports([port_obj1, port_obj2, port_obj3])
```

## 📝 Documentation Improvements
The API reference documentation has been greatly improved.

* **API summary tables** are added to the beginning of each module section. This facilitates API searching, helping users quickly understand what the API does, leading to increased productivity.
* **Using package and submodule names directly in the reference guide** makes it much easier for users to understand how to use the API and where to find them.
* **API Examples written in real Python scripts is added**, demonstrating their usage in practical scenarios. This helps users grasp the concepts more effectively.
* **Documentation has been streamlined** by removing unnecessary details. It delivers what is relevant to users, helping them focus on what matters.
  



**Full Changelog**: https://github.com/xenanetworks/tdl-xoa-driver/compare/v1.5.1...v1.6.1