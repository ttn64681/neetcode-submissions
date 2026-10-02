class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]: continue
            curr=nums[i]
            l,r = i+1,n-1
            while l<r:
                left,right = nums[l],nums[r]
                three_sum = curr+nums[l]+nums[r]
                if (three_sum == 0):
                    res.append([curr,left,right])
                    r-=1
                    while l<r and nums[r]==nums[r+1]: r-=1
                elif (three_sum < 0):
                    l+=1
                else:
                    r-=1
        return res

                