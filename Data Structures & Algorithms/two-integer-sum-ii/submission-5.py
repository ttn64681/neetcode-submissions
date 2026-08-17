class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) space... 1 exact soln == NO dupes
        # target=7, [1,2,3,4,5,8]
        # [4,5,8], l->3, r=5
        # [4], l->3, r=3
        l=0
        r=len(numbers)-1
        while l<r:
            two_sum=numbers[l]+numbers[r]
            if two_sum==target:
                return [l+1, r+1]
            elif two_sum<target:
                l+=1
            else: r-=1
        return []

            
        