class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*(n+1)
        suff = [1]*(n+1)
        res = []
        for i in range(1, n+1):
            pref[i] = pref[i-1] * nums[i-1]
        
        for i in range(n-1, -1, -1):
            suff[i] = suff[i+1] * nums[i]
        
        print(pref)
        print(suff)

        for i in range(n):
            print(pref[i])
            print(suff[i+1])
            res.append(pref[i] * suff[i+1])
        
        print(res)
        return res
