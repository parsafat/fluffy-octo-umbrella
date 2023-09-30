from common.net import network_pb2 as _network_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RoutingContext(_message.Message):
    __slots__ = ["InboundTag", "Network", "SourceIPs", "TargetIPs", "SourcePort", "TargetPort", "TargetDomain", "Protocol", "User", "Attributes", "OutboundGroupTags", "OutboundTag"]
    class AttributesEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    INBOUNDTAG_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    SOURCEIPS_FIELD_NUMBER: _ClassVar[int]
    TARGETIPS_FIELD_NUMBER: _ClassVar[int]
    SOURCEPORT_FIELD_NUMBER: _ClassVar[int]
    TARGETPORT_FIELD_NUMBER: _ClassVar[int]
    TARGETDOMAIN_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDGROUPTAGS_FIELD_NUMBER: _ClassVar[int]
    OUTBOUNDTAG_FIELD_NUMBER: _ClassVar[int]
    InboundTag: str
    Network: _network_pb2.Network
    SourceIPs: _containers.RepeatedScalarFieldContainer[bytes]
    TargetIPs: _containers.RepeatedScalarFieldContainer[bytes]
    SourcePort: int
    TargetPort: int
    TargetDomain: str
    Protocol: str
    User: str
    Attributes: _containers.ScalarMap[str, str]
    OutboundGroupTags: _containers.RepeatedScalarFieldContainer[str]
    OutboundTag: str
    def __init__(self, InboundTag: _Optional[str] = ..., Network: _Optional[_Union[_network_pb2.Network, str]] = ..., SourceIPs: _Optional[_Iterable[bytes]] = ..., TargetIPs: _Optional[_Iterable[bytes]] = ..., SourcePort: _Optional[int] = ..., TargetPort: _Optional[int] = ..., TargetDomain: _Optional[str] = ..., Protocol: _Optional[str] = ..., User: _Optional[str] = ..., Attributes: _Optional[_Mapping[str, str]] = ..., OutboundGroupTags: _Optional[_Iterable[str]] = ..., OutboundTag: _Optional[str] = ...) -> None: ...

class SubscribeRoutingStatsRequest(_message.Message):
    __slots__ = ["FieldSelectors"]
    FIELDSELECTORS_FIELD_NUMBER: _ClassVar[int]
    FieldSelectors: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, FieldSelectors: _Optional[_Iterable[str]] = ...) -> None: ...

class TestRouteRequest(_message.Message):
    __slots__ = ["RoutingContext", "FieldSelectors", "PublishResult"]
    ROUTINGCONTEXT_FIELD_NUMBER: _ClassVar[int]
    FIELDSELECTORS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHRESULT_FIELD_NUMBER: _ClassVar[int]
    RoutingContext: RoutingContext
    FieldSelectors: _containers.RepeatedScalarFieldContainer[str]
    PublishResult: bool
    def __init__(self, RoutingContext: _Optional[_Union[RoutingContext, _Mapping]] = ..., FieldSelectors: _Optional[_Iterable[str]] = ..., PublishResult: bool = ...) -> None: ...

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
