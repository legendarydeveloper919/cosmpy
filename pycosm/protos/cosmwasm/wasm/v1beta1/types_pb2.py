# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cosmwasm/wasm/v1beta1/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2

from pycosm.protos.cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from pycosm.protos.gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2

DESCRIPTOR = _descriptor.FileDescriptor(
    name="cosmwasm/wasm/v1beta1/types.proto",
    package="cosmwasm.wasm.v1beta1",
    syntax="proto3",
    serialized_options=b"Z&github.com/CosmWasm/wasmd/x/wasm/types\310\341\036\000\250\342\036\001",
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n!cosmwasm/wasm/v1beta1/types.proto\x12\x15\x63osmwasm.wasm.v1beta1\x1a\x19\x63osmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x19google/protobuf/any.proto"[\n\x0f\x41\x63\x63\x65ssTypeParam\x12\x42\n\x05value\x18\x01 \x01(\x0e\x32!.cosmwasm.wasm.v1beta1.AccessTypeB\x10\xf2\xde\x1f\x0cyaml:"value":\x04\x98\xa0\x1f\x01"\x87\x01\n\x0c\x41\x63\x63\x65ssConfig\x12L\n\npermission\x18\x01 \x01(\x0e\x32!.cosmwasm.wasm.v1beta1.AccessTypeB\x15\xf2\xde\x1f\x11yaml:"permission"\x12#\n\x07\x61\x64\x64ress\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address":\x04\x98\xa0\x1f\x01"\xa3\x02\n\x06Params\x12\x62\n\x12\x63ode_upload_access\x18\x01 \x01(\x0b\x32#.cosmwasm.wasm.v1beta1.AccessConfigB!\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"code_upload_access"\x12t\n\x1einstantiate_default_permission\x18\x02 \x01(\x0e\x32!.cosmwasm.wasm.v1beta1.AccessTypeB)\xf2\xde\x1f%yaml:"instantiate_default_permission"\x12\x39\n\x12max_wasm_code_size\x18\x03 \x01(\x04\x42\x1d\xf2\xde\x1f\x19yaml:"max_wasm_code_size":\x04\x98\xa0\x1f\x00"\x96\x01\n\x08\x43odeInfo\x12\x11\n\tcode_hash\x18\x01 \x01(\x0c\x12\x0f\n\x07\x63reator\x18\x02 \x01(\t\x12\x0e\n\x06source\x18\x03 \x01(\t\x12\x0f\n\x07\x62uilder\x18\x04 \x01(\t\x12\x45\n\x12instantiate_config\x18\x05 \x01(\x0b\x32#.cosmwasm.wasm.v1beta1.AccessConfigB\x04\xc8\xde\x1f\x00"\x84\x02\n\x0c\x43ontractInfo\x12\x1b\n\x07\x63ode_id\x18\x01 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12\x0f\n\x07\x63reator\x18\x02 \x01(\t\x12\r\n\x05\x61\x64min\x18\x03 \x01(\t\x12\r\n\x05label\x18\x04 \x01(\t\x12:\n\x07\x63reated\x18\x05 \x01(\x0b\x32).cosmwasm.wasm.v1beta1.AbsoluteTxPosition\x12"\n\x0bibc_port_id\x18\x06 \x01(\tB\r\xe2\xde\x1f\tIBCPortID\x12\x42\n\textension\x18\x07 \x01(\x0b\x32\x14.google.protobuf.AnyB\x19\xca\xb4-\x15\x43ontractInfoExtension:\x04\xe8\xa0\x1f\x01"\xea\x01\n\x18\x43ontractCodeHistoryEntry\x12J\n\toperation\x18\x01 \x01(\x0e\x32\x37.cosmwasm.wasm.v1beta1.ContractCodeHistoryOperationType\x12\x1b\n\x07\x63ode_id\x18\x02 \x01(\x04\x42\n\xe2\xde\x1f\x06\x43odeID\x12:\n\x07updated\x18\x03 \x01(\x0b\x32).cosmwasm.wasm.v1beta1.AbsoluteTxPosition\x12)\n\x03msg\x18\x04 \x01(\x0c\x42\x1c\xfa\xde\x1f\x18\x65ncoding/json.RawMessage"<\n\x12\x41\x62soluteTxPosition\x12\x14\n\x0c\x62lock_height\x18\x01 \x01(\x04\x12\x10\n\x08tx_index\x18\x02 \x01(\x04"]\n\x05Model\x12\x45\n\x03key\x18\x01 \x01(\x0c\x42\x38\xfa\xde\x1f\x34github.com/tendermint/tendermint/libs/bytes.HexBytes\x12\r\n\x05value\x18\x02 \x01(\x0c*\xe9\x01\n\nAccessType\x12\x36\n\x17\x41\x43\x43\x45SS_TYPE_UNSPECIFIED\x10\x00\x1a\x19\x8a\x9d \x15\x41\x63\x63\x65ssTypeUnspecified\x12,\n\x12\x41\x43\x43\x45SS_TYPE_NOBODY\x10\x01\x1a\x14\x8a\x9d \x10\x41\x63\x63\x65ssTypeNobody\x12\x37\n\x18\x41\x43\x43\x45SS_TYPE_ONLY_ADDRESS\x10\x02\x1a\x19\x8a\x9d \x15\x41\x63\x63\x65ssTypeOnlyAddress\x12\x32\n\x15\x41\x43\x43\x45SS_TYPE_EVERYBODY\x10\x03\x1a\x17\x8a\x9d \x13\x41\x63\x63\x65ssTypeEverybody\x1a\x08\x88\xa3\x1e\x00\xa8\xa4\x1e\x00*\xa6\x03\n ContractCodeHistoryOperationType\x12\x65\n0CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED\x10\x00\x1a/\x8a\x9d +ContractCodeHistoryOperationTypeUnspecified\x12W\n)CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT\x10\x01\x1a(\x8a\x9d $ContractCodeHistoryOperationTypeInit\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE\x10\x02\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeMigrate\x12]\n,CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS\x10\x03\x1a+\x8a\x9d \'ContractCodeHistoryOperationTypeGenesis\x1a\x04\x88\xa3\x1e\x00\x42\x30Z&github.com/CosmWasm/wasmd/x/wasm/types\xc8\xe1\x1e\x00\xa8\xe2\x1e\x01\x62\x06proto3',
    dependencies=[
        cosmos__proto_dot_cosmos__pb2.DESCRIPTOR,
        gogoproto_dot_gogo__pb2.DESCRIPTOR,
        google_dot_protobuf_dot_any__pb2.DESCRIPTOR,
    ],
)

_ACCESSTYPE = _descriptor.EnumDescriptor(
    name="AccessType",
    full_name="cosmwasm.wasm.v1beta1.AccessType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=b"\212\235 \025AccessTypeUnspecified",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TYPE_NOBODY",
            index=1,
            number=1,
            serialized_options=b"\212\235 \020AccessTypeNobody",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TYPE_ONLY_ADDRESS",
            index=2,
            number=2,
            serialized_options=b"\212\235 \025AccessTypeOnlyAddress",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="ACCESS_TYPE_EVERYBODY",
            index=3,
            number=3,
            serialized_options=b"\212\235 \023AccessTypeEverybody",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=b"\210\243\036\000\250\244\036\000",
    serialized_start=1472,
    serialized_end=1705,
)
_sym_db.RegisterEnumDescriptor(_ACCESSTYPE)

AccessType = enum_type_wrapper.EnumTypeWrapper(_ACCESSTYPE)
_CONTRACTCODEHISTORYOPERATIONTYPE = _descriptor.EnumDescriptor(
    name="ContractCodeHistoryOperationType",
    full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryOperationType",
    filename=None,
    file=DESCRIPTOR,
    create_key=_descriptor._internal_create_key,
    values=[
        _descriptor.EnumValueDescriptor(
            name="CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED",
            index=0,
            number=0,
            serialized_options=b"\212\235 +ContractCodeHistoryOperationTypeUnspecified",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT",
            index=1,
            number=1,
            serialized_options=b"\212\235 $ContractCodeHistoryOperationTypeInit",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE",
            index=2,
            number=2,
            serialized_options=b"\212\235 'ContractCodeHistoryOperationTypeMigrate",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.EnumValueDescriptor(
            name="CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS",
            index=3,
            number=3,
            serialized_options=b"\212\235 'ContractCodeHistoryOperationTypeGenesis",
            type=None,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    containing_type=None,
    serialized_options=b"\210\243\036\000",
    serialized_start=1708,
    serialized_end=2130,
)
_sym_db.RegisterEnumDescriptor(_CONTRACTCODEHISTORYOPERATIONTYPE)

ContractCodeHistoryOperationType = enum_type_wrapper.EnumTypeWrapper(
    _CONTRACTCODEHISTORYOPERATIONTYPE
)
ACCESS_TYPE_UNSPECIFIED = 0
ACCESS_TYPE_NOBODY = 1
ACCESS_TYPE_ONLY_ADDRESS = 2
ACCESS_TYPE_EVERYBODY = 3
CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED = 0
CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT = 1
CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE = 2
CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS = 3


_ACCESSTYPEPARAM = _descriptor.Descriptor(
    name="AccessTypeParam",
    full_name="cosmwasm.wasm.v1beta1.AccessTypeParam",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="value",
            full_name="cosmwasm.wasm.v1beta1.AccessTypeParam.value",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\014yaml:"value"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\230\240\037\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=136,
    serialized_end=227,
)


_ACCESSCONFIG = _descriptor.Descriptor(
    name="AccessConfig",
    full_name="cosmwasm.wasm.v1beta1.AccessConfig",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="permission",
            full_name="cosmwasm.wasm.v1beta1.AccessConfig.permission",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\021yaml:"permission"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="address",
            full_name="cosmwasm.wasm.v1beta1.AccessConfig.address",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\016yaml:"address"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\230\240\037\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=230,
    serialized_end=365,
)


_PARAMS = _descriptor.Descriptor(
    name="Params",
    full_name="cosmwasm.wasm.v1beta1.Params",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code_upload_access",
            full_name="cosmwasm.wasm.v1beta1.Params.code_upload_access",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\310\336\037\000\362\336\037\031yaml:"code_upload_access"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="instantiate_default_permission",
            full_name="cosmwasm.wasm.v1beta1.Params.instantiate_default_permission",
            index=1,
            number=2,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037%yaml:"instantiate_default_permission"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="max_wasm_code_size",
            full_name="cosmwasm.wasm.v1beta1.Params.max_wasm_code_size",
            index=2,
            number=3,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b'\362\336\037\031yaml:"max_wasm_code_size"',
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\230\240\037\000",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=368,
    serialized_end=659,
)


_CODEINFO = _descriptor.Descriptor(
    name="CodeInfo",
    full_name="cosmwasm.wasm.v1beta1.CodeInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code_hash",
            full_name="cosmwasm.wasm.v1beta1.CodeInfo.code_hash",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="creator",
            full_name="cosmwasm.wasm.v1beta1.CodeInfo.creator",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="source",
            full_name="cosmwasm.wasm.v1beta1.CodeInfo.source",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="builder",
            full_name="cosmwasm.wasm.v1beta1.CodeInfo.builder",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="instantiate_config",
            full_name="cosmwasm.wasm.v1beta1.CodeInfo.instantiate_config",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\310\336\037\000",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=662,
    serialized_end=812,
)


_CONTRACTINFO = _descriptor.Descriptor(
    name="ContractInfo",
    full_name="cosmwasm.wasm.v1beta1.ContractInfo",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="code_id",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.code_id",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\342\336\037\006CodeID",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="creator",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.creator",
            index=1,
            number=2,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="admin",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.admin",
            index=2,
            number=3,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="label",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.label",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="created",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.created",
            index=4,
            number=5,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="ibc_port_id",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.ibc_port_id",
            index=5,
            number=6,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\342\336\037\tIBCPortID",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="extension",
            full_name="cosmwasm.wasm.v1beta1.ContractInfo.extension",
            index=6,
            number=7,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\312\264-\025ContractInfoExtension",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=b"\350\240\037\001",
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=815,
    serialized_end=1075,
)


_CONTRACTCODEHISTORYENTRY = _descriptor.Descriptor(
    name="ContractCodeHistoryEntry",
    full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="operation",
            full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry.operation",
            index=0,
            number=1,
            type=14,
            cpp_type=8,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="code_id",
            full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry.code_id",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\342\336\037\006CodeID",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="updated",
            full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry.updated",
            index=2,
            number=3,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="msg",
            full_name="cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry.msg",
            index=3,
            number=4,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\372\336\037\030encoding/json.RawMessage",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1078,
    serialized_end=1312,
)


_ABSOLUTETXPOSITION = _descriptor.Descriptor(
    name="AbsoluteTxPosition",
    full_name="cosmwasm.wasm.v1beta1.AbsoluteTxPosition",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="block_height",
            full_name="cosmwasm.wasm.v1beta1.AbsoluteTxPosition.block_height",
            index=0,
            number=1,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="tx_index",
            full_name="cosmwasm.wasm.v1beta1.AbsoluteTxPosition.tx_index",
            index=1,
            number=2,
            type=4,
            cpp_type=4,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1314,
    serialized_end=1374,
)


_MODEL = _descriptor.Descriptor(
    name="Model",
    full_name="cosmwasm.wasm.v1beta1.Model",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="key",
            full_name="cosmwasm.wasm.v1beta1.Model.key",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=b"\372\336\0374github.com/tendermint/tendermint/libs/bytes.HexBytes",
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="value",
            full_name="cosmwasm.wasm.v1beta1.Model.value",
            index=1,
            number=2,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=1376,
    serialized_end=1469,
)

_ACCESSTYPEPARAM.fields_by_name["value"].enum_type = _ACCESSTYPE
_ACCESSCONFIG.fields_by_name["permission"].enum_type = _ACCESSTYPE
_PARAMS.fields_by_name["code_upload_access"].message_type = _ACCESSCONFIG
_PARAMS.fields_by_name["instantiate_default_permission"].enum_type = _ACCESSTYPE
_CODEINFO.fields_by_name["instantiate_config"].message_type = _ACCESSCONFIG
_CONTRACTINFO.fields_by_name["created"].message_type = _ABSOLUTETXPOSITION
_CONTRACTINFO.fields_by_name[
    "extension"
].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONTRACTCODEHISTORYENTRY.fields_by_name[
    "operation"
].enum_type = _CONTRACTCODEHISTORYOPERATIONTYPE
_CONTRACTCODEHISTORYENTRY.fields_by_name["updated"].message_type = _ABSOLUTETXPOSITION
DESCRIPTOR.message_types_by_name["AccessTypeParam"] = _ACCESSTYPEPARAM
DESCRIPTOR.message_types_by_name["AccessConfig"] = _ACCESSCONFIG
DESCRIPTOR.message_types_by_name["Params"] = _PARAMS
DESCRIPTOR.message_types_by_name["CodeInfo"] = _CODEINFO
DESCRIPTOR.message_types_by_name["ContractInfo"] = _CONTRACTINFO
DESCRIPTOR.message_types_by_name["ContractCodeHistoryEntry"] = _CONTRACTCODEHISTORYENTRY
DESCRIPTOR.message_types_by_name["AbsoluteTxPosition"] = _ABSOLUTETXPOSITION
DESCRIPTOR.message_types_by_name["Model"] = _MODEL
DESCRIPTOR.enum_types_by_name["AccessType"] = _ACCESSTYPE
DESCRIPTOR.enum_types_by_name[
    "ContractCodeHistoryOperationType"
] = _CONTRACTCODEHISTORYOPERATIONTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccessTypeParam = _reflection.GeneratedProtocolMessageType(
    "AccessTypeParam",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACCESSTYPEPARAM,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.AccessTypeParam)
    },
)
_sym_db.RegisterMessage(AccessTypeParam)

AccessConfig = _reflection.GeneratedProtocolMessageType(
    "AccessConfig",
    (_message.Message,),
    {
        "DESCRIPTOR": _ACCESSCONFIG,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.AccessConfig)
    },
)
_sym_db.RegisterMessage(AccessConfig)

Params = _reflection.GeneratedProtocolMessageType(
    "Params",
    (_message.Message,),
    {
        "DESCRIPTOR": _PARAMS,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.Params)
    },
)
_sym_db.RegisterMessage(Params)

CodeInfo = _reflection.GeneratedProtocolMessageType(
    "CodeInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CODEINFO,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.CodeInfo)
    },
)
_sym_db.RegisterMessage(CodeInfo)

ContractInfo = _reflection.GeneratedProtocolMessageType(
    "ContractInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTRACTINFO,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.ContractInfo)
    },
)
_sym_db.RegisterMessage(ContractInfo)

ContractCodeHistoryEntry = _reflection.GeneratedProtocolMessageType(
    "ContractCodeHistoryEntry",
    (_message.Message,),
    {
        "DESCRIPTOR": _CONTRACTCODEHISTORYENTRY,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.ContractCodeHistoryEntry)
    },
)
_sym_db.RegisterMessage(ContractCodeHistoryEntry)

AbsoluteTxPosition = _reflection.GeneratedProtocolMessageType(
    "AbsoluteTxPosition",
    (_message.Message,),
    {
        "DESCRIPTOR": _ABSOLUTETXPOSITION,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.AbsoluteTxPosition)
    },
)
_sym_db.RegisterMessage(AbsoluteTxPosition)

Model = _reflection.GeneratedProtocolMessageType(
    "Model",
    (_message.Message,),
    {
        "DESCRIPTOR": _MODEL,
        "__module__": "cosmwasm.wasm.v1beta1.types_pb2"
        # @@protoc_insertion_point(class_scope:cosmwasm.wasm.v1beta1.Model)
    },
)
_sym_db.RegisterMessage(Model)


DESCRIPTOR._options = None
_ACCESSTYPE._options = None
_ACCESSTYPE.values_by_name["ACCESS_TYPE_UNSPECIFIED"]._options = None
_ACCESSTYPE.values_by_name["ACCESS_TYPE_NOBODY"]._options = None
_ACCESSTYPE.values_by_name["ACCESS_TYPE_ONLY_ADDRESS"]._options = None
_ACCESSTYPE.values_by_name["ACCESS_TYPE_EVERYBODY"]._options = None
_CONTRACTCODEHISTORYOPERATIONTYPE._options = None
_CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name[
    "CONTRACT_CODE_HISTORY_OPERATION_TYPE_UNSPECIFIED"
]._options = None
_CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name[
    "CONTRACT_CODE_HISTORY_OPERATION_TYPE_INIT"
]._options = None
_CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name[
    "CONTRACT_CODE_HISTORY_OPERATION_TYPE_MIGRATE"
]._options = None
_CONTRACTCODEHISTORYOPERATIONTYPE.values_by_name[
    "CONTRACT_CODE_HISTORY_OPERATION_TYPE_GENESIS"
]._options = None
_ACCESSTYPEPARAM.fields_by_name["value"]._options = None
_ACCESSTYPEPARAM._options = None
_ACCESSCONFIG.fields_by_name["permission"]._options = None
_ACCESSCONFIG.fields_by_name["address"]._options = None
_ACCESSCONFIG._options = None
_PARAMS.fields_by_name["code_upload_access"]._options = None
_PARAMS.fields_by_name["instantiate_default_permission"]._options = None
_PARAMS.fields_by_name["max_wasm_code_size"]._options = None
_PARAMS._options = None
_CODEINFO.fields_by_name["instantiate_config"]._options = None
_CONTRACTINFO.fields_by_name["code_id"]._options = None
_CONTRACTINFO.fields_by_name["ibc_port_id"]._options = None
_CONTRACTINFO.fields_by_name["extension"]._options = None
_CONTRACTINFO._options = None
_CONTRACTCODEHISTORYENTRY.fields_by_name["code_id"]._options = None
_CONTRACTCODEHISTORYENTRY.fields_by_name["msg"]._options = None
_MODEL.fields_by_name["key"]._options = None
# @@protoc_insertion_point(module_scope)
