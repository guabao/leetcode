class Solution(object):
    def isMatch(self, s, p, good_p = False):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        if len(p) == 0:
            return len(s) == 0
        else:
            if len(s) == 0:
                if len(p) == 1:
                    return False
                elif p[1] == '*':
                    return self.isMatch(s, p[2:], good_p = good_p)
                else:
                    return False
        
        if len(p) == 1:
            if len(s) > 1:
                return False
            else:
                return (s[0] == p[0]) or (p[0] == '.')
        
        if not good_p:
            for i in xrange(len(p) - 1):
                if (p[i] == '*') and (p[i + 1] == '*'):
                    p = p[:i] + p[i + 1:]
            good_p = True
        
        #if throw:
        #for i in xrange(len(p)):
        if (s[0] == p[0]) or (p[0] == '.'):
            if p[:2] == '.*':
                for i in xrange(len(s) + 1):
                    if self.isMatch(s[i:], p[2:], good_p = good_p):
                        return True
            elif p[1] == '*':
                if self.isMatch(s, p[2:], good_p = good_p):
                    return True
                k = 0
                while s[k] == s[0]:
                    if self.isMatch(s[k + 1:], p[2:], good_p = good_p):
                        return True
                    k = k + 1
                    if k > len(s) - 1:
                        break
            elif self.isMatch(s[1:], p[1:], good_p = good_p):
                return True
        elif p[1] == '*':
            return self.isMatch(s, p[2:], good_p = good_p)
        return False
