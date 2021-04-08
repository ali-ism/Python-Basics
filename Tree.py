from collections import deque


class Tree:
    class _Node:
        def __init__(self, data, parent, children=None):
            if children is None:
                children = []
            self._data = data
            self._parent = parent  # of type Node
            self._children = children  # list of children nodes

    def __init__(self):
        self._root = None
        self._size = 0

    def __len__(self):
        return self._size

    def positions(self):  # breadth-first traversal
        queue = deque()
        queue.append(self._root)
        while queue:
            position = queue.pop()
            yield position
            for child in self.children(position):
                queue.appendleft(child)

    def __iter__(self):
        for position in self.positions():
            yield position._data
    
    def render(self):
        cursor_depth = 0
        for position in self.positions():
            if cursor_depth != self.depth(position):
                print('\n\n')
                cursor_depth = self.depth(position)
            spaces = ' ' * (self.num_children(position) + 1)
            print(spaces + str(self.element(position)) + spaces, end = '')
        print()

    def root(self):
        return self._root

    def element(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        return node._data

    def parent(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        return node._parent

    def children(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        return node._children

    def num_children(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        return len(node._children)

    def is_root(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        if node._parent is None:
            return True
        else:
            return False

    def is_leaf(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        if node._children == []:
            return True
        else:
            return False

    def depth(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))

    def height(self, node=None):
        if node is None:
            node = self._root
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(c) for c in self.children(node))

    def add(self, data, parent=None):
        if parent is None:
            if not self._root is None:
                raise ValueError('Root node already exists.')
            self._root = self._Node(data, None)
            self._size += 1
            return self._root
        else:
            new_node = self._Node(data, parent)
            parent._children.append(new_node)
            self._size += 1
            return new_node

    def delete(self, node):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        for child in node._children:
            child._parent = node._parent
        node._parent._children.remove(node)
        element = node._data
        node = None
        self._size -= 1
        return element

    def replace(self, node, new_data):
        if not isinstance(node, self._Node):
            raise TypeError('Node must be of proper type Node.')
        node._data = new_data