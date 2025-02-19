import sys


if "tdl_xoa_driver.internals.hli_v1" in sys.modules:
    raise ImportError("\33[101mUsing tdl_xoa_driver and tdl_xoa_driver.v2 at the same time is not allowed.\33[0m")

from tdl_xoa_driver.internals import warn

warn.resource(
    "tdl_xoa_driver.v2 is under development and it subject to changes without notice.",
)
