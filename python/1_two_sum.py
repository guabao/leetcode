class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        index1 = 0
        index2 = 0
        flag = []
        location = []
        minnum = min(num)
        if minnum < 0:
            add = abs(min(num))
            target = target + 2 * add
            #print target
            for i in xrange(0,len(num)):
                num[i] = num[i] + add
        else:
            add = 0
        #print num
        for i in xrange(0,max(max(num) + 1,target + 1)):
            flag.append(0)
            location.append(0)
        for i in xrange(0,len(num)):
            if (target - num[len(num)-1-i]>=0) and (flag[target - num[len(num)-1-i]] == 0):
                flag[target - num[len(num)-1-i]] = 1
                location[target - num[len(num)-1-i]] = len(num)-i
        #print flag
        #print location
        for i in xrange(0,len(num)):
            if (flag[num[i]] == 1) and (location[num[i]]!=i+1):
                break
        if i > location[num[i]]:
            temp = i
            i = location[num[i]]
            location[num[i]] = temp
        #return (i + 1, location[i] + 1)
        return (i + 1,location[num[i]])