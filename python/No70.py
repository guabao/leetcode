class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = [1, 2, 3]
        if n < 4:
            return l[n - 1]
        else:
            n1 = n - 3
            i = 0
            while i < n1:
                l[0], l[1], l[2] = l[1], l[2], l[1] + l[2]
                i += 1
            return l[-1]
