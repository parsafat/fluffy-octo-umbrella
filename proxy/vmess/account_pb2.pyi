from common.protocol import headers_pb2 as _headers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["id", "security_settings", "tests_enabled"]
    ID_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    TESTS_ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: str
    security_settings: _headers_pb2.SecurityConfig
    tests_enabled: str
    def __init__(self, id: _Optional[str] = ..., security_settings: _Optional[_Union[_headers_pb2.SecurityConfig, _Mapping]] = ..., tests_enabled: _Optional[str] = ...) -> None: ...
