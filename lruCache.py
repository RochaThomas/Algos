# morning algos
# neetcode LRU Cache

# most commonly used interview question for twitch
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # this will map our key to our nodes in a hashmap
        self.cache = {}

        # left = least recently used or LRU
        # right = most recently used
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        return node

    # insert at the right
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def get(self, key: int) -> int:
        if key in self.cache:
            # update to most recent
            self.insert(self.remove(self.cache[key]))
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from the list and delete the LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]