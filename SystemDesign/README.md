
![](pics/algo.jpg)
![](pics/general.png)

## Faster

1. divde a specialized databases in seperate db to handle request

example:
-  blob or file storage can be moved directly to a cloud provider such as Amazon S3.
- Analytics or full-text search can be handled by specialized services or a data warehouse.

2. CDN
- distributed servers in different geographical locations

- multiple replicas of data stored (cache)

3. Async jobs


## Read heavy

- Replication: reliability and robustness, spreads out the queries

- [caching](caching.md): speed up request (cache-aside or read-through cache)

- [load balancing](load-balance.md)

- [reduce latency](latency.md) by caching: geo-located query routing (CDN)



## Scalability + availability

- [sharding](sharding.md) (Query overhead for accessing multiple shards): e.g: netflix uses shard on time to get: Live view history and comparessed old view history

- Service level objectives (SLO) and service level agreements (SLA)


## Reliability / availability

- keepalived: auto re-routing

- (Netflix) memcache with write all, read one nearst & available

![ev-cache](pics/EV-Cache.jpg)



## Multimedia processing

- break into chunks + parallel processing

- transcoding or encoding (video / audio): converting the original media into different formats and resolutions
