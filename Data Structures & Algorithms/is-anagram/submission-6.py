class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are same length
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        # bbcc [ b,1 c,1 ]
        for i in range(len(s)):
            if s[i] in countS:
                countS[s[i]] += 1   
            else:
                countS[s[i]] = 0
        # ccbc
        for i in range(len(t)):
            if t[i] in countT:
                countT[t[i]] += 1    
            else: 
                countT[t[i]] = 0

        return countS == countT




