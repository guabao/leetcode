class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def permute1(nums, pre):
            if not nums:
                return [pre]
            else:
                l = []
                for i in xrange(len(nums)):
                    l = l + permute1(nums[:i] + nums[i+1:], pre + [nums[i]])
                return l
        return permute1(nums, [])
