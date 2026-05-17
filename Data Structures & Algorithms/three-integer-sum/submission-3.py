class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []
        result_set = set()

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    triplet = (nums[i], nums[l], nums[r])
                    if (triplet not in result_set):
                        result_set.add(triplet)
                        result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
        return result
        