from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["inbound_tag"]
    INBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    inbound_tag: str
    def __init__(self, inbound_tag: _Optional[str] = ...) -> None: ...
