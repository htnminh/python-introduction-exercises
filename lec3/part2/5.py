'''
mid = lambda x, y, z: x if posmid(x, y, z) == 'x' else \
                        y if posmid(x, y, z) == 'y' else \
                        z

def posmid(x, y, z):
    # x y z
    if x <= y and y <= z:
        return 'y'
    # y x z
    if y <= x and x <= z:
        return 'x'
    return 'z'
'''

'''
print(mid(1, 5, 10))
print(mid(1, 1, 10))
print(mid(12, 23, 14))
'''

mid = lambda x, y, z: y if (x <= y and y <= z) or (x >= y and y >= z) else\
                      x if (y <= x and x <= z) or (y >= x and x >= z)else\
                      z