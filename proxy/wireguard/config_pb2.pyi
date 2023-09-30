from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PeerConfig(_message.Message):
    __slots__ = ["public_key", "pre_shared_key", "endpoint", "keep_alive", "allowed_ips"]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    PRE_SHARED_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    KEEP_ALIVE_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_IPS_FIELD_NUMBER: _ClassVar[int]
    public_key: str
    pre_shared_key: str
    endpoint: str
    keep_alive: int
    allowed_ips: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, public_key: _Optional[str] = ..., pre_shared_key: _Optional[str] = ..., endpoint: _Optional[str] = ..., keep_alive: _Optional[int] = ..., allowed_ips: _Optional[_Iterable[str]] = ...) -> None: ...

class DeviceConfig(_message.Message):
    __slots__ = ["secret_key", "endpoint", "peers", "mtu", "num_workers", "reserved"]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PEERS_FIELD_NUMBER: _ClassVar[int]
    MTU_FIELD_NUMBER: _ClassVar[int]
    NUM_WORKERS_FIELD_NUMBER: _ClassVar[int]
    RESERVED_FIELD_NUMBER: _ClassVar[int]
    secret_key: str
    endpoint: _containers.RepeatedScalarFieldContainer[str]
    peers: _containers.RepeatedCompositeFieldContainer[PeerConfig]
    mtu: int
    num_workers: int
    reserved: bytes
    def __init__(self, secret_key: _Optional[str] = ..., endpoint: _Optional[_Iterable[str]] = ..., peers: _Optional[_Iterable[_Union[PeerConfig, _Mapping]]] = ..., mtu: _Optional[int] = ..., num_workers: _Optional[int] = ..., reserved: _Optional[bytes] = ...) -> None: ...
