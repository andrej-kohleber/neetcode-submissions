class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        res = []
        window_max = max(nums[:k])
        res.append(window_max)
        
        for i in range(k, len(nums)):
            # Если выходящий элемент был максимумом, ищем новый
            if nums[i - k] == window_max:
                window_max = max(nums[i - k + 1:i + 1])
            else:
                window_max = max(window_max, nums[i])
            res.append(window_max)
        
        return res