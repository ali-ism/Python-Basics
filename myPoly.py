from collections.abc import Iterable

class myPoly:
    def __init__(self,coeff):
        if not isinstance(coeff,Iterable):
            raise TypeError('Polynomial coefficients must be sorted in an iterable.')
        self._coeff = coeff
        
    def __len__(self):
        return len(self._coeff)
    
    def print_polynomial(self):
        for i in range(len(self) - 2):
            print(f'{self._coeff[i]}x^{len(self) - 1 - i} +',end = ' ')
        print(f'{self._coeff[-2]}x +',end = ' ')
        print(f'{self._coeff[-1]}')
    
    def poly_derivative(self):
        result = [0] * (len(self) - 1)
        for i in range(len(result)):
            result[i] = self._coeff[i] * (len(self) - 1 -i)
        return myPoly(result)