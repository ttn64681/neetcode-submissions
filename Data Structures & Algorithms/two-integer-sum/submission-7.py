class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [4, 3, 7, 11]
        # 4 + 7 = 11
        # 11 - 4 in array?
        # return index(4) and index(11-4)
        # this is too slow, can be optimized via hashmap O(1) check, insertion, removal

        # hashmap for O(1) check + to 
        diffs = defaultdict(int)

        for i, num in enumerate(nums):
            diff = target - num
            if diff in diffs:
                return [diffs[diff], i]
            else:
                diffs[num] = i
        return [0, 0]

        

        


            
