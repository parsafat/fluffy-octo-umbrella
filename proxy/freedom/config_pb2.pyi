from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DestinationOverride(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _server_spec_pb2.ServerEndpoint
    def __init__(self, server: _Optional[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]] = ...) -> None: ...

class Fragment(_message.Message):
    __slots__ = ["packets_from", "packets_to", "length_min", "length_max", "interval_min", "interval_max"]
    PACKETS_FROM_FIELD_NUMBER: _ClassVar[int]
    PACKETS_TO_FIELD_NUMBER: _ClassVar[int]
    LENGTH_MIN_FIELD_NUMBER: _ClassVar[int]
    LENGTH_MAX_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_MIN_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_MAX_FIELD_NUMBER: _ClassVar[int]
    packets_from: int
    packets_to: int
    length_min: int
    length_max: int
    interval_min: int
    interval_max: int
    def __init__(self, packets_from: _Optional[int] = ..., packets_to: _Optional[int] = ..., length_min: _Optional[int] = ..., length_max: _Optional[int] = ..., interval_min: _Optional[int] = ..., interval_max: _Optional[int] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["domain_strategy", "timeout", "destination_override", "user_level", "fragment"]
    class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        AS_IS: _ClassVar[Config.DomainStrategy]
        USE_IP: _ClassVar[Config.DomainStrategy]
        USE_IP4: _ClassVar[Config.DomainStrategy]
        USE_IP6: _ClassVar[Config.DomainStrategy]
    AS_IS: Config.DomainStrategy
    USE_IP: Config.DomainStrategy
    USE_IP4: Config.DomainStrategy
    USE_IP6: Config.DomainStrategy
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    USER_LEVEL_FIELD_NUMBER: _ClassVar[int]
    FRAGMENT_FIELD_NUMBER: _ClassVar[int]
    domain_strategy: Config.DomainStrategy
    timeout: int
    destination_override: DestinationOverride
    user_level: int
    fragment: Fragment
    def __init__(self, domain_strategy: _Optional[_Union[Config.DomainStrategy, str]] = ..., timeout: _Optional[int] = ..., destination_override: _Optional[_Union[DestinationOverride, _Mapping]] = ..., user_level: _Optional[int] = ..., fragment: _Optional[_Union[Fragment, _Mapping]] = ...) -> None: ...
