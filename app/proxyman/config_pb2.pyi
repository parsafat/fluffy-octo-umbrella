from common.net import address_pb2 as _address_pb2
from common.net import port_pb2 as _port_pb2
from transport.internet import config_pb2 as _config_pb2
from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class KnownProtocols(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    HTTP: _ClassVar[KnownProtocols]
    TLS: _ClassVar[KnownProtocols]
HTTP: KnownProtocols
TLS: KnownProtocols

class InboundConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AllocationStrategy(_message.Message):
    __slots__ = ["type", "concurrency", "refresh"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Always: _ClassVar[AllocationStrategy.Type]
        Random: _ClassVar[AllocationStrategy.Type]
        External: _ClassVar[AllocationStrategy.Type]
    Always: AllocationStrategy.Type
    Random: AllocationStrategy.Type
    External: AllocationStrategy.Type
    class AllocationStrategyConcurrency(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    class AllocationStrategyRefresh(_message.Message):
        __slots__ = ["value"]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: int
        def __init__(self, value: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    REFRESH_FIELD_NUMBER: _ClassVar[int]
    type: AllocationStrategy.Type
    concurrency: AllocationStrategy.AllocationStrategyConcurrency
    refresh: AllocationStrategy.AllocationStrategyRefresh
    def __init__(self, type: _Optional[_Union[AllocationStrategy.Type, str]] = ..., concurrency: _Optional[_Union[AllocationStrategy.AllocationStrategyConcurrency, _Mapping]] = ..., refresh: _Optional[_Union[AllocationStrategy.AllocationStrategyRefresh, _Mapping]] = ...) -> None: ...

class SniffingConfig(_message.Message):
    __slots__ = ["enabled", "destination_override", "domains_excluded", "metadata_only", "route_only"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    DOMAINS_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
    METADATA_ONLY_FIELD_NUMBER: _ClassVar[int]
    ROUTE_ONLY_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    destination_override: _containers.RepeatedScalarFieldContainer[str]
    domains_excluded: _containers.RepeatedScalarFieldContainer[str]
    metadata_only: bool
    route_only: bool
    def __init__(self, enabled: bool = ..., destination_override: _Optional[_Iterable[str]] = ..., domains_excluded: _Optional[_Iterable[str]] = ..., metadata_only: bool = ..., route_only: bool = ...) -> None: ...

class ReceiverConfig(_message.Message):
    __slots__ = ["port_list", "listen", "allocation_strategy", "stream_settings", "receive_original_destination", "domain_override", "sniffing_settings"]
    PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    LISTEN_FIELD_NUMBER: _ClassVar[int]
    ALLOCATION_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_ORIGINAL_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SNIFFING_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    port_list: _port_pb2.PortList
    listen: _address_pb2.IPOrDomain
    allocation_strategy: AllocationStrategy
    stream_settings: _config_pb2.StreamConfig
    receive_original_destination: bool
    domain_override: _containers.RepeatedScalarFieldContainer[KnownProtocols]
    sniffing_settings: SniffingConfig
    def __init__(self, port_list: _Optional[_Union[_port_pb2.PortList, _Mapping]] = ..., listen: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., allocation_strategy: _Optional[_Union[AllocationStrategy, _Mapping]] = ..., stream_settings: _Optional[_Union[_config_pb2.StreamConfig, _Mapping]] = ..., receive_original_destination: bool = ..., domain_override: _Optional[_Iterable[_Union[KnownProtocols, str]]] = ..., sniffing_settings: _Optional[_Union[SniffingConfig, _Mapping]] = ...) -> None: ...

class InboundHandlerConfig(_message.Message):
    __slots__ = ["tag", "receiver_settings", "proxy_settings"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    RECEIVER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    tag: str
    receiver_settings: _typed_message_pb2.TypedMessage
    proxy_settings: _typed_message_pb2.TypedMessage
    def __init__(self, tag: _Optional[str] = ..., receiver_settings: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ..., proxy_settings: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...

class OutboundConfig(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class SenderConfig(_message.Message):
    __slots__ = ["via", "stream_settings", "proxy_settings", "multiplex_settings"]
    VIA_FIELD_NUMBER: _ClassVar[int]
    STREAM_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PROXY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MULTIPLEX_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    via: _address_pb2.IPOrDomain
    stream_settings: _config_pb2.StreamConfig
    proxy_settings: _config_pb2.ProxyConfig
    multiplex_settings: MultiplexingConfig
    def __init__(self, via: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., stream_settings: _Optional[_Union[_config_pb2.StreamConfig, _Mapping]] = ..., proxy_settings: _Optional[_Union[_config_pb2.ProxyConfig, _Mapping]] = ..., multiplex_settings: _Optional[_Union[MultiplexingConfig, _Mapping]] = ...) -> None: ...

class MultiplexingConfig(_message.Message):
    __slots__ = ["enabled", "concurrency", "xudpConcurrency", "xudpProxyUDP443"]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    XUDPCONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    XUDPPROXYUDP443_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    concurrency: int
    xudpConcurrency: int
    xudpProxyUDP443: str
    def __init__(self, enabled: bool = ..., concurrency: _Optional[int] = ..., xudpConcurrency: _Optional[int] = ..., xudpProxyUDP443: _Optional[str] = ...) -> None: ...
