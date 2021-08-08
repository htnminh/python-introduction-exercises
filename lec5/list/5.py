def checkline(i, j):
    #for m in range(2):
    for n in range(2):
        if a[i][n] == a[j][n]:
            return returnFalse(i, j)
    return True

def checkdiag(i, j):
    for plus in range(-7, 8):
        if [a[i][0] + plus, a[i][1] + plus] == a[j] or \
           [a[i][0] + plus, a[i][1] - plus] == a[j]: 
                return returnFalse(i, j)
    return True

def check(i, j):
    if checkline(i, j) and checkdiag(i, j):
        return True
    return returnFalse(i, j)

def checkall():
    for i in range(8):
        for j in range(i + 1, 8):
            if not check(i, j):
                return returnFalse(i, j)
    return True

def returnFalse(i, j):
    #print(a[i], a[j])
    return False

cases = int(input())

for case in range(cases):
    a = list()
    for i in range(8):
        a.append( [int(x) for x in input().split()])
    #print(a)
    
    print('NO' if checkall() else 'YES')
    