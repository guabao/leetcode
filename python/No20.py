class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(':1, ')':-1, '[':2, ']':-2, '{':3, '}':-3}
        
        l = len(s)
        
        if l % 2 == 1:
            return False
        if d[s[0]] < 0:
            return False
        
        queue = []
        
        for i in xrange(l):
            if d[s[i]] > 0:
                queue += [d[s[i]]]
            elif d[s[i]] + queue[-1] == 0:
                queue.pop()
            else:
                return False
        
        if len(queue) == 0:
            return True
        else:
            return False
