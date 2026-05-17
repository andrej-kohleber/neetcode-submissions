class Solution:
    def trap(self, height: List[int]) -> int:
        
        result = []
        l, r = 0, len(height) - 1

        maxl = 0
        maxr = 0

        while l <= r:
            if maxl < maxr:
                maxl = max(height[l], maxl)
                height[l] = maxl - height[l]
                l += 1
            else:
                maxr = max(height[r], maxr)
                height[r] = maxr - height[r]
                r -= 1

        result = 0
        for i in range(len(height)):
            result += height[i]
        

        return result
    
   
        