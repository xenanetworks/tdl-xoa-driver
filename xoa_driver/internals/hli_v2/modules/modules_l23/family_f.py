import typing
from xoa_driver.v2 import ports
from xoa_driver.internals.hli_v2 import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-2P")
class MOdin10G1S2P(ModuleL23):
    """Test module Odin-10G-1S-2P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-2P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-2P[b]")
class MOdin10G1S2P_b(ModuleL23):
    """Test module Odin-10G-1S-2P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S2P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S2P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-2P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-2P[c]")
class MOdin10G1S2P_c(ModuleL23):
    """Test module Odin-10G-1S-2P[c]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S2P_c] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S2P_c,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-2P[c]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-6P")
class MOdin10G1S6P(ModuleL23):
    """Test module Odin-10G-1S-6P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S6P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S6P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-6P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-6P[b]")
class MOdin10G1S6P_b(ModuleL23):
    """Test module Odin-10G-1S-6P[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S6P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S6P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-6P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-2P-T")
class MOdin10G1S2PT(ModuleL23):
    """Test module Odin-10G-1S-2P-T"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S2PT] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S2PT,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-2P-T"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-2P[d]")
class MOdin10G1S2P_d(ModuleL23):
    """Test module Odin-10G-1S-2P[d]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S2P_d] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S2P_d,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager of Odin-10G-1S-2P[d]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-1S-12P")
class MOdin10G1S12P(ModuleL23):
    """Test module Odin-10G-1S-12P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G1S12P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G1S12P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port index manager Odin-10G-1S-12P"""

@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-6S-6P[a]")
class MOdin10G6S6P_a(ModuleL23):
    """Test module Odin-10G-6S-6P[a]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G6S6P_a] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G6S6P_a,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager Odin-10G-6S-6P[a]"""
