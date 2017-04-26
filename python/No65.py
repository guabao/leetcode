class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return False        
        if s[0] == ' ':
            return self.isNumber(s[1:])
        elif s[-1] == ' ':
            return self.isNumber(s[:-1])

        try:
            float(s)
            return True
        except:
            return False
