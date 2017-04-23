class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        max_length = 0
        length = 0
        pre = 0
        
        for i in xrange(len(nums)):
            if nums[i] == 1:
                length = length + 1
            else:
                if max_length < length:
                    max_length = length
                length = 0
            pre = nums[i]
        
        if max_length < length:
            max_length = length
            
        return max_length
