## reference

[link1](https://charlieinden.github.io/System-Design/2018-06-03_System-Design--Chapter-2--Sharding-484960c18f6.html)


## purpose

availability(logical independence), scalability, security (store data in different partitions)

## features

- scalability: scale the system out by adding further shards 

- improve performance -> faster response time: balancing the workload, locate shards in nearby physical location



## limitations

- Avoidance of cross-shard joins: inner-joins that span multiple shards

- Auto-increment key management

- reliability: 
-> to solve: at least 2 “live” copies of each shard 