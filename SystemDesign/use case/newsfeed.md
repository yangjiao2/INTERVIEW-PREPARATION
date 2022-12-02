# common requirement

- pull vs. push

### pull: also could be fan-out-on-load 

Pros:
1. keep data in memory on server
2. inactive user will not get update (resource saving)

Cons:
1. empty response


## push to pull (with thrid party) : 
Pros:
1. deliver through 3rd party

Cons:
1. latency
2. delivery rate
3. ordering



# Data Synchronization 
1. add timestamp for online/offline switch
2. client ack data


# database

### schema
1. user
2. entity
3. feeditem
4. likes

###  DDIA 写的优化

1. 读写分离
2. 内容in cache
2. 




