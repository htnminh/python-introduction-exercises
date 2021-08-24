temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
    a.append(input().split(' '))
for i in range(m):
    b.append(input().split(' '))
res = [[int(a[i][j]) + int(b[i][j]) for j in range(n)] for i in range(m)]
for line in res:
    print(*line)


# YOUR CODE HERE
'''
2 3
1 2 3
4 5 6
7 8 9
10 11 12
'''