from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FakeDnsPool(_message.Message):
    __slots__ = ["ip_pool", "lruSize"]
    IP_POOL_FIELD_NUMBER: _ClassVar[int]
    LRUSIZE_FIELD_NUMBER: _ClassVar[int]
    ip_pool: str
    lruSize: int
    def __init__(self, ip_pool: _Optional[str] = ..., lruSize: _Optional[int] = ...) -> None: ...

class FakeDnsPoolMulti(_message.Message):
    __slots__ = ["pools"]
    POOLS_FIELD_NUMBER: _ClassVar[int]
    pools: _containers.RepeatedCompositeFieldContainer[FakeDnsPool]
    def __init__(self, pools: _Optional[_Iterable[_Union[FakeDnsPool, _Mapping]]] = ...) -> None: ...
