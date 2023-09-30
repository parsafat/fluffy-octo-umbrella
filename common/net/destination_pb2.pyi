from common.net import network_pb2 as _network_pb2
from common.net import address_pb2 as _address_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Endpoint(_message.Message):
    __slots__ = ["network", "address", "port"]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    network: _network_pb2.Network
    address: _address_pb2.IPOrDomain
    port: int
    def __init__(self, network: _Optional[_Union[_network_pb2.Network, str]] = ..., address: _Optional[_Union[_address_pb2.IPOrDomain, _Mapping]] = ..., port: _Optional[int] = ...) -> None: ...
