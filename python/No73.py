class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        row = len(matrix)
        col = len(matrix[0])
        
        flip_row = [False for i in xrange(row)]
        flip_col = [False for i in xrange(col)]
        
        for i in xrange(row):
            for k in xrange(col):
                if matrix[i][k] == 0:
                    flip_row[i] = True
                    flip_col[k] = True
        
        for i in xrange(row):
            if flip_row[i] is True:
                for k in xrange(col):
                    matrix[i][k] = 0
        for k in xrange(col):
            if flip_col[k] is True:
                for i in xrange(row):
                    matrix[i][k] = 0
