import math 

def dot(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += v1[i] * v2[i]
    return res

def length(v):
    res = 0
    for i in range(len(v)):
        res += v[i]**2
    return math.sqrt(res)

def int_fl_format(num):
    if abs(num - int(num)) < 1e-10:
        return '%.1f' % num
    return '%.9f' % num

def manhattan_length(v1, v2):
    res = 0
    for i in range(len(v1)):
        res += abs(v1[i] - v2[i])
    return res
    
def cosine_angle(v1, v2):
    return dot(v1, v2) / (length(v1) * length(v2))

def euclidean_length(v1, v2):
    v = []
    for i in range(len(v1)):
        v.append(v1[i] - v2[i])
    return length(v)
    
def vector_distance(v1, v2, **kwargs):
    #print(kwargs)
    try:
        if kwargs['norm'] == 'manhattan':
            return int(manhattan_length(v1, v2))
        if kwargs['norm'] == 'cosine':
            return int_fl_format(cosine_angle(v1, v2))
        if kwargs['norm'] == 'euclidean':
            return int_fl_format(euclidean_length(v1, v2))
    except KeyError:
        return int_fl_format(euclidean_length(v1, v2))
    return None

'''print(vector_distance([1, 2], [4, 6], norm='manhattan'))
print(vector_distance([1, 2], [4, 6], norm='cosine'))
print(vector_distance([1, 2, 3], [4, 6, 7]))
print(vector_distance([1, 2], [4, 6]))'''

