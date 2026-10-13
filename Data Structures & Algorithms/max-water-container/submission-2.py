class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 1-pass 2 ptr soln, calc area each time, storing max area
        # note: can only take shortest bar-height for area calculation
        # 7:15pm -
        l,r = 0,len(heights)-1
        res=0 # maxArea
        while l<r:
            hl,hr = heights[l],heights[r]
            area=min(hl,hr) * (r-l) # shortest height * width
            res=max(res,area)
            if hl<hr: l+=1
            else: r-=1
        return res