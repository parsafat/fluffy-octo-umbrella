from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Addons(_message.Message):
    __slots__ = ["Flow", "Seed"]
    FLOW_FIELD_NUMBER: _ClassVar[int]
    SEED_FIELD_NUMBER: _ClassVar[int]
    Flow: str
    Seed: bytes
    def __init__(self, Flow: _Optional[str] = ..., Seed: _Optional[bytes] = ...) -> None: ...
