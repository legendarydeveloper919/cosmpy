# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ibc/core/channel/v1/tx.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ibc.core.client.v1 import client_pb2 as ibc_dot_core_dot_client_dot_v1_dot_client__pb2
from ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cibc/core/channel/v1/tx.proto\x12\x13ibc.core.channel.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fibc/core/client/v1/client.proto\x1a!ibc/core/channel/v1/channel.proto\"\x88\x01\n\x12MsgChannelOpenInit\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12\x33\n\x07\x63hannel\x18\x02 \x01(\x0b\x32\x1c.ibc.core.channel.v1.ChannelB\x04\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1c\n\x1aMsgChannelOpenInitResponse\"\xfd\x02\n\x11MsgChannelOpenTry\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12;\n\x13previous_channel_id\x18\x02 \x01(\tB\x1e\xf2\xde\x1f\x1ayaml:\"previous_channel_id\"\x12\x33\n\x07\x63hannel\x18\x03 \x01(\x0b\x32\x1c.ibc.core.channel.v1.ChannelB\x04\xc8\xde\x1f\x00\x12=\n\x14\x63ounterparty_version\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:\"counterparty_version\"\x12)\n\nproof_init\x18\x05 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:\"proof_init\"\x12M\n\x0cproof_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x07 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1b\n\x19MsgChannelOpenTryResponse\"\xf9\x02\n\x11MsgChannelOpenAck\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x43\n\x17\x63ounterparty_channel_id\x18\x03 \x01(\tB\"\xf2\xde\x1f\x1eyaml:\"counterparty_channel_id\"\x12=\n\x14\x63ounterparty_version\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:\"counterparty_version\"\x12\'\n\tproof_try\x18\x05 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:\"proof_try\"\x12M\n\x0cproof_height\x18\x06 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x07 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1b\n\x19MsgChannelOpenAckResponse\"\xf9\x01\n\x15MsgChannelOpenConfirm\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\'\n\tproof_ack\x18\x03 \x01(\x0c\x42\x14\xf2\xde\x1f\x10yaml:\"proof_ack\"\x12M\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1f\n\x1dMsgChannelOpenConfirmResponse\"\x7f\n\x13MsgChannelCloseInit\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12\x0e\n\x06signer\x18\x03 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1d\n\x1bMsgChannelCloseInitResponse\"\xfc\x01\n\x16MsgChannelCloseConfirm\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:\"port_id\"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:\"channel_id\"\x12)\n\nproof_init\x18\x03 \x01(\x0c\x42\x15\xf2\xde\x1f\x11yaml:\"proof_init\"\x12M\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\" \n\x1eMsgChannelCloseConfirmResponse\"\xe2\x01\n\rMsgRecvPacket\x12\x31\n\x06packet\x18\x01 \x01(\x0b\x32\x1b.ibc.core.channel.v1.PacketB\x04\xc8\xde\x1f\x00\x12\x35\n\x10proof_commitment\x18\x02 \x01(\x0c\x42\x1b\xf2\xde\x1f\x17yaml:\"proof_commitment\"\x12M\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x04 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x17\n\x15MsgRecvPacketResponse\"\x9a\x02\n\nMsgTimeout\x12\x31\n\x06packet\x18\x01 \x01(\x0b\x32\x1b.ibc.core.channel.v1.PacketB\x04\xc8\xde\x1f\x00\x12\x35\n\x10proof_unreceived\x18\x02 \x01(\x0c\x42\x1b\xf2\xde\x1f\x17yaml:\"proof_unreceived\"\x12M\n\x0cproof_height\x18\x03 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x39\n\x12next_sequence_recv\x18\x04 \x01(\x04\x42\x1d\xf2\xde\x1f\x19yaml:\"next_sequence_recv\"\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x14\n\x12MsgTimeoutResponse\"\xce\x02\n\x11MsgTimeoutOnClose\x12\x31\n\x06packet\x18\x01 \x01(\x0b\x32\x1b.ibc.core.channel.v1.PacketB\x04\xc8\xde\x1f\x00\x12\x35\n\x10proof_unreceived\x18\x02 \x01(\x0c\x42\x1b\xf2\xde\x1f\x17yaml:\"proof_unreceived\"\x12+\n\x0bproof_close\x18\x03 \x01(\x0c\x42\x16\xf2\xde\x1f\x12yaml:\"proof_close\"\x12M\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x39\n\x12next_sequence_recv\x18\x05 \x01(\x04\x42\x1d\xf2\xde\x1f\x19yaml:\"next_sequence_recv\"\x12\x0e\n\x06signer\x18\x06 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1b\n\x19MsgTimeoutOnCloseResponse\"\xf6\x01\n\x12MsgAcknowledgement\x12\x31\n\x06packet\x18\x01 \x01(\x0b\x32\x1b.ibc.core.channel.v1.PacketB\x04\xc8\xde\x1f\x00\x12\x17\n\x0f\x61\x63knowledgement\x18\x02 \x01(\x0c\x12+\n\x0bproof_acked\x18\x03 \x01(\x0c\x42\x16\xf2\xde\x1f\x12yaml:\"proof_acked\"\x12M\n\x0cproof_height\x18\x04 \x01(\x0b\x32\x1a.ibc.core.client.v1.HeightB\x1b\xf2\xde\x1f\x13yaml:\"proof_height\"\xc8\xde\x1f\x00\x12\x0e\n\x06signer\x18\x05 \x01(\t:\x08\xe8\xa0\x1f\x00\x88\xa0\x1f\x00\"\x1c\n\x1aMsgAcknowledgementResponse2\xaf\x08\n\x03Msg\x12k\n\x0f\x43hannelOpenInit\x12\'.ibc.core.channel.v1.MsgChannelOpenInit\x1a/.ibc.core.channel.v1.MsgChannelOpenInitResponse\x12h\n\x0e\x43hannelOpenTry\x12&.ibc.core.channel.v1.MsgChannelOpenTry\x1a..ibc.core.channel.v1.MsgChannelOpenTryResponse\x12h\n\x0e\x43hannelOpenAck\x12&.ibc.core.channel.v1.MsgChannelOpenAck\x1a..ibc.core.channel.v1.MsgChannelOpenAckResponse\x12t\n\x12\x43hannelOpenConfirm\x12*.ibc.core.channel.v1.MsgChannelOpenConfirm\x1a\x32.ibc.core.channel.v1.MsgChannelOpenConfirmResponse\x12n\n\x10\x43hannelCloseInit\x12(.ibc.core.channel.v1.MsgChannelCloseInit\x1a\x30.ibc.core.channel.v1.MsgChannelCloseInitResponse\x12w\n\x13\x43hannelCloseConfirm\x12+.ibc.core.channel.v1.MsgChannelCloseConfirm\x1a\x33.ibc.core.channel.v1.MsgChannelCloseConfirmResponse\x12\\\n\nRecvPacket\x12\".ibc.core.channel.v1.MsgRecvPacket\x1a*.ibc.core.channel.v1.MsgRecvPacketResponse\x12S\n\x07Timeout\x12\x1f.ibc.core.channel.v1.MsgTimeout\x1a\'.ibc.core.channel.v1.MsgTimeoutResponse\x12h\n\x0eTimeoutOnClose\x12&.ibc.core.channel.v1.MsgTimeoutOnClose\x1a..ibc.core.channel.v1.MsgTimeoutOnCloseResponse\x12k\n\x0f\x41\x63knowledgement\x12\'.ibc.core.channel.v1.MsgAcknowledgement\x1a/.ibc.core.channel.v1.MsgAcknowledgementResponseB:Z8github.com/cosmos/cosmos-sdk/x/ibc/core/04-channel/typesb\x06proto3')



_MSGCHANNELOPENINIT = DESCRIPTOR.message_types_by_name['MsgChannelOpenInit']
_MSGCHANNELOPENINITRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelOpenInitResponse']
_MSGCHANNELOPENTRY = DESCRIPTOR.message_types_by_name['MsgChannelOpenTry']
_MSGCHANNELOPENTRYRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelOpenTryResponse']
_MSGCHANNELOPENACK = DESCRIPTOR.message_types_by_name['MsgChannelOpenAck']
_MSGCHANNELOPENACKRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelOpenAckResponse']
_MSGCHANNELOPENCONFIRM = DESCRIPTOR.message_types_by_name['MsgChannelOpenConfirm']
_MSGCHANNELOPENCONFIRMRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelOpenConfirmResponse']
_MSGCHANNELCLOSEINIT = DESCRIPTOR.message_types_by_name['MsgChannelCloseInit']
_MSGCHANNELCLOSEINITRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelCloseInitResponse']
_MSGCHANNELCLOSECONFIRM = DESCRIPTOR.message_types_by_name['MsgChannelCloseConfirm']
_MSGCHANNELCLOSECONFIRMRESPONSE = DESCRIPTOR.message_types_by_name['MsgChannelCloseConfirmResponse']
_MSGRECVPACKET = DESCRIPTOR.message_types_by_name['MsgRecvPacket']
_MSGRECVPACKETRESPONSE = DESCRIPTOR.message_types_by_name['MsgRecvPacketResponse']
_MSGTIMEOUT = DESCRIPTOR.message_types_by_name['MsgTimeout']
_MSGTIMEOUTRESPONSE = DESCRIPTOR.message_types_by_name['MsgTimeoutResponse']
_MSGTIMEOUTONCLOSE = DESCRIPTOR.message_types_by_name['MsgTimeoutOnClose']
_MSGTIMEOUTONCLOSERESPONSE = DESCRIPTOR.message_types_by_name['MsgTimeoutOnCloseResponse']
_MSGACKNOWLEDGEMENT = DESCRIPTOR.message_types_by_name['MsgAcknowledgement']
_MSGACKNOWLEDGEMENTRESPONSE = DESCRIPTOR.message_types_by_name['MsgAcknowledgementResponse']
MsgChannelOpenInit = _reflection.GeneratedProtocolMessageType('MsgChannelOpenInit', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENINIT,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenInit)
  })
_sym_db.RegisterMessage(MsgChannelOpenInit)

MsgChannelOpenInitResponse = _reflection.GeneratedProtocolMessageType('MsgChannelOpenInitResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENINITRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenInitResponse)
  })
_sym_db.RegisterMessage(MsgChannelOpenInitResponse)

MsgChannelOpenTry = _reflection.GeneratedProtocolMessageType('MsgChannelOpenTry', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENTRY,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenTry)
  })
_sym_db.RegisterMessage(MsgChannelOpenTry)

MsgChannelOpenTryResponse = _reflection.GeneratedProtocolMessageType('MsgChannelOpenTryResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENTRYRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenTryResponse)
  })
_sym_db.RegisterMessage(MsgChannelOpenTryResponse)

MsgChannelOpenAck = _reflection.GeneratedProtocolMessageType('MsgChannelOpenAck', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENACK,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenAck)
  })
_sym_db.RegisterMessage(MsgChannelOpenAck)

MsgChannelOpenAckResponse = _reflection.GeneratedProtocolMessageType('MsgChannelOpenAckResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENACKRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenAckResponse)
  })
_sym_db.RegisterMessage(MsgChannelOpenAckResponse)

MsgChannelOpenConfirm = _reflection.GeneratedProtocolMessageType('MsgChannelOpenConfirm', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENCONFIRM,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenConfirm)
  })
_sym_db.RegisterMessage(MsgChannelOpenConfirm)

MsgChannelOpenConfirmResponse = _reflection.GeneratedProtocolMessageType('MsgChannelOpenConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELOPENCONFIRMRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelOpenConfirmResponse)
  })
_sym_db.RegisterMessage(MsgChannelOpenConfirmResponse)

MsgChannelCloseInit = _reflection.GeneratedProtocolMessageType('MsgChannelCloseInit', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELCLOSEINIT,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelCloseInit)
  })
_sym_db.RegisterMessage(MsgChannelCloseInit)

MsgChannelCloseInitResponse = _reflection.GeneratedProtocolMessageType('MsgChannelCloseInitResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELCLOSEINITRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelCloseInitResponse)
  })
_sym_db.RegisterMessage(MsgChannelCloseInitResponse)

MsgChannelCloseConfirm = _reflection.GeneratedProtocolMessageType('MsgChannelCloseConfirm', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELCLOSECONFIRM,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelCloseConfirm)
  })
_sym_db.RegisterMessage(MsgChannelCloseConfirm)

MsgChannelCloseConfirmResponse = _reflection.GeneratedProtocolMessageType('MsgChannelCloseConfirmResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGCHANNELCLOSECONFIRMRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgChannelCloseConfirmResponse)
  })
_sym_db.RegisterMessage(MsgChannelCloseConfirmResponse)

MsgRecvPacket = _reflection.GeneratedProtocolMessageType('MsgRecvPacket', (_message.Message,), {
  'DESCRIPTOR' : _MSGRECVPACKET,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgRecvPacket)
  })
_sym_db.RegisterMessage(MsgRecvPacket)

MsgRecvPacketResponse = _reflection.GeneratedProtocolMessageType('MsgRecvPacketResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGRECVPACKETRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgRecvPacketResponse)
  })
_sym_db.RegisterMessage(MsgRecvPacketResponse)

MsgTimeout = _reflection.GeneratedProtocolMessageType('MsgTimeout', (_message.Message,), {
  'DESCRIPTOR' : _MSGTIMEOUT,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgTimeout)
  })
_sym_db.RegisterMessage(MsgTimeout)

MsgTimeoutResponse = _reflection.GeneratedProtocolMessageType('MsgTimeoutResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGTIMEOUTRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgTimeoutResponse)
  })
_sym_db.RegisterMessage(MsgTimeoutResponse)

MsgTimeoutOnClose = _reflection.GeneratedProtocolMessageType('MsgTimeoutOnClose', (_message.Message,), {
  'DESCRIPTOR' : _MSGTIMEOUTONCLOSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgTimeoutOnClose)
  })
_sym_db.RegisterMessage(MsgTimeoutOnClose)

MsgTimeoutOnCloseResponse = _reflection.GeneratedProtocolMessageType('MsgTimeoutOnCloseResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGTIMEOUTONCLOSERESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgTimeoutOnCloseResponse)
  })
_sym_db.RegisterMessage(MsgTimeoutOnCloseResponse)

MsgAcknowledgement = _reflection.GeneratedProtocolMessageType('MsgAcknowledgement', (_message.Message,), {
  'DESCRIPTOR' : _MSGACKNOWLEDGEMENT,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgAcknowledgement)
  })
_sym_db.RegisterMessage(MsgAcknowledgement)

MsgAcknowledgementResponse = _reflection.GeneratedProtocolMessageType('MsgAcknowledgementResponse', (_message.Message,), {
  'DESCRIPTOR' : _MSGACKNOWLEDGEMENTRESPONSE,
  '__module__' : 'ibc.core.channel.v1.tx_pb2'
  # @@protoc_insertion_point(class_scope:ibc.core.channel.v1.MsgAcknowledgementResponse)
  })
_sym_db.RegisterMessage(MsgAcknowledgementResponse)

_MSG = DESCRIPTOR.services_by_name['Msg']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z8github.com/cosmos/cosmos-sdk/x/ibc/core/04-channel/types'
  _MSGCHANNELOPENINIT.fields_by_name['port_id']._options = None
  _MSGCHANNELOPENINIT.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELOPENINIT.fields_by_name['channel']._options = None
  _MSGCHANNELOPENINIT.fields_by_name['channel']._serialized_options = b'\310\336\037\000'
  _MSGCHANNELOPENINIT._options = None
  _MSGCHANNELOPENINIT._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELOPENTRY.fields_by_name['port_id']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELOPENTRY.fields_by_name['previous_channel_id']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['previous_channel_id']._serialized_options = b'\362\336\037\032yaml:\"previous_channel_id\"'
  _MSGCHANNELOPENTRY.fields_by_name['channel']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['channel']._serialized_options = b'\310\336\037\000'
  _MSGCHANNELOPENTRY.fields_by_name['counterparty_version']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['counterparty_version']._serialized_options = b'\362\336\037\033yaml:\"counterparty_version\"'
  _MSGCHANNELOPENTRY.fields_by_name['proof_init']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['proof_init']._serialized_options = b'\362\336\037\021yaml:\"proof_init\"'
  _MSGCHANNELOPENTRY.fields_by_name['proof_height']._options = None
  _MSGCHANNELOPENTRY.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGCHANNELOPENTRY._options = None
  _MSGCHANNELOPENTRY._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELOPENACK.fields_by_name['port_id']._options = None
  _MSGCHANNELOPENACK.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELOPENACK.fields_by_name['channel_id']._options = None
  _MSGCHANNELOPENACK.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGCHANNELOPENACK.fields_by_name['counterparty_channel_id']._options = None
  _MSGCHANNELOPENACK.fields_by_name['counterparty_channel_id']._serialized_options = b'\362\336\037\036yaml:\"counterparty_channel_id\"'
  _MSGCHANNELOPENACK.fields_by_name['counterparty_version']._options = None
  _MSGCHANNELOPENACK.fields_by_name['counterparty_version']._serialized_options = b'\362\336\037\033yaml:\"counterparty_version\"'
  _MSGCHANNELOPENACK.fields_by_name['proof_try']._options = None
  _MSGCHANNELOPENACK.fields_by_name['proof_try']._serialized_options = b'\362\336\037\020yaml:\"proof_try\"'
  _MSGCHANNELOPENACK.fields_by_name['proof_height']._options = None
  _MSGCHANNELOPENACK.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGCHANNELOPENACK._options = None
  _MSGCHANNELOPENACK._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELOPENCONFIRM.fields_by_name['port_id']._options = None
  _MSGCHANNELOPENCONFIRM.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELOPENCONFIRM.fields_by_name['channel_id']._options = None
  _MSGCHANNELOPENCONFIRM.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGCHANNELOPENCONFIRM.fields_by_name['proof_ack']._options = None
  _MSGCHANNELOPENCONFIRM.fields_by_name['proof_ack']._serialized_options = b'\362\336\037\020yaml:\"proof_ack\"'
  _MSGCHANNELOPENCONFIRM.fields_by_name['proof_height']._options = None
  _MSGCHANNELOPENCONFIRM.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGCHANNELOPENCONFIRM._options = None
  _MSGCHANNELOPENCONFIRM._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELCLOSEINIT.fields_by_name['port_id']._options = None
  _MSGCHANNELCLOSEINIT.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELCLOSEINIT.fields_by_name['channel_id']._options = None
  _MSGCHANNELCLOSEINIT.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGCHANNELCLOSEINIT._options = None
  _MSGCHANNELCLOSEINIT._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELCLOSECONFIRM.fields_by_name['port_id']._options = None
  _MSGCHANNELCLOSECONFIRM.fields_by_name['port_id']._serialized_options = b'\362\336\037\016yaml:\"port_id\"'
  _MSGCHANNELCLOSECONFIRM.fields_by_name['channel_id']._options = None
  _MSGCHANNELCLOSECONFIRM.fields_by_name['channel_id']._serialized_options = b'\362\336\037\021yaml:\"channel_id\"'
  _MSGCHANNELCLOSECONFIRM.fields_by_name['proof_init']._options = None
  _MSGCHANNELCLOSECONFIRM.fields_by_name['proof_init']._serialized_options = b'\362\336\037\021yaml:\"proof_init\"'
  _MSGCHANNELCLOSECONFIRM.fields_by_name['proof_height']._options = None
  _MSGCHANNELCLOSECONFIRM.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGCHANNELCLOSECONFIRM._options = None
  _MSGCHANNELCLOSECONFIRM._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGRECVPACKET.fields_by_name['packet']._options = None
  _MSGRECVPACKET.fields_by_name['packet']._serialized_options = b'\310\336\037\000'
  _MSGRECVPACKET.fields_by_name['proof_commitment']._options = None
  _MSGRECVPACKET.fields_by_name['proof_commitment']._serialized_options = b'\362\336\037\027yaml:\"proof_commitment\"'
  _MSGRECVPACKET.fields_by_name['proof_height']._options = None
  _MSGRECVPACKET.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGRECVPACKET._options = None
  _MSGRECVPACKET._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGTIMEOUT.fields_by_name['packet']._options = None
  _MSGTIMEOUT.fields_by_name['packet']._serialized_options = b'\310\336\037\000'
  _MSGTIMEOUT.fields_by_name['proof_unreceived']._options = None
  _MSGTIMEOUT.fields_by_name['proof_unreceived']._serialized_options = b'\362\336\037\027yaml:\"proof_unreceived\"'
  _MSGTIMEOUT.fields_by_name['proof_height']._options = None
  _MSGTIMEOUT.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGTIMEOUT.fields_by_name['next_sequence_recv']._options = None
  _MSGTIMEOUT.fields_by_name['next_sequence_recv']._serialized_options = b'\362\336\037\031yaml:\"next_sequence_recv\"'
  _MSGTIMEOUT._options = None
  _MSGTIMEOUT._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGTIMEOUTONCLOSE.fields_by_name['packet']._options = None
  _MSGTIMEOUTONCLOSE.fields_by_name['packet']._serialized_options = b'\310\336\037\000'
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_unreceived']._options = None
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_unreceived']._serialized_options = b'\362\336\037\027yaml:\"proof_unreceived\"'
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_close']._options = None
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_close']._serialized_options = b'\362\336\037\022yaml:\"proof_close\"'
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_height']._options = None
  _MSGTIMEOUTONCLOSE.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGTIMEOUTONCLOSE.fields_by_name['next_sequence_recv']._options = None
  _MSGTIMEOUTONCLOSE.fields_by_name['next_sequence_recv']._serialized_options = b'\362\336\037\031yaml:\"next_sequence_recv\"'
  _MSGTIMEOUTONCLOSE._options = None
  _MSGTIMEOUTONCLOSE._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGACKNOWLEDGEMENT.fields_by_name['packet']._options = None
  _MSGACKNOWLEDGEMENT.fields_by_name['packet']._serialized_options = b'\310\336\037\000'
  _MSGACKNOWLEDGEMENT.fields_by_name['proof_acked']._options = None
  _MSGACKNOWLEDGEMENT.fields_by_name['proof_acked']._serialized_options = b'\362\336\037\022yaml:\"proof_acked\"'
  _MSGACKNOWLEDGEMENT.fields_by_name['proof_height']._options = None
  _MSGACKNOWLEDGEMENT.fields_by_name['proof_height']._serialized_options = b'\362\336\037\023yaml:\"proof_height\"\310\336\037\000'
  _MSGACKNOWLEDGEMENT._options = None
  _MSGACKNOWLEDGEMENT._serialized_options = b'\350\240\037\000\210\240\037\000'
  _MSGCHANNELOPENINIT._serialized_start=144
  _MSGCHANNELOPENINIT._serialized_end=280
  _MSGCHANNELOPENINITRESPONSE._serialized_start=282
  _MSGCHANNELOPENINITRESPONSE._serialized_end=310
  _MSGCHANNELOPENTRY._serialized_start=313
  _MSGCHANNELOPENTRY._serialized_end=694
  _MSGCHANNELOPENTRYRESPONSE._serialized_start=696
  _MSGCHANNELOPENTRYRESPONSE._serialized_end=723
  _MSGCHANNELOPENACK._serialized_start=726
  _MSGCHANNELOPENACK._serialized_end=1103
  _MSGCHANNELOPENACKRESPONSE._serialized_start=1105
  _MSGCHANNELOPENACKRESPONSE._serialized_end=1132
  _MSGCHANNELOPENCONFIRM._serialized_start=1135
  _MSGCHANNELOPENCONFIRM._serialized_end=1384
  _MSGCHANNELOPENCONFIRMRESPONSE._serialized_start=1386
  _MSGCHANNELOPENCONFIRMRESPONSE._serialized_end=1417
  _MSGCHANNELCLOSEINIT._serialized_start=1419
  _MSGCHANNELCLOSEINIT._serialized_end=1546
  _MSGCHANNELCLOSEINITRESPONSE._serialized_start=1548
  _MSGCHANNELCLOSEINITRESPONSE._serialized_end=1577
  _MSGCHANNELCLOSECONFIRM._serialized_start=1580
  _MSGCHANNELCLOSECONFIRM._serialized_end=1832
  _MSGCHANNELCLOSECONFIRMRESPONSE._serialized_start=1834
  _MSGCHANNELCLOSECONFIRMRESPONSE._serialized_end=1866
  _MSGRECVPACKET._serialized_start=1869
  _MSGRECVPACKET._serialized_end=2095
  _MSGRECVPACKETRESPONSE._serialized_start=2097
  _MSGRECVPACKETRESPONSE._serialized_end=2120
  _MSGTIMEOUT._serialized_start=2123
  _MSGTIMEOUT._serialized_end=2405
  _MSGTIMEOUTRESPONSE._serialized_start=2407
  _MSGTIMEOUTRESPONSE._serialized_end=2427
  _MSGTIMEOUTONCLOSE._serialized_start=2430
  _MSGTIMEOUTONCLOSE._serialized_end=2764
  _MSGTIMEOUTONCLOSERESPONSE._serialized_start=2766
  _MSGTIMEOUTONCLOSERESPONSE._serialized_end=2793
  _MSGACKNOWLEDGEMENT._serialized_start=2796
  _MSGACKNOWLEDGEMENT._serialized_end=3042
  _MSGACKNOWLEDGEMENTRESPONSE._serialized_start=3044
  _MSGACKNOWLEDGEMENTRESPONSE._serialized_end=3072
  _MSG._serialized_start=3075
  _MSG._serialized_end=4146
# @@protoc_insertion_point(module_scope)
