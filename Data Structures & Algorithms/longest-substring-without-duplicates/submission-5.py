class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        _set = set()
        l = 0
        maxLength = 0
        
        for r in range(len(s)):
            # Пока находим повторяющийся символ
            while s[r] in _set:
                _set.remove(s[l])
                l += 1
            
            # Добавляем новый символ
            _set.add(s[r])
            
            # Обновляем максимальную длину
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength