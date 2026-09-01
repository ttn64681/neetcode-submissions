class Solution:
    def rob(self, nums: List[int]) -> int:
        # take 2 or 3 steps via dfs, return curr cost+max(dfs(i+2),dfs(i+3))
        # take max of dfs(0), dfs(1) for final answer, since dfs(0) skips i=1
        n = len(nums)
        rob1,rob2 = 0,0
        for n in nums:
            currMax = max(n+rob1, rob2)
            rob1=rob2
            rob2=currMax
        return rob2