from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Config(_message.Message):
    __slots__ = ["show", "dest", "type", "xver", "server_names", "private_key", "min_client_ver", "max_client_ver", "max_time_diff", "short_ids", "Fingerprint", "server_name", "public_key", "short_id", "spider_x", "spider_y"]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    DEST_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    XVER_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAMES_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_KEY_FIELD_NUMBER: _ClassVar[int]
    MIN_CLIENT_VER_FIELD_NUMBER: _ClassVar[int]
    MAX_CLIENT_VER_FIELD_NUMBER: _ClassVar[int]
    MAX_TIME_DIFF_FIELD_NUMBER: _ClassVar[int]
    SHORT_IDS_FIELD_NUMBER: _ClassVar[int]
    FINGERPRINT_FIELD_NUMBER: _ClassVar[int]
    SERVER_NAME_FIELD_NUMBER: _ClassVar[int]
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    SHORT_ID_FIELD_NUMBER: _ClassVar[int]
    SPIDER_X_FIELD_NUMBER: _ClassVar[int]
    SPIDER_Y_FIELD_NUMBER: _ClassVar[int]
    show: bool
    dest: str
    type: str
    xver: int
    server_names: _containers.RepeatedScalarFieldContainer[str]
    private_key: bytes
    min_client_ver: bytes
    max_client_ver: bytes
    max_time_diff: int
    short_ids: _containers.RepeatedScalarFieldContainer[bytes]
    Fingerprint: str
    server_name: str
    public_key: bytes
    short_id: bytes
    spider_x: str
    spider_y: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, show: bool = ..., dest: _Optional[str] = ..., type: _Optional[str] = ..., xver: _Optional[int] = ..., server_names: _Optional[_Iterable[str]] = ..., private_key: _Optional[bytes] = ..., min_client_ver: _Optional[bytes] = ..., max_client_ver: _Optional[bytes] = ..., max_time_diff: _Optional[int] = ..., short_ids: _Optional[_Iterable[bytes]] = ..., Fingerprint: _Optional[str] = ..., server_name: _Optional[str] = ..., public_key: _Optional[bytes] = ..., short_id: _Optional[bytes] = ..., spider_x: _Optional[str] = ..., spider_y: _Optional[_Iterable[int]] = ...) -> None: ...
