def sum_of_div(a):
    res = 0
    for i in range(1, a):
        if a % i == 0:
            res += i
    return res

def friendly(a, b):
    if a == sum_of_div(b) and b == sum_of_div(a):
        return 'YES'
    return 'NO'