class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        numdict = {}
        for element in num:
            if element in numdict:
                numdict[element] += 1
            else:
                numdict[element] = 1
        maxcount = 0
        target = 0
        for (k, v) in numdict.items():
            if v > maxcount:
                target = k
                maxcount = v
        return target
