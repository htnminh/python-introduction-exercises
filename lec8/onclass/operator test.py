import math

class cplx:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    #def str(self): <__main__.cplx object at 0x03E76F50>
        
    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + ' i' 
    
    def length(self):
        return math.sqrt(self.real ** 2 + self.imag ** 2)
        
        
print(cplx(4, 3))
print(cplx.length(cplx(3, 2)))