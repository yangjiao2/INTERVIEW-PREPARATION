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



#### Other usage:
https://www.linkedin.com/posts/alexxubyte_systemdesign-coding-interviewtips-activity-7016444408438923264-_pmB?utm_source=share&utm_medium=member_desktop

🔹Session
We can use Redis to share user session data among different services.

🔹Cache
We can use Redis to cache objects or pages, especially for hotspot data.

🔹Distributed lock
We can use a Redis string to acquire locks among distributed services.

🔹Counter
We can count how many likes or how many reads for articles.

🔹Rate limiter
We can apply a rate limiter for certain user IPs.

🔹Global ID generator
We can use Redis Int for global ID.

🔹Shopping cart
We can use Redis Hash to represent key-value pairs in a shopping cart.

🔹Calculate user retention
We can use Bitmap to represent the user login daily and calculate user retention.

🔹Message queue
We can use List for a message queue.

🔹Ranking
We can use ZSet to sort the articles.
