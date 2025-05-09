Introduction
====================

XOA Driver is a standalone Python library that provides a user-friendly and powerful interface for automating network testing tasks using Xena Networks test equipment. Xena test equipment is a high-performance network test device designed for testing and measuring the performance of network equipment and applications.

The XOA Driver is designed to be easy to use and integrate with other automation tools and frameworks. It provides a comprehensive set of methods and classes for interacting with Xena test equipment, including the ability to create and run complex test scenarios, generate and analyze traffic at line rate, and perform detailed analysis of network performance and behavior.

The XOA Driver simplifies the process of automating network testing tasks using Xena test equipment. It provides a simple, yet powerful, interface for interacting with Xena test equipment using the Python programming language. With the XOA Driver, network engineers and testing professionals can easily create and execute test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior, all while leveraging the power and flexibility of the Python programming language.

Additionally, the XOA Driver goes beyond providing object-oriented APIs and functions for executing test scripts. It seamlessly integrates with XOA CLI commands, enabling users to work with them effortlessly.

Overall, the XOA Driver is a valuable tool for anyone looking to automate their network testing tasks using Xena test equipment. With its simple, yet powerful, interface and support for the Python programming language, the XOA Driver provides a flexible and extensible framework for automating network testing tasks and improving the quality of network infrastructure.

.. important::
    
    To learn :term:`XOA CLI` commands, go to `XOA CLI Documentation <https://docs.xenanetworks.com/projects/tdl-xoa-cli>`_. 

Differences Between XOA Driver and CLI
------------------------------------------

XOA CLI is a command-line interface for managing Xena Networks test equipment and automating network testing tasks. The XOA CLI is part of the Xena OpenAutomation platform, which provides a framework for automating network testing tasks using Xena test equipment. XOA CLI allows users to interact with Xena test equipment from the command line, using a set of commands and parameters that can be used to automate a variety of testing tasks. The XOA CLI is designed to be user-friendly and easy to use, with a simple syntax and intuitive command structure.

The XOA Driver and XOA CLI are both tools for automating network testing tasks using Xena test equipment, but they differ in several ways:

* Interface: The XOA Driver provides a Pythonic interface to interact with Xena test equipment, while the XOA CLI provides a command-line interface to interact with Xena test equipment.

* Programming: The XOA Driver is a library that can be used with the Python programming language to create and execute complex test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior. The XOA CLI is a standalone tool that can be used to interact with Xena test equipment through the command line, without the need for programming.

* Functionality: While both tools can be used to create and execute test scenarios, generate and analyze traffic, and perform detailed analysis of network performance and behavior, the XOA Driver provides a more comprehensive and flexible set of functions for interacting with Xena test equipment. The XOA CLI provides a subset of the functionality available through the XOA Driver.

* Ease of use: The XOA Driver provides a more user-friendly and intuitive interface for interacting with Xena test equipment, while the XOA CLI can be more complex and requires knowledge of the command line interface.

Synergy Between XOA Driver and CLI
------------------------------------------

The synergy between the XOA Driver and XOA CLI lies in their integration capabilities. The XOA Driver seamlessly integrates with the XOA CLI, enabling users to work with CLI commands effortlessly within their Python scripts. This integration allows users to combine the flexibility and extensibility of the Python language with the precise control and configuration offered by the CLI commands.

The XOA Driver allows users to interact with Xena Networks test equipment using Python code, providing an object-oriented and user-friendly interface for automating network testing tasks. It enables users to create and execute test scenarios, generate traffic, and analyze network performance using Python programming language. On the other hand, the XOA CLI allows users to configure and control Xena test equipment through command-line commands. It provides a familiar and efficient way to interact with the equipment, allowing users to perform various configuration tasks, manage ports, and execute test commands.

By leveraging both the XOA Driver and XOA CLI, users can take advantage of the best of both worlds. They can harness the power of Python for automation, scripting, and advanced data analysis while utilizing the precise control and configuration options provided by the CLI commands. With the XOA Driver, users can seamlessly work with CLI commands and port configuration files from `XenaManager <https://xenanetworks.com/product/xenamanager/>`_, streamlining the configuration process. Whether users prefer a programming approach or a straightforward command-line interface, both options are available to suit different requirements and preferences when working with Xena test equipment. This synergy enhances the overall testing experience, enabling users to perform complex testing tasks efficiently and effectively.

In summary, the XOA Driver and XOA CLI work together to provide a comprehensive and flexible testing solution. The Python API brings automation and scripting capabilities, while the CLI offers precise control and configuration options. The integration between the two allows users to leverage their respective strengths and achieve a synergistic testing workflow.

.. figure:: /_static/xoa_cli_synergy.png
    :align: left

    Synergy Between XOA Driver and XOA CLI

    * Save port configurations from XenaManager and load them via XenaManager to configure the ports.

    * Use CLI commands to manage and control testers.

    * Save port configurations from XenaManager and load them using XOA Driver configure the ports. Use CLI commands inside XOA Driver to manage and control testers.