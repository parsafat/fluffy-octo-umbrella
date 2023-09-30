from common.serial import typed_message_pb2 as _typed_message_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ["level", "email", "account"]
    LEVEL_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    level: int
    email: str
    account: _typed_message_pb2.TypedMessage
    def __init__(self, level: _Optional[int] = ..., email: _Optional[str] = ..., account: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...
