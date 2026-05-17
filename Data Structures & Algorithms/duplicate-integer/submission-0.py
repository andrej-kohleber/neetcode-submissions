

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        
        for key in nums:
            if key in counter:
                return True
            else:
                counter[key] = 1

        return False
        