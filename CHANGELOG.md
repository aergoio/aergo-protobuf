# Changelog

## 2.0.0 (November 25, 2019)

```diff
+ blockchain.proto::BlockHeader::consensus (type: bytes, fieldNo: 12)
+ blockchain.proto::TxType::FEEDELEGATION (3)
+ blockchain.proto::TxType::TRANSFER (4)
+ blockchain.proto::TxType::CALL (5)
+ blockchain.proto::TxType::DEPLOY (6)
+ blockchain.proto::Receipt::feeDelegation (type: bool, fieldNo: 14)
+ blockchain.proto::Receipt::gasUsed (type: uint64, fieldNo: 15)
+ blockchain.proto::Function::fee_delegation (type: bool, fieldNo: 5)
+ blockchain.proto::Proposal

+ node.proto::PeerRole
+ node.proto::PeerAddress::role (type: PeerRole, fieldNo: 4)
+ node.proto::PeerAddress::version (type: string, fieldNo: 5)
+ node.proto::PeerAddress::addresses (type: repeated string, fieldNo: 6)
+ node.proto::PeerAddress::producerIDs (type: repeated bytes, fieldNo: 7)
+ node.proto::AgentCertificate

+ p2p.proto::Status::certificates (type: repeated AgentCertificate, fieldNo: 8)
+ p2p.proto::Status::issueCertificate (type: bool, fieldNo: 9)
+ p2p.proto::IssueCertificateRequest
+ p2p.proto::IssueCertificateResponse
+ p2p.proto::CertificateRenewedNotice

+ rpc.proto::ChainId::version (type: int32, fieldNo: 5)
+ rpc.proto::Peer::certificates (type: repeated AgentCertificate, fieldNo: 8)
+ rpc.proto::Peer::acceptedRole (type: PeerRole, fieldNo: 9)
- rpc.proto::VoteInfo::id (type: string, fieldNo: 2)
- rpc.proto::VoteInfo::candidates (type: repeated string, fieldNo: 3)
+ rpc.proto::VoteInfo::id (type: string, fieldNo: 1)
+ rpc.proto::VoteInfo::candidates (type: repeated string, fieldNo: 2)
+ rpc.proto::VoteInfo::amount (type: string, fieldNo: 3)
```

## 1.3.0 (June 4, 2019)

```diff
+ polarrpc.proto::BLConfEntries
+ polarrpc.proto::AddEntryParams
+ polarrpc.proto::RmEntryParams

+ rpc.proto::SingleString
```

## 1.2.0 (June 4, 2019)
```diff
+ blockchain.proto::TxType::REDEPLOY (2)
- blockchain.proto::TxType::key (type: string, fieldNo: 3)
+ blockchain.proto::TxType::key (type: bytes, fieldNo: 9)
- blockchain.proto::StateQuery::storageKeys (type: repeated string, fieldNo: 2)
+ blockchain.proto::StateQuery::storageKeys (type: repeated bytes, fieldNo: 5)

+ p2p.proto::Status::genesis (type: bytes, fieldNo: 7)

- raft.proto::MemberAttr::url (type: string, fieldNo: 3)
+ raft.proto::MemberAttr::address (type: string, fieldNo: 3)
- raft.proto::MembershipChange::attr (type: MemberAttr, fieldNo: 2)
+ raft.proto::MembershipChange::requestID (type: uint64, fieldNo: 2)
+ raft.proto::MembershipChange::attr (type: MemberAttr, fieldNo: 3)
+ raft.proto::HardStateInfo
+ raft.proto::GetClusterInfoRequest::bestBlockHash (type: bytes, fieldNo: 1)
- raft.proto::GetClusterInfoResponse::error (type: string, fieldNo: 2)
- raft.proto::GetClusterInfoResponse::mbrAttrs (type: repeated MemberAttr, fieldNo: 3)
+ raft.proto::GetClusterInfoResponse::clusterID (type: uint64, fieldNo: 2)
+ raft.proto::GetClusterInfoResponse::error (type: string, fieldNo: 3)
+ raft.proto::GetClusterInfoResponse::mbrAttrs (type: repeated MemberAttr, fieldNo: 4)
+ raft.proto::GetClusterInfoResponse::bestBlockNo (type: uint64, fieldNo: 5)
+ raft.proto::GetClusterInfoResponse::hardStateInfo (type: HardStateInfo, fieldNo: 6)
+ raft.proto::ConfChangeState
+ raft.proto::ConfChangeProgress
+ raft.proto::SnapshotResponse

+ rpc.proto::AergoRPCService::GetEnterpriseConfig (arg: EnterpriseConfigKey, ret: EnterpriseConfig)
+ rpc.proto::AergoRPCService::GetConfChangeProgress (arg: SingleBytes, ret: ConfChangeProgress)
+ rpc.proto::BlockchainStatus::chain_info (type: ChainInfo, fieldNo: 5)
+ rpc.proto::EnterpriseConfigKey
+ rpc.proto::EnterpriseConfig
```

## 1.1.0 (June 4, 2019)

```diff
+ p2p.proto::Status::version (type: string, fieldNo: 6)
- p2p.proto::GetMissingResponse

+ polarrpc.proto::PolarisPeer::verion (type: string, fieldNo: 4)

+ raft.proto::MembershipChangeType
+ raft.proto::MemberAttr
+ raft.proto::MembershipChange
+ raft.proto::MembershipChangeReply
+ raft.proto::GetClusterInfoRequest
+ raft.proto::GetClusterInfoResponse

+ rpc.proto::AergoRPCService::ChainStat (arg: Empty, ret: ChainStats)
+ rpc.proto::AergoRPCService::ChangeMembership (arg: MembershipChange, ret: MembershipChangeReply)
+ rpc.proto::ChainStats
+ rpc.proto::Peer::version (type: string, fieldNo: 7)
+ rpc.proto::BlockMetadata::size (type: int64, fieldNo: 4)
+ rpc.proto::Name::blockNo (type: uint64, fieldNo: 2)
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

+ p2p.proto::Status::noExpose (type: bool, fieldNo: 5)

- rpc.proto::AergoRPCService::GetVotes (arg: SingleBytes, ret: VoteList)
+ rpc.proto::AergoRPCService::GetVotes (arg: VoteParams, ret: VoteList)
+ rpc.proto::AergoRPCService::GetAccountVotes (arg: AccountAddress, ret: AccountVoteInfo)
- rpc.proto::AergoRPCService::GetStaking (arg: SingleBytes, ret: Staking)
+ rpc.proto::AergoRPCService::GetStaking (arg: AccountAddress, ret: Staking)
+ rpc.proto::AergoRPCService::GetServerInfo (arg: KeyParams, ret: ServerInfo)
+ rpc.proto::AergoRPCService::GetConsensusInfo (arg: Empty, ret: ConsensusInfo)
+ rpc.proto::BlockchainStatus::consensus_info (type: string, fieldNo: 3)
+ rpc.proto::BlockchainStatus::best_chain_id_hash (type: bytes, fieldNo: 4)
- rpc.proto::ChainId::coinbasefee (type: bytes, fieldNo: 4)
- rpc.proto::ChainId::consensus (type: string, fieldNo: 5)
+ rpc.proto::ChainId::consensus (type: string, fieldNo: 4)
- rpc.proto::ChainInfo::chainid (type: ChainId, fieldNo: 1)
- rpc.proto::ChainInfo::bpnumber (type: uint32, fieldNo: 2)
+ rpc.proto::ChainInfo::id (type: ChainId, fieldNo: 1)
+ rpc.proto::ChainInfo::bpNumber (type: uint32, fieldNo: 2)
+ rpc.proto::ChainInfo::totalstaking (type: bytes, fieldNo: 6)
+ rpc.proto::ChainInfo::gasprice (type: bytes, fieldNo: 7)
+ rpc.proto::ChainInfo::nameprice (type: bytes, fieldNo: 8)
+ rpc.proto::AccountAddress
+ rpc.proto::VoteParams
+ rpc.proto::AccountVoteInfo
+ rpc.proto::VoteInfo
+ rpc.proto::VoteList::id (type: string, fieldNo: 2)
+ rpc.proto::KeyParams
+ rpc.proto::ServerInfo
+ rpc.proto::ConfigItem
+ rpc.proto::ConsensusInfo
```

## 0.12.0 (March 5, 2019)

```diff
+ blockchain.proto::Receipt::txHash (type: bytes, fieldNo: 4)
+ blockchain.proto::Receipt::feeUsed (type: bytes, fieldNo: 5)
+ blockchain.proto::Receipt::cumulativeFeeUsed (type: bytes, fieldNo: 6)
+ blockchain.proto::Receipt::bloom (type: bytes, fieldNo: 7)
+ blockchain.proto::Receipt::events (type: repeated Event, fieldNo: 8)
+ blockchain.proto::Receipt::blockNo (type: uint64, fieldNo: 9)
+ blockchain.proto::Receipt::blockHash (type: bytes, fieldNo: 10)
+ blockchain.proto::Receipt::txIndex (type: int32, fieldNo: 11)
+ blockchain.proto::Receipt::from (type: bytes, fieldNo: 12)
+ blockchain.proto::Receipt::to (type: bytes, fieldNo: 13)
+ blockchain.proto::Event
+ blockchain.proto::FilterInfo

- rpc.proto::AergoRPCService::GetPeers (arg: Empty, ret: PeerList)
+ rpc.proto::AergoRPCService::GetPeers (arg: PeersParams, ret: PeerList)
+ rpc.proto::AergoRPCService::ListEventStream (arg: FilterInfo, ret: stream Event)
+ rpc.proto::AergoRPCService::ListEvents (arg: FilterInfo, ret: EventList)
+ rpc.proto::Peer::selfpeer (type: bool, fieldNo: 6)
+ rpc.proto::NameInfo::destination (type: bytes, fieldNo: 3)
+ rpc.proto::PeersParams
+ rpc.proto::EventList
```

## 0.11.0 (February 8, 2019)

```diff
- blockchain.proto::StateProof
+ blockchain.proto::AccountProof
- blockchain.proto::StateQueryProof::contractProof (type: StateProof, fieldNo: 1)
- blockchain.proto::StateQueryProof::varProof (type: ContractVarProof, fieldNo: 2)
+ blockchain.proto::StateQueryProof::contractProof (type: AccountProof, fieldNo: 1)
+ blockchain.proto::StateQueryProof::varProofs (type: repeated ContractVarProof, fieldNo: 2)
- blockchain.proto::StateQuery::varName (type: string, fieldNo: 2)
- blockchain.proto::StateQuery::varIndex (type: string, fieldNo: 3)
- blockchain.proto::StateQuery::root (type: bytes, fieldNo: 4)
- blockchain.proto::StateQuery::compressed (type: bool, fieldNo: 5)
+ blockchain.proto::StateQuery::storageKeys (type: repeated string, fieldNo: 2)
+ blockchain.proto::StateQuery::root (type: bytes, fieldNo: 3)
+ blockchain.proto::StateQuery::compressed (type: bool, fieldNo: 4)

+ rpc.proto::AergoRPCService::GetChainInfo (arg: Empty, ret: ChainInfo)
+ rpc.proto::AergoRPCService::GetBlockMetadata (arg: SingleBytes, ret: BlockMetadata)
+ rpc.proto::AergoRPCService::GetBlockBody (arg: BlockBodyParams, ret: BlockBodyPaged)
- rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: StateProof)
+ rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: AccountProof)
+ rpc.proto::ChainId
+ rpc.proto::ChainInfo
+ rpc.proto::Peer::lashCheck (type: int64, fieldNo: 5)
+ rpc.proto::PageParams
+ rpc.proto::BlockBodyPaged
+ rpc.proto::BlockBodyParams
```

## 0.10.0 (January 23, 2019)

```diff
- node.proto::PeerAddress::address (type: bytes, fieldNo: 1)
+ node.proto::PeerAddress::address (type: string, fieldNo: 1)

+ polarrpc.proto::PolarisRPCService
+ polarrpc.proto::Paginations
+ polarrpc.proto::PolarisPeerList
+ polarrpc.proto::PolarisPeer

+ rpc.proto::Peer::hidden (type: bool, fieldNo: 4)
```

## 0.9.5 (December 27, 2018)

```diff
+ p2p.proto::Status::chainID (type: bytes, fieldNo: 4)

+ pmap.proto::MapResponse::message (type: string, fieldNo: 3)
```

## 0.9.4 (December 21, 2018)

```diff
+ p2p.proto::BlockProducedNotice

+ pmap.proto::MapQuery
+ pmap.proto::MapResponse
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
