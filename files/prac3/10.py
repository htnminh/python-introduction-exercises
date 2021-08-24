tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
# YOUR CODE HERE
res = [[j for j in range(i, i+n)] for i in range(1, m*n, n)]
for line in res:
    print(*line)