def hanoi_tower(n):
    '''run and return number of transfers'''
    def transfer(n, start, end, mid):
        if n == 1:
            nonlocal count
            count += 1
            mapind = ['A', 'B', 'C']
            print(' '*18 + 'Step '+ str(count) + ': ' + mapind[start] + ' -> ' + mapind[end])
            move(start, end)
            printboard()
        else:
            transfer(n - 1, start, mid, end)
            transfer(1, start, end, mid)
            transfer(n - 1, mid, end, start)
    count = 0
    transfer(n, 0, 2, 1)
    return count

'''
a =                     
      0  1  2  3                    

0     4  3  2  1                    
1     0  0  0  0                    
2     0  0  0  0

printed :
                A  B  C

                1  |  |
                2  |  |
                3  |  |
                4  |  |
'''
def printboard():
    '''print current board'''
    print('|  A  B  C  |')
    
    for col in range(n - 1, -1, -1):
        print('|  ', end = '')
        for row in range(3):
            character = '.' if a[row][col] == 0 else a[row][col]
            print(str(character) + '  ', end = '')
        print('|')
        

def move(rowstart, rowend):
    '''make a move'''
    def col_lastnonenull(row):
        for col_ind in range(n - 1, -1, -1):
            if a[row][col_ind] != 0:
                return col_ind
            # return n - 1
    def col_firstnull(row):
        for col_ind in range(n):
            if a[row][col_ind] == 0:
                return col_ind
            # return 0
    a[rowend][col_firstnull(rowend)] = a[rowstart][col_lastnonenull(rowstart)]
    a[rowstart][col_lastnonenull(rowstart)] = 0

# MAIN:

# input n
n = int(input('n = '))

#initialize list of list a, n = 4, 
'''
a =
      0  1  2  3
      
0     4  3  2  1
1     0  0  0  0
2     0  0  0  0
'''
a = [[n - i for i in range(n)]]
for i in range(2):
    a.append([0 for j in range(n)])
    
# print init a board
printboard()

# run and return result
hanoi_tower(n)








