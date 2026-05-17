class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        result = r
        while l <= r:
            m = l + (r - l) // 2

            hours = 0
            for p in piles:
                hours += math.ceil(p / m)
            
            if hours <= h:
                result = min(result, m)
                r = m - 1
            else:
                l = m + 1

        return result
        