from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["host", "service_name", "multi_mode", "idle_timeout", "health_check_timeout", "permit_without_stream", "initial_windows_size", "user_agent"]
    HOST_FIELD_NUMBER: _ClassVar[int]
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    MULTI_MODE_FIELD_NUMBER: _ClassVar[int]
    IDLE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HEALTH_CHECK_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PERMIT_WITHOUT_STREAM_FIELD_NUMBER: _ClassVar[int]
    INITIAL_WINDOWS_SIZE_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    host: str
    service_name: str
    multi_mode: bool
    idle_timeout: int
    health_check_timeout: int
    permit_without_stream: bool
    initial_windows_size: int
    user_agent: str
    def __init__(self, host: _Optional[str] = ..., service_name: _Optional[str] = ..., multi_mode: bool = ..., idle_timeout: _Optional[int] = ..., health_check_timeout: _Optional[int] = ..., permit_without_stream: bool = ..., initial_windows_size: _Optional[int] = ..., user_agent: _Optional[str] = ...) -> None: ...
