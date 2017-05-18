# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = operator.attrgetter('start'))
        l = [intervals[0]] if intervals else []
        for i in xrange(1, len(intervals)):
            if intervals[i].start <= l[-1].end:
                l[-1].end = max(intervals[i].end, l[-1].end)
            else:
                l += [intervals[i]]
        return l
