class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        l1 = obstacleGrid[0]
        l = []
        for i, li in enumerate(l1):
            if li == 1:
                i = i - 1
                break
            else:
                l += [1]
        if l:
            l += [0 for i in xrange(len(l1) - i - 1)]
            n = len(obstacleGrid[0])
        
            for i in xrange(1, len(obstacleGrid)):
                if obstacleGrid[i][0] == 1:
                    l[0] = 0
                for k in xrange(1, n):
                    if obstacleGrid[i][k] == 1:
                        l[k] = 0
                    else:
                        l[k] = l[k - 1] + l[k]
            return l[-1]
        else:
            return 0
        
