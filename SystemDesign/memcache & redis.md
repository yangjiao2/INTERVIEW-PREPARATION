![](pics/mem-vs-redis.png)

[aws](https://aws.amazon.com/elasticache/redis-vs-memcached/)

[bytebytego](https://blog.bytebytego.com/p/redis-vs-memcached)

## Distributed cache

Redis: complex data structure (up to 1GB). Built-in high availability (Replication async), supports queue -> messaging, more operation

Memcache: simple key-value, high concurrency (multi-thread) -> caching relatively small and static data, such as HTML code fragments, easy scale up


## Memcache specialization:
- multi-thread: faster in large dataset

- simple string format: will not need more allocated momery than specified


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

🔹 Recording the number of clicks and comments for each post (hash), or status of sub-process of a task

```

   // get the index of the smallest false bit for use in determining if the task is done

    Long leftMostZero = jedis.bitpos(task, false);

 

    // count the number of true bits aka the number of steps that are done

    long count = jedis.bitcount(task);

```


🔹 Sorting the commented user list and deduping the users (zset) -> check distinct user by set
```
  jedis.setbit(REDIS_KEY, userId, true);

  // count the number of true bits aka the number of distinct users

  long count = jedis.bitcount(REDIS_KEY);


```

🔹 Caching user behavior history and filtering malicious behaviors (zset, hash)

🔹 Storing boolean information of extremely large data into small space. For example, login status, membership status. (bitmap)
