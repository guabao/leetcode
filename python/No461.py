class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        x1 = x
        y1 = y
        diff = 0
        while (x1 != 0) or (y1 != 0):
            x1, xx1 = divmod(x1, 2)
            y1, yy1 = divmod(y1, 2)
            diff = diff + int(xx1 != yy1)
        
        return diff
