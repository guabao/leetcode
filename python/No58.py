class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.split():
            return 0
        else:
            return len(s.split()[-1])