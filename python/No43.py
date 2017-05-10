class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        l1 = len(num1)
        l2 = len(num2)
        
        result = [0 for i in xrange(l1 + l2 + 1)]
        
        for i in xrange(l1):
            for k in xrange(l2):
                p = l1 + l2 - i - k
                result[p] = result[p] + int(num1[l1 - 1 - i]) * int(num2[l2 - 1 - k])
        
        for i in xrange(l1 + l2, -1, -1):
            temp = result[i] / 10
            result[i] = result[i] - temp * 10
            result[i - 1] = result[i - 1] + temp
        
        while result[0] == 0:
            result = result[1:]
            if not result:
                return "0"
        return "".join(map(str, result))
