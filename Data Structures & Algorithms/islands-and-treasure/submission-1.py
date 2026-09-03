class Solution:

    def islandsAndTreasure(self, grid: List[List[int]]) -> None:   
        # BFS from gates to get nearest
        # multi-source BFS for every single gate simultaneously
        # so when they overlap, they don't override the distance
        # thus ensuring each gate has the proper nearest distances
        # marked on their visited lands.
        ROWS,COLS = len(grid),len(grid[0])
        directions= [[1,0],[0,1],[-1,0],[0,-1]]
        seen=set()
        q=deque()
        # add all gates to queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
                    seen.add((r,c))

        """ helper to check if coord is valid """
        def bfs(r,c) -> void:
            if r>=ROWS or r<0 or c>=COLS or c<0 or \
                grid[r][c]==-1 or (r,c) in seen:
                return
            seen.add((r,c))
            q.append((r,c))
                    
        # iterate each gate
        # for each gate, add the bfs coords to queue
        # (ensures each gate breadth is covered sequentially)
        # (e.g. up,down,left,right for gate 1, then for gate 2, etc.)
        dist=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=dist # set dist

                for dr,dc in directions:
                    bfs(r+dr,c+dc)
            dist+=1
        
        
        
                        