import typing
import functools
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.utils.cap_id import CapID
from xoa_driver.internals.commands import P_CAPABILITIES

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23

D_FAMELY_ID = CapID(1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
F_FAMELY_ID = CapID(0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


CombiTypes = typing.Union[
    ports.POdin1G4S4PCombi,
    ports.POdin10G4S2PCombi,
]

CombiTypesB = typing.Union[
    ports.POdin1G4S4PCombi_b,
    ports.POdin10G4S2PCombi_b,
]

async def _port_resolver(conn: "itf.IConnection", module_id: int, port_id: int, port_map: typing.Dict[int, typing.Type]) -> typing.Coroutine[typing.Any, typing.Any, CombiTypes]:
    cap = await P_CAPABILITIES(conn, module_id, port_id).get()
    current_port_id = CapID.create_from_capabilities(cap)
    port_type = port_map[current_port_id.to_int()]
    return await port_type(conn, module_id, port_id)

@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-4S-2P-Combi")
class MOdin10G4S2PCombi(ModuleL23):
    """Test module Odin-10G-4S-2P-Combi
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        PORTS_MAP = {
            D_FAMELY_ID.to_int(): ports.POdin1G4S4PCombi,
            F_FAMELY_ID.to_int(): ports.POdin10G4S2PCombi,
        }
        self.ports: pm.PortsCombiManager[CombiTypes] = pm.PortsCombiManager(
            conn=conn,
            resolver=functools.partial(_port_resolver, port_map=PORTS_MAP),
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-4S-2P-Combi

        :type: PortsCombiManager
        """


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-4S-2P-Combi[b]")
class MOdin10G4S2PCombi_b(ModuleL23):
    """Test module Odin-10G-4S-2P-Combi[b]
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        PORTS_MAP = {
            D_FAMELY_ID.to_int(): ports.POdin1G4S4PCombi_b,
            F_FAMELY_ID.to_int(): ports.POdin10G4S2PCombi_b,
        }
        self.ports: pm.PortsCombiManager[CombiTypesB] = pm.PortsCombiManager(
            conn=conn,
            resolver=functools.partial(_port_resolver, port_map=PORTS_MAP),
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-4S-2P-Combi[b]

        :type: PortsCombiManager
        """

@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P")
class MOdin1G3S6P(ModuleL23):
    """Test module Odin-1G-3S-6P"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P[b]")
class MOdin1G3S6P_b(ModuleL23):
    """Test module Odin-1G-3S-6P[b]"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6P_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6P_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P-E")
class MOdin1G3S6PE(ModuleL23):
    """Test module Odin-1G-3S-6P-E"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6PE] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6PE,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P-E"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-2P-T")
class MOdin1G3S2PT(ModuleL23):
    """Test module Odin-1G-3S-2P-T"""

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S2PT] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S2PT,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-2P-T"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-5G-4S-6P-CU")
class MOdin5G4S6PCU(ModuleL23):
    """Test module Odin-5G-4S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin5G4S6PCU] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin5G4S6PCU,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-5G-4S-6P-CU"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-5S-6P-CU")
class MOdin10G5S6PCU(ModuleL23):
    """Test module Odin-10G-5S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G5S6PCU] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G5S6PCU,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-5S-6P-CU"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-5S-6P-CU[b]")
class MOdin10G5S6PCU_b(ModuleL23):
    """Test module Odin-10G-5S-6P-CU[b]"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G5S6PCU_b] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G5S6PCU_b,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-5S-6P-CU[b]"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-3S-6P-CU")
class MOdin10G3S6PCU(ModuleL23):
    """Test module Odin-10G-3S-6P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G3S6PCU] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G3S6PCU,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-3S-6P-CU"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-10G-3S-2P-CU")
class MOdin10G3S2PCU(ModuleL23):
    """Test module Odin-10G-3S-2P-CU"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin10G3S2PCU] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin10G3S2PCU,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-10G-3S-2P-CU"""


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
        """Port Index Manager of Odin-10G-1S-2P"""


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
        """Port Index Manager of Odin-10G-1S-2P[b]"""


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
        """Port Index Manager of Odin-10G-1S-2P[c]"""


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
        """Port Index Manager of Odin-10G-1S-6P"""


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
        """Port Index Manager of Odin-10G-1S-6P[b]"""


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
        """Port Index Manager of Odin-10G-1S-2P-T"""


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
        """Port Index Manager of Odin-10G-1S-2P[d]"""


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
        """Port Index Manager Odin-10G-1S-12P"""


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

@typing.final
@revisions.register_valkyrie_module(rev="Odin-100G-3S-1P")
class MOdin100G3S1P(ModuleL23):
    """Test module Odin-100G-3S-1P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin100G3S1P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin100G3S1P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-100G-3S-1P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-1G-3S-6P-T1-RJ45")
class MOdin1G3S6PT1RJ45(ModuleL23):
    """Test module Odin-1G-3S-6P-T1-RJ45"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin1G3S6PT1RJ45] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin1G3S6PT1RJ45,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-1G-3S-6P-T1-RJ45"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-40G-2S-2P")
class MOdin40G2S2P(ModuleL23):
    """Test module Odin-40G-2S-2P"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin40G2S2P] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin40G2S2P,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-40G-2S-2P"""


@typing.final
@revisions.register_valkyrie_module(rev="Odin-40G-2S-2P-B")
class MOdin40G2S2PB(ModuleL23):
    """Test module Odin-40G-2S-2P-B"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        self.ports: pm.PortsManager[ports.POdin40G2S2PB] = pm.PortsManager(
            conn=conn,
            ports_type=ports.POdin40G2S2PB,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """Port Index Manager of Odin-40G-2S-2P-B"""