class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count/sort via hash
        # turn hash to list of tuples (val, count)
        # sort tuples (val, count)
        # extract most frequent vals ()

        freq = {}
        for num in nums:
            if num in freq: freq[num] += 1
            else: freq[num] = 1

        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num)) # push with count first -> count-based minheap
            if len(heap) > k:
                heapq.heappop(heap) 

        res = []
        print(len(heap))
        for i in range(len(heap)):
            res.append(heapq.heappop(heap)[1])
        
        return res

        