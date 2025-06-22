import typing
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.utils.managers import ports_manager as pm

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    import __interfaces as m_itf
from .l47_base import ModuleL47Base

@revisions.register_vulcan_module(rev="Xena L47 Module")
class ModuleL47(ModuleL47Base):
    """Test module Xena L47 Module"""
    def __init__(self, conn: "itf.IConnection", init_data: "m_itf.ModuleInitData") -> None:
        super().__init__(conn, init_data)
        """Port Index Manager of Xena L47 Module"""