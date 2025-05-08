Installing XOA Driver
=========================

XOA Driver is available to install and upgrade via the `Python Package Index <https://pypi.org/>`_. Alternatively, you can also install and upgrade from the source file.

Prerequisites
-------------

Before installing XOA Driver, please make sure your environment has installed `Python <https://www.python.org/>`_ and ``pip``.

Python
^^^^^^^

XOA Driver requires that you `install Python <https://realpython.com/installing-python/>`_  on your system.

.. note:: 

    XOA Driver requires Python >= 3.11

``pip``
^^^^^^^

Make sure ``pip`` is installed on your system. ``pip`` is the `package installer for Python <https://packaging.python.org/guides/tool-recommendations/>`_ . You can use it to install packages from the Python Package Index and other indexes.

Usually, ``pip`` is automatically installed if you are:

* working in a `virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_ (`virtualenv <https://virtualenv.pypa.io/en/latest/#>`_ or `venv <https://docs.python.org/3/library/venv.html>`_ ). It is not necessary to use ``sudo pip`` inside a virtual Python environment.
* using Python downloaded from `python.org <https://www.python.org/>`_ 

If you don't have ``pip`` installed, you can:

* Download the script, from https://bootstrap.pypa.io/get-pip.py.
* Open a terminal/command prompt, ``cd`` to the folder containing the ``get-pip.py`` file and run:

.. tab:: Windows

    .. code-block:: doscon
        :caption: Install pip in Windows environment.

        > py get-pip.py

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install pip in macOS/Linux environment.

        $ python3 get-pip.py

.. seealso::

    Read more details about this script in `pypa/get-pip <https://github.com/pypa/get-pip>`_.

    Read more about installation of ``pip`` in `pip installation <https://pip.pypa.io/en/stable/installation/>`_.


Installing From PyPI Using ``pip``
--------------------------------------

``pip`` is the recommended installer for XOA Driver. The most common usage of ``pip`` is to install from the Python Package Index using `Requirement Specifiers <https://pip.pypa.io/en/stable/cli/pip_install/#requirement-specifiers>`_.


Install to Global Namespace
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install XOA Driver in Windows environment from PyPi.

        > pip install tdl-xoa-driver -U         # latest version
        > pip install tdl-xoa-driver==1.1.0     # specific version
        > pip install tdl-xoa-driver>=1.1.0     # minimum version

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install XOA Driver in macOS/Linux environment from PyPi.

        $ pip3 install tdl-xoa-driver -U         # latest version
        $ pip3 install tdl-xoa-driver==1.1.0     # specific version
        $ pip3 install tdl-xoa-driver>=1.1.0     # minimum version


Install in Activated Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Install XOA Driver in a virtual environment, so it does not pollute your global namespace. 

For example, your project folder is called ``/my_xoa_project``.

.. tab:: Windows

    .. code-block:: doscon
        :caption: Install XOA Driver in a virtual environment in Windows from PyPI.

        [my_xoa_project]> python -m venv .\env
        [my_xoa_project]> .\env\Scripts\activate

        (env) [my_xoa_project]> pip install tdl-xoa-driver

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install XOA Driver in a virtual environment in macOS/Linux from PyPI.

        [my_xoa_project]$ python3 -m venv ./env
        [my_xoa_project]$ source ./env/bin/activate

        (env) [my_xoa_project]$ pip3 install tdl-xoa-driver

.. seealso::

    * `Virtual Python environment <https://packaging.python.org/en/latest/tutorials/installing-packages/#creating-and-using-virtual-environments>`_
    * `virtualenv <https://virtualenv.pypa.io/en/latest/#>`_
    * `venv <https://docs.python.org/3/library/venv.html>`_


Deactivate Virtual Environment
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can deactivate a virtual environment by typing ``deactivate`` in your shell.


.. tab:: Windows

    .. code-block:: doscon
        :caption: Deactivate virtual environment on Windows.

        (env) [my_xoa_project]> deactivate
        [my_xoa_project]>

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Deactivate virtual environment on macOS/Linux.
        
        (env) [my_xoa_project]$ deactivate
        [my_xoa_project]$


Upgrading From PyPI Using ``pip``
--------------------------------------------

To upgrade XOA Driver package from PyPI:

.. tab:: Windows
    :new-set:
    
    .. code-block:: doscon
        :caption: Upgrade XOA Driver in Windows environment from PyPi.

        > pip install tdl-xoa-driver -U

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Upgrade XOA Driver in macOS/Linux environment from PyPi.

        $ pip3 install tdl-xoa-driver -U


Installing Manually From Source
--------------------------------------------

If for some reason you need to install or upgrade XOA Driver manually from source, the steps are:

**Step 1**, make sure Python packages `wheel <https://wheel.readthedocs.io/en/stable/>`_ and  `setuptools <https://setuptools.pypa.io/en/latest/index.html>`_ are installed on your system. Install ``wheel`` and ``setuptools`` using ``pip``:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install ``wheel`` and ``setuptools`` in Windows environment.

        > pip install wheel setuptools

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install ``wheel`` and ``setuptools`` in macOS/Linux environment.

        $ pip3 install wheel setuptools

**Step 2**, download the XOA Driver source distribution from `XOA Driver Releases <https://github.com/xenanetworks/tdl-xoa-driver/releases>`_. Unzip the archive and run the ``setup.py`` script to install the package:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Install XOA Driver in Windows environment from source.

        [xoa_driver]> python setup.py install

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Install XOA Driver in macOS/Linux environment from source.

        [xoa_driver]$ python3 setup.py install


**Step 3**, if you want to distribute, you can build ``.whl`` file for distribution from the source:

.. tab:: Windows
    :new-set:

    .. code-block:: doscon
        :caption: Build XOA Driver wheel in Windows environment for distribution.

        [xoa_driver]> python setup.py bdist_wheel

.. tab:: macOS/Linux

    .. code-block:: console
        :caption: Build XOA Driver wheel in macOS/Linux environment for distribution.

        [xoa_driver]$ python3 setup.py bdist_wheel