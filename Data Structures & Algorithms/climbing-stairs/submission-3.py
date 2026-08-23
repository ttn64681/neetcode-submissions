class Solution:
    def climbStairs(self, n: int) -> int:
        # temp=n
        useMemo=defaultdict(int)
        #4-> 4,3,2,1,0 or 4,3,2,0 or 4,3,1,0 or 4,2,1,0 or 4,2,0
        #1 + 1 + 1 + 1 + 1
        def recurse(num) -> int:
            if num in useMemo:
                return useMemo[num]
            if num==0:
                return 1
            elif num<0:
                return 0
            result = recurse(num-1) + recurse(num-2)
            useMemo[num] = result
            return result
            
        return recurse(n)