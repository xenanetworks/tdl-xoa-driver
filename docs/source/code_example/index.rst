Python Script Examples
======================

You can find various XOA Python scripts in our public GitHub repository `Xena OpenAutomation Script Example Library <https://github.com/xenanetworks/tld-xoa-python-script-library>`_. It includes script examples of how you can use XOA Driver to configure a Xena tester.

What Example Folder Contains
----------------------------

Each folder contains:

* Python script file - this is where the example code locates
* requirements.txt - dependencies to run the code. You should `pip install -r requirements.txt` (for Windows) or `pip3 install -r requirements.txt` (for macOS/Linux) to update your Python environment (either global or virtual) to have the necessary dependencies.

Installing XOA Driver
----------------------------

This section details how to install ``tdl-xoa-driver``. Installation is necessary to execute scripts that use XOA Driver.

Before installing ``tdl-xoa-driver``, please make sure your environment has installed `python>=3.11` and `pip`.

You can install the ``tdl-xoa-driver`` to your global or virtual environment for Windows, macOS, and Linux using the commands below. 

.. code-block:: python

    pip install tdl-xoa-driver -U            # latest version (For Windows)
    pip3 install tdl-xoa-driver -U           # latest version (For macOS/Linux)


Once the ``tdl-xoa-driver`` is installed, you can execute the script.
