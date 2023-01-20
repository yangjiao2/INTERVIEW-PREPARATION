 https://eng.uber.com/cherami/

1. [Real time data analysis](#real-time-data-analysis): [link](https://www.slideshare.net/AnkurBansal50/uber-real-time-data-analytics)

 # Real time data analysis
![](../pics/Kakfa-uber.png)

Requirements:
- qps: 1 trillion
- throughput: 100TB -> PB
- reliability: 99.9%
- low latency
- multi-language
- reliable replication

![](../pics/uber-kafka-cluster.png)
## clusters
async user data
logging
time sensitive data - low latency (e.g: surging, push )
high value -at least once, sync- (e.g: pament)

Solution:
1. add secondary fallback

## kafka REST proxy
- multi-language support
- reliability


## Kafka Ack
For high throughput:
- batching
- ack before produce (ack'ed != committed)

Solution:
- use 2 cluster in broker (`min.insync.replicas = 2`)
- wait till leader come back (`unclear.leader.election = false`)
