class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        res = (-1, -1)
        resLen = float("infinity")
        win = {}
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        need = len(countT)
        have = 0
        l = 0
        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c, 0)

            if c in countT and win[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = (l, r)
                
                win[s[l]] -= 1
                if s[l] in countT and win[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l : r + 1] if resLen != float("infinity") else ""