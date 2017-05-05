class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        import bisect
        x1 = bisect.bisect_left(nums, target)
        if x1 <= len(nums) - 1:
            if nums[x1] == target:
                x2 = bisect.bisect_right(nums, target)
                return [x1, x2 - 1]
            else:
                return [-1, -1]
        else:
            return [-1, -1]
