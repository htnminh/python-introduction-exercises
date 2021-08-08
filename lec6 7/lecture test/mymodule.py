def sumsquared(a, b):
    return a ** 2 + b ** 2
# TypeError: unsupported operand type(s) for ** or pow(): 'str' and 'int'

def sumsquared2(a, b):
    return float(a) ** 2 + float(b) ** 2

if __name__ == '__main__':
    import sys
    print('Tong binh phuong la', sumsquared2(sys.argv[1], sys.argv[2]))
    
'''
python mymodule.py 8 3
Tong binh phuong la 73.0
'''