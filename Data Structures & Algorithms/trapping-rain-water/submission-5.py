class Solution:
    def trap(self, height: List[int]) -> int:

        res = []
        for i in range(len(height)):
            res.append(self.calc(i, height))
            

        trap = 0
        for r in res:
            if r > 0:
                trap += r


        return trap
    
    def calc(self, i: int, height: List[int]) -> int:
        l = i - 1
        lmax = 0
        while l >= 0:
            if height[l] > lmax:
                lmax = height[l]
            l -= 1

        r = i + 1 
        rmax = 0
        while r < len(height):
            if height[r] > rmax:
                rmax = height[r]
            r += 1

        w = min(lmax, rmax) - height[i]
        print(str(lmax) + "-" + str(rmax) + " = " + str(w))
        return w
        