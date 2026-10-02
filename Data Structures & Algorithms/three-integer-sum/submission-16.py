class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums) # 6
        res=[]
        # [-1,-1,1,2,-1,-4] -> [-4,-1,-1,-1,  1,2]

        for i in range(n): # 5-2= 3 -> i=0,1,2 (-4,-1, -1)
            if i>0 and nums[i]==nums[i-1]: continue
            curr=nums[i]
            l,r = i+1,n-1
            while l<r:
                while (l>i+1 and l<r and nums[l]==nums[l-1]): 
                    # print(f"l={l}")
                    l+=1
                if not l<r: break
                while (r<n-1 and l<r and nums[r]==nums[r+1]): 
                    # print(f"r={r}")
                    r-=1
                if not l<r: break
                left,right = nums[l],nums[r]
                three_sum = curr+left+right # -1 + -1 + 2 = 0
                if (three_sum == 0):
                    res.append([curr,left,right])
                    l+=1
                elif (three_sum < 0):
                    l+=1
                else:
                    r-=1
        return res

                