# def run and return result
def hanoi_tower(n):
    def transfer(n, start, end, mid):
        if n == 1:
            nonlocal count
            count += 1
            mapind = ['A', 'B', 'C']
            fo.write(' '*18 + 'Step '+ str(count) + ': ' + mapind[start] + ' -> ' + mapind[end] + '\n')
            # fo.write('A  B  C\n')
            move(start, end)
            printboard()
        else:
            transfer(n - 1, start, mid, end)
            transfer(1, start, end, mid)
            transfer(n - 1, mid, end, start)
    count = 0
    transfer(n, 0, 2, 1)
    return count

# def print current board to file
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

    fo.write('|  A  B  C  |\n')
    
    for col in range(n - 1, -1, -1):
        fo.write('|  ')
        for row in range(3):
            character = '.' if a[row][col] == 0 else a[row][col]
            fo.write(str(character) + '  ')
        fo.write('|\n')
        
# make a move
def move(rowstart, rowend):
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
# open file
fo = open('hanoi_tower_out.txt', 'w')

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

fo.close()








'''
def initialize():
    for row in range(n):
        for col in range(3):
            a[row][col] = str(row + 1) if col == 0 else '|'
            
def printboard():
    for row in a:
        for ele in row:
            fo.write(ele + '  ')
        fo.write('\n')
    
    for row in a:
        print(row)
    

def move1_inboard(start, end):
    def row_firstnonenull(col):
        for row_ind in range(n):
            if a[row_ind][col] != '|':
                return row_ind
            return -1
    def row_lastnull(col):
        for row_ind in range(n - 1, -1, -1):
            if a[row_ind][col] == '|':
                return row_ind
            return n - 1
    a[row_lastnull(end)][end] = \
                            a[row_firstnonenull(start)][start]
    a[row_firstnonenull(start)][start] = '|'
    
fo = open('hanoi_tower_out.txt', 'w')

a = [ ['|' for row in range(3) ] for col in range(n) ]

initialize()
printboard()
'''