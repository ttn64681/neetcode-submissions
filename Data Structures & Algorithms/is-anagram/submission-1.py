class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check if strings are same length
        if len(s) != len(t):
            return False
        
        # turn strings to char arrays
        sArray = list(s)
        tArray = list(t)
        # sort char arrays
        sArray.sort()
        tArray.sort()

        # compare each letter simultaneously in each array
        for i in range(len(sArray)):
            if sArray[i] != tArray[i]:
                return False
        return True
