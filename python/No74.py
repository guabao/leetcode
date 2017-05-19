class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if (not matrix) or (not matrix[0]):
            return False
        
        lo = 0
        hi = len(matrix) - 1
        
        while hi - lo > 1:
            mid = (lo + hi) / 2
            if matrix[mid][0] > target:
                hi = mid
            else:
                lo = mid
        
        row = hi if matrix[hi][0] <= target else lo
            
        lo = 0
        hi = len(matrix[row]) - 1
        
        l = []
        while hi > lo:
            mid = (lo + hi) / 2
            if matrix[row][mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return matrix[row][lo] == target
