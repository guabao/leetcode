class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        d = {}
        for stri in strs:
            sort_str = "".join(sorted(stri))
            if sort_str in d:
                d[sort_str].append(stri)
            else:
                d[sort_str] = [stri]
        return d.values()
