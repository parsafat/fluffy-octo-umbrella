from common.protocol import server_spec_pb2 as _server_spec_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["vnext"]
    VNEXT_FIELD_NUMBER: _ClassVar[int]
    vnext: _containers.RepeatedCompositeFieldContainer[_server_spec_pb2.ServerEndpoint]
    def __init__(self, vnext: _Optional[_Iterable[_Union[_server_spec_pb2.ServerEndpoint, _Mapping]]] = ...) -> None: ...
