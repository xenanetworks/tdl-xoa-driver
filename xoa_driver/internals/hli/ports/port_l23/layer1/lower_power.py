from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_LPENABLE,
    P_LPTXMODE,
    P_LPSTATUS,
    P_LPPARTNERAUTONEG,
    P_LPSNRMARGIN,
    P_LPRXPOWER,
    P_LPSUPPORT,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf

class LowPowerMode:
    """L23 port low power mode."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.enable = P_LPENABLE(conn, module_id, port_id)
        """Energy Efficiency Ethernet.
        
        :type: P_LPENABLE
        """

        self.mode = P_LPTXMODE(conn, module_id, port_id)
        """Low power TX mode.
        
        :type: P_LPTXMODE
        """
        self.status = P_LPSTATUS(conn, module_id, port_id)
        """Low power status.
        
        :type: P_LPSTATUS
        """

        self.partner_capabilities = P_LPPARTNERAUTONEG(conn, module_id, port_id)
        """EEE capabilities advertised during auto-negotiation by the far side.
        
        :type: P_LPPARTNERAUTONEG
        """

        self.snr_margin = P_LPSNRMARGIN(conn, module_id, port_id)
        """SNR margin on the four link channels by the PHY.
        
        :type: P_LPSNRMARGIN
        """

        self.rx_power = P_LPRXPOWER(conn, module_id, port_id)
        """RX power recorded during training for the four channels.
        
        :type: P_LPRXPOWER
        """

        self.capabilities = P_LPSUPPORT(conn, module_id, port_id)
        """EEE capabilities of the port.
        
        :type: P_LPSUPPORT
        """