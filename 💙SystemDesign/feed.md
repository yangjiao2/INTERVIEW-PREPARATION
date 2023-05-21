1. prefetch next items
2. paging as well as head fetching
- user page number + offset: server changes on the list (or new item add to list), could also have duplicate
- last photo id: how to ensure stable sort
- opaque server key: server setup window based on time with TTL, after wards, reset to 1


like interaction:
- receive: sockets
- send: optimistic + offline storage and retries

rapid scrolling:
- enable cancel
- initiate request after short pause (throttle)
- prefetching / batching
