class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = list(s)
        a1.sort()

        a2 = list(t)
        a2.sort()

        return a1 == a2