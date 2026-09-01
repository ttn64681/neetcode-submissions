class Solution:
    def rob(self, nums: List[int]) -> int:
        # always take 2 hops, starting at i=0 or i=1
        # aggregate total cost via equation: nums[i] + dfs(i+2)
        # take min(dfs(0), dfs(1)) as final answer
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