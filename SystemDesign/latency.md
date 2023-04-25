Latency Comparison Numbers (~2012)
----------------------------------
L1 cache reference                           0.5 ns
Branch mispredict                            5   ns
L2 cache reference                           7   ns                      14x L1 cache
Mutex lock/unlock                           25   ns
Main memory reference                      100   ns                      20x L2 cache, 200x L1 cache
Compress 1K bytes with Zippy             3,000   ns        3 us
Send 1K bytes over 1 Gbps network       10,000   ns       10 us
Read 4K randomly from SSD*             150,000   ns      150 us          ~1GB/sec SSD
Read 1 MB sequentially from memory     250,000   ns      250 us
Round trip within same datacenter      500,000   ns      500 us
Read 1 MB sequentially from SSD*     1,000,000   ns    1,000 us    1 ms  ~1GB/sec SSD, 4X memory
Disk seek                           10,000,000   ns   10,000 us   10 ms  20x datacenter roundtrip
Read 1 MB sequentially from disk    20,000,000   ns   20,000 us   20 ms  80x memory, 20X SSD
Send packet CA->Netherlands->CA    150,000,000   ns  150,000 us  150 ms

Notes
-----
1 ns = 10^-9 seconds
1 us = 10^-6 seconds = 1,000 ns
1 ms = 10^-3 seconds = 1,000 us = 1,000,000 ns

Credit
------
By Jeff Dean:               http://research.google.com/people/jeff/
Originally by Peter Norvig: http://norvig.com/21-days.html#answers

Contributions
-------------
'Humanized' comparison:  https://gist.github.com/hellerbarde/2843375
Visual comparison chart: http://i.imgur.com/k0t1e.png



## optimize the latency

1\ server level

- CDN
Using CDN (Content Delivery Network) is a major step towards reducing the latency. CDN, caches content, serves it from the nearest data centre & provides an efficient path for data packets to travel on, which drastically reduces the round trip time and so latency.

- HTTP/2
HTTP/2 is a highly efficient protocol which reduces the latency by enabling parallelised data transfers, response multiplexing, requests prioritisation, minimised protocol overhead by efficient compression of HTTP headers, reduced round trips and many more.

- Client Side Caching
Browsers can cache some of the resources which reduces the calls to the server and improves the latency.

- Server Side Optimisations
Server side optimisations such as preload / prepush upon ML algorithm, less disk I/O, caching, efficient algorithms, smart database layer & asynchronous programming can help in optimising the latency.


2\ db level

- index
- materialize view
- sharding

