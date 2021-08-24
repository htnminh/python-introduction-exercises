import math

class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2) 
    
    def __str__(self):
        return 'Point coor: <' + str(self.x) + ', ' + str(self.y) + '>'
    
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Coordinate(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __len__(self):
        return int(Coordinate.distance(Coordinate(0, 0), self) ** 2)
    
if __name__ == '__main__':    
    point1 = Coordinate(1, 2)
    point2 = Coordinate(5, 10)
    print(point1.x, point1.y)
    print(point2.x, point2.y)

    print(point1.distance(point2))
    print(Coordinate.distance(point1, point2))

    print(point1)
    print(type(point1))
    print(Coordinate)
    print(type(Coordinate))

    print(isinstance(point1, Coordinate))
    
    print(point1 + point2)
    print(point1 - point2)
    print(point1 == point2)
    print(len(point1))