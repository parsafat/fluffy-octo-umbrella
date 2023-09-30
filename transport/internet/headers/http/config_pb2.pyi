from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Header(_message.Message):
    __slots__ = ["name", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Iterable[str]] = ...) -> None: ...

class Version(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class Method(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class RequestConfig(_message.Message):
    __slots__ = ["version", "method", "uri", "header"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    version: Version
    method: Method
    uri: _containers.RepeatedScalarFieldContainer[str]
    header: _containers.RepeatedCompositeFieldContainer[Header]
    def __init__(self, version: _Optional[_Union[Version, _Mapping]] = ..., method: _Optional[_Union[Method, _Mapping]] = ..., uri: _Optional[_Iterable[str]] = ..., header: _Optional[_Iterable[_Union[Header, _Mapping]]] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ["code", "reason"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: str
    reason: str
    def __init__(self, code: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class ResponseConfig(_message.Message):
    __slots__ = ["version", "status", "header"]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    version: Version
    status: Status
    header: _containers.RepeatedCompositeFieldContainer[Header]
    def __init__(self, version: _Optional[_Union[Version, _Mapping]] = ..., status: _Optional[_Union[Status, _Mapping]] = ..., header: _Optional[_Iterable[_Union[Header, _Mapping]]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["request", "response"]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    request: RequestConfig
    response: ResponseConfig
    def __init__(self, request: _Optional[_Union[RequestConfig, _Mapping]] = ..., response: _Optional[_Union[ResponseConfig, _Mapping]] = ...) -> None: ...
