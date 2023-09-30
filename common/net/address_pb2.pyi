from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class IPOrDomain(_message.Message):
    __slots__ = ["ip", "domain"]
    IP_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ip: bytes
    domain: str
    def __init__(self, ip: _Optional[bytes] = ..., domain: _Optional[str] = ...) -> None: ...
