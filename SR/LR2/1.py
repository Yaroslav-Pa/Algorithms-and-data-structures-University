class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hashF(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hashF(key)
        if self.table[index] is None:
            self.table[index] = (key, value)
        else:
            i = 1
            while self.table[(index + i) % self.size] is not None:
                i += 1
            self.table[(index + i) % self.size] = (key, value)
            

    def search(self, key):
        index = self.hashF(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return None

    def remove(self, key):
        if self.search(key) is not None:
            index = self.hashF(key)
            while self.table[index] is not None:
                if self.table[index][0] == key:
                    self.table[index] = None
                    print(f"-> Deleted: {key}")
                    return
                index = (index + 1) % self.size
        else:
            print("In table there is no such key")   

    def display(self):
        print('--------Current hesh table:----------')
        for i in range(self.size):
            if self.table[i] is not None:
                print(f"Index {i}: {self.table[i][0]} -> {self.table[i][1]}")


hash_table = HashTable(9999)

with open('file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        key, value = line.strip().split(':')
        hash_table.insert(key, value)

hash_table.display()

search_key = 'fish'
result = hash_table.search(search_key)
if result is not None:
    print(f"--> Finded: {search_key} -> {result}")
else:
    print(f"--> {search_key} couldnt find")

remove_key = 'fish'
hash_table.remove(remove_key)

hash_table.display()
print(f"--> Adding:")
hash_table.insert('bread', 'хліб')
hash_table.insert('warning', 'застереження')
hash_table.insert('signal', 'сигнал')
hash_table.insert('apple', 'яблуко')
hash_table.insert(2, 'два')

hash_table.display()