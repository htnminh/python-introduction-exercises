import math

ax, ay, bx, by, cx, cy = [float(i) for i in input().split()]

def length(v):
    res = 0
    for i in range(len(v)):
        res += v[i]**2
    return math.sqrt(res)

def pythagoras(a, b, c):
    if length(a) + length(b) == length(c) or \
       length(a) + length(c) == length(b) or \
       length(b) + length(c) == length(a):
        return 'line'
    if length(a) ** 2 + length(b) ** 2 == length(c) ** 2 or \
       length(a) ** 2 + length(c) ** 2 == length(b) ** 2 or \
       length(b) ** 2 + length(c) ** 2 == length(a) ** 2:
        return 'right'
    if length(a) ** 2 + length(b) ** 2 > length(c) ** 2 or \
       length(a) ** 2 + length(c) ** 2 > length(b) ** 2 or \
       length(b) ** 2 + length(c) ** 2 > length(a) ** 2:
        return 'obtuse'
    return 'acute'

print(pythagoras((ax-bx, ay-by), (bx-cx, by-cy), (cx-ax, cy-ay)))