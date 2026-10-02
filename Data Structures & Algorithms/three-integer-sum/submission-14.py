class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums) # 6
        res=[]
        seen=set()
        # [-1,-1,1,2,-1,-4] -> [-4,-1,-1,-1,  1,2]

        for i in range(n-2): # 5-2= 3 -> i=0,1,2 (-4,-1, -1)
            # i=1
            curr=nums[i]
            l,r = i+1,n-1 # l=2, r=5
            while l<r:
                left,right = nums[l],nums[r]
                three_sum = curr+left+right # -1 + -1 + 2 = 0
                if (three_sum == 0):
                    if ((curr,left,right) not in seen):
                        res.append([curr,left,right])
                        seen.add((curr,left,right))
                    l+=1
                elif (three_sum < 0):
                    l+=1
                else:
                    r-=1
        return res

                