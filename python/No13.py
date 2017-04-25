class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = 0
        l = len(s)
        if l == 1:
            return d[s[0]]
        i = 0
        while i < len(s) - 1:
            if d[s[i + 1]] <= d[s[i]]:
                value = value + d[s[i]]
                i = i + 1
            else:
                value = value + d[s[i + 1]] - d[s[i]]
                i = i + 2
        if i < len(s):
            value = value + d[s[i]]
        
        return value
