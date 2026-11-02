class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.res = {}
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    # helper to remove node 
    def remove(self, n: Node):
        n.prev.next = n.next
        n.next.prev = n.prev
    
    # places node right before tail
    def insert(self, n: Node):
        prev = self.tail.prev
        prev.next = n
        n.next = self.tail
        n.prev = prev
        self.tail.prev = n

    def get(self, key: int) -> int:
        if key in self.res:
            node = self.res[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.res:
            node = self.res[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = Node(key, value)
            self.res[key] = node
            self.insert(node)
        
        while len(self.res) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.res[lru.key]


        


''' A Node class with key, val, prev, next. (Think about why the node needs the key too. It comes up during eviction.)
__init__: capacity, the dict, and the two dummies linked to each other.
The helpers remove(node) and insert(node).'''