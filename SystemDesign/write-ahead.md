
## Idea

1) log the complete set of actions to durable storage (e.g. disk).
2) could try batch update
3) truncate easier lgos by segment


## concept
- Durability: writing to the WAL first (for crash)

- Atomicity: maintain orders
