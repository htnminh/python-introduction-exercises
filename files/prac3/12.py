def merge_dict(d1, d2):
    # YOUR CODE HERE
    for ele in d2:
        d1[ele] = d1.get(ele, 0) + d2[ele]
    return d1
#print(merge_dict({'a': 3, 'b': 2, 'c': 1}, {'b': 3, 'c': 2, 'd': 1}))
