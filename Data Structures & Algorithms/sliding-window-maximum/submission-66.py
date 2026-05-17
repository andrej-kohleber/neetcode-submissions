class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        l = 0
        r = 0

        for r in range(len(nums)):
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            

            if (r + 1) >= k:
                res.append(nums[dq[0]])
                l += 1 

            if l > dq[0]:
                dq.popleft()                           

            r += 1

        return res