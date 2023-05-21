
## Idea

1) log the complete set of actions to durable storage (e.g. disk).
2) could try batch update
3) truncate easier lgos by segment


## concept
- Durability: writing to the WAL first (for crash)

- Atomicity: maintain orders


## To Sync Or Not To Sync?
Given that sync-ing is so expensive, what do other databases do?

LevelDB actually defaults to not syncing. They claim that non-sync writes can often be used safely, and that a user should choose when they wish to sync.
Cassandra defaults to periodic syncing every 10s. Writes are acknowledged once placed in the OS file buffer.
etcd has some logic around whether to sync, but best I can tell user writes would end up causing a sync.
