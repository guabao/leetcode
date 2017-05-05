class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        if not nums: return -1
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (high + low) / 2
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid
                else:
                    low = mid + 1
            else:
                if nums[mid + 1] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid
        if nums[low] == target:
            return low 
        else:
            return -1
