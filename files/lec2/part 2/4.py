#correct

n = int(input())
for i in range(1, n+1):
    res = ' ' * (n - i)
    for j in range(1, i):
        res += str(j)
    res += str(i)
    for j in range(i-1, 0, -1):
        res += str(j)
    print(res)