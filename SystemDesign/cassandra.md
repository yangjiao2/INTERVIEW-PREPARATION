
[Uber](https://www.uber.com/blog/real-time-push-platform/)


## system


Netty: Netty is a widely used and high performance library to build network servers and clients. Netty’s bytebuf allows zero-copy buffers that make the system very efficient.

Apache ZooKeeper:
- a consistent hashing of network connections allows direct streaming of data without needing any storage layer in between
- distributed synchronization and configuration management and can detect failures of connected nodes quickly.

Apache Helix:
-  a robust cluster management framework that works on top of ZooKeeper
- allowing defining custom topologies and rebalancing algorithms
- uses ZooKeeper for monitoring of connected workers and propagating sharding state information change

Redis & Apache Cassandra (replication & storage):
- Cassandra is a durable and cross region replicated storage
- Redis was used as a capacity cache on top of Cassandra to avoid thundering herd problems commonly associated with the sharded systems on deployments or failover events.

[Thundering Herds & Promises](https://instagram-engineering.com/thundering-herds-promises-82191c8af57d)

![](./pics/thunder-herd.png)
 instead of caching the actual value, we cached a Promise that will eventually provide the value. When we use our cache atomically and get a miss, instead of going immediately to the backend we create a Promise and insert it into the cache. This new Promise then starts the work against the backend. The benefit this provides is other concurrent requests will not miss as they’ll find the existing Promise — and all these simultaneous workers will wait on the single backend request.


##  consistency

- **NetworkToplogyStrategy**
- no slave / server
- eventually consistent thus all nodes across all datacenters sees the same state only after few seconds


-  consistency level:
https://www.baeldung.com/cassandra-consistency-levels

|  Consistency Level | |
| -- | -- |
| ONE | ack from one |
| QUROM | ack from 51% or a majority of replica |
|  LOCAL_QUORUM | ack within the same datacenter > 51%  |
| ALL| ack from all nodes |


❓ Strong consistency
- W + R > RF
examples:

Given Write CL = QUORUM and Read CL = QUORUM

1) If RF = 3, W = QUORUM or LOCAL_QUORUM, R = QUORUM or LOCAL_QUORUM, then W (2) + R (2) > RF (3)

2) If RF = 3, W = ALL, R = ONE, then W (3) + R (1) > RF (3)
