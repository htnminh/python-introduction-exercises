def closest_tuple(tuple_list, query, k):
    k -= 1
    mark = 0
    min = abs(tuple_list[0][k] - query[k])
    
    for i in range(len(tuple_list)):
        dist = abs(tuple_list[i][k] - query[k])
        if dist < min:
            mark = i
            min = dist
    return tuple_list[mark]
'''
tuple_list = [(-3, 4, 9), (5, 6, 7), (10, 16, 70), (1, 6, -7)]
query = (1, 2, 5)
k = 3
print(closest_tuple(tuple_list, query, k))'''