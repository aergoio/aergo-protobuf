# aergo-protobuf

This is a respository for the AERGO Protocol Buffers.

# Change rule

Protobuf recognize message as a key-value pair. So you __must not remove or reuse already occupied field number__. For example, you must not change protobuf in a following way:

```proto
// from
message sometype {
  bytes hash = 1;
  string name = 2;
}

// to
message sometype {
  string hash = 1; // please DO NOT reuse it
  string name = 2;
}
```

Rather change like this

```proto
message sometype {
  reserved 1;
  string name = 2;
  string hash = 3; // redefine field with a new field number
}
```

Follow these rules for backword compatibility. Remember that you should add any changes to the [CHANGELOG](./CHANGELOG.md).

## Add

Just add a new field (or message). Protobuf parser automatically ignore unknown fields. Client can check if unknown fields exists or not.

eg. somefile.proto
```
// from
message sometype {
  bytes hash = 1;
  string name = 2;
}

// to
message sometype {
  bytes hash = 1;
  string name = 2;
  bytes payload = 3; // just add it
}
```

Add following line to the changelog
```md
+ somefile.proto::sometype::payload (type: bytes, fieldNo: 3)
```

## Remove

Just remove field. Remember that you should not reorder the field numbers.

eg. somefile.proto
```
// from
message sometype {
  bytes hash = 1;
  string name = 2;
  bytes payload = 3;
}

// to
message sometype {
  reserved 1;  // left already occupied field number
  string name = 2;
  bytes payload = 3;
}
```

Add following line to the changelog
```md
- somefile.proto::sometype::hash (type: bytes, fieldNo: 1)
```

## Update (Remove + Add)

Just a combination of remove & add

eg. somefile.proto
```
// from
message sometype {
  bytes hash = 1;
  string name = 2;
}

// to
message sometype {
  reserved 1;  // left already occupied field number
  string name = 2;
  string hash = 3; // add a field with an new number
}
```

Add following lines to the changelog
```md
- somefile.proto::sometype::hash (type: bytes, fieldNo: 1)
+ somefile.proto::sometype::hash (type: string, fieldNo: 3)
```

see also
* [updating message type in proto3](https://developers.google.com/protocol-buffers/docs/proto3#updating)
* [protobuf message structure](https://developers.google.com/protocol-buffers/docs/encoding#structure)
