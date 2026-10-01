class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Folk-valley:
        # Need to figure out the start and end of the sequence
        # we know its the start of a sequence if list doesn't have curr_num-1
        # once we get start_seq, we just check if the next num exists and count it.
        n=len(nums)
        if n==0: return 0
        elif n==1: return 1
        set_nums=set(nums) # O(n)
        start_seqs=[]
        res=1
        for n in set_nums: # O(n)
            if n-1 not in set_nums: # if start of seq
                start_seqs.append(n) # store 
           
        count=1
        for s in start_seqs: # O(n)
            t=s
            while t+1 in set_nums:
                count+=1
                res=max(res,count)
                t+=1
            count=1
        
        return res


                
                





