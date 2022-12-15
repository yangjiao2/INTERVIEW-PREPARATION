## reference

[link1](https://charlieinden.github.io/System-Design/2018-06-03_System-Design--Chapter-2--Sharding-484960c18f6.html)

[sharding stretegy, pros and cons](https://www.linode.com/docs/guides/sharded-database/)


The shards are distributed across the different servers in the cluster. Each shard has the same database schema and table definitions. This maintains consistency across the shards. 


## Purpose

availability(logical independence), scalability, security (store data in different partitions), Query Performance (less loading)

## Features

- scalability: scale the system out by adding further shards 

- improve performance -> faster response time: balancing the workload, locate shards in nearby physical location

- expands the storage capacity


## Limitations

- Avoidance of cross-shard joins: inner-joins that span multiple shards

- Auto-increment key management

- reliability: 
-> to solve: at least 2 “live” copies of each shard 

## Strategies

- range based

- hash based

- entity / relationship based (e.g: user and payment)

- geography based (e.g: country)

## Cons

- Increase complexity: failure cause inconsistency and hard to maintain (upgrade, backup)

