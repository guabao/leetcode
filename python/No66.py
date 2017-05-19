class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        d1 = [0] + digits
        
        t = 1
        for i in xrange(len(d1) - 1, 0, -1):
            t, d1[i] = divmod(d1[i] + t, 10)
        d1[0] = t
        
        if d1[0] == 0:
            return d1[1:]
        else:
            return d1
