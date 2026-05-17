class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2

            if nums[m] == target:
                return m

             # Check if left half is sorted
            if nums[l] <= nums[m]:
                # Target is in left sorted half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right half is sorted
            else:
                # Target is in right sorted half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
                

        return -1