## calculation

1. TPS: dau * percent of upload * average size per video (300MB)
2. Storage: upload speed


## common topics
1. video pre processing using Message queue: cut in chunks (prevent failure, parallel processing), content verfiication, distribution service
2. 



## API
1. get
2. search 
3. upload (CRUD)


## video encoding

1. once start, udpate to metadata database
2. processing queue will encode videos in containers (format: avi, mov, mp4, dash)
3. compressing algorithm: H.264, vp9
4. at the same time, generate thumbnail / other info -> which also updates in cache
5. store video in S3 (example)

