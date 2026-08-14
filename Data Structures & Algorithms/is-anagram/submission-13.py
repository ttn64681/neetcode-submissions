class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # edge case
            return False

        # O(2n) space
        s_charcount = defaultdict(int)
        t_charcount = defaultdict(int)
        
        for c in s: # O(n) loop
            s_charcount[c] += 1 # O(1) hashmap insert/update/removal
        for c in t:
            t_charcount[c] += 1
        return s_charcount == t_charcount

            
