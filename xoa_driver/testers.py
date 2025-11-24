#: All available tester types.

"""Xena chassis types."""

from .internals.hli.testers.l23_tester import L23Tester
from .internals.hli.testers.l23ve_tester import L23VeTester
from .internals.hli.testers.l47_tester import L47Tester
from .internals.hli.testers.l47ve_tester import L47VeTester

import typing

GenericAnyTester = typing.Union[
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
]
GenericAnyGenuineTester = typing.Union[
    "L23Tester",
    "L47Tester",
]
GenericAnyVirtualTester = typing.Union[
    "L23VeTester",
    "L47VeTester",
]

__all__ = (
    "L23Tester",
    "L23VeTester",
    "L47Tester",
    "L47VeTester",
    "GenericAnyTester",
    "GenericAnyGenuineTester",
    "GenericAnyVirtualTester",
)
