class Solution:
    def rob(self, nums: List[int]) -> int:
        # take 2 or 3 steps via dfs, return curr cost+max(dfs(i+2),dfs(i+3))
        # take max of dfs(0), dfs(1) for final answer, since dfs(0) skips i=1
        n = len(nums)
        memo = [-1 for i in range(n)]
        def dfs(i):
            if i >= n:
                return 0
            elif memo[i] != -1:
                return memo[i]
            memo[i] = nums[i] + max(dfs(i+2), dfs(i+3))
            # print(f"for i={i}, nums[i]:{nums[i]} -> {memo[i]}")
            return memo[i]
        return max(dfs(0), dfs(1))