class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1: return nums[0]
        def helper(arr):
            currMax,prevPrevMax,prevMax = 0,0,0
            for n in arr: # aggregate maxes left to right
                currMax = max(n+prevPrevMax, prevMax)
                prevPrevMax=prevMax
                prevMax=currMax
            return currMax # the aggregate max leftwards from i=n
        return max(helper(nums[:-1]), helper(nums[1:]))
                        