## master (unreleased)

```diff
+ blockchaon.proto::Block::size (type: int64, fieldNo: 4)
```

## 1.0.0 (April 1, 2019)

```diff
- blockchain.proto::TxBody::limit (type: uint64, fieldNo: 6)
- blockchain.proto::TxBody::price (type: bytes, fieldNo: 7)
+ blockchain.proto::TxBody::gasLimit (type: uint64, fieldNo: 6)
+ blockchain.proto::TxBody::gasPrice (type: bytes, fieldNo: 7)

- blockchain.proto::TxBody::sign (type: bytes, fieldNo: 9)
+ blockchain.proto::TxBody::chainIdHash (type: bytes, fieldNo: 9)
+ blockchain.proto::TxBody::sign (type: bytes, fieldNo: 10)

+ blockchain.proto::Function::payable (type: bool, fieldNo: 3)
+ blockchain.proto::Function::view (type: bool, fieldNo: 4)

+ blockchain.proto::StateVar::len (type: int32, fieldNo: 3)

- rpc.proto::AergoRPCService::GetVotes (arg: SingleBytes, ret: PeerList)
+ rpc.proto::AergoRPCService::GetVotes (arg: VoteParams, ret: PeerList)

+ rpc.proto::BlockchainStatus::consensus_info (type: string, fieldNo: 3)
+ rpc.proto::BlockchainStatus::best_chain_id_hash (type: string, fieldNo: 4)

- rpc.proto::ChainId::coinbasefee (type: bytes, fieldNo: 4)
- rpc.proto::ChainId::consensus (type: string, fieldNo: 5)
+ rpc.proto::ChainId::consensus (type: string, fieldNo: 4)

- rpc.proto::ChainId::chainid (type: ChainId, fieldNo: 1)
- rpc.proto::ChainId::bpnumber (type: uint32, fieldNo: 2)
+ rpc.proto::ChainId::id (type: ChainId, fieldNo: 1)
+ rpc.proto::ChainId::bpNumber (type: uint32, fieldNo: 2)
+ rpc.proto::ChainId::totalstaking (type: bytes, fieldNo: 6)
+ rpc.proto::ChainId::gasprice (type: bytes, fieldNo: 7)
+ rpc.proto::ChainId::nameprice (type: bytes, fieldNo: 8)

+ rpc.proto::ConsensusInfo
+ rpc.proto::AccountAddress
+ rpc.proto::VoteParams
+ rpc.proto::AccountVoteInfo
+ rpc.proto::VoteInfo
+ rpc.proto::VoteList::id (type: string, fieldNo: 2)
```

## 0.12.0 (March 5, 2019)

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

+ rpc.proto::PeersParams (type: message)
+ rpc.proto::Peer::selfpeer (type: boolean, fieldNo: 6)
- rpc.proto::AergoRPCService::GetPeers (arg: Empty, ret: PeerList)
+ rpc.proto::AergoRPCService::GetPeers (arg: PeersParams, ret: PeerList)

+ rpc.proto::NameInfo::destination (type: bytes, fieldNo: 3)
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
