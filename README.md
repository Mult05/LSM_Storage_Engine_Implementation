# LSM Storage Engine (Python)

#Backround 

Designing and understanding database storage engines is central to how modern databases manage data on disk and in memory. At the heart of this system lies the storage engine — responsible for coordinating I/O operations and memory layout while balancing trade-offs between performance, durability, and throughput.

I wanted to learn more about DBMS so it got me into exploring different implementations and algoritihms for different search engines. Through this, I learned about how writes directly to the disk are really expensive (hence why they are basically immutable), which is why in database systems like LevelDB, they only write to memory, and then use SStables on the disk.  From this I wanted to implement my own verison to learn more about how the storage actually works and work more optimization problems. It gave me the opportunity to dive into how real databases optimize for write-heavy workloads. I wanted to learn not just how databases use storage engines, but how they’re actually built.

One of the most widely adopted designs for write-optimized systems is the Log-Structured Merge Tree (LSM Tree). LSM Trees write updates to an in-memory, sorted structure (the MemTable) and periodically flush these to disk in the form of immutable, sorted files called SSTables. Unlike traditional storage engines that perform random writes to disk (e.g. B-Trees), LSM Trees are designed for high write throughput, enabling efficient sequential disk writes and fast merges. These properties make LSM Trees especially well-suited for modern databases like LevelDB, RocksDB, and Cassandra, where write speed and compaction strategies are critical. Through this project, I’m learning to model these systems from the ground up — building components like the MemTable, flush mechanism, SSTable format, and eventually compaction logic — in Python.

This repository is my hands-on implementation and learning journey through the architecture of storage systems, and how write-optimized databases really work under the hood.

This is a ongoing project, right now this is what is implemented:
- ✅ In-memory `MemTable` using `SortedDict`
- ✅ Tombstone-based deletes
- ✅ Flushing sorted key-value pairs to immutable SSTables on disk
- ✅ CLI for inserting, retrieving, and inspecting keys

#Design and Structure
Coming soon :)
---
