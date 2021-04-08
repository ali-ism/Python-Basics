from collections.abc import Iterable

class Vector:
    def __init__(self,d):
        if isinstance(d,Iterable):
            self._coords = list(d)
        else:
            self._coords = [0] * d
    
    def __len__(self):
        return len(self._coords)
    
    def __getitem__(self,j):
        return self._coords[j]
    
    def __setitem__(self,j,val):
        self._coords[j] = val
    
    def __add__(self,other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result
    
    def __radd__(self,other):
        return self.__add__(other)
    
    def __sub__(self,other):
        if len(self) != len(other):
            raise ValueError('Dimensions must agree!')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    def __neg__(self):
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = - self[j]
        return result
    
    def __mul__(self,other):
        if isinstance(other,Vector):
            result = list(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other[j]
            return sum(result)
        else:
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = self[j] * other
            return result
    
    def __rmul__(self,n):
        return self.__mul__(n)
    
    def __eq__(self,other):
        return self._coords == other._coords
    
    def __ne__(self,other):
        return self._coords != other._coords
    
    def __str__(self):
        return '<' + str(self._coords)[1:-1] + '>'