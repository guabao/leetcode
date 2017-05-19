class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        max_digit = (len(str(x)) + 1) / 2
        basis = [10 ** i for i in xrange(max_digit, -1, -1)]
        number = 0
        for current in xrange(len(basis)):
            while (number + basis[current]) * (number + basis[current]) <= x:
                number = number + basis[current]
        return number
