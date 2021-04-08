class ArrayQueue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        return self._data[self._front]
    
    def dequeue(self):
        result = self.first()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result
    
    def enqueue(self,elem):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elem
        self._size += 1
    
    def resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

class ArrayDequeue:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def add_first(self,elem):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = elem
        self._size += 1
    
    def add_last(self,elem):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = elem
        self._size += 1
    
    def delete_first(self):
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return result
    
    def delete_last(self):
        back = (self._front + (self._size - 1)) % len(self._data)
        result = self._data[back]
        self._data[back] = None
        self._size -= 1
        return result
    
    def first(self):
        return self._data[self._front]
    
    def last(self):
        return self._data[self._front + (self._size - 1)]
    
    def resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for i in range(self._size):
            self._data[i] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0