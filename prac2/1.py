def is_perfect(n):
    t = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            t += i
            
    if t == n:
        return True
    return False
