from storage.memtable import MemTable

def main():
    memtable = MemTable()
    
    while True:
        command = input("Please enter a command (put, get, all, exit): ").strip().lowers()
        if command == "put":
            key = input("Enter key: ")
            value = input("Enter values: ")
            memtable.put(key, value)
        elif command == "get":
            key = input("Enter key: ")
            result = memtable.get(key)
            if result is not None:
                print("Value:", result)
            else:
                print("Key not found.")
        elif command == "all":
            for k, v in memtable.all_items():
                print(f"{k} => {v}")
        elif command == "flush:":
            memtable.flush()
        elif command == "exit":
            print("exiting..")
            break
        else:
            print("Unknown command, please input 'put', 'get', 'all'. or 'exit'.")
        
if __name__ == "__main__":
    main()
