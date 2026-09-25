from typing import TYPE_CHECKING
from xoa_driver.internals.commands import (
    PS_UE_LLR_DESIRE,
    PS_UE_CBFC_VC,
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.utils import kind
    from xoa_driver.internals.utils.indices import observer as idx_obs


class SUecLlr:
    """UEC LLR configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.desire = PS_UE_LLR_DESIRE(conn, module_id, port_id, stream_idx)
        """Configures the desired LLR mode of the stream.

        :type: PS_UE_LLR_DESIRE
        """


class SUecCbfc:
    """UEC CBFC configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.vc = PS_UE_CBFC_VC(conn, module_id, port_id, stream_idx)
        """Configures the VC mapping of the stream.

        :type: PS_UE_CBFC_VC
        """
        

class SUec:
    """UEC configuration"""
    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int, stream_idx: int) -> None:
        self.llr = SUecLlr(conn, module_id, port_id, stream_idx)
        """UEC LLR configuration

        :type: SUecLlr
        """
        
        self.cbfc = SUecCbfc(conn, module_id, port_id, stream_idx)
        """UEC CBFC configuration

        :type: SUecCbfc
        """