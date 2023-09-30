from common.net import network_pb2 as _network_pb2
from common.net import address_pb2 as _address_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ServerConfig(_message.Message):
    __slots__ = ["method", "key", "email", "level", "network"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    method: str
    key: str
    email: str
    level: int
    network: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    def __init__(self, method: _Optional[str] = ..., key: _Optional[str] = ..., email: _Optional[str] = ..., level: _Optional[int] = ..., network: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ...) -> None: ...

class MultiUserServerConfig(_message.Message):
    __slots__ = ["method", "key", "users", "network"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    method: str
    key: str
    users: _containers.RepeatedCompositeFieldContainer[User]
    network: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    def __init__(self, method: _Optional[str] = ..., key: _Optional[str] = ..., users: _Optional[_Iterable[_Union[User, _Mapping]]] = ..., network: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ...) -> None: ...

class RelayDestination(_message.Message):
    __slots__ = ["key", "address", "port", "email", "level"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    key: str
    address: _address_pb2.IPOrDomain
    port: int
    email: str
    level: int
    def __init__(self, key: _Optional[str] = ..., address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., email: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...

class RelayServerConfig(_message.Message):
    __slots__ = ["method", "key", "destinations", "network"]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    method: str
    key: str
    destinations: _containers.RepeatedCompositeFieldContainer[RelayDestination]
    network: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    def __init__(self, method: _Optional[str] = ..., key: _Optional[str] = ..., destinations: _Optional[_Iterable[_Union[RelayDestination, _Mapping]]] = ..., network: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["key", "email", "level"]
    KEY_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    key: str
    email: str
    level: int
    def __init__(self, key: _Optional[str] = ..., email: _Optional[str] = ..., level: _Optional[int] = ...) -> None: ...

class ClientConfig(_message.Message):
    __slots__ = ["address", "port", "method", "key", "udp_over_tcp", "udp_over_tcp_version"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    UDP_OVER_TCP_FIELD_NUMBER: _ClassVar[int]
    UDP_OVER_TCP_VERSION_FIELD_NUMBER: _ClassVar[int]
    address: _address_pb2.IPOrDomain
    port: int
    method: str
    key: str
    udp_over_tcp: bool
    udp_over_tcp_version: int
    def __init__(self, address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ..., method: _Optional[str] = ..., key: _Optional[str] = ..., udp_over_tcp: bool = ..., udp_over_tcp_version: _Optional[int] = ...) -> None: ...
