# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proxy/vless/outbound/config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common.protocol import server_spec_pb2 as common_dot_protocol_dot_server__spec__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!proxy/vless/outbound/config.proto\x12\x19xray.proxy.vless.outbound\x1a!common/protocol/server_spec.proto\"=\n\x06\x43onfig\x12\x33\n\x05vnext\x18\x01 \x03(\x0b\x32$.xray.common.protocol.ServerEndpointBm\n\x1d\x63om.xray.proxy.vless.outboundP\x01Z.github.com/xtls/xray-core/proxy/vless/outbound\xaa\x02\x19Xray.Proxy.Vless.Outboundb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proxy.vless.outbound.config_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\035com.xray.proxy.vless.outboundP\001Z.github.com/xtls/xray-core/proxy/vless/outbound\252\002\031Xray.Proxy.Vless.Outbound'
  _globals['_CONFIG']._serialized_start=99
  _globals['_CONFIG']._serialized_end=160
# @@protoc_insertion_point(module_scope)
