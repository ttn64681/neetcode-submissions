class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        for s in strs:
            sortedS = ''.join(sorted(s))
            if sortedS in dict:
                dict[sortedS].append(s)
            else:
                dict[sortedS] = [s]
        
        print(dict)
        return list(dict.values())




