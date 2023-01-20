
server:

50k concurrent request
100 gb storage




image: 200KB

video:

---

## Example calculation:

- Each user will post 5 photos in average with 200KB of size and 100 million active users each day.
- Read to write ratio is 100 : 1

1. capcity:

5 (request) * 100 * 10 ^6 ( 100 million active users) / 24 * 60 * 60 = 5787 QPS

2. bandwidth:

Write Bandwidth = 5787 (QPS) * 200KB / 1024 =  1.1 GBps

Read Bandwidth = 1.1 GBps * 100 (read write ratio) = 110 GBps
