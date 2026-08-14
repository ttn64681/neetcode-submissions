class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complements = {}

        for i in range(len(numbers)):
            num = numbers[i]
            print('num', num)
            compl = target - num
            print('compl', compl)
            if compl in complements:
                return [complements[compl]+1, i+1]
            else:
                complements[num] = i
                print('complements', complements)
        
        return [-1,-1]