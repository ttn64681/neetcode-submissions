class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        n=len(nums)
        nums.sort()
        #[-1,-1,-1,0,1,2]
        for i,i_num in enumerate(nums):
            if i>0 and nums[i-1]==i_num:
                continue
            l,r=i+1,n-1
            while l<r:
                l_num,r_num=nums[l],nums[r]
                threeSum=i_num+l_num+r_num
                if threeSum==0:
                    res.append([i_num,l_num,r_num])
                    r-=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1                
                elif threeSum>0:
                    r-=1
                else: l+=1
        return res
        