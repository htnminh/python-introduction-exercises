def floyd(n):
    current = '1'
    s = ''
    for i in range(n):
        s = current + s
        current = str(abs(int(current)-1))
        print(s)
