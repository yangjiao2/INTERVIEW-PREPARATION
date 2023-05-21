### reference:
[link](https://www.pankajtanwar.in/blog/generating-unique-ids-in-a-distributed-environment-at-high-scale)



### Auto Incrementing Ids / Current Timestamp
Pros:

The simplest approach ever
Sorted in nature

Cons:

Fails in case of sharded databases
Auto-incrementing ids are leaky


### UUIDs (128 bits)
Pros:

Totally independent (uses current timestamp, process id, MAC address) and works very well for sharded databases at high scale
by using timestamp as the first component of the ID, the IDs remain time-sortable.

Cons:

Require more space (128 bit)
Index size incrase when dataset increases
No sorting, completely random


### Database ticketing server (Flicker): uses a centralized database server to generate unique incrementing ids

Pros:

Works very well for sharded database 
Short length

Cons:

Single point of failure 
Can become a write bottleneck at scale 


## MongoDB object ID

[link](https://www.mongodb.com/docs/manual/reference/method/ObjectId/)


Pros: enable mo

Cons:  12 bytes, more storage space

### (Twitter) Snowflake ( 4-bits)

Pros:
64 bits: timestamp (41 bits) + configured machine id (10 bits = 1024 machines) + sequence number (12 bits) + 1 random

Cons: 
additional complexity


### Instagram (64bits, sharded, Postgres’ existing auto-increment functionality)

[link](https://instagram-engineering.com/sharding-ids-at-instagram-1cf5a71e5a5c)


41 bits for time in milliseconds (gives us 41 years of IDs with a custom epoch)
13 bits that represent the logical shard ID (user id % total shard count)
10 bits that represent an auto-incrementing sequence, % 1024

=> can generate 1024 IDs, per shard, per millisecond