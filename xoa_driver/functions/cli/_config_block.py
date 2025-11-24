from xoa_driver import __version__, __name__
from typing import Union, List
from enum import Enum
from dataclasses import dataclass

class ConfigMetadataType(Enum):
    DEFAULT = "XENA"
    PORT = "XENAPORT"
    MODULE = "XENAMODULE"
    TESTCASE = "XENACASE"

@dataclass
class BaseConfigMetadata:
    type: ConfigMetadataType = ConfigMetadataType.DEFAULT
    formated_version: int = 3
    saved_by: str = __name__ + __version__

    def to_str(self) -> str:
        header_lines = [
            f";{self.type.value}",
            f";FormatVersion: {self.formated_version}",
            f";Savedby: {self.saved_by}",
        ]
        return "\n".join(header_lines)

# Module config metadata dataclass
@dataclass
class TestCaseMetadata(BaseConfigMetadata):
    type: ConfigMetadataType = ConfigMetadataType.TESTCASE
    testbed_name: str = "<testbed>"
    chassis_name: str = "<chassis_name>"
    chassis_sn: str = "<chassis_sn>"
    chassis_version_str: str = "<chassis_version_str>"
    module_name: str = "<module_name>"
    module_model: str = "<module_model>"
    module_sn: str = "<module_sn>"
    module_version_str: str = "<module_version_str>"
    module_revision: str = "<module_revision>"

    def to_str(self) -> str:
        header_lines = [
            f";{self.type.value}",
            f";FormatVersion: {super().formated_version}",
            f";Savedby: {super().saved_by}",
            f";Testbed: {self.testbed_name}",
        ]
        return "\n".join(header_lines)

# Module config metadata dataclass
@dataclass
class ModuleConfigMetadata(BaseConfigMetadata):
    type: ConfigMetadataType = ConfigMetadataType.MODULE
    testbed_name: str = "<testbed>"
    chassis_name: str = "<chassis_name>"
    chassis_sn: str = "<chassis_sn>"
    chassis_version_str: str = "<chassis_version_str>"
    module_name: str = "<module_name>"
    module_model: str = "<module_model>"
    module_sn: str = "<module_sn>"
    module_version_str: str = "<module_version_str>"
    module_revision: str = "<module_revision>"
    module_id: str = "<module_id>"

    def to_str(self) -> str:
        header_lines = [
            f";{self.type.value}",
            f";FormatVersion: {super().formated_version}",
            f";Savedby: {super().saved_by}",
            f";ChassisName: {self.chassis_name}",
            f";ChassisSerial: {self.chassis_sn}",
            f";ChassisVersion: {self.chassis_version_str}",
            f";ModuleName: {self.module_name}",
            f";ModuleModel: {self.module_model.replace('_', '')}",
            f";ModuleSerial: {self.module_sn}",
            f";ModuleVersion: {self.module_version_str}",
            f";ModuleRevision: {self.module_revision}",
            f";Module: {self.module_id}",
        ]
        return "\n".join(header_lines)
    
# Port config metadata dataclass
@dataclass
class PortConfigMetadata(BaseConfigMetadata):
    type = ConfigMetadataType.PORT
    testbed_name: str = "<testbed>"
    chassis_name: str = "<chassis_name>"
    chassis_sn: str = "<chassis_sn>"
    chassis_version_str: str = "<chassis_version_str>"
    module_name: str = "<module_name>"
    module_model: str = "<module_model>"
    module_sn: str = "<module_sn>"
    module_version_str: str = "<module_version_str>"
    module_revision: str = "<module_revision>"
    port_id: str = "<port_id>"

    def to_str(self) -> str:
        header_lines = [
            f";{self.type.value}",
            f";FormatVersion: {super().formated_version}",
            f";Savedby: {super().saved_by}",
            f";ChassisName: {self.chassis_name}",
            f";ChassisSerial: {self.chassis_sn}",
            f";ChassisVersion: {self.chassis_version_str}",
            f";ModuleName: {self.module_name}",
            f";ModuleModel: {self.module_model.replace('_', '')}",
            f";ModuleSerial: {self.module_sn}",
            f";ModuleVersion: {self.module_version_str}",
            f";ModuleRevision: {self.module_revision}",
            f";Port: {self.port_id}",
        ]
        return "\n".join(header_lines)

# Config block
class ConfigBlock:
    def __init__(self):
        self._config_block_str: str
        self._metadata: Union[TestCaseMetadata, PortConfigMetadata, ModuleConfigMetadata]
        self._commands: List[str] = []

    @property
    def type(self) -> ConfigMetadataType:
        return self._metadata.type

    @type.setter
    def type(self, v: ConfigMetadataType) -> None:
        if v == ConfigMetadataType.MODULE:
            self._metadata = ModuleConfigMetadata()
            self._metadata.type = v
        elif v == ConfigMetadataType.PORT:
            self._metadata = PortConfigMetadata()
            self._metadata.type = v
        elif v == ConfigMetadataType.TESTCASE:
            self._metadata = TestCaseMetadata()
            self._metadata.type = v
        else:
            raise ValueError("Invalid config type")

    @property
    def config_block_str(self) -> str:
        header_str = self._metadata.to_str()
        if len(self._commands) == 0:
            return header_str
        else:
            commands_str = "\n".join(self._commands)
            return header_str + "\n" + commands_str
    
    @config_block_str.setter
    def config_block_str(self, v: str) -> None:
        self._config_block_str = v

        metadata_list = []
        line_list = self._config_block_str.splitlines()
        
        for line in line_list:
            if line.startswith(';'):
                metadata_list.append(line)
            else:
                self._commands.append(line)

        if line_list[0].startswith(f";{ConfigMetadataType.MODULE.value}"):
            self._metadata = ModuleConfigMetadata()
            for line in metadata_list:
                if line.startswith(f";ChassisName:"):
                    self._metadata.chassis_name = line.split(" ")[1].strip()
                elif line.startswith(f";ChassisSerial:"):
                    self._metadata.chassis_sn = line.split(" ")[1].strip()
                elif line.startswith(f";ChassisVersion:"):
                    self._metadata.chassis_version_str = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleName:"):
                    self._metadata.module_name = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleModel:"):
                    self._metadata.module_model = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleSerial:"):
                    self._metadata.module_sn = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleVersion:"):
                    self._metadata.module_version_str = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleRevision:"):
                    self._metadata.module_revision = line.split(" ")[1].strip()
                elif line.startswith(f";Module:"):
                    self._metadata.module_id = line.split(" ")[1].strip()

        if line_list[0].startswith(f";{ConfigMetadataType.PORT.value}"):
            self._metadata = PortConfigMetadata()
            for line in metadata_list:
                if line.startswith(f";ChassisName:"):
                    self._metadata.chassis_name = line.split(" ")[1].strip()
                elif line.startswith(f";ChassisSerial:"):
                    self._metadata.chassis_sn = line.split(" ")[1].strip()
                elif line.startswith(f";ChassisVersion:"):
                    self._metadata.chassis_version_str = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleName:"):
                    self._metadata.module_name = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleModel:"):
                    self._metadata.module_model = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleSerial:"):
                    self._metadata.module_sn = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleVersion:"):
                    self._metadata.module_version_str = line.split(" ")[1].strip()
                elif line.startswith(f";ModuleRevision:"):
                    self._metadata.module_revision = line.split(" ")[1].strip()
                elif line.startswith(f";Port:"):
                    self._metadata.port_id = line.split(" ")[1].strip()

    @property
    def testbed_name(self) -> str:
        return self._metadata.testbed_name
    
    @testbed_name.setter
    def testbed_name(self, v: str) -> None:
        self._metadata.testbed_name = v
    
    @property
    def chassis_name(self) -> str:
        return self._metadata.chassis_name
    
    @chassis_name.setter
    def chassis_name(self, v: str) -> None:
        self._metadata.chassis_name = v
    
    @property
    def chassis_sn(self) -> str:
        return self._metadata.chassis_sn
    
    @chassis_sn.setter
    def chassis_sn(self, v: str) -> None:
        self._metadata.chassis_sn = v

    @property
    def chassis_version_str(self) -> str:
        return self._metadata.chassis_version_str
    
    @chassis_version_str.setter
    def chassis_version_str(self, v: str) -> None:
        self._metadata.chassis_version_str = v

    @property
    def module_name(self) -> str:
        return self._metadata.module_name

    @module_name.setter
    def module_name(self, v: str) -> None:
        self._metadata.module_name = v

    @property
    def module_model(self) -> str:
        return self._metadata.module_model
    
    @module_model.setter
    def module_model(self, v: str) -> None:
        self._metadata.module_model = v

    @property
    def module_sn(self) -> str:
        return self._metadata.module_sn
    
    @module_sn.setter
    def module_sn(self, v: str) -> None:
        self._metadata.module_sn = v

    @property
    def module_version_str(self) -> str:
        return self._metadata.module_version_str
    
    @module_version_str.setter
    def module_version_str(self, v: str) -> None:
        self._metadata.module_version_str = v

    @property
    def module_revision(self) -> str:
        return self._metadata.module_revision

    @module_revision.setter
    def module_revision(self, v: str) -> None:
        self._metadata.module_revision = v

    @property
    def module_id(self) -> str:
        if isinstance(self._metadata, ModuleConfigMetadata):
            return self._metadata.module_id
        return ""
    
    @module_id.setter
    def module_id(self, v: str) -> None:
        if isinstance(self._metadata, ModuleConfigMetadata):
            self._metadata.module_id = v
        else:
            raise AttributeError("module_id is only available for ModuleConfigMetadata")

    @property
    def port_id(self) -> str:
        if isinstance(self._metadata, PortConfigMetadata):
            return self._metadata.port_id
        return ""
    
    @port_id.setter
    def port_id(self, v: str) -> None:
        if isinstance(self._metadata, PortConfigMetadata):
            self._metadata.port_id = v
        else:
            raise AttributeError("port_id is only available for PortConfigMetadata")

    @property
    def metadata(self) -> Union[TestCaseMetadata, PortConfigMetadata, ModuleConfigMetadata]:
        return self._metadata

    @property
    def commands(self) -> List[str]:
        return self._commands

    @commands.setter
    def commands(self, v: str) -> None:
        # Remove the <SYNC> tag
        v = v.replace('<SYNC>', '')

        if self.type == ConfigMetadataType.PORT:
            v = v.replace(f"{self.port_id}  ", '')
            v = f"P_RESET\n" + v

        if self.type == ConfigMetadataType.MODULE:
            v = v.replace(f"{self.module_id}  ", '')

        self._commands = v.splitlines()

# Determine type of config block
def config_block_type(config_block_str: str) -> ConfigMetadataType:
    line_list = config_block_str.splitlines()
    if line_list[0].startswith(f";{ConfigMetadataType.MODULE.value}"):
        return ConfigMetadataType.MODULE
    elif line_list[0].startswith(f";{ConfigMetadataType.PORT.value}"):
        return ConfigMetadataType.PORT
    elif line_list[0].startswith(f";{ConfigMetadataType.TESTCASE.value}"):
        return ConfigMetadataType.TESTCASE
    else:
        return ConfigMetadataType.DEFAULT