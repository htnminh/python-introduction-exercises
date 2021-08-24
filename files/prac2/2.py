def pline(i):
    def ele(i, j):
        if i == 1 or j == 1 or j == i:
            return 1
        return ele(i - 1, j - 1) + ele(i - 1, j)
    def loopj(j):
        '''if j == 1:
            print(' ', end = '')'''
        print(ele(i,j), end = ' ')
        if j != i:
            loopj(j+1)
    loopj(1)
    print()
    
def pascal(i, n):
    pline(i)
    if i != n:
        pascal(i+1, n)

def pascal_triangle(n):
    pascal(1, n)

#pascal_triangle(5)
