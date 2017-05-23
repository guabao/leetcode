class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        pre = []
        l = min(map(len, strs))
        
        for i in xrange(l):
            letter = strs[0][i]
            flag = reduce(lambda x, y: x and (y[i] == letter), [True] + strs)
            if flag:
                pre += [letter]
            else:
                break
        return "".join(pre)
