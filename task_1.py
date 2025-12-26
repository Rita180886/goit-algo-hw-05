class HashTable:

    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _get_hash(self, key):
        return hash(key) % self.size
    
    def set(self, key, value):
        index = self._get_hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value))

    def get(self, key):
        index = self._get_hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
            
        return None
    
    def delete(self, key):
        index = self._get_hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
    
if __name__ == "__main__":
    ht = HashTable()

    ht.set("apple", 10)
    ht.set("banana", 20)

    print(ht.get("apple"))
    print(ht.get("banana"))
    print(ht.get("pear"))

    print(ht.delete("apple"))
    print(ht.get("apple"))

    print(ht.delete("pear"))

    print(ht.table)
