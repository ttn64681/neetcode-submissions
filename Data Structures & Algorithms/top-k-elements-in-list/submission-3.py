import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {} # key: num, val: count
        resArray = []

        for x in nums: # sets count as values of hashmap
            if x not in hashmap:
                hashmap[x] = 1
            else:
                hashmap[x] = hashmap[x] + 1
        
        print(hashmap)

        sorted_items = sorted(hashmap.items(), key=lambda kv: kv[1]) # results in [(#,#),(#,#), ...]

        print(sorted_items)

        for i in range(len(sorted_items)):
            if (i >= len(sorted_items) - k):
                resArray.append(sorted_items[i][0])

        print(resArray)

        return resArray


        
        

        
            