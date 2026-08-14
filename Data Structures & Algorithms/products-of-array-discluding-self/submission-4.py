class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums:   [2, 3, 4, 5]  ->  [60,40,30,24]

        # res: [1, 1, 1, 1]
        # res: [1, 1, 5, 1]
        # res: [1, 20, 5, 1]
        # res: [60, 20, 5, 1]

        # res: [1, 1, 1, 1]
        # res: [1, 2, 1, 1]
        # res: [1, 2, 6, 1]
        # res: [1, 2, 6, 24]

        length=len(nums)  # Time O(n)
        res=[1]*length    # Space O(n)
        prefix=1
        suffix=1
        for i in range(length-1,-1,-1): # suffix Time O(n)
            res[i]=suffix
            suffix*=nums[i]
        for j in range(length): # prefix Time O(n)
            res[j]*=prefix
            prefix*=nums[j]
        return res
 
