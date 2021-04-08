class LeakyStack:
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [] * self.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
    
    def is_empty(self):
        return self._size == 0
    
    def push(self,elem):
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = elem
        self._size += 1
    
    def pop(self):
        result = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        return result