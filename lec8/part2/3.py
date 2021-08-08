class Vehicle:
    def __init__(self, name, mileage, cap):
        self.name = name
        self.mileage = mileage
        self.cap = cap
    
    def __str__(self):
        return 'Vehicle: name = %s, mileage = %i, cap = %i' \
                % (self.name, self.mileage, self.cap)
                
    def fare(self):
        return self.cap * 100
        
class Bus(Vehicle):
    def __init__(self, name, mileage, cap = 50):
        Vehicle.__init__(self, name, mileage, cap)
        
    def __str__(self):
        return 'Bus: name = %s, mileage = %i, cap = %i' \
                % (self.name, self.mileage, self.cap)
    
    def fare(self):
        return self.cap * 100 * 1.1
    
'''
print(Vehicle("Camry", 100, 5))
b = Bus("Bach Khoa", 12, 10)
print(b)
print(b.fare())
print(isinstance(b, Bus))
print(isinstance(b, Vehicle))
'''
