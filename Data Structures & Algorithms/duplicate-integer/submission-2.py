class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list = {}

        for i in range(len(nums)):
	        if nums[i] not in list:
		        list[nums[i]] = True
	        else:
		        return True
        return False
   