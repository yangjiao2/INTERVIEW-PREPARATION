![](pics/mem-vs-redis.png)

[aws](https://aws.amazon.com/elasticache/redis-vs-memcached/)

[bytebytego](https://blog.bytebytego.com/p/redis-vs-memcached)

## Distributed cache

Redis: complex data structure. Built-in high availability
Memcache: simple key-value, high concurrency (multi-thread)

## Redis specialization: 
- Advanced data structures

Redis supports lists, sets, sorted sets, hashes, bit arrays, and hyperloglogs. 

- Snapshots

archiving or recovery. using Backup file (RDB)

- Replication

multiple replicas of a Redis primary. Master-slave

- Transactions

Redis supports transactions, atomic operation.

- Pub/Sub

use for ***high performance chat rooms, real-time comment streams, social media feeds, and server intercommunication***.


- Custom data eviction
custom TTL, even if the system is out of memory

![](pics/mem-vs-redis.jpg)

The advantages of data structures make Redis a good choice for:

🔹 Recording the number of clicks and comments for each post (hash)

🔹 Sorting the commented user list and deduping the users (zset)

🔹 Caching user behavior history and filtering malicious behaviors (zset, hash)

🔹 Storing boolean information of extremely large data into small space. For example, login status, membership status. (bitmap)