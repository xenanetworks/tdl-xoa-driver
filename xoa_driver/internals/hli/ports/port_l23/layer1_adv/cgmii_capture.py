from dataclasses import dataclass
from typing import (
    TYPE_CHECKING,
)

from xoa_driver.internals.commands import (
    PL1_CGMII_CAPTURE_CONFIG,
    PL1_CGMII_CAPTURE_CONSUMED,
    PL1_CGMII_CAPTURE_DATA,
    PL1_CGMII_CAPTURE_MODE,
    PL1_CGMII_CAPTURE_QLEN,
    PL1_CGMII_CAPTURE_READ,
    PL1_CGMII_CAPTURE_STATE,
    PL1_CGMII_CAPTURE_SIZE,
)

from xoa_driver.internals.commands.enums import (
    L1CGMIICaptureTriggerType,
)

from xoa_driver.internals.commands.subtypes import (
    L1CGMIICodeword
)

if TYPE_CHECKING:
    from xoa_driver.internals.core import interfaces as itf


class L1CGMIICaptureConfigure:
    """Configuration of the Layer-1 CGMII Capture."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self.mode = PL1_CGMII_CAPTURE_MODE(conn, module_id, port_id)
        """Get/Set the current mode of the CGMII capture.

        :type: PL1_CGMII_CAPTURE_MODE
        """

        self.size = PL1_CGMII_CAPTURE_SIZE(conn, module_id, port_id)
        """Get/Set the size of the CGMII capture.

        :type: PL1_CGMII_CAPTURE_SIZE
        """

        self.state = PL1_CGMII_CAPTURE_STATE(conn, module_id, port_id)
        """Get/Set the current state of the CGMII capture.

        :type: PL1_CGMII_CAPTURE_STATE
        """

        self.config = PL1_CGMII_CAPTURE_CONFIG(conn, module_id, port_id)
        """Set the configuration of the CGMII capture.

        :type: PL1_CGMII_CAPTURE_CONFIG
        """


class L1CGMIICaptureObtain:
    """Obtaining captured data of the Layer-1 CGMII Capture."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:
        self._conn = conn
        self._module_id = module_id
        self._port_id = port_id

        self.read = PL1_CGMII_CAPTURE_READ(conn, module_id, port_id)
        """Get meta data of the oldest captured CGMII codewords.

        :type: PL1_CGMII_CAPTURE_READ
        """

        self.consumed = PL1_CGMII_CAPTURE_CONSUMED(conn, module_id, port_id)
        """Mark the oldest captured CGMII codewords as consumed.

        :type: PL1_CGMII_CAPTURE_CONSUMED
        """

        self.qlen = PL1_CGMII_CAPTURE_QLEN(conn, module_id, port_id)
        """Get the queue length of event logging.

        :type: PL1_CGMII_CAPTURE_QLEN
        """

    async def getdata(self, offset: int, count: int = 0) -> PL1_CGMII_CAPTURE_DATA.GetDataAttr:
        """Obtain the captured CGMII codewords starting from the given offset.

        :param offset: The offset from which to start reading the captured data.
        :type offset: int
        :param count: The number of captured CGMII codewords to obtain. If 0, obtain all available codewords.
        :type count: int
        :rtype: PL1_CGMII_CAPTURE_DATA.GetDataAttr
        """
        return await PL1_CGMII_CAPTURE_DATA(self._conn, self._module_id, self._port_id, offset, count).get()


@dataclass
class L1CGMIICaptureInfo:
    trtype: L1CGMIICaptureTriggerType
    timestamp: int
    trpos: int
    captured_data: list[L1CGMIICodeword]


class L1CGMIICapture:
    """Layer-1 CGMII Capture interface for the actual CGMII capture."""

    def __init__(self, conn: "itf.IConnection", module_id: int, port_id: int) -> None:

        self.config = L1CGMIICaptureConfigure(conn, module_id, port_id)
        """Set the configuration of the CGMII capture.

        :type: L1CGMIICaptureConfigure
        """

        self.obtain = L1CGMIICaptureObtain(conn, module_id, port_id)
        """Get the obtain interface for the oldest captured CGMII codewords.

        :type: L1CGMIICaptureObtain
        """

    async def getfullcapture(self) -> L1CGMIICaptureInfo:
        """Obtain the full captured CGMII codewords of the Layer-1 CGMII Capture.

        :rtype: L1CGMIICaptureInfo
        """
        metadata = await self.obtain.read.get()
        capinfo = L1CGMIICaptureInfo(
            trtype=metadata.triggertype,
            timestamp=metadata.timestamp,
            trpos=metadata.triggerpos,
            captured_data=[]
        )
        datasize = metadata.cgmii_data_size
        offset = 0
        while datasize > 0:
            r = await self.obtain.getdata(offset, count=0)
            cgmiiwords = r.cgmii_data
            chunksize = len(cgmiiwords)
            offset += chunksize
            datasize -= chunksize
            capinfo.captured_data.extend(cgmiiwords)
        await self.obtain.consumed.set()
        return capinfo

    def cgmii_codeword_str(self, cgmii_codeword: L1CGMIICodeword):
        """
        Generate a string representation of the 8 bytes in a CGMII codeword.
        """
        def ctrlsymbol(c):
            if c == 0x07:
                return "I"  # Idle
            if c == 0xFB:
                return "S"  # Start
            if c == 0xFD:
                return "T"  # Terminate
            if c == 0xFE:
                return "E"  # Error
            if c == 0x9C:
                return "Q"  # Sequence
            if c == 0x5C:
                return "C"  # UEC CtLOS
            return "K"      # Other control

        def datasymbol(b):
            if b == 0x55:
                return "P"  # preamble
            if b == 0xD5:
                return "F"  # SFD
            return "D"      # payload/data

        str = ''
        for i in range(8):
            b = (cgmii_codeword.data >> (8 * i)) & 0xFF
            c = (cgmii_codeword.ctrl >> i) & 0x1
            str += ctrlsymbol(b) if c else datasymbol(b)

        return str
