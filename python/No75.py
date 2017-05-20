class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]
        for n in nums: 
            count[n] += 1
        i = 0
        while i < count[0]:
            nums[i] = 0
            i += 1
        while i < count[0] + count[1]:
            nums[i] = 1
            i += 1
        while i < count[0] + count[1] + count[2]:
            nums[i] = 2
            i += 1
