class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count-> element:freq
        # max heap based on count
        # pop k times into list
        # return

        # ex: [3,5,5,7,7,7]
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        # count_map = {3:1, 5:2, 7:3}   
        tup_list = [(-count,val) for val,count in count_map.items()]
        # tup_list = [(-1,3), (-2,5), (-3,7)]
        heapq.heapify(tup_list) # ?? 2nd param needed
        # tup_list = [(-3,7), (-2,5), (-1,3)]
        res = []
        for i in range(k):
            res.append(heapq.heappop(tup_list)[1])
        return res




        



