from common.log import log_pb2 as _log_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LogType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    None: _ClassVar[LogType]
    Console: _ClassVar[LogType]
    File: _ClassVar[LogType]
    Event: _ClassVar[LogType]
None: LogType
Console: LogType
File: LogType
Event: LogType

class Config(_message.Message):
    __slots__ = ["error_log_type", "error_log_level", "error_log_path", "access_log_type", "access_log_path", "enable_dns_log"]
    ERROR_LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOG_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ERROR_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACCESS_LOG_PATH_FIELD_NUMBER: _ClassVar[int]
    ENABLE_DNS_LOG_FIELD_NUMBER: _ClassVar[int]
    error_log_type: LogType
    error_log_level: _log_pb2.Severity
    error_log_path: str
    access_log_type: LogType
    access_log_path: str
    enable_dns_log: bool
    def __init__(self, error_log_type: _Optional[_Union[LogType, str]] = ..., error_log_level: _Optional[_Union[_log_pb2.Severity, str]] = ..., error_log_path: _Optional[str] = ..., access_log_type: _Optional[_Union[LogType, str]] = ..., access_log_path: _Optional[str] = ..., enable_dns_log: bool = ...) -> None: ...
