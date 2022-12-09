

## Use case

1. memcache


2. 


## technique

1. LRU

## distributed cache


[link](https://www.alachisoft.com/resources/articles/readthru-writethru-writebehind.html)



***Cache-aside (synchronized)***:  The cache is "kept aside" as a faster and more scalable in-memory data store. 

read: 1) checks cache

write: 1) update memory 2) update cache


-> read-heavy workloads: Memcached and Redis

***Read-through/Write-through (read heavy with first time loading )***: store and reads / writes data to cache. The cache is responsible for reading and writing this data to the database

read: 1) checks cache

write: 1) update cache  2) update memory


-> Better read scalability with Read-through

-> Better write performance with Write-behind, schedule the database writes 

-> Solution to first time loading: ‘warming’ or ‘pre-heating’ the cache


Write-through: 
- pro: consistency (simultaneously updated to cache and memory), helps in data recovery 
- cons: 


Write-back / Write-behind: 
- pro:  less memory access (updated into the memory at a later time with batch job), use "Dirty Bit" to indicate if the data present in the cache was modified(Dirty) or not modified(Clean).
- cons: can be inconsist if Cache fails
