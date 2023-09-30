from transport.internet import config_pb2 as _config_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["transport_settings"]
    TRANSPORT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    transport_settings: _containers.RepeatedCompositeFieldContainer[_config_pb2.TransportConfig]
    def __init__(self, transport_settings: _Optional[_Iterable[_Union[_config_pb2.TransportConfig, _Mapping]]] = ...) -> None: ...
