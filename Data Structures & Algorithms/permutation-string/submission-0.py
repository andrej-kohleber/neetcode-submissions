class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1 = "".join(sorted(s1))
        win_len = len(s1)  
        print(win_len)      
        for r in range(win_len, len(s2) + 1):
            print(sorted(s2[l:r]))
            if "".join(sorted(s2[l:r])) == s1:
                return True
            else:
                l += 1
        
        return False

        