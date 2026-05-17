class Solution:
    def findMin(self, nums: List[int]) -> int:
        rs = nums[0]
        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]:
                rs = min(rs, nums[l])
                break
            m = l + (r - l) // 2
            rs = min(rs, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return rs



 
            
      

        