size

The minimum size for char is 8 bits, the minimum size for short and int is 16 bits, for long it is 32 bits


Write Throughput = 1 billion/86400 = 10K hashtags per second

calculation example:
1. write: individual content size * amount of contnet

500 hours of videos uploaded every minute. Assuming 1 hr of video = 1 GB size, total size of videos uploaded every second = 500*1Gb/min = 9 GB/s (write throughput)

2. read: content consumption / time
1 billion hours of videos streamed every day, total size of videos watched per second = 10⁹ GB/day = 10⁹/86400 = 12 TB/s (read throughput)

3. storage: write * 5 years

4. peak:

5. hot: 0.5%

### DB instance:

100MB/s


### server:

300ms QPS (8 core)
32 - 144 gb memory
50k concurrent request
1 TB = 100 GB HDD

1 billion orders per day = 12K orders per second

### file system:
10TB
100MB/s throughput
RAM read 4 GB/s

### cache
bandwidth 20 GB/s


### Redis
1 million  QPS
70K

### SQL
1K QPS (can be handle by a web server)

### Cassandra
20KB /s throughput
100K - 1M QPS
1 M cache QPS

20K writes per second

|    |   | billion |trillion  |
|--  | --|  --     |  --     |
|    |   |  10 ^ 9 |  10 ^ 12 |
KB   |MB |  GB     |      TB  |   PB

image: 200KB - 500 KB
file:
video: 4GB


ID calculation:
timestamp + unique integer => 32 + 10 bit => 2^42 photos
-> sorted

---

## Example calculation:

- Each user will post 5 photos in average with 200KB of size and 100 million active users each day.
- Read to write ratio is 100 : 1

1. capcity:

5 (request) * 100 * 10 ^6 ( 100 million active users) / 24 * 60 * 60 = 5787 QPS

2. bandwidth:

Write Bandwidth = 5787 (QPS) * 200KB / 1024 =  1.1 GBps

Read Bandwidth = 1.1 GBps * 100 (read write ratio) = 110 GBps
