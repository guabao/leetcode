class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        s1 = []
        l = len(s)
        l1 = 2 * numRows - 2
        if l1 > 0:
            s1 += [s[l1 * i] for i in xrange((l - 1) / l1 + 1)]
            for i in xrange(1, numRows - 1):
                for k in xrange((l - 1) / l1 + 1):
                    if l1 * k + i < l:
                        s1 += s[l1 * k + i]
                    if l1 * (k + 1) - i < l:
                        s1 += s[l1 * (k + 1) - i]
            s1 += [s[l1 * i + numRows - 1] for i in xrange((l - numRows) / l1 + 1)]
            return ''.join(s1)
        else:
            return s
