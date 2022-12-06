
## Faster

1. divde a specialized databases in seperate db to handle request

example:
-  blob or file storage can be moved directly to a cloud provider such as Amazon S3. 
- Analytics or full-text search can be handled by specialized services or a data warehouse. 


## Read heavy

- Replication: reliability and robustness, spreads out the queries 

- [caching](caching.md): speed up request

- [load balancing](load-balance.md)

- [reduce latency](latency.md) by caching: geo-located query routing (CDN)



## Scalability + availability

- [sharding](sharding.md) (Query overhead for accessing multiple shards)

- Service level objectives (SLO) and service level agreements (SLA)


## Reliability / availability

- keepalived: auto re-routing

