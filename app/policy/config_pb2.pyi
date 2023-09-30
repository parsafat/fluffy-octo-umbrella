from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Second(_message.Message):
    __slots__ = ["value"]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class Policy(_message.Message):
    __slots__ = ["timeout", "stats", "buffer"]
    class Timeout(_message.Message):
        __slots__ = ["handshake", "connection_idle", "uplink_only", "downlink_only"]
        HANDSHAKE_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_IDLE_FIELD_NUMBER: _ClassVar[int]
        UPLINK_ONLY_FIELD_NUMBER: _ClassVar[int]
        DOWNLINK_ONLY_FIELD_NUMBER: _ClassVar[int]
        handshake: Second
        connection_idle: Second
        uplink_only: Second
        downlink_only: Second
        def __init__(self, handshake: _Optional[_Union[Second, _Mapping]] = ..., connection_idle: _Optional[_Union[Second, _Mapping]] = ..., uplink_only: _Optional[_Union[Second, _Mapping]] = ..., downlink_only: _Optional[_Union[Second, _Mapping]] = ...) -> None: ...
    class Stats(_message.Message):
        __slots__ = ["user_uplink", "user_downlink"]
        USER_UPLINK_FIELD_NUMBER: _ClassVar[int]
        USER_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
        user_uplink: bool
        user_downlink: bool
        def __init__(self, user_uplink: bool = ..., user_downlink: bool = ...) -> None: ...
    class Buffer(_message.Message):
        __slots__ = ["connection"]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        connection: int
        def __init__(self, connection: _Optional[int] = ...) -> None: ...
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    STATS_FIELD_NUMBER: _ClassVar[int]
    BUFFER_FIELD_NUMBER: _ClassVar[int]
    timeout: Policy.Timeout
    stats: Policy.Stats
    buffer: Policy.Buffer
    def __init__(self, timeout: _Optional[_Union[Policy.Timeout, _Mapping]] = ..., stats: _Optional[_Union[Policy.Stats, _Mapping]] = ..., buffer: _Optional[_Union[Policy.Buffer, _Mapping]] = ...) -> None: ...

class SystemPolicy(_message.Message):
    __slots__ = ["stats"]
    class Stats(_message.Message):
        __slots__ = ["inbound_uplink", "inbound_downlink", "outbound_uplink", "outbound_downlink"]
        INBOUND_UPLINK_FIELD_NUMBER: _ClassVar[int]
        INBOUND_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_UPLINK_FIELD_NUMBER: _ClassVar[int]
        OUTBOUND_DOWNLINK_FIELD_NUMBER: _ClassVar[int]
        inbound_uplink: bool
        inbound_downlink: bool
        outbound_uplink: bool
        outbound_downlink: bool
        def __init__(self, inbound_uplink: bool = ..., inbound_downlink: bool = ..., outbound_uplink: bool = ..., outbound_downlink: bool = ...) -> None: ...
    STATS_FIELD_NUMBER: _ClassVar[int]
    stats: SystemPolicy.Stats
    def __init__(self, stats: _Optional[_Union[SystemPolicy.Stats, _Mapping]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["level", "system"]
    class LevelEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Policy
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Policy, _Mapping]] = ...) -> None: ...
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    level: _containers.MessageMap[int, Policy]
    system: SystemPolicy
    def __init__(self, level: _Optional[_Mapping[int, Policy]] = ..., system: _Optional[_Union[SystemPolicy, _Mapping]] = ...) -> None: ...
