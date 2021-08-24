
def myexp(x):
    res = 1
    gt = 1
    i = 1
    while abs(res - e ** x) < 1e-9:
        gt *= i
        res += x**i / gt
        i += 1
    
def mysin(x):
    res = x
    gt = 1
    i = 1
    while abs(res - e ** x) < 1e-9:
        gt *= i
        res += x**i / gt
    