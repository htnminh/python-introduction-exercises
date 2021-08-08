n = int(input()) - 1

borns = [tuple(input().split()) for i in range(n)]
sons = [borns[i][0] for i in range(n)]
dads = [borns[i][1] for i in range(n)]

h = dict()
for dad in dads:
    if dad not in sons:
        h[dad] = 0

for checktime in range(n):
    for i in range(n):
        son = sons[i]
        dad = dads[i]
        if dad in h:
            h[son] = h[dad] + 1

listh = [(name, h[name]) for name in h]
listh.sort()
for ele in listh:
    print(*ele)