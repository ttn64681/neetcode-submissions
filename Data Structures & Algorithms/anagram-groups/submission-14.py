class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        # either the key is the sorted word (O(nlogn))
        # or create custom sort (O(n) time, O(n space))
        
        # O(n)
        for word in strs:
            key = self.countChars(word) # O(m)
            res[key].append(word)
        return list(res.values())
        # O(n*m) time, O(n) space

    def countChars(self, word: str) -> Tuple: # O(m) time where m is avg word size
            key = [0]*26 # O(1) fixed space
            for c in word:
                key[ord(c)-ord('z')] += 1
            return tuple(key) # convert to tuple is cheaper than to str
            
                




