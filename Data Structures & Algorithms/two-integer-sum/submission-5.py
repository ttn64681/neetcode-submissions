class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4, 3, 7, 11]
        # 4 + 7 = 11
        # 11 - 4 in array?
        # return index(4) and index(11-4)

        # start search
        # O(n)
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            # if diff exists
            if diff in nums: # O(n)
                j=i+1
                # search upwards for diff index
                while j < len(nums):
                    if nums[j] == diff:
                        return [i, j]
                    j += 1
        
        return [0, 0] # dummy answer



            
