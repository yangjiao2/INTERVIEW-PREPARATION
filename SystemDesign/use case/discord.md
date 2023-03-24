Data structure:

Parition by snowflake ID (channel + bucket) where bucket is time range


Cassandara - Log structure merge tree:
1. reads - hot spots (query memtable, mutliple on-disk sstable )

write (write amplication) - append to commit log then write to memtable (in memoty), eventually to disk

during write to SSD
- write to new block
- ease old block later in bargage collection


2. write


Whereas B+tree has leaf nodes as pages
insert, update, delete -> all insert, (delete is tombstone)
