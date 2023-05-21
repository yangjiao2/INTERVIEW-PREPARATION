
https://mecha-mind.medium.com/system-design-backend-for-google-photos-e0abcd74dd36


##  Key topics:
###  custom ID with timestamp, file system, consistent hashing avoid hot key issue, Redis with LRU cache for high read throughput

# id with auto chronological order embed
 (photo_id = timestamp in seconds (32 bits) + 10 bit integer M)

# db tables

user id : [photo ids]
photo id: location, offsite


# storage

1. filesystem (XFS): photos
fast read,
immutable,
no index support,

❓ when create a new file ?

Maintain a min-heap of the current file sizes and file locations. For a new photo, calculate its size and then fetch the file with the lowest size (i.e. root of heap). If the lowest size + photo_size > max_size, then create a new file

on restart, reconstruct

![](./../pics/photo%20fs.webp)


❓ locate photo in server (with potential hotspot/hot key)?

 [Consistent Hashing](../consistent%20hashing.md)


❓ fault tolerance?

add duplications of file system server *1 main + 2 dup*

skip the next 2 servers each time a crash happens


2. Redis LRU write through: (photo location)



# partition

full data server: throughput * number of server * 3 replica instance for failover


❓ read / write consistency

quorum:

- write:

out of 3 instances, a write is successful only when at-least 2 (out of 3) send back

- read:

the response with the highest photo_id value (i.e. most recent timestamp) among the first 2 instances to send response back is considered.
