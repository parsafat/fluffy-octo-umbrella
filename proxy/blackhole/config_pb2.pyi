from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NoneResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class HTTPResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Config(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: _typed_message_pb2.TypedMessage
    def __init__(self, response: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...
