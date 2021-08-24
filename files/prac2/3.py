import math

def prime(n):
    if n < 2:
        return False
        
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
            
    return True         
    
def print_prime(n):
    prime_arr = [i for i in range(n) if prime(i)]
    print(*prime_arr)
    
def main():
    print_prime(30)
    print_prime(80)
    
main()