https://mecha-mind.medium.com/system-design-cryptocurrency-exchange-d09be2874c6b

##  Key topics:
###  cassandra

![](../pics/wallet.webp)

SQL Table: user_account

(user_id, balance)
SQL Table: wallet

(user_id, symbol, quantity)
SQL Table: price

(symbol, price)
NoSQL Table: order_book

(order_id, user_id, symbol, order_type, order_price, order_type, quantity, timestamp, is_active)
NoSQL Table: pending_orders

(user_id, order_id)


❓ buy/sell trigger from order_book

once "buy" or "sell" is placed, is_active = True

query
```
SELECT * FROM order_book WHERE symbol=<symbol> AND order_type=’BUY’ AND is_active=1;

```
cache it in Redis and sync on db


❓ partition order_book

 partition on order_id  -> query need to fetch all partitions and then do map-reduce


 or a combination of (symbol, order_type) -> could lead to hot partition


❓ fast write with consistency?

- Cassandra with **NetworkToplogyStrategy**
- no slave / server
- replica in DC (by user id) between 2 nodes so that write is very fast
- eventually consistent thus all nodes across all datacenters sees the same state only after few seconds
-  consistency level:

|  Consistency Level | |
| -- | -- |
| ONE | ack from one |
| QUROM | ack from 51% or a majority of replica |
|  LOCAL_QUORUM | ack within the same datacenter > 51%  |
| ALL| ack from all nodes |


❓ Strong consistency in Cassandra
- W + R > RF
examples:

Given Write CL = QUORUM and Read CL = QUORUM

1) If RF = 3, W = QUORUM or LOCAL_QUORUM, R = QUORUM or LOCAL_QUORUM, then W (2) + R (2) > RF (3)

2) If RF = 3, W = ALL, R = ONE, then W (3) + R (1) > RF (3)



❓ Strong consistency in MySql

account balance and wallet tables we are using MySQL database.

We could have a LEADER-FOLLOWER replication approach
