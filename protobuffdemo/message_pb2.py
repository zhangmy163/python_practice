# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='model',
  syntax='proto3',
  serialized_options=b'\n\031com.datatreker.inti.modelB\016MessageFactoryZ\005model',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rmessage.proto\x12\x05model\"\xb0\x03\n\x07Message\x12\x0b\n\x03\x63id\x18\x01 \x01(\t\x12\x0b\n\x03uid\x18\x02 \x01(\t\x12\x0b\n\x03sid\x18\x03 \x01(\t\x12\x0e\n\x06\x64omain\x18\x04 \x01(\t\x12.\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x1d.model.Message.MessageContext\x12,\n\x06packet\x18\x06 \x03(\x0b\x32\x1c.model.Message.MessagePacket\x1aM\n\x0eMessageContext\x12\n\n\x02ln\x18\x01 \x01(\t\x12\n\n\x02lv\x18\x02 \x01(\t\x12\n\n\x02ip\x18\x03 \x01(\t\x12\x0b\n\x03ref\x18\x04 \x01(\t\x12\n\n\x02ua\x18\x05 \x01(\t\x1a\xc0\x01\n\rMessagePacket\x12\x0b\n\x03vid\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\x03\x12\x0e\n\x06status\x18\x03 \x01(\x05\x12\x0c\n\x04size\x18\x04 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x05 \x01(\x0c\x12:\n\x07payload\x18\x06 \x03(\x0b\x32).model.Message.MessagePacket.PayloadEntry\x1a.\n\x0cPayloadEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c:\x02\x38\x01\x42\x32\n\x19\x63om.datatreker.inti.modelB\x0eMessageFactoryZ\x05modelb\x06proto3'
)




_MESSAGE_MESSAGECONTEXT = _descriptor.Descriptor(
  name='MessageContext',
  full_name='model.Message.MessageContext',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ln', full_name='model.Message.MessageContext.ln', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lv', full_name='model.Message.MessageContext.lv', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='model.Message.MessageContext.ip', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ref', full_name='model.Message.MessageContext.ref', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ua', full_name='model.Message.MessageContext.ua', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=185,
  serialized_end=262,
)

_MESSAGE_MESSAGEPACKET_PAYLOADENTRY = _descriptor.Descriptor(
  name='PayloadEntry',
  full_name='model.Message.MessagePacket.PayloadEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='model.Message.MessagePacket.PayloadEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='model.Message.MessagePacket.PayloadEntry.value', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=411,
  serialized_end=457,
)

_MESSAGE_MESSAGEPACKET = _descriptor.Descriptor(
  name='MessagePacket',
  full_name='model.Message.MessagePacket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='vid', full_name='model.Message.MessagePacket.vid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ts', full_name='model.Message.MessagePacket.ts', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='model.Message.MessagePacket.status', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='size', full_name='model.Message.MessagePacket.size', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='model.Message.MessagePacket.data', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='payload', full_name='model.Message.MessagePacket.payload', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_MESSAGEPACKET_PAYLOADENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=265,
  serialized_end=457,
)

_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='model.Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cid', full_name='model.Message.cid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='uid', full_name='model.Message.uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sid', full_name='model.Message.sid', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='domain', full_name='model.Message.domain', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='context', full_name='model.Message.context', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='packet', full_name='model.Message.packet', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_MESSAGE_MESSAGECONTEXT, _MESSAGE_MESSAGEPACKET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=457,
)

_MESSAGE_MESSAGECONTEXT.containing_type = _MESSAGE
_MESSAGE_MESSAGEPACKET_PAYLOADENTRY.containing_type = _MESSAGE_MESSAGEPACKET
_MESSAGE_MESSAGEPACKET.fields_by_name['payload'].message_type = _MESSAGE_MESSAGEPACKET_PAYLOADENTRY
_MESSAGE_MESSAGEPACKET.containing_type = _MESSAGE
_MESSAGE.fields_by_name['context'].message_type = _MESSAGE_MESSAGECONTEXT
_MESSAGE.fields_by_name['packet'].message_type = _MESSAGE_MESSAGEPACKET
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {

  'MessageContext' : _reflection.GeneratedProtocolMessageType('MessageContext', (_message.Message,), {
    'DESCRIPTOR' : _MESSAGE_MESSAGECONTEXT,
    '__module__' : 'message_pb2'
    # @@protoc_insertion_point(class_scope:model.Message.MessageContext)
    })
  ,

  'MessagePacket' : _reflection.GeneratedProtocolMessageType('MessagePacket', (_message.Message,), {

    'PayloadEntry' : _reflection.GeneratedProtocolMessageType('PayloadEntry', (_message.Message,), {
      'DESCRIPTOR' : _MESSAGE_MESSAGEPACKET_PAYLOADENTRY,
      '__module__' : 'message_pb2'
      # @@protoc_insertion_point(class_scope:model.Message.MessagePacket.PayloadEntry)
      })
    ,
    'DESCRIPTOR' : _MESSAGE_MESSAGEPACKET,
    '__module__' : 'message_pb2'
    # @@protoc_insertion_point(class_scope:model.Message.MessagePacket)
    })
  ,
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:model.Message)
  })
_sym_db.RegisterMessage(Message)
_sym_db.RegisterMessage(Message.MessageContext)
_sym_db.RegisterMessage(Message.MessagePacket)
_sym_db.RegisterMessage(Message.MessagePacket.PayloadEntry)


DESCRIPTOR._options = None
_MESSAGE_MESSAGEPACKET_PAYLOADENTRY._options = None
# @@protoc_insertion_point(module_scope)
