n, k = (int(x) for x in input().split())
a = ['I' for i in range(n)]

for time in range(k):
    fr, to = (int(x) - 1 for x in input().split())
    for i in range(fr, to + 1):
        a[i] = '.'

for ele in a: print(ele, end = '')