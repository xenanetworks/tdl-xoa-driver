from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    P_AUTONEGSELECTION,  # questionable which ports are electrical
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

from .bases.port_l23_genuine import BasePortL23Genuine


class LowPowerMode:
    """L23 port low power mode."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.enable = P_LPENABLE(conn, module_id, port_id)
        """Energy Efficiency Ethernet.
        Representation of P_LPENABLE
        """

        self.mode = P_LPTXMODE(conn, module_id, port_id)
        """Low power TX mode.
        Representation of P_LPTXMODE
        """
        self.status = P_LPSTATUS(conn, module_id, port_id)
        """Low power status.
        Representation of P_LPSTATUS
        """

        self.partner_capabilities = P_LPPARTNERAUTONEG(conn, module_id, port_id)
        """EEE capabilities advertised during auto-negotiation by the far side.
        Representation of P_LPPARTNERAUTONEG
        """

        self.snr_margin = P_LPSNRMARGIN(conn, module_id, port_id)
        """SNR margin on the four link channels by the PHY.
        Representation of P_LPSNRMARGIN
        """

        self.rx_power = P_LPRXPOWER(conn, module_id, port_id)
        """RX power recorded during training for the four channels.
        Representation of P_LPRXPOWER
        """

        self.capabilities = P_LPSUPPORT(conn, module_id, port_id)
        """EEE capabilities of the port.
        Representation of P_LPSUPPORT
        """


class FamilyE(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.autoneg_selection = P_AUTONEGSELECTION(conn, module_id, port_id)
        """L23 port's auto-negotiation selection.
        Representation of P_AUTONEGSELECTION
        """

        self.eee = LowPowerMode(conn, module_id, port_id)
        """L23 port Low Power mode settings."""


class POdin5G4S6PCU(FamilyE):
    """L23 port on Odin-5G-4S-6P-CU module.
    """
    ...


class POdin10G5S6PCU(FamilyE):
    """L23 port on Odin-10G-5S-6P-CU module.
    """
    ...


class POdin10G5S6PCU_b(FamilyE):
    """L23 port on Odin-10G-5S-6P-CU[b] module.
    """
    ...


class POdin10G3S6PCU(FamilyE):
    """L23 port on Odin-10G-3S-6P-CU module.
    """
    ...


class POdin10G3S2PCU(FamilyE):
    """L23 port on Odin-10G-3S-2P-CU module.
    """
    ...
