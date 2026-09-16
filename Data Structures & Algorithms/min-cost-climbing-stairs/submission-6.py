class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # calc top-down the min cost rightwards from each position
        # store min cost from that pos in separate array/dict
        # return min of starting from ind 0 or ind 1
        minCost=defaultdict(int)
        # {2:1, 1:1, 0:2}
        def findMinCost(i):
            if i>=len(cost): return 0
            if i in minCost: return minCost[i]
            c1,c2 = findMinCost(i+1),findMinCost(i+2)
            res = cost[i] + min(c1,c2)
            minCost[i] = res
            return minCost[i]
        return min(findMinCost(0), findMinCost(1))

        
