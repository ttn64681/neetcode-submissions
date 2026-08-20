class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        if n==0 or n==1 or n==2: return 0
        # Find  max left and right bar heights for each i
        # for each i, min_bar_heights - curr_ith_height 
        max_l,max_r=[0]*n,[0]*n
        curr_max_l,curr_max_r=0,0
        l,r=0,n-1
        sum=0
        for i in range(n): # Time O(n)
            curr_max_l=max(curr_max_l,height[l])
            max_l[l]=curr_max_l
            curr_max_r=max(curr_max_r,height[r])
            max_r[r]=curr_max_r
            l+=1
            r-=1
            # print(f"max_l:{max_l},\nmax_r:{max_r}\n")
        for i in range(n): # Time O(n)
            min_h=max(0,min(max_l[i],max_r[i])-height[i])
            sum+=min_h
            # print(f"i:{i},l:{l},r:{r},min_h:{min_h}\n")
        return sum
        # Overall Space O(n), Time O(n)
        

