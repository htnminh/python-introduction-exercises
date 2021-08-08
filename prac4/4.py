import math
import trig
n = int(input())

my_res = 0
math_res = 0
for i in range(1, 21):
    my_res += trig.sin(n + i) if i % 2 == 1 else trig.cos(n + i)
    math_res += math.sin(n + i) if i % 2 == 1 else math.cos(n + i)
    #print(i, my_res)
    
print('Your own implementation:     %.6f' % my_res)
print('Math module implementation:  %.6f' % math_res)