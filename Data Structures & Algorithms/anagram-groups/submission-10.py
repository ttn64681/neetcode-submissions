class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
            key = [0] * 26
            for c in x:
                key[ord(c) - ord('a')] += 1
            print(key)
            tupKey = tuple(key)
            print(tupKey)
            if tupKey in hashmap:
                hashmap[tupKey].append(x)
            else:
                hashmap[tupKey] = [x]
        return list(hashmap.values())
    
