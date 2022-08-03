# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/channel.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/core/channel/v1/channel.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\"\xed\x01\n\x07\x43hannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x33\n\x0f\x63onnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:\"connection_hops\"\x12\x0f\n\x07version\x18\x05 \x01(\t:\x04\x88\xa0\x1f\x00\"\x9c\x02\n\x11IdentifiedChannel\x12)\n\x05state\x18\x01 \x01(\x0e\x32\x1a.ibc.core.channel.v1.State\x12,\n\x08ordering\x18\x02 \x01(\x0e\x32\x1a.ibc.core.channel.v1.Order\x12=\n\x0c\x63ounterparty\x18\x03 \x01(\x0b\x32!.ibc.core.channel.v1.CounterpartyB\x04\xc8\xde\x1f\x00\x12\x33\n\x0f\x63onnection_hops\x18\x04 \x03(\tB\x1a\xf2\xde\x1f\x16yaml:\"connection_hops\"\x12\x0f\n\x07version\x18\x05 \x01(\t\x12\x0f\n\x07port_id\x18\x06 \x01(\t\x12\x12\n\nchannel_id\x18\x07 \x01(\t:\x04\x88\xa0\x1f\x00\"d\n\x0c\x43ounterparty\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\":\x04\x88\xa0\x1f\x00\"\x8e\x03\n\x06Packet\x12\x10\n\x08sequence\x18\x01 \x01(\x04\x12+\n\x0bsource_port\x18\x02 \x01(\tB\x16\xf2\xde\x1f\x12yaml:\"source_port\"\x12\x31\n\x0esource_channel\x18\x03 \x01(\tB\x19\xf2\xde\x1f\x15yaml:\"source_channel\"\x12\x35\n\x10\x64\x65stination_port\x18\x04 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:\"destination_port\"\x12;\n\x13\x64\x65stination_channel\x18\x05 \x01(\tB\x1e\xf2\xde\x1f\x1ayaml:\"destination_channel\"\x12\x0c\n\x04\x64\x61ta\x18\x06 \x01(\x0c\x12Q\n\x0etimeout_height\x18\x07 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1d\xf2\xde\x1f\x15yaml:\"timeout_height\"\xc8\xde\x1f\x00\x12\x37\n\x11timeout_timestamp\x18\x08 \x01(\x04\x42\x1c\xf2\xde\x1f\x18yaml:\"timeout_timestamp\":\x04\x88\xa0\x1f\x00\"\x83\x01\n\x0bPacketState\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x10\n\x08sequence\x18\x03 \x01(\x04\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c:\x04\x88\xa0\x1f\x00\"@\n\x0f\x41\x63knowledgement\x12\x10\n\x06result\x18\x15 \x01(\x0cH\x00\x12\x0f\n\x05\x65rror\x18\x16 \x01(\tH\x00\x42\n\n\x08response*\xb7\x01\n\x05State\x12\x36\n\x1fSTATE_UNINITIALIZED_UNSPECIFIED\x10\x00\x1a\x11\x8a\x9d \rUNINITIALIZED\x12\x18\n\nSTATE_INIT\x10\x01\x1a\x08\x8a\x9d \x04INIT\x12\x1e\n\rSTATE_TRYOPEN\x10\x02\x1a\x0b\x8a\x9d \x07TRYOPEN\x12\x18\n\nSTATE_OPEN\x10\x03\x1a\x08\x8a\x9d \x04OPEN\x12\x1c\n\x0cSTATE_CLOSED\x10\x04\x1a\n\x8a\x9d \x06\x43LOSED\x1a\x04\x88\xa3\x1e\x00*w\n\x05Order\x12$\n\x16ORDER_NONE_UNSPECIFIED\x10\x00\x1a\x08\x8a\x9d \x04NONE\x12\"\n\x0fORDER_UNORDERED\x10\x01\x1a\r\x8a\x9d \tUNORDERED\x12\x1e\n\rORDER_ORDERED\x10\x02\x1a\x0b\x8a\x9d \x07ORDERED\x1a\x04\x88\xa3\x1e\x00\x42;Z9github.com/cosmos/ibc-go/v2/modules/core/04-channel/typesb\x06proto3')

_STATE = DESCRIPTOR.enum_types_by_name['State']
State = enum_type_wrapper.EnumTypeWrapper(_STATE)
_ORDER = DESCRIPTOR.enum_types_by_name['Order']
Order = enum_type_wrapper.EnumTypeWrapper(_ORDER)
STATE_UNINITIALIZED_UNSPECIFIED = 0
STATE_INIT = 1
STATE_TRYOPEN = 2
STATE_OPEN = 3
STATE_CLOSED = 4
ORDER_NONE_UNSPECIFIED = 0
ORDER_UNORDERED = 1
ORDER_ORDERED = 2


_CHANNEL = DESCRIPTOR.message_types_by_name['Channel']
_IDENTIFIEDCHANNEL = DESCRIPTOR.message_types_by_name['IdentifiedChannel']
_COUNTERPARTY = DESCRIPTOR.message_types_by_name['Counterparty']
_PACKET = DESCRIPTOR.message_types_by_name['Packet']
_PACKETSTATE = DESCRIPTOR.message_types_by_name['PacketState']
_ACKNOWLEDGEMENT = DESCRIPTOR.message_types_by_name['Acknowledgement']
Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), {
  'DESCRIPTOR' : _CHANNEL,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Channel)
  })
_sym_db.RegisterMessage(Channel)

IdentifiedChannel = _reflection.GeneratedProtocolMessageType('IdentifiedChannel', (_message.Message,), {
  'DESCRIPTOR' : _IDENTIFIEDCHANNEL,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.IdentifiedChannel)
  })
_sym_db.RegisterMessage(IdentifiedChannel)

Counterparty = _reflection.GeneratedProtocolMessageType('Counterparty', (_message.Message,), {
  'DESCRIPTOR' : _COUNTERPARTY,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Counterparty)
  })
_sym_db.RegisterMessage(Counterparty)

Packet = _reflection.GeneratedProtocolMessageType('Packet', (_message.Message,), {
  'DESCRIPTOR' : _PACKET,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Packet)
  })
_sym_db.RegisterMessage(Packet)

PacketState = _reflection.GeneratedProtocolMessageType('PacketState', (_message.Message,), {
  'DESCRIPTOR' : _PACKETSTATE,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.PacketState)
  })
_sym_db.RegisterMessage(PacketState)

Acknowledgement = _reflection.GeneratedProtocolMessageType('Acknowledgement', (_message.Message,), {
  'DESCRIPTOR' : _ACKNOWLEDGEMENT,
  '__module__' : 'ibc.core.channel.v1.channel_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.Acknowledgement)
  })
_sym_db.RegisterMessage(Acknowledgement)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z9github.com/cosmos/ibc-go/v2/modules/core/04-channel/types'
  _STATE._options = None
  _STATE._serialized_options = b'\210\243\036\000'
  _STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._options = None
  _STATE.values_by_name["STATE_UNINITIALIZED_UNSPECIFIED"]._serialized_options = b'\212\235 \rUNINITIALIZED'
  _STATE.values_by_name["STATE_INIT"]._options = None
  _STATE.values_by_name["STATE_INIT"]._serialized_options = b'\212\235 \004INIT'
  _STATE.values_by_name["STATE_TRYOPEN"]._options = None
  _STATE.values_by_name["STATE_TRYOPEN"]._serialized_options = b'\212\235 \007TRYOPEN'
  _STATE.values_by_name["STATE_OPEN"]._options = None
  _STATE.values_by_name["STATE_OPEN"]._serialized_options = b'\212\235 \004OPEN'
  _STATE.values_by_name["STATE_CLOSED"]._options = None
  _STATE.values_by_name["STATE_CLOSED"]._serialized_options = b'\212\235 \006CLOSED'
  _ORDER._options = None
  _ORDER._serialized_options = b'\210\243\036\000'
  _ORDER.values_by_name["ORDER_NONE_UNSPECIFIED"]._options = None
  _ORDER.values_by_name["ORDER_NONE_UNSPECIFIED"]._serialized_options = b'\212\235 \004NONE'
  _ORDER.values_by_name["ORDER_UNORDERED"]._options = None
  _ORDER.values_by_name["ORDER_UNORDERED"]._serialized_options = b'\212\235 \tUNORDERED'
  _ORDER.values_by_name["ORDER_ORDERED"]._options = None
  _ORDER.values_by_name["ORDER_ORDERED"]._serialized_options = b'\212\235 \007ORDERED'
  _CHANNEL.fields_by_name['counterparty']._options = None
  _CHANNEL.fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _CHANNEL.fields_by_name['connection_hops']._options = None
  _CHANNEL.fields_by_name['connection_hops']._serialized_options = b'\362\336\037\026yaml:\"connection_hops\"'
  _CHANNEL._options = None
  _CHANNEL._serialized_options = b'\210\240\037\000'
  _IDENTIFIEDCHANNEL.fields_by_name['counterparty']._options = None
  _IDENTIFIEDCHANNEL.fields_by_name['counterparty']._serialized_options = b'\310\336\037\000'
  _IDENTIFIEDCHANNEL.fields_by_name['connection_hops']._options = None
  _IDENTIFIEDCHANNEL.fields_by_name['connection_hops']._serialized_options = b'\362\336\037\026yaml:\"connection_hops\"'
  _IDENTIFIEDCHANNEL._options = None
  _IDENTIFIEDCHANNEL._serialized_options = b'\210\240\037\000'
  _COUNTERPARTY.fields_by_name['port_id']._options = None
  _COUNTERPARTY.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _COUNTERPARTY.fields_by_name['channel_id']._options = None
  _COUNTERPARTY.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _COUNTERPARTY._options = None
  _COUNTERPARTY._serialized_options = b'\210\240\037\000'
  _PACKET.fields_by_name['source_port']._options = None
  _PACKET.fields_by_name['source_port']._serialized_options = b'\362\336\037\022yaml:\"source_port\"'
  _PACKET.fields_by_name['source_channel']._options = None
  _PACKET.fields_by_name['source_channel']._serialized_options = b'\362\336\037\025yaml:\"source_channel\"'
  _PACKET.fields_by_name['destination_port']._options = None
  _PACKET.fields_by_name['destination_port']._serialized_options = b'\362\336\037\027yaml:\"destination_port\"'
  _PACKET.fields_by_name['destination_channel']._options = None
  _PACKET.fields_by_name['destination_channel']._serialized_options = b'\362\336\037\032yaml:\"destination_channel\"'
  _PACKET.fields_by_name['timeout_height']._options = None
  _PACKET.fields_by_name['timeout_height']._serialized_options = b'\362\336\037\025yaml:\"timeout_height\"\310\336\037\000'
  _PACKET.fields_by_name['timeout_timestamp']._options = None
  _PACKET.fields_by_name['timeout_timestamp']._serialized_options = b'\362\336\037\030yaml:\"timeout_timestamp\"'
  _PACKET._options = None
  _PACKET._serialized_options = b'\210\240\037\000'
  _PACKETSTATE.fields_by_name['port_id']._options = None
  _PACKETSTATE.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _PACKETSTATE.fields_by_name['channel_id']._options = None
  _PACKETSTATE.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _PACKETSTATE._options = None
  _PACKETSTATE._serialized_options = b'\210\240\037\000'
  _STATE._serialized_start=1344
  _STATE._serialized_end=1527
  _ORDER._serialized_start=1529
  _ORDER._serialized_end=1648
  _CHANNEL._serialized_start=114
  _CHANNEL._serialized_end=351
  _IDENTIFIEDCHANNEL._serialized_start=354
  _IDENTIFIEDCHANNEL._serialized_end=638
  _COUNTERPARTY._serialized_start=640
  _COUNTERPARTY._serialized_end=740
  _PACKET._serialized_start=743
  _PACKET._serialized_end=1141
  _PACKETSTATE._serialized_start=1144
  _PACKETSTATE._serialized_end=1275
  _ACKNOWLEDGEMENT._serialized_start=1277
  _ACKNOWLEDGEMENT._serialized_end=1341
# @@protoc_insertion_point(module_scope)
