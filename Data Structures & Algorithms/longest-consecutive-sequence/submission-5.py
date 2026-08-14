class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numz = set(nums)
        maxFreq = 0

        for num in numz:
            if num-1 not in numz: # if num is start of sequence
                currFreq = 1
                i = 1
                while num+i in numz:
                    currFreq += 1
                    i += 1
                if currFreq > maxFreq: maxFreq = currFreq
        
        return maxFreq
