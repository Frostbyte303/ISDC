import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        # TODO - your code here
        if len(self[0]) == 1:    #self.h ==1
            selfDeterminant = self  #.g[0][0]
        else:
            selfDeterminant = (self[0][0]*self[1][1] - self[0][1]*self[1][0]) # why self not self.g[][] 
        return selfDeterminant
    
    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        # TODO - your code here
        if (self[0]) == 1:  #why don't we use if len(self.h) == 1: 
            self = self
            return self
        else:
            selfTrace = (self[0][0]*self[1][1] - self[0][1]*self[1][0])
        return selfTrace

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
           
        # TODO - your code here
        if (self[0]) == 1:   
            selfInvert = (1/(self[0]))
        else:
            selfInvert = ((1/selfDeterminant)((selfTrace)(I))- self)

        return Matrix(selfInvert)
    
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        if len(self.h) == 1:
            selfT = self
        else:
            selfT = self[[0][0],[1][0]],[[0][1],[1][1]]
        
        return selfT
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        #   
        # TODO - your code here
        #
        selfAdd = [[0 for row in range(self.w)] for col in range(self.h)]
        for i in range(self.h):
            #row = []
            for j in range(self.w):
                #row.append
                selfAdd[i][j] = ([self[i][j] + other[i][j]])
                #selfAdd.append(row)
        
        return Matrix(selfAdd)
        
    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        #   
        # TODO - your code here
        #self = [[0 for i in range(self.w)] for j in range(self.h)]
        for i in range(self.h):
            for j in range(self.w):
                self[i][j] *= -1
        #print (self)
        #type(self.h)
        return self
             
            
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        #   
        # TODO - your code here
        #
        #selfSub= [[0 for row in range(self.h)] for col in range(self.w)]
        #selfSub = [[0]* self.h for i in range (self.w)] # is this calling zeros?
        selfSub = [[0 for row in range(self.w)] for col in range(self.h)]

        for i in range(self.h):
            for j in range(self.w):
                selfSub[i][j] = ([self[i][j] + other[i][j]])
                        
        return Matrix(selfSub)                   

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        #   
        # TODO - your code here
        #
        selfMul= [[0 for row in range(self.h)] for col in range(self.w)]
        for i in range(self.h):
            for j in range(self.w):
                 selfMul[i][j] = self.g[i][j] * other.g[i][j]                     
        return Matrix(selfMul)                         

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            #   
            # TODO - your code here
            #
        selfRmul= [[0 for row in range(self.h)] for col in range(self.w)]
        for i in range(self.h):
            for j in range(self.w):
                 selfRmul[i][j] = (self.g[i][j] * (other.g))                     
        return Matrix(selfRmul) 
