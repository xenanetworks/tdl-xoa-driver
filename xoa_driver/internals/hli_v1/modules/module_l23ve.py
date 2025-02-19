import asyncio
import typing
from typing_extensions import Self
from xoa_driver.internals.commands import (
    M_COMMENT,
    M_CAPABILITIES,
    M_MULTIUSER
)
from xoa_driver import ports
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.state_storage import modules_state
from . import base_module as bm
if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from . import __interfaces as m_itf


class ModuleL23VE(bm.BaseModule["modules_state.ModuleLocalState"]):
    """
    This is a conceptual class of L23 test module on ValkyrieVE tester.
    """

    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)

        self._local_states = modules_state.ModuleLocalState()

        self.comment = M_COMMENT(conn, self.module_id)
        """Test module's description.

        :type: M_COMMENT
        """

        self.capabilities = M_CAPABILITIES(conn, self.module_id)
        """Test module's capabilities.

        :type: M_CAPABILITIES
        """

        self.multiuser = M_MULTIUSER(conn, self.module_id)
        """If multiple users are allowed to control the same test module.

        :type: M_MULTIUSER
        """

        self.ports: pm.PortsManager[ports.PortL23VE] = pm.PortsManager(
            conn=conn,
            ports_type=ports.PortL23VE,
            module_id=self.module_id,
            ports_count=self.ports_count
        )
        """L23 VE Port index manager of this test module.

        :type: PortsManager
        """

    @property
    def info(self) -> modules_state.ModuleLocalState:
        """Return the module's local state

        :return: the module's local state
        :rtype: ModuleLocalState
        """

        return self._local_states

    async def _setup(self) -> Self:
        await asyncio.gather(
            self._local_states.initiate(self),
            self.ports.fill()
        )
        self._local_states.register_subscriptions(self)
        return self
