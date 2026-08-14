class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums: [2,3,4,5]->[60,40,30,24]

        # from i=0 to i=len-1:
        #   prefix[i] = nums[i-1] * prefix[i-1]
        # Prefix: [1, 1, 1, 1]
        # Prefix: [1, 2, 1, 1]
        # Prefix: [1, 2, 6, 1]
        # Prefix: [1, 2, 6, 24]

        # from i=len-1 to i=0:
        #   suffix[i] = nums[i+1] * suffix[i+1]
        # Suffix: [1, 1, 1, 1]
        # Suffix: [1, 1, 5, 1]
        # Suffix: [1, 20, 5, 1]
        # Suffix: [60, 20, 5, 1]

        res=[]
        length=len(nums)
        prefix=[1]*length
        suffix=[1]*length
        # O(n)
        for i in range(length-1,-1,-1): # suffix arr
            if i==length-1:
                continue
            suffix[i] = nums[i+1] * suffix[i+1] # O(1)
        # O(n)
        for j in range(length): # prefix + result prodExceptSelf arr
            if j==0:
                res.append(prefix[j]*suffix[j]) # O(1)
                continue
            prefix[j] = nums[j-1] * prefix[j-1] # O(1)
            res.append(prefix[j]*suffix[j]) # O(1)
        return res
 
