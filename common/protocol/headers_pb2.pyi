from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SecurityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[SecurityType]
    AUTO: _ClassVar[SecurityType]
    AES128_GCM: _ClassVar[SecurityType]
    CHACHA20_POLY1305: _ClassVar[SecurityType]
    NONE: _ClassVar[SecurityType]
    ZERO: _ClassVar[SecurityType]
UNKNOWN: SecurityType
AUTO: SecurityType
AES128_GCM: SecurityType
CHACHA20_POLY1305: SecurityType
NONE: SecurityType
ZERO: SecurityType

class SecurityConfig(_message.Message):
    __slots__ = ["type"]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: SecurityType
    def __init__(self, type: _Optional[_Union[SecurityType, str]] = ...) -> None: ...
