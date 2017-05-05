class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 1
        l = len(nums)
        for i in xrange(l):
            nums[i] = l + 1 if nums[i] <= 0 else nums[i]
        
        for i in xrange(l):
            if abs(nums[i]) <= l:
                nums[abs(nums[i]) - 1] = -1 * abs(nums[abs(nums[i]) - 1])
        
        for i in xrange(l):
            if nums[i] > 0:
                return i + 1
        return l + 1
