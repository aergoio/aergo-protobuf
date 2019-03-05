# aergo-protobuf

This respository stores the AERGO Protocol Buffer definitions that are used by different server and client implementations.

## Change rule

Protobuffer recognizes messages as ordered key-value pairs.
You __must not remove or reuse already occupied field numbers__.
For example, you must not change protobuf in a following way:

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

Rather change like this:

```proto
message sometype {
  reserved 1;
  string name = 2;
  string hash = 3; // redefine field with a new field number
}
```

Follow these rules for backwards compatibility. Remember that you should add any changes to the [CHANGELOG](./CHANGELOG.md).

### Add

Just add a new field (or message).
Assing additional fields does not break backwards compatability, as protobuffer parser automatically ignores unknown fields.
A client can check if unknown fields exists or not.

Example: somefile.proto
```proto
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

Please add the following line to the changelog:
```diff
+ somefile.proto::sometype::payload (type: bytes, fieldNo: 3)
```

### Remove

Please do not just remove a field, as this breaks backwards compatability.
You can keep removed fields as "reserved". Remember that you should not reorder the field numbers.

Example: somefile.proto
```proto
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

Add the following line to the changelog:
```diff
- somefile.proto::sometype::hash (type: bytes, fieldNo: 1)
```

### Update (Remove + Add)

Just a combination of remove and add.

Example: somefile.proto
```proto
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

Add the following lines to the changelog:
```diff
- somefile.proto::sometype::hash (type: bytes, fieldNo: 1)
+ somefile.proto::sometype::hash (type: string, fieldNo: 3)
```

### See also

* [Reserved fields in proto3](https://developers.google.com/protocol-buffers/docs/proto3#reserved)
* [Updating message type in proto3](https://developers.google.com/protocol-buffers/docs/proto3#updating)
* [Protobuf message structure](https://developers.google.com/protocol-buffers/docs/encoding#structure)
