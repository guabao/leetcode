class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #if m == 0 or n == 0:
        #    return 0
        l = [1 for i in range(n)]
        for i in range(m-1):
            for k in range(1, n):
                l[k] = l[k - 1] + l[k]
        
        return l[-1]
