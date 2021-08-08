class Fraction(object):
    '''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    '''
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)
        
    def __add__(self, other):
        return Fraction(self.numerator*other.denominator \
                        + self.denominator*other.numerator,
                        self.denominator*other.denominator)
    
    def inverse(self):
        return Fraction(self.denominator, self.numerator)

def inverse(fraction):
    return Fraction(fraction.denominator, fraction.numerator)

def float(fraction):
    return fraction.numerator / fraction.denominator
    
'''    
f1 = Fraction(3, 5)
f2 = Fraction(6, 7)
print(f1)
print(f1 + f2)
print(inverse(f1))
print(float(f1))
'''


    
        