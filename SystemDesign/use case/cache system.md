
# sync

 any change occurs by the user, it will notify the Index Controller(another client component) about the action of the user.

## heap + count-min sketch


1. Count-Min sketch: + 1 for each data
2. Heap
3. Put the element to the sketch
Estimate the frequency of the element using the sketch. If frequency is greater than a threshold (k*N), then put the element to the heap.

Heap should be periodically or continuously cleaned up to remove elements that do not meet the threshold anymore.


## concurrency:

lock is not good for hot key

updates are written to a log and replayed in asynchronous batches.


# availability:

replica

master-slave

commited log



✓ Local Database will keep track of all the files, chunks, directory path, etc. in the client system.

✓ The Chunk Controller will split files into smaller pieces. It will also perform the duty to reconstruct the full file from its chunks. And this part will help to determine only the latest modified chunk of a file. And only modified chunks of a file will be sent to the server, which will save bandwidth and server computation time.

✓ The Watcher will observe client-side folders, and if any change occurs by the user, it will notify the Index Controller about the action of the user. It will also monitor if any change is happening on other clients(devices), which are broadcasted by Synchronization service.

✓ The Index controller will process events received from the Watcher and update the local Database about modified file-chunk information. It will communicate with the Metadata service to transfer changes to other devices and update the metadata database. This request will be sent to the metadata service via the message request queue.
