from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Header(_message.Message):
    __slots__ = ["key", "value"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["path", "header", "accept_proxy_protocol", "ed"]
    PATH_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ED_FIELD_NUMBER: _ClassVar[int]
    path: str
    header: _containers.RepeatedCompositeFieldContainer[Header]
    accept_proxy_protocol: bool
    ed: int
    def __init__(self, path: _Optional[str] = ..., header: _Optional[_Iterable[_Union[Header, _Mapping]]] = ..., accept_proxy_protocol: bool = ..., ed: _Optional[int] = ...) -> None: ...
