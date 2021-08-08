import numpy as np

def pr(name):
    print(name, '=\n', eval(name), '\n')

a = np.array([
        [3, 4],
        [5, 6],
        [7, 8]
    ])
pr('a')

b = np.array([10, 100])
pr('b')

pr('a * b')

c = np.array([
        [3, 4, 5],
        [6, 7, 8]
    ])

pr('c')

#pr('c * b')
#ValueError: operands could not be broadcast together with shapes (2,3) (2,)

pr('b[:, None]')

pr('c * b[:, None]')
