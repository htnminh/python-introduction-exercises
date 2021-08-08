#correct

def prime(a):
    if a<=1:
        return False
    for i in range(2, int(a ** 1/2) + 1):
        if a % i == 0:
            return False
    return True

def if_sum_of_2_primes(a):
    for i in range(2, int(a/2)):
        if prime(i) and prime(a-i):
            return True
    return False

n = int(input())
for i in range(n):
    x = int(input())
    if if_sum_of_2_primes(x):
        print('YES')
    else:
        print('NO')