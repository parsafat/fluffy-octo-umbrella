from common.net import address_pb2 as _address_pb2
from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    NO_AUTH: _ClassVar[AuthType]
    PASSWORD: _ClassVar[AuthType]

class Version(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    SOCKS5: _ClassVar[Version]
    SOCKS4: _ClassVar[Version]
    SOCKS4A: _ClassVar[Version]
NO_AUTH: AuthType
PASSWORD: AuthType
SOCKS5: Version
SOCKS4: Version
SOCKS4A: Version

class Account(_message.Message):
    __slots__ = ["username", "password"]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    username: str
    password: str
    def __init__(self, username: _Optional[str] = ..., password: _Optional[str] = ...) -> None: ...

class ServerConfig(_message.Message):
    __slots__ = ["auth_type", "accounts", "address", "udp_enabled", "timeout", "user_level"]
    class AccountsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    AUTH_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    UDP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    auth_type: AuthType
    accounts: _containers.ScalarMap[str, str]
    address: _address_pb2.IPOrDomain
    udp_enabled: bool
    timeout: int
    user_level: int
    def __init__(self, auth_type: _Optional[_Union[AuthType, str]] = ..., accounts: _Optional[_Mapping[str, str]] = ..., address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., udp_enabled: bool = ..., timeout: _Optional[int] = ..., user_level: _Optional[int] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["server", "version"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    server: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    version: Version
    def __init__(self, server: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ..., version: _Optional[_Union[Version, str]] = ...) -> None: ...
