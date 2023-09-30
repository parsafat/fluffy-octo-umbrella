from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["id", "flow", "encryption"]
    ID_FIELD_NUMBER: _ClassVar[int]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_FIELD_NUMBER: _ClassVar[int]
    id: str
    flow: str
    encryption: str
    def __init__(self, id: _Optional[str] = ..., flow: _Optional[str] = ..., encryption: _Optional[str] = ...) -> None: ...
