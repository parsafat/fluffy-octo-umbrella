from common.net import network_pb2 as _network_pb2
from common.protocol import user_pb2 as _user_pb2
from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CipherType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    UNKNOWN: _ClassVar[CipherType]
    AES_128_GCM: _ClassVar[CipherType]
    AES_256_GCM: _ClassVar[CipherType]
    CHACHA20_POLY1305: _ClassVar[CipherType]
    XCHACHA20_POLY1305: _ClassVar[CipherType]
    NONE: _ClassVar[CipherType]
UNKNOWN: CipherType
AES_128_GCM: CipherType
AES_256_GCM: CipherType
CHACHA20_POLY1305: CipherType
XCHACHA20_POLY1305: CipherType
NONE: CipherType

class Account(_message.Message):
    __slots__ = ["password", "cipher_type", "iv_check"]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    CIPHER_TYPE_FIELD_NUMBER: _ClassVar[int]
    IV_CHECK_FIELD_NUMBER: _ClassVar[int]
    password: str
    cipher_type: CipherType
    iv_check: bool
    def __init__(self, password: _Optional[str] = ..., cipher_type: _Optional[_Union[CipherType, str]] = ..., iv_check: bool = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["users", "network"]
    USERS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_user_pb2.User]
    network: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    def __init__(self, users: _Optional[_Iterable[_Union[_user_pb2.User, _Mapping]]] = ..., network: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...
