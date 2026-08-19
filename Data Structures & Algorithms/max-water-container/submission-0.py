class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointers, track max and curr area
        # calc area via the smallest_height x width
        max_area=0
        l,r=0,len(heights)-1
        while l<r:
            l_height,r_height=heights[l],heights[r]
            width=r-l
            height=0
            if l_height<r_height:
                l+=1
                height=l_height
            else:
                r-=1
                height=r_height
            curr_area=width*height
            max_area=curr_area if curr_area>max_area else max_area

        return max_area