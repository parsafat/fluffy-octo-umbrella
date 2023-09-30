from common.serial import typed_message_pb2 as _typed_message_pb2
from common.protocol import headers_pb2 as _headers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["key", "security", "header"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    key: str
    security: _headers_pb2.SecurityConfig
    header: _typed_message_pb2.TypedMessage
    def __init__(self, key: _Optional[str] = ..., security: _Optional[_Union[_headers_pb2.SecurityConfig, _Mapping]] = ..., header: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...
