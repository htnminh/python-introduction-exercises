#from math import abs

n = int(input())
a = [int(ele) for ele in input().split()]
x = int(input())

mark = 0
min = abs(a[0] - x)


for i in range(n):
    dist = abs(a[i] - x)
    if dist < min:
        min = dist
        mark = i

print(a[mark])