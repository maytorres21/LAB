def display_hash(hashTable):
    for i in range(len(hashTable)):
        print(i, end=" ")
        for j in hashTable[i]:
            print("-->", end=" ")
            print(j, end=" ")
        print()

HashTable = [[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue)
    Hashtable[hash_key].append(value)

insert(HashTable, 10, 'red')
insert(HashTable, 25, 'black')
insert(HashTable, 20, 'white')
insert(HashTable, 9, 'blue')
insert(HashTable, 21, 'green')
insert(HashTable, 21, 'pink')
display_hash(HashTable)