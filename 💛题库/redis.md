
## Redis Datatypes

- String - 缓存 计数 （访问次数， 点赞转发）
    - int, emstr, raw
    - command: 
            O(1) :`SET`, `GET`, `GETSET`, `INCR`, `DECR` 
            O(N) :`MSET` `MSETTNX` (set if value not exist)


- Hash - 存储信息 
    - ziplist (<512 byte), hashtable
    - command:
        O(1): `HSET`, `HGET`, `HEXIST`, `HINSCRBY`
        O(M): `HMSET`, `HMGET`, `HDEL`
        O(N): `HGETALL`


- List - 双向链表，购票
    - ziplist, linkedlist
    - command:
        O(1): `LPUSH`, `LPOP`, `RPUSH`, `RPOP`
        O(M): `LRANGE`
        o(N): `LINDEX`, `LINSERT`


- SET - 标签，共同好友/粉丝
    - inset, hashtable
    - command:
        O(1): `SISMEMEBR`, `SADD`, `SMOVE`(move from a set to another), `SCARD` (member count), `SPOP`, 
        O(M): `SREM`
        o(N): `SMEMEBERS`, `SUNION`, `SINTER`, `SDIFF`



- ZSET - 排行榜，点赞数，根据权重排列，实时用户排行，分数排行，弹幕消息
    - ziplist(< 128 byte entries, <64 byte value), skiplist
    - command:
        O(MlogN): `ZCOUNT`(count between scores),  `ZADD`, `ZREM`, `SCARD` (member count), `SPOP`, 
        O(1): `ZCARD`, `ZSCORE` (get score of a key)
        O(logN+M): `ZRANK`, `ZINCRBY`, `ZRANGE`, `ZRANGEBYSCORE`, `ZREMRANGEBYRANK`

- BITMAPS

- HYBERLOGLOG


## Redis vs. Memcache


