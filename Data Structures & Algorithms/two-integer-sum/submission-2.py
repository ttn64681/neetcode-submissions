class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in prevMap:
                return [prevMap[complement], i]
            prevMap[nums[i]] = i
        return []