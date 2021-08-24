#n = int(input())

def fibo(n):
    a = [0, 1]
    for i in range(n - 1):
        a.append(None)
    if a[n] is not None:
        return a[n]
    a[n] = fibo(n - 2) + fibo(n - 1)
    return a[n]
    
#print(*[fibo(i) for i in range(n)])