from Derivatives import *
import math

class Sine1(FuncWithDerivatives):
    def __init__(self):
        FuncWithDerivatives.__init__(self)
    
    def __call__(self, x):
        return math.sin(x)
        
    def df(self, x):
        return FuncWithDerivatives.df(self, x)
    
    def ddf(self, x):
        return FuncWithDerivatives.ddf(self, x)
    
    
class Sine2(FuncWithDerivatives):
    def __init__(self):
        pass
        
    def __call__(self, x):
        return math.sin(x)
        
    def df(self, x):
        return math.cos(x)
        
    def ddf(self, x):
        return -math.sin(x)