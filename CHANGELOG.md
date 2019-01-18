## Development (master)
```diff
+ polarrpc.proto

+ rpc.proto::Peer::hidden (type: bool, fieldNo: 4)
- node.proto::PeerAddress::address (type: bytes, fieldNo: 1)
+ node.proto::PeerAddress::address (type: string, fieldNo: 1)

- blockchain.proto::StateProof (type: message)
+ blockchain.proto::AccountProof (type: message)
- blockchain.proto::ContractVarProof::key (type: string, fieldNo: 3)
- blockchain.proto::StateQueryProof::contractProof (type: StateProof, fieldNo: 1)
+ blockchain.proto::StateQueryProof::contractProof (type: AccountProof, fieldNo: 1)
- blockchain.proto::StateQueryProof::varProof (type: AccountProof, fieldNo: 2)
+ blockchain.proto::StateQueryProof::varProofs (type: repeated ContractVarProof, fieldNo: 2)
- blockchain.proto::StateQuery::varName (type: string, fieldNo: 2)
- blockchain.proto::StateQuery::varIndex (type: string, fieldNo: 3)
+ blockchain.proto::StateQuery::storageKeys (type: repeated string, fieldNo: 2)
- rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: StateProof)
+ rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: AccountProof)

+ rpc.proto::AergoRPCService::GetBlockMetadata
+ rpc.proto::AergoRPCService::GetBlockBody
+ rpc.proto::PageParams (type: message)
+ rpc.proto::BlockBodyPaged (type: message)
+ rpc.proto::BlockBodyParams (type: message)
```

## 0.9.5 (December 27, 2018)
```diff
+ p2p.proto::Status::chainId (type: bytes, fieldNo: 4)
+ mpap.proto::MapResponse::message (type: string, fieldNo: 3)
```

## 0.9.4 (December 21, 2018)
```diff
+ p2p.proto::BlockProducedNotice (type: message)
+ pmap.proto
```

## 0.9.0 (December 19, 2018)

Start tracking changes.

```diff
+ account.proto
+ blockchain.proto
+ metric.proto
+ node.proto
+ p2p.proto
+ rpc.proto
```
