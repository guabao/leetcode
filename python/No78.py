class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return reduce(lambda x, y: x + map(list, list(itertools.combinations(nums, y))), [[[]]] + range(1, len(nums) + 1))
