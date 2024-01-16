![](./pics/redis%20vs%20mem.png)
![](./pics/redis6.0.png)

With a Redis set, you can add, remove, and test for existence O(1) time (in other words, regardless of the number of set elements). For more information, see:

[link](https://redis.io/docs/management/persistence/)

Redis persistence:
RDB (Redis Database): RDB persistence performs point-in-time snapshots of your dataset at specified intervals.
AOF (Append Only File): AOF persistence logs every write operation
replayed again at server startup, reconstructing the original dataset

RDB:
- perfect for backups ( RDB snapshot )
- single compact file  -> easy to transfer
- On replicas, RDB supports partial resynchronizations after restarts and failovers.

cons:
- might lose latest data due to periodic snapshot (data loss could happen)



AOF:
- more durable:  no fsync at all, fsync every second, fsync at every query

-  append-only log: no corruption problem

- can revert if no re-write happen

cons:
- space


[Redis Sorted Sets](https://medium.com/@sandeep4.verma/building-real-time-leaderboard-with-redis-82c98aa47b9f) are, similarly to Redis Sets, non repeating collections of Strings. The difference is that every member of a Sorted Set is associated with score, that is used in order to take the sorted set ordered, from the smallest to the greatest score. While members are unique, scores may be repeated.


ZADD : Add one/more member for a given score to ZSET/initialize a ZSET with one/more member

ZREM : Removes an item from the ZSET, if exists

ZRANGE : Fetches all the items in the ZSET from their position in sorted order

ZRANGEBYSCORE : Fetches items in the ZSET based on range of scores

ZCOUNT : Returns the number of members with scores between the provided minimum and maximum in ZSET

ZRANK : Returns the position of the given member based on his score in ZSET

ZSCORE : Returns the score of the member in the ZSET

ZINCRBY : Increments the score of a member in the ZSET


[Redis keyspace](https://redis.io/docs/manual/keyspace-notifications/)

 clients to subscribe to Pub/Sub channels in order to receive events on key changes - affecting a given key: LPUSH or delete


[Distributed Locks](https://redis.io/docs/manual/patterns/distributed-locks/)

 different processes must operate with shared resources in a mutually exclusive way.


 lock a resource is to create a key in an instance. The key is usually created with a limited time to live, using the Redis expires feature, so that eventually it will get released (property 2 in our list). When the client needs to release the resource, it deletes the key.

 lock require time: require time (ms) + auto-release time, request to  lock N/2+1 instance