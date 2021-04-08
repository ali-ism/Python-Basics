class Stack:
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self) == 0
    
    def push(self,elem):
        self._data.append(elem)
    
    def top(self):
        return self._data[-1]
    
    def pop(self):
        return self._data.pop()
    
    def make_empty(self):
        if self.is_empty():
            return
        self.pop()
        self.make_empty()

def transfer(stack,newstack):
    while not stack.is_empty():
        newstack.push(stack.pop())

def reverse_list(array):
    stack = Stack()
    for elem in array:
        stack.push(elem)
    for i in range(len(stack)):
        array[i] = stack.pop()