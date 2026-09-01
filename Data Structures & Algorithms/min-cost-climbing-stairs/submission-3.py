class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # either take +1 or +2 steps til i >= len
        # idea is to recurse to top, returning cost[i] + min((+1),(+2))
        # at base case, return 0
        # store aggregate cost either in separate array
        # that separate array acts as cache for min cost rightwards
        n = len(cost)
        memo = [-1 for i in range(n)]
        def dfs(i):
            if i >= n:
                return 0
            elif memo[i] != -1:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        return min(dfs(0), dfs(1))

