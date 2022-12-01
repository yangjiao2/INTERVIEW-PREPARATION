
| relational | non-relational | note | 
| ----- | ------ | ---- |
| ACID |  | ***extra configuration*** requires for achieving ACID for non-relational (Cassandra replication factor gives the consistency level) | 
| |  scalability | requires ***sharding or master slave techniques***, more difficult for multiple DB | 
| |performance |  |
 


- MYSQL

 1\ INDEX

 #### hash

 #### r- tree

 #### geohash

 #### bitmap

 #### b-tree index (balanced tree) - O(log N) search/insert/delete
    - mapping from column <-> pointer
    - pro: quick
    - cons: space (grow with table), complexity

Note: MySQL put indexes in memory.
Note: Index does not work (meaning will do full table scan):

```
 SELECT total(amount)
	FROM orders
	WHERE YEAR(createdAt) = 2020;
```
    - function `YEAR()` inside where clause for computing
    - function `total()` in select to fetch all amount; to solve this, needs another index on amount