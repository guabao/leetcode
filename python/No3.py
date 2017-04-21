class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        sdict = {}
        start = 0
        maxstr = 0
        for j in xrange(0,len(s)):
            if s[j] in sdict:
                if sdict[s[j]][0] == 1:
                    for i in xrange(start,sdict[s[j]][1]):
                        sdict[s[i]][0] = 0
                    maxstr = max(maxstr, len(s[start:j]))
                    start = sdict[s[j]][1] + 1
            sdict[s[j]] = [1, j]
        maxstr = max(maxstr, len(s[start:]))
        return maxstr
