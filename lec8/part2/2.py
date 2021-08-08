from Polygon import *
from math import sqrt

'''
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]
    def inputSides(self):
        self.sides = [float(input()) for i in range(self.n)]
    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])
'''

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    def findArea(self):
        a, b, c = tuple(self.sides)
        print('The area of the triangle is %.2f' \
        % (sqrt(4 * a**2 * b**2 - (a**2 + b**2 - c**2)**2) / 4))