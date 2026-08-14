class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for x in nums:
            if x in hashmap:
                return True
            else:
                hashmap[x] = 1
        return False