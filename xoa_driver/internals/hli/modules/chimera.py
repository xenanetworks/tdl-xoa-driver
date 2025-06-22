import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    import __interfaces as m_itf
from .ne_base import ModuleNEBase


@typing.final
@revisions.register_chimera_module(rev="Chimera-100G-5S-2P")
class MChi100G5S2P(ModuleNEBase):
    """Chimera module Chi-100G-5S-2P"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi100G5S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi100G5S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-100G-5S-2P

        :type: PortsManager
        """


@typing.final
@revisions.register_chimera_module(rev="Chimera-100G-5S-2P[b]")
class MChi100G5S2P_b(ModuleNEBase):
    """Chimera module Chi-100G-5S-2P[b]"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi100G5S2P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi100G5S2P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-100G-5S-2P[b]

        :type: PortsManager
        """


@typing.final
@revisions.register_chimera_module(rev="Chimera-40G-5S-2P")
class MChi40G2S2P(ModuleNEBase):
    """Chimera module Chi-40G-2S-2P"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.PChi40G2S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PChi40G2S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Chi-40G-2S-2P

        :type: PortsManager
        """
