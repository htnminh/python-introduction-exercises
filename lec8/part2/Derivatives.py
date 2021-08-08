class FuncWithDerivatives(object):
    def __init__(self, h=1.0E-5):
        self.h = h  # spacing for numerical derivatives
    def __call__(self, x):
        raise NotImplementedError('__call__ \
             missing in class %s' % self.__class__.__name__)
    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)
    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference:
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)