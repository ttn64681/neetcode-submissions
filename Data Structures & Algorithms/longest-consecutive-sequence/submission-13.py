class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #2,4,3,10,9,8,7
        max_seq_len=0
        nums_set=set(nums)
        for i in range(len(nums)):
            num=nums[i]
            if num-1 not in nums_set: # start of seq
                curr_seq_len=1
                while(num+curr_seq_len in nums_set):
                    curr_seq_len+=1
                # print(f"curr:{curr_seq_len}, max:{max_seq_len}")
                max_seq_len=max(max_seq_len,curr_seq_len)
        return max_seq_len
                






