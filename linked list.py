class Linkedlist:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)

        if self.buckets[index] is None:
            # loome uue linked listi
            self.buckets[index] = Linkedlist(key, value)
        else:
            # kui bucket ei ole tuhi lisame linked listi algusesse
            new_node = Linkedlist(key, value)
            new_node.next = self.buckets[index]
            self.buckets[index] = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.buckets[index]

        while current is not None:
            if current.key == key:
                return current.value
            current = current.next

        # kui voti ei ole 
        return None

    def display(self):
        for i in range(self.size):
            current = self.buckets[i]
            print(f"Bucket {i}:", end=" ")
            while current:
                print(f"({current.key}: {current.value})", end=" ")
                current = current.next
            print()

hash_table = HashTable(size=10)
hash_table.insert("apple", 5)
hash_table.insert("banana", 8)
hash_table.insert("cherry", 12)
hash_table.insert("apple pie", 15)
hash_table.insert("brick", 20)
hash_table.insert("orange", 3)

hash_table.display()

search_result = hash_table.search("banana")
print("Search Result for 'banana':", search_result)
