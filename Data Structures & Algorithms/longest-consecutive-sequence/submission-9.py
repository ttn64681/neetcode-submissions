class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #2,4,3,10,9,8,7
        max_seq_len=0
        nums_set=set(nums)
        for num in nums_set:
            if num-1 not in nums_set: # start of seq
                curr_seq_len=1
                while(num+1 in nums_set):
                    curr_seq_len+=1
                    num+=1
                # print(f"curr:{curr_seq_len}, max:{max_seq_len}")
                max_seq_len=max(max_seq_len,curr_seq_len)
        return max_seq_len
                






