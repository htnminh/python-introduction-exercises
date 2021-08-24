from abc import ABC, abstractmethod
from math import sqrt

class Figure(ABC):
    @abstractmethod
    def getArea():
        pass
        
    @abstractmethod
    def getPerimeter():
        pass  


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        return sqrt(4 * self.a**2 * self.b**2 - (self.a**2 + self.b**2 - self.c**2)**2) / 4
    
 
class Rectangle(Figure):
    def __init__(self, h, w):
        self.h = h
        self.w = w
    
    def getArea(self):
        return self.h * self.w
        
    def getPerimeter(self):
        return 2 * (self.h + self.w)
    
    
class Square(Figure):
    def __init__(self, a):
        self.a = a
    
    def getArea(self):
        return self.a ** 2
    
    def getPerimeter(self):
        return 4 * self.a