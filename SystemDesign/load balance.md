## reference

[link (concept)](https://charlieinden.github.io/System-Design/2018-06-09_System-Design--Chapter-3--Load-Balancing-e1c89148e37.html)

[link (features)](https://www.enjoyalgorithms.com/blog/load-balancers-in-system-design) [🔗](#features)

1. Vertical Scaling: add hardware capacity (memory (RAM), processor (CPU), and network connections)
2. Horizontal Scaling: add machine 
3. network layer
4. application layer
    1) [DNS load balance (scale system horizontally)](#dns-load-balance): DNS parse domain to different ip addresses. (If we have multiple data centers, DNS will find the geographically closest data center)
    2) [server load balance](#server-load-balance): connection pool
    3) [database load balance]: *** Partition Horizontally by  partition key*** [sharding](sharding.md)
    4) [client load balance](#client-load-balance)


![load-balancer](pics/load-balancer.png)

## Purpose
1. distribute among cluster

2. avoid fail-over

## Location

client -> server

server -> application server

application -> cache server

cache -> db server

## Features 

Caching: An application-layer load balancer may offer the ability to cache responses

Autoscaling: Starting up and shutting down resources in response to demand conditions.

Sticky sessions: The ability to assign the same user or device to the same resource in order to maintain the session state on the resource.

Healthchecks: The ability to determine if a resource is down or performing poorly in order to remove the resource from the load balancing pool.

Persistence connections: Allowing a server to open a persistent connection with a client such as a **WebSocket**.

Encryption: Handling encrypted connections such as Transport Layer Security (TLS) and SSL.



## layer 4 load-balance
use  load balancer’s IP address as destination IP address  in the packet header

"Layer 4 load balancing equires less computation than more sophisticated load balancing methods (such as Layer 7), but CPU and memory are now sufficiently fast and cheap that the performance advantage for Layer 4 load balancing has become negligible or irrelevant in most situations"


## DNS load-balance
'authoritative nameserver' to distribute among real server

Pro: easy, faster
Cons:  no detection for server failure.  does not check for server and network outages.


## server-load-balance

algorithms: 
Round robin (LRU), Least Connections,  Least Response Time Method, URL Hash (Consistent hashing),  etc


## client-load-balance
Cross Site Scripting: need to enable CORS to allow requests (domain changes)

major issue: security reasons


## services 


- [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing)
- [Azure Load Balancing](https://azure.microsoft.com/en-in/services/load-balancer)
- [GCP Load Balancing](https://cloud.google.com/load-balancing)
- [Nginx](https://www.nginx.com)



### load balancer vs reverse proxy

- SSL termination - Decrypt incoming requests and encrypt server responses so backend servers do not have to perform these potentially expensive operations

- Compression - Compress server responses

- Caching - Return the response for cached requests