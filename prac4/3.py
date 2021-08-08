import numpy as np
'''
a = [[ 1,  3, -2,  5],
 [ 3,  5,  6,  7],
 [ 2,  4,  3,  8]]
'''
def system_solver(a):
    a = np.array(a)

    A = a[:, :- 1]
    B = a[:, -1]

    return (np.linalg.solve(A, B).reshape(-1, 1))
