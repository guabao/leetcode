class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        if not nums:
            return 0
        l = len(nums)
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right = right - 1
            else:
                left = left + 1
        
        if nums[left] == val:
            return left
        else:
            return left + 1
