class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        n = len(s)
        
        # Перебираем все возможные начала подстрок
        for i in range(n):
            # Перебираем все возможные концы подстрок
            for j in range(i, n):
                # Считаем частоты в подстроке s[i:j+1]
                freq = {}
                for char in s[i:j+1]:
                    freq[char] = freq.get(char, 0) + 1
                
                # Находим самый частый символ в этой подстроке
                max_freq = max(freq.values())
                window_len = j - i + 1
                
                # Проверяем условие
                if window_len - max_freq <= k:
                    max_length = max(max_length, window_len)
        
        return max_length