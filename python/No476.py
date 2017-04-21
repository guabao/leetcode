class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = bin(num)
        return 2 ** (len(a) - 2) - 1 - num
