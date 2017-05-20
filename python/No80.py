class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l < 3:
            return l
        
        left = 0
        right = 2
        while right < l:
            if nums[left] == nums[right]:
                nums.pop(right)
                l -= 1
            else:
                left += 1
                right += 1
        return len(nums)
