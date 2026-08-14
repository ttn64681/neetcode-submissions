class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = [0] * 26,[0] * 26
        for char in s:
            countS[97 - ord(char)] += 1
        print(countS)
        for char in t:
            countT[97 - ord(char)] += 1
        print(countT)
        return countS == countT