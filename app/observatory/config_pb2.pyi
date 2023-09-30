from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ObservationResult(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _containers.RepeatedCompositeFieldContainer[OutboundStatus]
    def __init__(self, status: _Optional[_Iterable[_Union[OutboundStatus, _Mapping]]] = ...) -> None: ...

class OutboundStatus(_message.Message):
    __slots__ = ["alive", "delay", "last_error_reason", "outbound_tag", "last_seen_time", "last_try_time"]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    OUTBOUND_TAG_FIELD_NUMBER: _ClassVar[int]
    LAST_SEEN_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_TRY_TIME_FIELD_NUMBER: _ClassVar[int]
    alive: bool
    delay: int
    last_error_reason: str
    outbound_tag: str
    last_seen_time: int
    last_try_time: int
    def __init__(self, alive: bool = ..., delay: _Optional[int] = ..., last_error_reason: _Optional[str] = ..., outbound_tag: _Optional[str] = ..., last_seen_time: _Optional[int] = ..., last_try_time: _Optional[int] = ...) -> None: ...

class ProbeResult(_message.Message):
    __slots__ = ["alive", "delay", "last_error_reason"]
    ALIVE_FIELD_NUMBER: _ClassVar[int]
    DELAY_FIELD_NUMBER: _ClassVar[int]
    LAST_ERROR_REASON_FIELD_NUMBER: _ClassVar[int]
    alive: bool
    delay: int
    last_error_reason: str
    def __init__(self, alive: bool = ..., delay: _Optional[int] = ..., last_error_reason: _Optional[str] = ...) -> None: ...

class Intensity(_message.Message):
    __slots__ = ["probe_interval"]
    PROBE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    probe_interval: int
    def __init__(self, probe_interval: _Optional[int] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = ["subject_selector", "probe_url", "probe_interval", "enable_concurrency"]
    SUBJECT_SELECTOR_FIELD_NUMBER: _ClassVar[int]
    PROBE_URL_FIELD_NUMBER: _ClassVar[int]
    PROBE_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CONCURRENCY_FIELD_NUMBER: _ClassVar[int]
    subject_selector: _containers.RepeatedScalarFieldContainer[str]
    probe_url: str
    probe_interval: int
    enable_concurrency: bool
    def __init__(self, subject_selector: _Optional[_Iterable[str]] = ..., probe_url: _Optional[str] = ..., probe_interval: _Optional[int] = ..., enable_concurrency: bool = ...) -> None: ...
