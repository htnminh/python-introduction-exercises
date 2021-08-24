import numpy as np

a = np.arange(1, 21)
'''
a = (((a - 1) * 5) % 19 + 1).reshape(4, 5)
a[3, 4] = 20
'''
a = a.reshape((5, 4), order='F').reshape(4, 5)
print(a)