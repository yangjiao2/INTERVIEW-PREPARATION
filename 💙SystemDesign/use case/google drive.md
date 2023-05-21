![](../pics/gg-drive.jpg)


upload and download of the files, detecting file changes in the sync folder


Once the chunks are successfully submitted to the Cloud Storage, the Indexer will communicate with the Synchronization Service using the Message Queuing Service to update the Metadata Database with the changes.


Queuing Service supports asynchronous and loosely coupled message-based communication between distributed components of the system.

```

chunk:
object:{
    file:
    extension:
    user: {

    }
}
```

response queue: delivering the update messages to each client
request queue: global queue (shared)
