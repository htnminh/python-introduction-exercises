def pline(i):
    def ele(i, j):
        if i == 1 or j == 1 or j == i:
            return 1
        return ele(i - 1, j - 1) + ele(i - 1, j)
    def loopj(j):
        if j == 1:
            print(' ' * 5 * (n - i), end = '')
        print(ele(i,j), end = '         ')
        if j != i:
            loopj(j+1)
    print()
    loopj(1)

def pascal(i):
    pline(i)
    if i != n:
        pascal(i+1)

n = int(input('n = '))
pascal(1)

# here oke ??