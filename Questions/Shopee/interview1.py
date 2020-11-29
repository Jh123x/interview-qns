"""

LRU cache

Implement an LRU cache (with size n) with the following interface:
put(key, value)
get(key)

expiry time, variable
put(key, value, ttl) # ttl = duration/seconds/ms 

"""
from queue import Queue #For the queue used by the cache

class LRUCache:
    def __init__(self, size:int):
        """LRU Cache
            size: maximum number of elements it will store.
        """
        self._size = size
        self._data = {}
        self._usage = {} #Keep tracks of number of same key in the queue
        self._queue = Queue()
        
    def getValidFront(self):
        """
        Get the valid front of queue
        """
        key = self._queue.get()
        while (not key in self._usage):
            key = self._queue.get()
        return key
       
    
    def _getLRU(self):
        """Get the least recently used item"""
        key = self.getValidFront()
        self._usage[key] -= 1
        
        while (self._usage[key] != 0 and not self._queue.empty()):
            
            #Remove least recently used item
            key = self.getValidFront()
            
            #Check when the item was last used
            self._usage[key] -= 1
            
        return key
    
    def getTime(self, value:tuple):
        return value[1]
    
    def getValue(self, value:tuple):
        return value[0]
    
    def removeItem(self, key:str):
        if(not key in self._data):
            return
        del self._data[key]
        del self._usage[key]
        
    def put(self, key:str, value, ttl):
        """Stores the give key,value pair
            key: The key to retrieve the value
            value: The data to be stored
        """
        #If the cache is full
        if (len(self._data) >= self._size):
            LRU_key = self._getLRU()
            print(f"Item deleted {LRU_key}")
            self.removeItem(LRU_key)
            
        #Add the new value into cache
        self._data[key] = (value,ttl)
        self._queue.put(key)
        self._usage[key] = 1 #Reset key / Initialise new key
        
    def get(self, key:str):
        """Gets the value based on the key.
            key: the key to retrieve the value.
            returns None if the item is not found
        """
        
        #Retrieve current time
        currTime = 10 #10 to represent current time
        
        if (not key in self._data):
            #Get from Main data before returning 
            #Simulated here by the None obj
            return None
        
        #Get the item
        item = self._data[key]
        
        #Check if tts has expired
        if (currTime >= self.getTime(item)):
            
            print(f"TTL is over {key}:{item}")
            self.removeItem(key)
            return None
        
        #If increased usage counter
        self._usage[key] += 1
        
        #Put item to back of queue
        self._queue.put(key)
        
        #Return item
        return self.getValue(item)

if __name__ == "__main__":
    MAX_SIZE = 2
    ITEMS = {
        "key1":("value1",100),
        "key2":("value2",11),
        "key3":("value3",10),
        "key4":("value4",2),
    }
    cache = LRUCache(MAX_SIZE)
    
    for k,v in ITEMS.items():
        cache.put(k,*v)
        print(f"Item placed {k}, {v}")
        
    for k in ITEMS.keys():
        value = cache.get(k)
        print(f"Value found: {value}")
        
    cache.get("key3")
    cache.put("key5", "value5", 20)
    
    for k in ITEMS.keys():
        value = cache.get(k)
        print(f"Value found: {value}")
    
    value = cache.get("key5")
    print(f"Value found: {value}")
    
    
"""
Size = 2
Item1 is put into cache. 
Current Queue: [Item1]
Current usage: {Item1: 1}


Item2 is put into cache. 
Current Queue: [Item1, Item2]
Current usage: {Item1: 1, Item2: 1}


Item1 is retrieved
Current Queue: [Item1, Item2, Item1]
Current usage: {Item1: 2, Item2:1}

Item3 is put into the cache

getLRU:
    Top of Queue: Item1 
    Check Usage: {Item1: 1, Item2:1}

    Next top of Queue: Item2
    Check Usage: {Item1: 1, Item2:0}

    return Item2

Delete Item2
Add item 3

Current Queue: [Item1, Item3]
Current usage: {Item1: 1, Item3:1}

"""
            
            
            
            
            
            
            
            
            
            
            
            
            
            