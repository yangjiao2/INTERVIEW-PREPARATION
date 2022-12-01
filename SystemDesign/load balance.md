## reference

[link1](https://charlieinden.github.io/System-Design/2018-06-09_System-Design--Chapter-3--Load-Balancing-e1c89148e37.html)


1. Vertical Scaling: add hardware capacity (memory (RAM), processor (CPU), and network connections)
2. Horizontal Scaling: add machine 
3. network layer
4. application layer
    1) [DNS load balance](#dns-load-balance)
    2) [server load balance](#server-load-balance)
    3) [client load balance](#client-load-balance)

 
## purpose
1. distribute among cluster

2. avoid fail-over


## features 

Caching: An application-layer load balancer may offer the ability to cache responses


Autoscaling: Starting up and shutting down resources in response to demand conditions.

Sticky sessions: The ability to assign the same user or device to the same resource in order to maintain the session state on the resource.

Healthchecks: The ability to determine if a resource is down or performing poorly in order to remove the resource from the load balancing pool.

Persistence connections: Allowing a server to open a persistent connection with a client such as a **WebSocket**.

Encryption: Handling encrypted connections such as Transport Layer Security (TLS) and SSL.



# layer 4 load-balance
use  load balancer’s IP address as destination IP address  in the packet header

"Layer 4 load balancing equires less computation than more sophisticated load balancing methods (such as Layer 7), but CPU and memory are now sufficiently fast and cheap that the performance advantage for Layer 4 load balancing has become negligible or irrelevant in most situations"


# dns-load-balance
'authoritative nameserver' to distribute among real server

Pro: easy, faster
Cons:  no detection for server failure.  does not check for server and network outages.


# server-load-balance

algorithms: 
Round robin (LRU), Least Connections,  Least Response Time Method,  URL Hash (Consistent hashing),  etc


# client-load-balance
Cross Site Scripting": need to enable CORS to allow requests (domain changes)

major issue: security reasons


## services 


- [Amazon Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing)
- [Azure Load Balancing](https://azure.microsoft.com/en-in/services/load-balancer)
- [GCP Load Balancing](https://cloud.google.com/load-balancing)
- [Nginx](https://www.nginx.com)