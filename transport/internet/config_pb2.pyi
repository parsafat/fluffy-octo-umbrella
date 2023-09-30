from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TransportProtocol(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    TCP: _ClassVar[TransportProtocol]
    UDP: _ClassVar[TransportProtocol]
    MKCP: _ClassVar[TransportProtocol]
    WebSocket: _ClassVar[TransportProtocol]
    HTTP: _ClassVar[TransportProtocol]
    DomainSocket: _ClassVar[TransportProtocol]

class DomainStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    AS_IS: _ClassVar[DomainStrategy]
    USE_IP: _ClassVar[DomainStrategy]
    USE_IP4: _ClassVar[DomainStrategy]
    USE_IP6: _ClassVar[DomainStrategy]
TCP: TransportProtocol
UDP: TransportProtocol
MKCP: TransportProtocol
WebSocket: TransportProtocol
HTTP: TransportProtocol
DomainSocket: TransportProtocol
AS_IS: DomainStrategy
USE_IP: DomainStrategy
USE_IP4: DomainStrategy
USE_IP6: DomainStrategy

class TransportConfig(_message.Message):
    __slots__ = ["protocol", "protocol_name", "settings"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_NAME_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    protocol: TransportProtocol
    protocol_name: str
    settings: _typed_message_pb2.TypedMessage
    def __init__(self, protocol: _Optional[_Union[TransportProtocol, str]] = ..., protocol_name: _Optional[str] = ..., settings: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...

class StreamConfig(_message.Message):
    __slots__ = ["protocol", "protocol_name", "transport_settings", "security_type", "security_settings", "socket_settings"]
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PROTOCOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TRANSPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SOCKET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    protocol: TransportProtocol
    protocol_name: str
    transport_settings: _containers.RepeatedCompositeFieldContainer[TransportConfig]
    security_type: str
    security_settings: _containers.RepeatedCompositeFieldContainer[_typed_message_pb2.TypedMessage]
    socket_settings: SocketConfig
    def __init__(self, protocol: _Optional[_Union[TransportProtocol, str]] = ..., protocol_name: _Optional[str] = ..., transport_settings: _Optional[_Iterable[_Union[TransportConfig, _Mapping]]] = ..., security_type: _Optional[str] = ..., security_settings: _Optional[_Iterable[_Union[_typed_message_pb2.TypedMessage, _Mapping]]] = ..., socket_settings: _Optional[_Union[SocketConfig, _Mapping]] = ...) -> None: ...

class ProxyConfig(_message.Message):
    __slots__ = ["tag", "transportLayerProxy"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    TRANSPORTLAYERPROXY_FIELD_NUMBER: _ClassVar[int]
    tag: str
    transportLayerProxy: bool
    def __init__(self, tag: _Optional[str] = ..., transportLayerProxy: bool = ...) -> None: ...

class SocketConfig(_message.Message):
    __slots__ = ["mark", "tfo", "tproxy", "receive_original_dest_address", "bind_address", "bind_port", "accept_proxy_protocol", "domain_strategy", "dialer_proxy", "tcp_keep_alive_interval", "tcp_keep_alive_idle", "tcp_congestion", "interface", "v6only", "tcp_window_clamp", "tcp_user_timeout", "tcp_max_seg", "tcp_no_delay", "tcp_mptcp"]
    class TProxyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
        Off: _ClassVar[SocketConfig.TProxyMode]
        TProxy: _ClassVar[SocketConfig.TProxyMode]
        Redirect: _ClassVar[SocketConfig.TProxyMode]
    Off: SocketConfig.TProxyMode
    TProxy: SocketConfig.TProxyMode
    Redirect: SocketConfig.TProxyMode
    MARK_FIELD_NUMBER: _ClassVar[int]
    TFO_FIELD_NUMBER: _ClassVar[int]
    TPROXY_FIELD_NUMBER: _ClassVar[int]
    RECEIVE_ORIGINAL_DEST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BIND_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BIND_PORT_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_PROXY_PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_STRATEGY_FIELD_NUMBER: _ClassVar[int]
    DIALER_PROXY_FIELD_NUMBER: _ClassVar[int]
    TCP_KEEP_ALIVE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    TCP_KEEP_ALIVE_IDLE_FIELD_NUMBER: _ClassVar[int]
    TCP_CONGESTION_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    V6ONLY_FIELD_NUMBER: _ClassVar[int]
    TCP_WINDOW_CLAMP_FIELD_NUMBER: _ClassVar[int]
    TCP_USER_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TCP_MAX_SEG_FIELD_NUMBER: _ClassVar[int]
    TCP_NO_DELAY_FIELD_NUMBER: _ClassVar[int]
    TCP_MPTCP_FIELD_NUMBER: _ClassVar[int]
    mark: int
    tfo: int
    tproxy: SocketConfig.TProxyMode
    receive_original_dest_address: bool
    bind_address: bytes
    bind_port: int
    accept_proxy_protocol: bool
    domain_strategy: DomainStrategy
    dialer_proxy: str
    tcp_keep_alive_interval: int
    tcp_keep_alive_idle: int
    tcp_congestion: str
    interface: str
    v6only: bool
    tcp_window_clamp: int
    tcp_user_timeout: int
    tcp_max_seg: int
    tcp_no_delay: bool
    tcp_mptcp: bool
    def __init__(self, mark: _Optional[int] = ..., tfo: _Optional[int] = ..., tproxy: _Optional[_Union[SocketConfig.TProxyMode, str]] = ..., receive_original_dest_address: bool = ..., bind_address: _Optional[bytes] = ..., bind_port: _Optional[int] = ..., accept_proxy_protocol: bool = ..., domain_strategy: _Optional[_Union[DomainStrategy, str]] = ..., dialer_proxy: _Optional[str] = ..., tcp_keep_alive_interval: _Optional[int] = ..., tcp_keep_alive_idle: _Optional[int] = ..., tcp_congestion: _Optional[str] = ..., interface: _Optional[str] = ..., v6only: bool = ..., tcp_window_clamp: _Optional[int] = ..., tcp_user_timeout: _Optional[int] = ..., tcp_max_seg: _Optional[int] = ..., tcp_no_delay: bool = ..., tcp_mptcp: bool = ...) -> None: ...
