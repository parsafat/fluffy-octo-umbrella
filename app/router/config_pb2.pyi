from common.net import port_pb2 as _port_pb2
from common.net import network_pb2 as _network_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Domain(_message.Message):
    __slots__ = ["type", "value", "attribute"]
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Plain: _ClassVar[Domain.Type]
        Regex: _ClassVar[Domain.Type]
        Domain: _ClassVar[Domain.Type]
        Full: _ClassVar[Domain.Type]
    Plain: Domain.Type
    Regex: Domain.Type
    Domain: Domain.Type
    Full: Domain.Type
    class Attribute(_message.Message):
        __slots__ = ["key", "bool_value", "int_value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
        INT_VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        bool_value: bool
        int_value: int
        def __init__(self, key: _Optional[str] = ..., bool_value: bool = ..., int_value: _Optional[int] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    type: Domain.Type
    value: str
    attribute: _containers.RepeatedCompositeFieldContainer[Domain.Attribute]
    def __init__(self, type: _Optional[_Union[Domain.Type, str]] = ..., value: _Optional[str] = ..., attribute: _Optional[_Iterable[_Union[Domain.Attribute, _Mapping]]] = ...) -> None: ...

class CIDR(_message.Message):
    __slots__ = ["ip", "prefix"]
    IP_FIELD_NUMBER: _ClassVar[int]
    PREFIX_FIELD_NUMBER: _ClassVar[int]
    ip: bytes
    prefix: int
    def __init__(self, ip: _Optional[bytes] = ..., prefix: _Optional[int] = ...) -> None: ...

class GeoIP(_message.Message):
    __slots__ = ["country_code", "cidr", "reverse_match"]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    REVERSE_MATCH_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    cidr: _containers.RepeatedCompositeFieldContainer[CIDR]
    reverse_match: bool
    def __init__(self, country_code: _Optional[str] = ..., cidr: _Optional[_Iterable[_Union[CIDR, _Mapping]]] = ..., reverse_match: bool = ...) -> None: ...

class GeoIPList(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[GeoIP]
    def __init__(self, entry: _Optional[_Iterable[_Union[GeoIP, _Mapping]]] = ...) -> None: ...

class GeoSite(_message.Message):
    __slots__ = ["country_code", "domain"]
    COUNTRY_CODE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    country_code: str
    domain: _containers.RepeatedCompositeFieldContainer[Domain]
    def __init__(self, country_code: _Optional[str] = ..., domain: _Optional[_Iterable[_Union[Domain, _Mapping]]] = ...) -> None: ...

class GeoSiteList(_message.Message):
    __slots__ = ["entry"]
    ENTRY_FIELD_NUMBER: _ClassVar[int]
    entry: _containers.RepeatedCompositeFieldContainer[GeoSite]
    def __init__(self, entry: _Optional[_Iterable[_Union[GeoSite, _Mapping]]] = ...) -> None: ...

class RoutingRule(_message.Message):
    __slots__ = ["tag", "balancing_tag", "domain", "cidr", "geoip", "port_range", "port_list", "network_list", "networks", "source_cidr", "source_geoip", "source_port_list", "user_email", "inbound_tag", "protocol", "attributes", "domain_matcher"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TAG_FIELD_NUMBER: _ClassVar[int]
    BALANCING_TAG_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CIDR_FIELD_NUMBER: _ClassVar[int]
    GEOIP_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGE_FIELD_NUMBER: _ClassVar[int]
    PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LIST_FIELD_NUMBER: _ClassVar[int]
    NETWORKS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CIDR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_GEOIP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PORT_LIST_FIELD_NUMBER: _ClassVar[int]
    USER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    INBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_MATCHER_FIELD_NUMBER: _ClassVar[int]
    tag: str
    balancing_tag: str
    domain: _containers.RepeatedCompositeFieldContainer[Domain]
    cidr: _containers.RepeatedCompositeFieldContainer[CIDR]
    geoip: _containers.RepeatedCompositeFieldContainer[GeoIP]
    port_range: _port_pb2.PortRange
    port_list: _port_pb2.PortList
    network_list: _network_pb2.NetworkList
    networks: _containers.RepeatedScalarFieldContainer[_network_pb2.Network]
    source_cidr: _containers.RepeatedCompositeFieldContainer[CIDR]
    source_geoip: _containers.RepeatedCompositeFieldContainer[GeoIP]
    source_port_list: _port_pb2.PortList
    user_email: _containers.RepeatedScalarFieldContainer[str]
    inbound_tag: _containers.RepeatedScalarFieldContainer[str]
    protocol: _containers.RepeatedScalarFieldContainer[str]
    attributes: _containers.ScalarMap[str, str]
    domain_matcher: str
    def __init__(self, tag: _Optional[str] = ..., balancing_tag: _Optional[str] = ..., domain: _Optional[_Iterable[_Union[Domain, _Mapping]]] = ..., cidr: _Optional[_Iterable[_Union[CIDR, _Mapping]]] = ..., geoip: _Optional[_Iterable[_Union[GeoIP, _Mapping]]] = ..., port_range: _Optional[_Union[_port_pb2.PortRange, _Mapping]] = ..., port_list: _Optional[_Union[_port_pb2.PortList, _Mapping]] = ..., network_list: _Optional[_Union[_network_pb2.NetworkList, _Mapping]] = ..., networks: _Optional[_Iterable[_Union[_network_pb2.Network, str]]] = ..., source_cidr: _Optional[_Iterable[_Union[CIDR, _Mapping]]] = ..., source_geoip: _Optional[_Iterable[_Union[GeoIP, _Mapping]]] = ..., source_port_list: _Optional[_Union[_port_pb2.PortList, _Mapping]] = ..., user_email: _Optional[_Iterable[str]] = ..., inbound_tag: _Optional[_Iterable[str]] = ..., protocol: _Optional[_Iterable[str]] = ..., attributes: _Optional[_Mapping[str, str]] = ..., domain_matcher: _Optional[str] = ...) -> None: ...

class BalancingRule(_message.Message):
    __slots__ = ["tag", "outbound_selector", "strategy"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    tag: str
    outbound_selector: _containers.RepeatedScalarFieldContainer[str]
    strategy: str
    def __init__(self, tag: _Optional[str] = ..., outbound_selector: _Optional[_Iterable[str]] = ..., strategy: _Optional[str] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["domain_strategy", "rule", "balancing_rule"]
    class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        AsIs: _ClassVar[Config.DomainStrategy]
        UseIp: _ClassVar[Config.DomainStrategy]
        IpIfNonMatch: _ClassVar[Config.DomainStrategy]
        IpOnDemand: _ClassVar[Config.DomainStrategy]
    AsIs: Config.DomainStrategy
    UseIp: Config.DomainStrategy
    IpIfNonMatch: Config.DomainStrategy
    IpOnDemand: Config.DomainStrategy
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    RULE_FIELD_NUMBER: _ClassVar[int]
    BALANCING_RULE_FIELD_NUMBER: _ClassVar[int]
    domain_strategy: Config.DomainStrategy
    rule: _containers.RepeatedCompositeFieldContainer[RoutingRule]
    balancing_rule: _containers.RepeatedCompositeFieldContainer[BalancingRule]
    def __init__(self, domain_strategy: _Optional[_Union[Config.DomainStrategy, str]] = ..., rule: _Optional[_Iterable[_Union[RoutingRule, _Mapping]]] = ..., balancing_rule: _Optional[_Iterable[_Union[BalancingRule, _Mapping]]] = ...) -> None: ...
