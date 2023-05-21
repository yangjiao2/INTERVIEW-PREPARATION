Apache Kafka: 2 Million Writes Per Second

 Kafka is a message bus optimized for high-ingress data streams and replay. Kafka can be seen as a durable message broker where applications can process and re-process streamed data on disk."

Casanddrda: 1 million writes per second (Scale-Up Linearity)
consistency configure

[Read/Write Consistency Levels](https://docs.datastax.com/en/archived/cassandra/2.0/cassandra/dml/dml_config_consistency_c.html)
ALL, QUORUM, ONE -> THREE, LOCAL, ANY (write to at least one)
