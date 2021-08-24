class Matrix(object):
    def __init__(self, lst):
        self.lst = lst
    
    def size(self):
        return (len(self.lst), len(self.lst[0]))
        #     (number of rows, number of columns)
        
    def __str__(self):
        s = ''
        num_row, num_col = self.size()
        
        for row_ind in range(num_row):
            if row_ind != 0:
                s += '\n'
            for col_ind in range(num_col):
                s += str(self.lst[row_ind][col_ind])
                if col_ind < num_col - 1:
                    s += '\t'
        return s    
    
'''  
m = Matrix([[1, 0], [0, 1]])
print(m)
print(m.size())
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
print(m.size())
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)
print(m.size())
'''