class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numz = set(nums)
        maxim = 0
        curr_max = 0

        for num in numz:
            if num-1 not in numz:
                curr_max = 1
                i = 1
                while num+i in numz:
                    curr_max += 1
                    i += 1
                if curr_max > maxim:
                    maxim = curr_max
                
        return maxim

                

