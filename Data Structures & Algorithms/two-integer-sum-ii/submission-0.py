class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        compl = {}

        for i in range(len(numbers)):
            diff = target-numbers[i]
            if diff in compl:
                return [compl[diff], i+1]
            else:
                compl[numbers[i]] = i+1
            print(compl)
        return [-1,-1]
            