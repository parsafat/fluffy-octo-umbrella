# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transport/internet/headers/http/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,transport/internet/headers/http/config.proto\x12$xray.transport.internet.headers.http\"%\n\x06Header\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x03(\t\"\x18\n\x07Version\x12\r\n\x05value\x18\x01 \x01(\t\"\x17\n\x06Method\x12\r\n\x05value\x18\x01 \x01(\t\"\xd8\x01\n\rRequestConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06method\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Method\x12\x0b\n\x03uri\x18\x03 \x03(\t\x12<\n\x06header\x18\x04 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"&\n\x06Status\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x0e\n\x06reason\x18\x02 \x01(\t\"\xcc\x01\n\x0eResponseConfig\x12>\n\x07version\x18\x01 \x01(\x0b\x32-.xray.transport.internet.headers.http.Version\x12<\n\x06status\x18\x02 \x01(\x0b\x32,.xray.transport.internet.headers.http.Status\x12<\n\x06header\x18\x03 \x03(\x0b\x32,.xray.transport.internet.headers.http.Header\"\x96\x01\n\x06\x43onfig\x12\x44\n\x07request\x18\x01 \x01(\x0b\x32\x33.xray.transport.internet.headers.http.RequestConfig\x12\x46\n\x08response\x18\x02 \x01(\x0b\x32\x34.xray.transport.internet.headers.http.ResponseConfigB\x8e\x01\n(com.xray.transport.internet.headers.httpP\x01Z9github.com/xtls/xray-core/transport/internet/headers/http\xaa\x02$Xray.Transport.Internet.Headers.Httpb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transport.internet.headers.http.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.xray.transport.internet.headers.httpP\001Z9github.com/xtls/xray-core/transport/internet/headers/http\252\002$Xray.Transport.Internet.Headers.Http'
  _globals['_HEADER']._serialized_start=86
  _globals['_HEADER']._serialized_end=123
  _globals['_VERSION']._serialized_start=125
  _globals['_VERSION']._serialized_end=149
  _globals['_METHOD']._serialized_start=151
  _globals['_METHOD']._serialized_end=174
  _globals['_REQUESTCONFIG']._serialized_start=177
  _globals['_REQUESTCONFIG']._serialized_end=393
  _globals['_STATUS']._serialized_start=395
  _globals['_STATUS']._serialized_end=433
  _globals['_RESPONSECONFIG']._serialized_start=436
  _globals['_RESPONSECONFIG']._serialized_end=640
  _globals['_CONFIG']._serialized_start=643
  _globals['_CONFIG']._serialized_end=793
# @@protoc_insertion_point(module_scope)
