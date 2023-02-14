TAO:

MySQL databases → durability
Leader cache → coordinates writes to each object
Follower caches → serve reads but not writes. forward all writes to leader.

- Association allows reverse operation (create & delete )
- range query are supported( time, cursor)
- sharding: shard id stored id fbid -> Collocation objects having connections
