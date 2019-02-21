## master (unreleased)

```diff
+ blockchain.proto::Event (type: message)
+ blockchain.proto::FilterInfo (type: message)

+ blockchain.proto::Receipt::txHash (type: bytes, fieldNo: 4)
+ blockchain.proto::Receipt::feeUsed (type: bytes, fieldNo: 5)
+ blockchain.proto::Receipt::cumulativeFeeUsed (type: bytes, fieldNo: 6)
+ blockchain.proto::Receipt::bloom (type: bytes, fieldNo: 7)
+ blockchain.proto::Receipt::events (type: repeated Events, fieldNo: 8)
+ blockchain.proto::Receipt::blockNo (type: uint64, fieldNo: 9)
+ blockchain.proto::Receipt::blockHash (type: bytes, fieldNo: 10)
+ blockchain.proto::Receipt::txIndex (type: int32, fieldNo: 11)
+ blockchain.proto::Receipt::from (type: bytes, fieldNo: 12)
+ blockchain.proto::Receipt::to (type: bytes, fieldNo: 13)

+ rpc.proto::AergoRPCService::ListEventStream (arg: FilterInfo, ret: Event)
+ rpc.proto::AergoRPCService::ListEvent (arg: FilterInfo, ret: EventList)
+ rpc.proto::EventList (type: message)
```

## 0.11.0 (February 8, 2019)

```diff
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

+ rpc.proto::AergoRPCService::GetChainInfo
+ rpc.proto::ChainId (type: message)
+ rpc.proto::ChainInfo (type: message)

+ p2p.proto::Peer::lashCheck (type: int64, fieldNo: 5)
```

## 0.10.0 (January 23, 2019)
```diff
+ polarrpc.proto

+ rpc.proto::Peer::hidden (type: bool, fieldNo: 4)

- node.proto::PeerAddress::address (type: bytes, fieldNo: 1)
+ node.proto::PeerAddress::address (type: string, fieldNo: 1)
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

Started tracking changes.

```diff
+ account.proto
+ blockchain.proto
+ metric.proto
+ node.proto
+ p2p.proto
+ rpc.proto
```
