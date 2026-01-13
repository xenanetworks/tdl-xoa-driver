import typing
import functools
from xoa_driver import ports
from xoa_driver.internals.hli import revisions
from xoa_driver.internals.commands import P_CAPABILITIES
from xoa_driver.internals.utils.managers import ports_manager as pm
from xoa_driver.internals.utils.cap_id import CapID

if typing.TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from .. import __interfaces as m_itf

from .module_l23_base import ModuleL23






