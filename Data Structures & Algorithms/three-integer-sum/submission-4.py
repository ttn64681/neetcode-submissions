class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -nums[i]=nums[j]+nums[k]
        # for each i, find j,k pair that satisfies equation
        n=len(nums)
        nums_sorted=sorted(nums)
        res=set()
        #[-4,-1,-1,0,1,2]
        for i in range(n):
            j,k=i+1,n-1
            i_num=nums_sorted[i]
            # print(f"i={i}")
            while j<k:
                j_num=nums_sorted[j]
                k_num=nums_sorted[k]
                two_sum=j_num+k_num
                # print(f"[{i_num},{j_num},{k_num}]")
                if two_sum==-i_num:
                    res.add((i_num,j_num,k_num))
                    # print(f"UPDATED: {res}")
                    k-=1
                elif -i_num<two_sum:
                    k-=1
                elif -i_num>two_sum:
                    j+=1
        
        return [[n for n in x] for x in res]

