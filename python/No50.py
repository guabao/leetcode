class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            if n == 0:
                return 1
            else:
                return 0
        elif n == 0:
            return 1
        i = 1
        xs = [x]
        pow = [1]
        
        n1 = abs(n)
        
        while i < n1:
            xs += [xs[-1] * xs[-1]]
            i = i * 2
            pow += [i]
            
        l = len(xs)
        result = 1
        k = 0
        for i in xrange(-1, -l - 1, -1):
            if k + pow[i] <= n1:
                k = k + pow[i]
                result = result * xs[i]
        if n > 0:
            return result
        else:
            return 1. / result
