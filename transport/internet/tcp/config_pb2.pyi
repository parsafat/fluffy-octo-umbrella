from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["header_settings", "accept_proxy_protocol"]
    HEADER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    header_settings: _typed_message_pb2.TypedMessage
    accept_proxy_protocol: bool
    def __init__(self, header_settings: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ..., accept_proxy_protocol: bool = ...) -> None: ...
