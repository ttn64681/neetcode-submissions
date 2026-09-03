class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS,COLS=len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        rotten=set()
        q=deque()    
        count=0
        for r in range(ROWS):
            for c in range(COLS):
                rC=grid[r][c]
                if rC==1:
                    count+=1
                if rC==2:
                    count+=1
                    q.append((r,c))
        # print(f"q: {q}")

        def bfs(r,c):
            if r>=ROWS or r<0 or c>=COLS or c<0 or\
                grid[r][c]==0 or grid[r][c]==2 or (r,c) in rotten:
                return
            q.append((r,c))
            rotten.add((r,c))

        minute=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                rotten.add((r,c))
                # print(f"r:{r},c:{c}")
                for dr,dc in directions:
                    bfs(r+dr,c+dc)
            # print(f"minute: {minute}")
            if len(q)!=0:
                minute+=1
        # print(f"rotten: {rotten}")
        return minute if len(rotten)==count else -1


        