class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {} # hashmap 

        for x in strs:
            sortedX = ''.join(sorted(x))
            if sortedX not in hashmap:
                hashmap[sortedX] = [x]
            else:
                hashmap[sortedX].append(x)

        return list(hashmap.values())
        

            