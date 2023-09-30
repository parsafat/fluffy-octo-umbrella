from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class ChannelConfig(_message.Message):
    __slots__ = ["Blocking", "SubscriberLimit", "BufferSize"]
    BLOCKING_FIELD_NUMBER: _ClassVar[int]
    SUBSCRIBERLIMIT_FIELD_NUMBER: _ClassVar[int]
    BUFFERSIZE_FIELD_NUMBER: _ClassVar[int]
    Blocking: bool
    SubscriberLimit: int
    BufferSize: int
    def __init__(self, Blocking: bool = ..., SubscriberLimit: _Optional[int] = ..., BufferSize: _Optional[int] = ...) -> None: ...
