class Node:
    def __init__(self, key: int = 0, value: int = 0, prev: Node = None, next: Node = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = Node()
        self.right = Node()
        self.left.next, self.right.prev = self.right, self.left
        
    def insert(self, node: Node):
        node.prev = self.right.prev
        node.next = self.right
        self.right.prev.next = node
        self.right.prev = node
     
    def remove(self, node: Node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(self.cache[key])
        else:
            self.cache[key].value = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
           
           
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
       

        
        
        
