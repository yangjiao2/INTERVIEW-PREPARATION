### term sharding vs document sharding

| term sharding | document sharding
| -- | -- |
| h = hash(word) | h = hash(sid) |
| for each word add (w->sid) on server | for each word add (w->sid) on server |
| query fetch on server s for each word, then union / intersection | query on each server and do local union / intersection|

for term sharding, bottle neck is the "hot" word, un-even distribution

for document sharding, updates is O(1) and query is O(N) where as term sharding, updates is O(M) where M = number of words, and query = O(M)
