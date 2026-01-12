``ports`` module
=========================

Port APIs Overview
--------------------

.. csv-table:: TG Port APIs Overview
    :header: "Id", "Action", "API", "Description"
    :widths: auto
    :file: ports.csv


.. csv-table:: Impairment Port APIs Overview
    :header: "Id", "Action", "API", "Description"
    :file: ports_chimera.csv


.. csv-table:: Stream APIs Overview
    :header: "Id", "Action", "API", "Description"
    :file: streams.csv



Examples - Traffic Generation APIs
---------------------------------------------

.. literalinclude:: ports.py
    :caption: Examples - Traffic Generation APIs
    :start-at: [ports]
    :end-before: [Layer-1 Advanced Features]


Examples - Layer-1 APIs
-----------------------------

.. literalinclude:: ports.py
    :caption: Examples - Layer-1 APIs
    :start-at: [Layer-1 Advanced Features]
    :end-before: [Transceiver Management]


Examples - Transceiver APIs
-----------------------------

.. literalinclude:: ports.py
    :caption: Examples - Transceiver APIs
    :start-at: [Transceiver Management]
    :end-before: [end]


Examples - E100 Chimera Specific Port APIs
---------------------------------------------

.. literalinclude:: ports_chimera.py
    :caption: Examples - E100 Chimera Specific Port APIs
    :start-at: [chimera ports]
    :end-before: [end]


Examples - Traffic Generation Stream APIs
---------------------------------------------

.. literalinclude:: streams.py
    :caption: Examples - Traffic Generation Stream APIs
    :start-at: [streams]
    :end-before: [end]