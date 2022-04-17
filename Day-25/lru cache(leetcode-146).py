class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.mru=Node(-1,-1)
        self.lru=Node(-1,-1)
        self.mru.next=self.lru
        self.lru.prev=self.mru
        
        self.dic={}
        self.capacity=capacity
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node=self.dic[key]
            self.delete(node)
            self.insert(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node=self.dic[key]
            self.delete(node)
        if self.capacity==len(self.dic):
            self.delete(self.lru.prev)
        self.insert(Node(key,value))
        
    def insert(self,node):
        self.mru.next.prev=node
        node.next=self.mru.next
        self.mru.next=node
        node.prev=self.mru
        
        self.dic[node.key]=node
    def delete(self,node):
        del self.dic[node.key]

        node.next.prev=node.prev
        node.prev.next=node.next
        
        
        
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)