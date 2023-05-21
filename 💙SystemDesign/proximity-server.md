1. dynamically sized grid: quad tree
2. index:
- grid -> place index hash table:
50M * 2(grid id + place id) * 8(size of ID) = 0.8G
- quad tree:
50M grid with 100 places in each grid, 500K nodes
1/3 as internal nodes, 4 pointers on each internal node
500K * 100 * 8 bytes

Sharding:
term sharding vs. document sharding
- region based sharding: query based on region
problem: un-uniform growth / hot regions -> dynamic re-partition, duplicate hot shards

vs.
- shard by place id: query all shard with a central aggregator server
