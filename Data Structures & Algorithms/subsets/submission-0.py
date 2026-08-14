class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_sol = []
        n = len(nums)

        def dfs(i):
            print("At ind: ", i)
            if (i >= n):
                print("Reached end: ", curr_sol, " and appending at ind: ", i)
                res.append(curr_sol[:]) # add possible subset to res
                return
            elif (nums[i] in curr_sol): # go back if duplicate num in sol
                print("Duplicate found: ", nums[i])
                return

            print("loop: ", nums[i])
            # Travel left (don't choose current num)
            dfs(i+1)
            print("Exhausted left side")
            curr_sol.append(nums[i]) # choose next possible num
            # Travel right to add new possible subset
            print("Appending: ", curr_sol, " at ind: ", i)
            dfs(i+1)

            print("Exhausted right and returning to ind: ", i)
            curr_sol.pop() # go back

        dfs(0)

        return res
        

