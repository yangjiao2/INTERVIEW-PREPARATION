# on load

fresh start: by check reset timer for background loading / fresh laoding
coordinator: 1) check cache 2) fetch graphQL data from pool

conditions on checking cache: not tab click / back click , not pre-fetch request
throttling on cold start


![](./pics/feed%20load.png)
![](./pics/feed%20start.png)
![](./pics/story%20stream.png)

# cursor

- support pagination
- need to be serializable and comparable

types:
start cursor, end cursor
time cursor, serial cursor for batch request

# ranking
1. query hit backend
2. filter out seen stories
3. load new inventory / stories
4. rerank
