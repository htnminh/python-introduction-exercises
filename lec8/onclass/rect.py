class Rect(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return '<Width = ' + str(self.width) + ', Height = ' + str(self.height) + '>'
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)
'''      
a = Rect(4, 5)
print(a)
'''