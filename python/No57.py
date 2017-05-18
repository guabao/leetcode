# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        
        l = len(intervals)
        s = newInterval.start
        e = newInterval.end
        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]
        if left + right != intervals:
            newInterval.start = min(newInterval.start, intervals[len(left)].start)
            newInterval.end = max(newInterval.end, intervals[l - 1 - len(right)].end)
        return left + [newInterval] + right
