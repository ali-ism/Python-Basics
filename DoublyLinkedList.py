class _DoublyLinkedBase:
    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None,None,None)
        self._tail = self._Node(None,None,None)
        self._header._next = self._tail
        self._tail._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self,elem,predecessor,successor):
        new_node = self._Node(elem,predecessor,successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node
    
    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        element = node._element
        node._prev = node._next = node._element = None
        self._size -= 1
        return element

class PositionalList(_DoublyLinkedBase):
    class Position:
        def __init__(self,container,node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self,other):
            return not (self == other)
    
    def _validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be of Position type.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._next is None:
            raise ValueError('p is no longer valid.')
        return p._node
    
    def _make_position(self,node):
        if node is self._header or node is self._tail:
            return None
        else:
            return self.Position(node)
    
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._tail._prev)
    
    def middle(self):
        cursor = self.first()
        count = 1
        while count < self._size // 2:
            cursor = self.after(cursor)
            count += 1
        return cursor
    
    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)
    
    def _insert_between(self,elem,predecessor,successor):
        new_node = super()._insert_between(elem,predecessor,successor)
        return self._make_position(new_node)
    
    def add_first(self,elem):
        return self._insert_between(elem,self._header,self._header._next)
    
    def add_last(self,elem):
        return self._insert_between(elem,self._tail._prev,self._tail)
    
    def add_before(self,elem,p):
        right_node = self._validate(p)
        return self._insert_between(elem,right_node._prev,right_node)
    
    def add_after(self,elem,p):
        left_node = self._validate(p)
        return self._insert_between(elem,left_node,left_node._next)
    
    def delete(self,p):
        node = self._validate(p)
        return self._delete_node(node)
    
    def replace(self,p,elem):
        old_node = self._validate(p)
        result = old_node._element
        old_node._element = elem
        return result
    
    def insertion_sort(self):
        if self._size > 1:
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker)
                if pivot.element() > marker.element():
                    marker = pivot
                else:
                    walk = marker
                    while walk != self.first() and \
                    self.before(walk)._element > pivot._element:
                        walk = self.before(walk)
                    value = pivot.element()
                    self.delete(pivot)
                    self.add_before(value,walk)