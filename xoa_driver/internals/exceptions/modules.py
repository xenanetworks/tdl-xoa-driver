from typing import Set


class WrongModuleError(Exception):
    """Module cannot be assigned to the connected tester object."""
    def __init__(self, module_revision: str, allowed_revisions: Set[str]) -> None:
        self.module_revision = module_revision
        self.allowed_revisions = allowed_revisions
        self.msg = (
            f"Module of revision <{self.module_revision}> detected.\n" 
            f"This module is not supported by the tester object in the current tdl-xoa-driver.\n"
            f"Supported module revisions are: {allowed_revisions}"
        )
        super().__init__(self.msg)
