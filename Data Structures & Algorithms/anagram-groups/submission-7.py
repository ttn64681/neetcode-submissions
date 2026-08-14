class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for x in strs: # iterate each word
            print(x)
            key = [0] * 26
            for c in x: # count each character
                key[ord(c) - ord('a')] += 1 # char - ascii val of 'a' gives difference (c-a = 99-97= 2)
                print(key)

            keyStr = tuple(key)

            if keyStr in hashmap:
                hashmap[keyStr].append(x)
            else:
                hashmap[keyStr] = [x]
            print(hashmap)
        
        return list(hashmap.values())
        
        