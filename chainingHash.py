class Linknode:
    def __init__(self,key,value):
        self.key=key
        self.value = value
        self.next = None
        

class MyHashMap:

    def __init__(self):
        """
        Initializing data structure here.
        """
        self.size = 1000
        self.hash = [None]*self.size
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.size
        if(self.hash[index] is None):
            self.hash[index] = Linknode(key,value)
            return
        curr_node = self.hash[index]
        while(True):
            if(curr_node.key==key):
                curr_node.value = value
                return
            if(curr_node.next is None):
                break
        curr_node.next = Linknode(key,value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.size
        if(self.hash[index] is None):
            return -1
        curr_node = self.hash[index]
        while(curr_node):
            if(curr_node.key == key):
                return curr_node.value
            curr_node= curr_node.next
            
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.size
        if(self.hash[index] is None):
            return
        prev_node = curr_node = self.hash[index]
        if(curr_node.key==key):
            self.hash[index] = curr_node.next
        else:
            curr_node = curr_node.next
            while(curr_node):
                if(curr_node.key == key):
                    prev_node = curr_node.next
                    break
                pre_node ,curr_node= pre_node.next,curr_node.next
        
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)