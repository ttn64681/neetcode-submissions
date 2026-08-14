import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # [2,3,6,2,4]

        neg_stones = [-s for s in stones] #(O(n))
        # for s in stones:
        #   neg_s = -s
        #   neg_stones.append(neg_s)

        # heapify stones to have root node always contain 
        heapq.heapify(neg_stones) # (O(n))
        
        # [-2,-3,-6,-2,-4] -> [-6,]


        while (len(neg_stones) > 1):
            # get 2 heaviest weights (2*logn)
            weight1 = -heapq.heappop(neg_stones)
            weight2 = -heapq.heappop(neg_stones)

            # weight1 is either > or = weight2

            # smash stones, insert back into heap
            if weight1 != weight2:
                new_weight = weight1 - weight2
                heapq.heappush(neg_stones, -new_weight) # O(logn)

        if len(neg_stones) != 0:
            return -neg_stones[0]
        return 0
        
