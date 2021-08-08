def print_prime(n):
    a = [None for i in range(n)]
    for i in range(2, n):
        if a[i] is None:
            a[i] = True
            print(i, end = ' ')
            for j in range(i * i, n, i):
                a[j] = False
              
    #prime_arr = [i for i in range(2, n) if d[i]]
    #print(*prime_arr)
        
#print_prime(80)
    
