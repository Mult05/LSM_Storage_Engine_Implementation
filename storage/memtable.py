from sortedcontainers import SortedDict 
import os

TOMBSTONE = "__TOMBSTONE__"
class MemTable:
    def __init__(self):
        self.table = SortedDict()

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        if self.table.get(key) == TOMBSTONE:
            return None
        return self.table.get(key)
    
    def delete(self,key):
        self.table[key] = TOMBSTONE
            
    def all_items(self):
        return ((k, v) for k, v in self.table.items() if v != TOMBSTONE)
    
    def flush(self):
        #make directory it it doesnt exist
        if not os.path.exists("SStables"):
            os.makedirs("SStables")
            
        #want to make sure the ss table file and names unique 
        existing_file = os.listdir("SStables")
        SStables_file = []
        for file in existing_file:
            if file.startswith("sstable_") and file.endswith(".txt"):
                SStables_file.append(file)
        ids = []
        for file in SStables_file:
            try:
                ids.append(int(file.split("_")[1].split(".")[0]))
            except ValueError:
                continue
        next_id = max(ids) + 1 if ids else 0
        
        #now build next file name 
        sstable = f"sstables/sstable_{next_id}.txt"
        with open(sstable, "w") as reader:
            for k,v in self.all_items():
                 reader.write(f"{k},{v}\n")
        self.table.clear()
        print(f"Flushed to {sstable}")