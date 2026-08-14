class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        x.sort()
        y.sort()
        if x == y: return True
        else: return False