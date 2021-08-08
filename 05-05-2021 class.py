'''
sum_of_squares = lambda x, y: x*x + y*y
print(sum_of_squares(3, 5))

f1 = lambda a, b, c: max(a, b, c)
f = lambda a, b, c: a if a >= b and a >= c \
                    else b if b >= c \
                    else c
print(f1(12, 34, 56))
print(f(13, 23, 21))

gcd = lambda a, b: b if a % b == 0 \
                      else gcd(b, a % b)
#print(gcd(8,36))
'''

import time
x = int(input('x = '))
y = int(input('y = '))

print('Not recursion:')
print('    n                    Result                      Time')
fibb = [0, 1]
      #12345 1234567890123456789012345 1234567890123456789012345
start = time.time()
for i in range(2, y + 1):
    fibb.append(fibb[i-2] + fibb[i-1])
    if x <= i and i <= y:
        #time.sleep(0.01)
        print('{:5.0f} {:25.0f} {:25.15f}'.format(i, fibb[i], time.time() - start))
    
print('Recursion:')

print('    n                    Result                      Time')
def fib(i):
    if i == 0: return 0
    if i == 1: return 1
    return fib(i-2) + fib(i-1)
start = time.time()
for i in range(x, y + 1):
    print('{:5.0f} {:25.0f} {:25.15f}'.format(i, fib(i), time.time() - start))
