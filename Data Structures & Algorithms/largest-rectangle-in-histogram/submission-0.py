class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        res = []
        for i in range(len(heights)):
            res.append(self.calc(heights, i))
        return max(res)


    #heights=[7,1,7,2,2,4]
    def calc(self, heights: List[int], i: int) -> int:
        h = heights[i]
        l = i
        while l - 1 >= 0 and heights[l - 1] >= h:
            l -= 1
        
        r = i
        length = len(heights)
        while r + 1 <= length - 1 and heights[r + 1] >= h:
            r += 1
    
    
        return (r - l + 1) * h
        