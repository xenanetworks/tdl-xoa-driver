from typing import TYPE_CHECKING

from xoa_driver.internals.commands import P_BRRMODE, P_BRRSTATUS

from .bases.port_l23_genuine import BasePortL23Genuine

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class FamilyM(BasePortL23Genuine):
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        super().__init__(conn, module_id, port_id)
        self.brr_mode = P_BRRMODE(conn, module_id, port_id)
        """BRR mode.
        Representation of P_BRRMODE
        """
        self.brr_status = P_BRRSTATUS(conn, module_id, port_id)
        """Actual BRR status.
        
        :type: P_BRRSTATUS
        """


class POdin1G3S6PT1RJ45(FamilyM):
    """L23 port on Odin-1G-3S-6P-T1-RJ45 module.
    """
    ...
