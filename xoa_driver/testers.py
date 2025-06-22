#: All available tester types.
import sys

if "xoa_driver.v2" in sys.modules:
    raise ImportError("\33[31mOnly Single interface version is allowed to being use at the same time.\33[0m")

from .internals.hli_v1.testers.l23_tester import L23Tester
from .internals.hli_v1.testers.l47_tester import L47Tester

import typing

GenericTesterAny = typing.Union[
    "L23Tester",
    "L47Tester",
]

__all__ = (
    "L23Tester",
    "L47Tester",
    "GenericTesterAny",
)
