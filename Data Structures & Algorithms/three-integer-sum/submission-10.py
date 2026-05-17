class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Оптимизация 1: если минимальный элемент > 0, сумма не может быть 0
            if nums[i] > 0:
                break
                
            # Оптимизация 2: если сумма трех минимальных > 0, тоже можно выйти
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
                
            # Оптимизация 3: если сумма трех максимальных < 0, пропускаем этот i
            if nums[i] + nums[-2] + nums[-1] < 0:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:

                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    result.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1

                    l += 1
                    r -= 1

                elif total > 0:
                    r -= 1
                else:
                    l += 1

        return result
        