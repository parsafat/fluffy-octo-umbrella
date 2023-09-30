from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PortRange(_message.Message):
    __slots__ = ["From", "To"]
    FROM_FIELD_NUMBER: _ClassVar[int]
    TO_FIELD_NUMBER: _ClassVar[int]
    From: int
    To: int
    def __init__(self, From: _Optional[int] = ..., To: _Optional[int] = ...) -> None: ...

class PortList(_message.Message):
    __slots__ = ["range"]
    RANGE_FIELD_NUMBER: _ClassVar[int]
    range: _containers.RepeatedCompositeFieldContainer[PortRange]
    def __init__(self, range: _Optional[_Iterable[_Union[PortRange, _Mapping]]] = ...) -> None: ...
