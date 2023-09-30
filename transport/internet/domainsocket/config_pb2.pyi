from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["path", "abstract", "padding"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ABSTRACT_FIELD_NUMBER: _ClassVar[int]
    PADDING_FIELD_NUMBER: _ClassVar[int]
    path: str
    abstract: bool
    padding: bool
    def __init__(self, path: _Optional[str] = ..., abstract: bool = ..., padding: bool = ...) -> None: ...
