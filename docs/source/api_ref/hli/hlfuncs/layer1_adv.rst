``layer1_adv`` module
===============================

The ``layer1_adv`` module offers high-level functions for advanced Layer 1 configurations and operations.

.. currentmodule:: xoa_driver.hlfuncs.layer1_adv


.. rubric:: PCSL Skew

.. autosummary::

    get_rx_pcsl_skew


.. rubric:: Rx PCS Status and Flags

.. autosummary::
    
    get_cdr_lol_status
    get_port_loa_status
    get_pcsl_loa_status
    get_hi_ber_status
    set_hi_ser_alarm
    get_hi_ser_status
    get_deg_ser_status
    set_deg_ser_thresholds
    get_deg_ser_thresholds
    get_lf_status
    get_rf_status
    get_lf_rf_status
    get_link_down_status
    

.. rubric:: Rx PCS Error Events

.. autosummary::

    get_rx_errors_since_clear

    clear_rx_err_cnt


.. rubric:: Tx PCS Error Injection

.. autosummary::

    inject_errcwd_once
    inject_itb_once
    inject_hi_ser_once
    inject_am_error_once
    inject_loa_once


.. rubric:: Tx PCS Error Events

.. autosummary::

    get_tx_errors_since_clear
    get_tx_pcsl_errors_since_clear

    clear_tx_err_cnt
    

.. rubric:: PMA Tx/Rx Frequency and PPM

.. autosummary::

    get_tx_freq
    get_rx_freq


.. rubric:: PMA Tx/Rx Frequency (Hz)

If you only want to get frequency parameters, you can use the following functions.

.. autosummary::

    get_tx_freq_all
    get_tx_freq_curr
    get_tx_freq_min
    get_tx_freq_max
    get_rx_freq_all
    get_rx_freq_curr
    get_rx_freq_min
    get_rx_freq_max


.. rubric:: PMA Tx/Rx Frequency Offset (PPM)

If you only want to get frequency offset parameters, you can use the following functions.

.. autosummary::
    
    get_tx_ppm_all
    get_tx_ppm_curr
    get_tx_ppm_min
    get_tx_ppm_max
    get_rx_ppm_all
    get_rx_ppm_curr
    get_rx_ppm_min
    get_rx_ppm_max

    
.. rubric:: PMA Tx/Rx Data Rate (bps)

.. autosummary::

    get_tx_datarate_all
    get_tx_datarate_curr
    get_tx_datarate_min
    get_tx_datarate_max
    get_rx_datarate_all
    get_rx_datarate_curr
    get_rx_datarate_min
    get_rx_datarate_max


.. rubric:: Deprecated Functions

.. autosummary::
    
    get_cdr_lol
    get_rx_lane_skew
    get_hi_ber
    get_hi_ser
    get_deg_ser
    set_cw_err
    set_itb
    get_cw_err_since_last
    get_itb_since_last
    get_total_loa_since_last
    get_link_down_since_last
    get_local_fault_since_last
    get_remote_fault_since_last
    

Module Contents
-----------------

.. automodule:: xoa_driver.hlfuncs.layer1_adv
    :members:
    :show-inheritance:
    :undoc-members:
    :member-order: bysource