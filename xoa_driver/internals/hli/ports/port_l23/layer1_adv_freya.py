from typing import (
    TYPE_CHECKING,
    Tuple,
)
if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf
    from xoa_driver.internals.hli.ports.port_l23.family_freya import FamilyFreya

from .layer1_adv.deg_ser import *
from .layer1_adv.err_cw import *
from .layer1_adv.err_stats import *
from .layer1_adv.freq import *
from .layer1_adv.hi_ber import *
from .layer1_adv.hi_ser import *
from .layer1_adv.itb import *



class Layer1Adv:
    def __init__(self, conn: "itf.IConnection", port: "FamilyFreya") -> None:
        module_id, port_id = port.kind

        self.lane: Tuple["PcsLaneAdv", ...] = tuple(
            PcsLaneAdv(conn, module_id, port_id, lane_idx=idx)
            for idx in range(port.info.capabilities.lane_count)
        )  # TODO: need to fix, currently port.info.capabilities must be none because lanes are created before awaiting the port
        """PCS Lane
        
        :type: Tuple[PcsLane, ...]
        """

        self.err_stats = ErrStats(conn, module_id, port_id)
        """Port PCS Error Statistics

        :type: ErrStats
        """

        self.degraded_ser = DegradedSer(conn, module_id, port_id)
        """Degraded Symbol Error Rate (SER) Management

        :type: DegradedSer
        """

        self.err_cw = ErrorCodeword(conn, module_id, port_id)
        """Erroneous Codeword (CW) Management

        :type: ErrorCodeword
        """

        self.freq = FrequencyAdv(conn, module_id, port_id)
        """Frequency Management

        :type: FrequencyAdv
        """

        self.hi_ber = HighBer(conn, module_id, port_id)
        """High Bit Error Rate (BER)

        :type: HighBer
        """

        self.hi_ser = HighSer(conn, module_id, port_id)
        """High Symbol Error Rate (SER)

        :type: HighSer
        """

        self.itb = InvalidTranscodeBlock(conn, module_id, port_id)
        """Invalid Transcode Block (ITB) Management

        :type: InvalidTranscodeBlock
        """



        