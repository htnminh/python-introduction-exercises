def digit_sum(a):
    s = str(a)
    res = 0
    for digit in s:
        res += int(digit)
    return res

def digit_sum_greater(a, b):
    if digit_sum(a) > digit_sum(b):
        return 'YES'
    return 'NO'
