class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        maxjump = l - 1
        i = l - 2
        while i > -1:
            if i + nums[i] >= maxjump:
                maxjump = i
            i -= 1
        return not maxjump
