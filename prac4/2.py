import numpy as np
'''
def convert(a):
    res = np.array(a[0] / np.sum(a[0]))
    
    for i in range(1, a.shape[0]):
        res = np.concatenate( (res, a[i] / np.sum(a[i])))
    return res.reshape(a.shape)
'''

def convert(a):
    sum_all = np.sum(a, axis = 1, keepdims = True)
    return a / sum_all
'''
a = np.arange(9).reshape(3, 3)
print(convert(a))
a = np.arange(20).reshape(4, 5)
print(convert(a))
'''