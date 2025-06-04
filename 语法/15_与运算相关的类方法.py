import copy

class Matrix(list):

    def __init__(self, val: tuple|list):
        if type(val) == list:
            super().__init__(val)
            self.ln = len(val)
            self.col = len(val[0])
        if type(val) == tuple:
            ln, col = val
            super().__init__()
            for i in range(ln):
                self.append([0 for i in range(col)])
            self.ln = ln
            self.col = col
        
    def batch_getval(self, func):
        for i in range(self.ln):
            for j in range(self.col):
                self[i][j] = func(i, j)
        
    def __add__(self, another):
        if not isinstance(another, Matrix):
            raise TypeError
        if (self.ln, self.col) != (another.ln, another.col):
            raise ValueError
        newmat = Matrix((self.ln, self.col))
        func = lambda i, j: self[i][j] + another[i][j]
        newmat.batch_getval(func)
        return newmat
    
    def __mul__(self, another):
        if isinstance(another, int):
            another = float(another)
        if isinstance(another, float):
            newmat = copy.deepcopy(self)
            for i in range(self.ln):
                for j in range(self.col):
                    newmat[i][j] *= another
            return newmat
        if isinstance(another, Matrix):
            if another.ln != self.col:
                raise ValueError
            newmat = Matrix((self.ln, another.col))
            func = lambda i, j:sum(map(lambda x:self[i][x] * another[x][j], range(self.col)))
            newmat.batch_getval(func)
            return newmat
        else:
            raise TypeError
    
    def __imul__(self, another):
        return self * another
    
    def __iadd__(self, another):
        return self + another
    
    def __rmul__(self, another):
        if isinstance(another, int) or isinstance(another, float) :
            return self * another
        if isinstance(another, Matrix):
            return another * self
        raise TypeError
    
    def __int__(self):
        return self.ln * self.col
    
def test_matrix():
    a = Matrix([[0, 1], [1, 0]])
    b = Matrix([[1, 2], [3, 4]])
    print(int(a))

test_matrix()

