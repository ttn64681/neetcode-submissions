class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start_nums = {}
        maxFreq = 0 if len(nums)==0 else 1 # edge case

        # get start num of consec sequences
        for x in nums:
            if (x-1) not in nums and (x+1) in nums:
                start_nums[x] = [x]
        print(start_nums)

        print("adding consecutive values to list(s):")
        # for each start num, add consecutive values to list
        for x in start_nums.keys():
            for i in range(len(nums)):
                print("iteration: ", i)
                if x+i+1 in nums:
                    start_nums[x].append(x+i+1)
                    print(start_nums)
                else: break # break if the item found in nums is not consecutive
        
        # find max-size sequence length
        for y in list(start_nums.values()):
            if len(y) > maxFreq:
                maxFreq = len(y)

        print(maxFreq)
        return(maxFreq)


