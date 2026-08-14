import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top-k -> heap 

        # map: num -> list of all elements of that number
        # create list of tuples (count, num) of those lists

        # insert tuples into max_heap
        # pop top k into list
        # return that list

        # [1,3,3,5,5,5]


        num_counts = defaultdict(list)
        count_heap = []
        res = []

        for num in nums:
            num_counts[num].append(num)
        counts_heap = [(-len(list), list[0]) for list in num_counts.values()] # -> [(1,1), (2,3), (3,5)]
        heapq.heapify(counts_heap)
        print(counts_heap)
        for i in range(k):
            res.append(heapq.heappop(counts_heap)[1])
        return res
            
