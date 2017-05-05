class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        if l == 0: return l
        i = 0
        k = 1
        for k in xrange(1, l):
            if nums[k] != nums[i]:
                nums[k], nums[i + 1] = nums[i + 1], nums[k]
                i = i + 1
        
        return i + 1
