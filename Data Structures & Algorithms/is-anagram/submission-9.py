class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # check unequal lengths
            return False
        
        s_count = {}
        t_count = {}

        for i in range(len(s)): # count str s chars
            if s[i] in s_count:
                s_count[s[i]] = s_count[s[i]] + 1
            else:
                s_count[s[i]] = 1
        
        for i in range(len(t)): # count str t chars
            if t[i] in t_count:
                t_count[t[i]] = t_count[t[i]] + 1
            else:
                t_count[t[i]] = 1
        
        return s_count == t_count # compares hashmaps
