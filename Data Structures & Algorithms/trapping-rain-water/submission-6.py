class Solution:
    def trap(self, height: List[int]) -> int:
        # 7:42pm - 7:
        # at each point, we have to know the left and right wall
        # specifically, we need to know TALLEST left and right
        # we can use prefix/postfix arrays to store this as pre-check
        # Note: this excludes the current bar-height as a l/r wall
        # Then calc each index's water content, given the shortest
        # bar-height to the left/right (water exists at an index up
        # to the shortest wall - the current height)
        # when subtracting current height, don't calc/add neg vals
        n=len(height)
        if n==1 or n==2: return 0
        left_tallest=[0]*n
        right_tallest=[0]*n
        accum=0
        for i in range(n): # left_tallest
            left_tallest[i]=accum # set idx to curr tallest to left
            accum=max(accum,height[i]) # set accum to tallest
        # print(left_tallest) # 0,0,2,2,3,3,3,3,3,3
        accum=0
        for i in range(n-1,-1,-1): # right_tallest
            right_tallest[i]=accum # set idx to curr tallest to right
            accum=max(accum,height[i])
        # print(right_tallest)# 3,3,3,3,3,3,3,2,1,0
        accum=0
        for i in range(n): # calc water per idx
            bound=min(left_tallest[i],right_tallest[i]) # min wall
            water=max(0,bound-height[i])
            accum+=water
        return accum
        #0: 0-0
        #1: 0-2 = 0
        #2: 2-0 = 2
        #3: 2-3 = 0
        #4: 3-1 = 2
        #5: 3-0 = 3
        #6: 3-1 = 2
        #7: 2-3 = 0
        #8: 1-2 = 0
        #9: 0-1 = 0
        # answer = 9






