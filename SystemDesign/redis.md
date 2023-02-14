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
