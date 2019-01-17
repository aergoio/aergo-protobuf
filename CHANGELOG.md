## Development (master)

* <span style="color:green">+ polarrpc.proto</span>
* <span style="color:green">+ rpc.proto::Peer::hidden (type: bool, fieldNo: 4)</span>
* <span style="color:red">- node.proto::PeerAddress::address (type: bytes, fieldNo: 1)</span>
* <span style="color:green">+ node.proto::PeerAddress::address (type: string, fieldNo: 1)</span>
* <span style="color:red">- blockchain.proto::StateProof (type: message)</span>
* <span style="color:green">+ blockchain.proto::AccountProof (type: message)</span>
* <span style="color:red">- blockchain.proto::ContractVarProof::key (type: string, fieldNo: 3)</span>
* <span style="color:red">- blockchain.proto::StateQueryProof::contractProof (type: StateProof, fieldNo: 1)</span>
* <span style="color:green">+ blockchain.proto::StateQueryProof::contractProof (type: AccountProof, fieldNo: 1)</span>
* <span style="color:red">- blockchain.proto::StateQueryProof::varProof (type: AccountProof, fieldNo: 2)</span>
* <span style="color:green">+ blockchain.proto::StateQueryProof::varProofs (type: repeated ContractVarProof, fieldNo: 2)</span>
* <span style="color:red">- blockchain.proto::StateQuery::varName (type: string, fieldNo: 2)</span>
* <span style="color:red">- blockchain.proto::StateQuery::varIndex (type: string, fieldNo: 3)</span>
* <span style="color:green">+ blockchain.proto::StateQuery::storageKeys (type: repeated string, fieldNo: 2)</span>
* <span style="color:red">- rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: StateProof)</span>
* <span style="color:green">+ rpc.proto::AergoRPCService::GetStateAndProof (arg: AccountAndRoot, ret: AccountProof)</span>

## 0.9.5 (December 27, 2018)

* <span style="color:green">+ p2p.proto::Status::chainId (type: bytes, fieldNo: 4)</span>
* <span style="color:green">+ mpap.proto::MapResponse::message (type: string, fieldNo: 3)</span>

## 0.9.4 (December 21, 2018)

* <span style="color:green">+ p2p.proto::BlockProducedNotice (type: message)</span>
* <span style="color:green">+ pmap.proto</span>

## 0.9.0 (December 19, 2018)

Start traking changes.
* <span style="color:green">+ account.proto</span>
* <span style="color:green">+ blockchain.proto</span>
* <span style="color:green">+ metric.proto</span>
* <span style="color:green">+ node.proto</span>
* <span style="color:green">+ p2p.proto</span>
* <span style="color:green">+ rpc.proto</span>