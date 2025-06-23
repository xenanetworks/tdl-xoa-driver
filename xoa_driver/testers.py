#: All available tester types.

from .internals.hli.testers.l23_tester import L23Tester
from .internals.hli.testers.l47_tester import L47Tester

import typing

GenericTesterAny = typing.Union[
    L23Tester,
    L47Tester,
]

__all__ = (
    "L23Tester",
    "L47Tester",
    "GenericTesterAny",
)
