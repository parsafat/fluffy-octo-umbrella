from common.protocol import user_pb2 as _user_pb2
from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Account(_message.Message):
    __slots__ = ["password"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    password: str
    def __init__(self, password: _Optional[str] = ...) -> None: ...

class Fallback(_message.Message):
    __slots__ = ["name", "alpn", "path", "type", "dest", "xver"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALPN_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    XVER_FIELD_NUMBER: _ClassVar[int]
    name: str
    alpn: str
    path: str
    type: str
    dest: str
    xver: int
    def __init__(self, name: _Optional[str] = ..., alpn: _Optional[str] = ..., path: _Optional[str] = ..., type: _Optional[str] = ..., dest: _Optional[str] = ..., xver: _Optional[int] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["users", "fallbacks"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    FALLBACKS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    fallbacks: _containers.RepeatedCompositeFieldContainer[Fallback]
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., fallbacks: _Optional[_Iterable[_Union[Fallback, _Mapping]]] = ...) -> None: ...
