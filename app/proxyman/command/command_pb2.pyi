from common.protocol import user_pb2 as _user_pb2
from common.serial import typed_message_pb2 as _typed_message_pb2
from core import config_pb2 as _config_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AddUserOperation(_message.Message):
    __slots__ = ["user"]
    USER_FIELD_NUMBER: _ClassVar[int]
    user: _user_pb2.User
    def __init__(self, user: _Optional[_Union[_user_pb2.User, _Mapping]] = ...) -> None: ...

class RemoveUserOperation(_message.Message):
    __slots__ = ["email"]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    email: str
    def __init__(self, email: _Optional[str] = ...) -> None: ...

class AddInboundRequest(_message.Message):
    __slots__ = ["inbound"]
    INBOUND_FIELD_NUMBER: _ClassVar[int]
    inbound: _config_pb2.InboundHandlerConfig
    def __init__(self, inbound: _Optional[_Union[_config_pb2.InboundHandlerConfig, _Mapping]] = ...) -> None: ...

class AddInboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveInboundRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class RemoveInboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AlterInboundRequest(_message.Message):
    __slots__ = ["tag", "operation"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    tag: str
    operation: _typed_message_pb2.TypedMessage
    def __init__(self, tag: _Optional[str] = ..., operation: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...

class AlterInboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AddOutboundRequest(_message.Message):
    __slots__ = ["outbound"]
    OUTBOUND_FIELD_NUMBER: _ClassVar[int]
    outbound: _config_pb2.OutboundHandlerConfig
    def __init__(self, outbound: _Optional[_Union[_config_pb2.OutboundHandlerConfig, _Mapping]] = ...) -> None: ...

class AddOutboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class RemoveOutboundRequest(_message.Message):
    __slots__ = ["tag"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    tag: str
    def __init__(self, tag: _Optional[str] = ...) -> None: ...

class RemoveOutboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class AlterOutboundRequest(_message.Message):
    __slots__ = ["tag", "operation"]
    TAG_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    tag: str
    operation: _typed_message_pb2.TypedMessage
    def __init__(self, tag: _Optional[str] = ..., operation: _Optional[_Union[_typed_message_pb2.TypedMessage, _Mapping]] = ...) -> None: ...

class AlterOutboundResponse(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Config(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
