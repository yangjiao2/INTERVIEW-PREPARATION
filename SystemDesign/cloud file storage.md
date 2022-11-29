## reference:

[link1](https://www.pankajtanwar.in/blog/system-design-how-to-design-google-drive-dropbox-a-cloud-file-storage-service)


Scale
Total Users : ~100 M

Daily Active Users : ~50 M

QPS : ~500M request per day (~9000 Queries Per Second)

50M * 10 request per day / 86400 s = 5.7k per second

-- computation --

Storage: 1MB per file * 100 files per user * 100M user = 100MB x 100B = 10000PB.

Traffic: 100MB / 10 * 6 query per second / 2 (read : write = 1:1) = 5GB per second

Memory: Assume, each user access 5 files daily and reading chunks of 200KB out of 1MB. So, following the 80-20 rule (80% traffic comes for 20% of the files), our cache size -

((50 M x 200KB x 5 ) x 0.2) = 10 Tera Byte



## business logic / apis:

uplaod
downlaod
edit / delete
share ? 

## handling upload efficiently

- by chunk (each chunk with metadata info)
  -> for 1) optimises network bandwidth utilisation / concurrency utilization
  2) Cloud Storage utilisation when doing modification
  3) version control
  
Note
chunk size depends on I/O on cloud storage, network bandwitdth, average file size


## synchronisation 

- HTTP long polling: Server keeps the request open and waits for the new changes. Server sends HTTP response upon client changes made.

Note:
mobile use sync on demand for reduce bandwidth usage.



## metadata

- requirement: indexes of chunks + versioning

- refer to [database.md](https://github.com/Yjiao917/2022-SWE-INTERVIEW-PREPARATION/blob/main/SystemDesign/database.md)


