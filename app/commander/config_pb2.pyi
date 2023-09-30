from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["tag", "service"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    SERVICE_FIELD_NUMBER: _ClassVar[int]
    tag: str
    service: _containers.RepeatedCompositeFieldContainer[_typed_message_pb2.TypedMessage]
    def __init__(self, tag: _Optional[str] = ..., service: _Optional[_Iterable[_Union[_typed_message_pb2.TypedMessage, _Mapping]]] = ...) -> None: ...

class ReflectionConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
