class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # get distance = xi**2 + yi**2, and store them

        # you could store in array, and then sort array based
        # on distance, then return top k.
        # BUT -> O(nlogn) due to Timsort algorithm

        # INSTEAD:
        # store in min-heap of size k,
        # kick out farthest points from heap,
        # leaving the largest k points remaining in heap

        min_heap = [] # Space O(n*1.5)
        closest_k_points = [] # Space O(k)
        
        for x, y in points: # Time O(n) 
            dist = (x**2 + y**2)
            min_heap.append([dist, x, y])
        
        heapq.heapify(min_heap) # O(n)

        for i in range(k): # O(k)
            dist, x, y = heapq.heappop(min_heap)
            closest_k_points.append([x,y])
        
        return closest_k_points

        # points = [[0,2],[2,0],[2,2]], k = 2
        # min_heap = [[4, 0,2],[4, 2,0],[8, 2,2]]
        # min_heap = [[4, 0,2],[4, 2,0],[8, 2,2]]
        # closest_k_points = [[0,2],[2,0]]


        
        
        