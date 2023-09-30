from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SessionConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Config(_message.Message):
    __slots__ = ["settings"]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    settings: SessionConfig
    def __init__(self, settings: _Optional[_Union[SessionConfig, _Mapping]] = ...) -> None: ...
