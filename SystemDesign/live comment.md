Key points:

Use socket to allow server sent events
Keep track of userId to connected serverId
Keep track of postId to watching userId(s)
Two ways to keep information in the above two tables/caches up to date: 1) TTL; 2) actively update the information above as user scroll away, or disconnect the socket
When user A leaves a comment on a post, firstly, persist that; secondly push that to an queue.
In the queue processor/comsumer, look up the list of users that is currently watching this post, for reach user, look up the server that it is connected to via soket, and fanout push the messages to all those users through all those connected servers.


Write Locally, Read Globally
- writes are applied to one database and asynchronously replicated to databases across all regions.
