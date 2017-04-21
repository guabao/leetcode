class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        l = []
        if dividend >= 0 :
            if divisor > 0 :
                sign = 1
            else:
                sign = -1
        else:
            if divisor > 0:
                sign = -1
            else:
                sign = 1
        
        d1 = abs(dividend)
        d2 = abs(divisor)
        
        l = [d2]
        ll = [1]
        
        while l[-1] < d1:
            l += [l[-1] + l[-1]]
            ll += [ll[-1] + ll[-1]]
            
        ans = 0
        maxi = len(l) - 2
        
        for i in xrange(maxi, -1, -1):
            if d1 == 0:
                break
            if l[i] < d1:
                d1 = d1 - l[i]
                ans = ans + ll[i]
        
        return ans
