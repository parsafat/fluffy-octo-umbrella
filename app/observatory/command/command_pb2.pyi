from app.observatory import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOutboundStatusRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class GetOutboundStatusResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _config_pb2.ObservationResult
    def __init__(self, status: _Optional[_Union[_config_pb2.ObservationResult, _Mapping]] = ...) -> None: ...

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
