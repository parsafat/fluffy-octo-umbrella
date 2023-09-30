from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    Unknown: _ClassVar[Severity]
    Error: _ClassVar[Severity]
    Warning: _ClassVar[Severity]
    Info: _ClassVar[Severity]
    Debug: _ClassVar[Severity]
Unknown: Severity
Error: Severity
Warning: Severity
Info: Severity
Debug: Severity
