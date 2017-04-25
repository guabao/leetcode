class Solution(object): 
    def maxArea(self, height): 
        """ 
        :type height: List[int] 
        :rtype: int 
        """ 
         
        left = 0
        right = len(height) - 1
        maxvol = 0
        
        while left != right:
            maxvol = max(maxvol, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left = left + 1
            elif height[left] > height[right]:
                right = right - 1
        return maxvol
