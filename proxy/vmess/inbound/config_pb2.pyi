from common.protocol import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DetourConfig(_message.Message):
    __slots__ = ["to"]
    TO_FIELD_NUMBER: _ClassVar[int]
    to: str
    def __init__(self, to: _Optional[str] = ...) -> None: ...

class DefaultConfig(_message.Message):
    __slots__ = ["level"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    level: int
    def __init__(self, level: _Optional[int] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["user", "default", "detour"]
    USER_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_FIELD_NUMBER: _ClassVar[int]
    DETOUR_FIELD_NUMBER: _ClassVar[int]
    user: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    default: DefaultConfig
    detour: DetourConfig
    def __init__(self, user: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., default: _Optional[_Union[DefaultConfig, _Mapping]] = ..., detour: _Optional[_Union[DetourConfig, _Mapping]] = ...) -> None: ...
