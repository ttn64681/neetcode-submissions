import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n=len(stones)
        if n==1: return stones[0]
        elif n==2:
            s1,s2=stones[0],stones[1]
            diff=s2-s1 if s2>=s1 else s1-s2
            return diff
        heapq.heapify_max(stones)
        diff=0
        while len(stones)>1:
            s1=heapq.heappop_max(stones)
            s2=heapq.heappop_max(stones)
            diff=s2-s1 if s2>=s1 else s1-s2
            heapq.heappush_max(stones, diff)
            print(stones)
            print(f"s1:{s1},s2:{s2},diff:{diff}\n")
        return stones[0]




        
        
