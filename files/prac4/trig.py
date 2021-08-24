import math

def exp(x):
    res = 0
    
    x_up = 1
    fact = 1
    
    cnt = 1
    
    while abs(res - math.e**x) >= 1e-9:
        #print('%f \n%i / %i' % (res, x_up, fact))
        res += x_up / fact
        x_up *= x
        fact *= cnt
        cnt += 1
        
    return res
        
        
def sin(x):
    while x >= 2 * math.pi:
        x -= 2 * math.pi
    
    
    res = 0
    
    x_up = x
    fact = 1
    
    cnt = 1
    current_sign = 1
    
    while abs(res - math.sin(x)) >= 1e-9:
#         print('in sin', end = ' ')
        res += current_sign * x_up / fact
        
        x_up *= x * x
        fact *= (cnt + 1) * (cnt + 2)
        
        cnt += 2
        current_sign *= -1
    return res
    

def cos(x):
    while x >= 2 * math.pi:
        x -= 2 * math.pi
    res = 0
    
    x_up = 1
    fact = 1
    
    cnt = 0
    current_sign = 1
    
    while abs(res - math.cos(x)) >= 1e-9:
#         print('in cos', end = ' ')
        res += current_sign * x_up / fact
        #print(res)
        x_up *= x * x
        fact *= (cnt + 1) * (cnt + 2)
        
        cnt += 2
        current_sign *= -1
    return res
    
if __name__ == '__main__':
    print(exp(3))
    print(sin(20))
    print(cos(26))
