# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rmessage.proto\"+\n\x07\x41\x64\x64\x65nds\x12\x0f\n\x07\x61\x64\x64\x65nd1\x18\x01 \x01(\x02\x12\x0f\n\x07\x61\x64\x64\x65nd2\x18\x02 \x01(\x02\"\x12\n\x03Sum\x12\x0b\n\x03sum\x18\x01 \x01(\x02\x32*\n\x0c\x43\x61lculateSum\x12\x1a\n\x06my_sum\x12\x08.Addends\x1a\x04.Sum\"\x00\x62\x06proto3')
)




_ADDENDS = _descriptor.Descriptor(
  name='Addends',
  full_name='Addends',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addend1', full_name='Addends.addend1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addend2', full_name='Addends.addend2', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=17,
  serialized_end=60,
)


_SUM = _descriptor.Descriptor(
  name='Sum',
  full_name='Sum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sum', full_name='Sum.sum', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
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
  serialized_start=62,
  serialized_end=80,
)

DESCRIPTOR.message_types_by_name['Addends'] = _ADDENDS
DESCRIPTOR.message_types_by_name['Sum'] = _SUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Addends = _reflection.GeneratedProtocolMessageType('Addends', (_message.Message,), {
  'DESCRIPTOR' : _ADDENDS,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:Addends)
  })
_sym_db.RegisterMessage(Addends)

Sum = _reflection.GeneratedProtocolMessageType('Sum', (_message.Message,), {
  'DESCRIPTOR' : _SUM,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:Sum)
  })
_sym_db.RegisterMessage(Sum)



_CALCULATESUM = _descriptor.ServiceDescriptor(
  name='CalculateSum',
  full_name='CalculateSum',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=82,
  serialized_end=124,
  methods=[
  _descriptor.MethodDescriptor(
    name='my_sum',
    full_name='CalculateSum.my_sum',
    index=0,
    containing_service=None,
    input_type=_ADDENDS,
    output_type=_SUM,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATESUM)

DESCRIPTOR.services_by_name['CalculateSum'] = _CALCULATESUM

# @@protoc_insertion_point(module_scope)
