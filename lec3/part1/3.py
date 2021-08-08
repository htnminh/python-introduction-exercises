def reverse(n):
    res = 0
    while n != 0:
        digit = n % 10
        n //= 10
        res = res * 10 + digit
    print(res)
# reverse(74321)