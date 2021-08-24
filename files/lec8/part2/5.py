import copy

class Matrix(object):
    def __init__(self, lst):
        self.lst = lst
        self.num_row, self.num_col = len(self.lst), len(self.lst[0])
        
    def size(self):
        return (self.num_row, self.num_col)
        #     (number of rows, number of columns)
        
    def __str__(self):
        s = ''
        
        for row_ind in range(self.num_row):
            if row_ind != 0:
                s += '\n'
            for col_ind in range(self.num_col):
                s += str(self.lst[row_ind][col_ind])
                if col_ind < self.num_col - 1:
                    s += '\t'
        return s    
    
    def __add__(self, other):
        res = [ [None for i in range(self.num_col)] for j in range(self.num_row)]
        
        for row_ind in range(self.num_row):
            for col_ind in range(self.num_col):
                res[row_ind][col_ind] = self.lst[row_ind][col_ind] + \
                                        other.lst[row_ind][col_ind]
                                        
        return Matrix(res)


    def __mul__(self, num):
        res = [ [None for i in range(self.num_col)] for j in range(self.num_row)]
        for row_ind in range(self.num_row):
            for col_ind in range(self.num_col):
                res[row_ind][col_ind] = self.lst[row_ind][col_ind] * num
        return Matrix(res)
        
    def __rmul__(self, num):
        return self.__mul__(num)
  
    def remove_row_col(M, i, j):
            # remove i-th row, j-th col
        res = copy.deepcopy(M.lst)
        for row_ind in range(M.num_row):
            del res[row_ind][j]
        del res[i]
        return Matrix(res)
    
    def det(M):
    # det of of the Matrix M    
        if M.size() == (1, 1):
            return M.lst[0][0]
            
        res = 0
        current_sign = 1
        #print(M.size())
        for col_ind in range(M.num_col):
            #print(col_ind)
            res += current_sign * M.lst[0][col_ind] * \
                   M.remove_row_col(0, col_ind).det()
            current_sign *= -1
            
        return res
        
    def transpose(M):
        res = [ [None for i in range(M.num_row)] for j in range(M.num_col)]
        for row_ind in range(M.num_row):
            for col_ind in range(M.num_col):
                res[col_ind][row_ind] = M.lst[row_ind][col_ind]
                
        return Matrix(res)
        
    def inverse(M):
        C = [ [None for i in range(M.num_col)] for j in range(M.num_row)]
        for row_ind in range(M.num_row):
            for col_ind in range(M.num_col):
                C[row_ind][col_ind] = M.remove_row_col(row_ind, col_ind).det() \
                                      * (-1) ** (col_ind + row_ind)
        C = Matrix(C).transpose()
        return (1/M.det()) * C
    
    def mats_mul(M, N):
        def dot_prod(row, col):
            res = 0
            for i in range(len(row)):
                res += row[i] * col[i]
            return res
        
        def take_col(j):
            return [N.lst[i][j] for i in range(N.num_row)]
           
        
        res = [ [None for i in range(N.num_col)] for j in range(M.num_row)]
        for i in range(M.num_row):
            for j in range(M.num_col):
                #print(j, take_col(j))
                try:
                    res[i][j] = dot_prod(M.lst[i], take_col(j))
                except:
                    pass
                
        return Matrix(res)
        
    def solve(M, b):
        '''
        solve Mx = b
               x = M^-1 * b
        1   2   3    5 = b      x = 5
        6   8   9    6              -12
        5   2   1    9              8
        '''
        
        res = M.inverse().mats_mul(Matrix([b]).transpose())
        res = [ele for row in res.lst\
                for ele in row if ele is not None]
        res_str = str()
        for solution in res:
            res_str += '%.2f' % solution + ' '
        return res_str[:-1] 
        
        

class SquareMatrix(Matrix):
    def __init__(self, lst):
        Matrix.__init__(self, lst)
        
    def unit_matrix(self):
        res = [ [0 for i in range(self.num_col)] for j in range(self.num_row)]
        for i in range(self.num_col):
            res[i][i] = 1
        #print(res)
        return Matrix(res)
        
    def __pow__(self, n):
        if n == 0:
            return self.unit_matrix()
        if n >= 1:
            res = copy.deepcopy(self)
            root = copy.deepcopy(self)
            for i in range(n - 1):
                res = res.mats_mul(root)
            return res
        if n <= -1:
            res = copy.deepcopy(self) 
            res = res.inverse()
            res = SquareMatrix(res.lst)
            res = res ** -n

            res = [[round(ele) for ele in row] for row in res.lst]
            return Matrix(res)


'''
m = SquareMatrix([[1, 0], [0, 1]])
print(isinstance(m, Matrix))
m = SquareMatrix([[1, 1], [0, 1]])
for i in range(-5, 6):
    print(i)
    print(m ** i)
    '''


