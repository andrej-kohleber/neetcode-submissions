class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        result = 0
        maxF = 0
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            maxF = max(maxF, count[s[right]])
            while (right - left + 1) - maxF > k:
                count[s[left]] -= 1
                left += 1                
                
            result = max(result, right - left + 1)


        return result