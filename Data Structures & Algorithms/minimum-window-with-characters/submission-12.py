class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        res = (-1, -1)
        resLen = float("infinity")

        win = {}
        l = 0

        for r in range(len(s)):
            win[s[r]] = 1 + win.get(s[r], 0)

            while self.winContainsAll(countT, win):
                if self.foundSmaller(l, r, resLen):
                    resLen = min(r - l + 1, resLen)
                    res = (l, r)
                win[s[l]] = win.get(s[l], 0) - 1
                l += 1   
                            
        print(resLen)
        print(res)
        return s[res[0]: res[1] + 1] if resLen != float("infinity") else ""
    
    def winContainsAll(self, countT: dict[str, int], win: dict[str, int]) -> bool:
        for c in countT:
            if countT[c] > win.get(c, 0):
                return False
        return True
    
    def foundSmaller(self, l: int, r: int, resLen: int):        
        return r - l + 1 < resLen                      


