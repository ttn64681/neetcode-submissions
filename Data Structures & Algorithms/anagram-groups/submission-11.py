class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        # either the key is the sorted word (O(nlogn))
        # or create custom sort (O(n) time, O(n space))
        
        for word in strs:
            key = self.countChars(word)
            res[key].append(word)
        return list(res.values())

    def countChars(self, word: str) -> Tuple:
            key = [0]*26
            for i in range(len(word)):
                key[ord('z')-ord(word[i])-1] += 1
            return tuple(key) # convert to tuple is cheaper than to str
            
                




