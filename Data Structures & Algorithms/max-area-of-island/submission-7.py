class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        seen=set()
        ROWS,COLS = len(grid),len(grid[0])
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(x,y) -> int:
            q=collections.deque() # coords to check
            q.append((x,y)) # add curr coord to q
            seen.add((x,y)) # mark as seen
            curr_area=1 # tally
            while q:
                row,col = q.pop() # get coord to check
                for dr,dc in directions:
                    r,c = row+dr,col+dc
                    if r<ROWS and c<COLS and\
                            r>=0 and c>=0 and\
                            (r,c) not in seen and\
                            grid[r][c] == 1:
                        seen.add((r,c)) # mark as seen
                        q.append((r,c))
                        curr_area+=1 #tally
            return curr_area

        for x in range(ROWS):
            for y in range(COLS):
                c=grid[x][y]
                if c==1 and (x,y) not in seen:
                    max_area=max(max_area, dfs(x,y))
        return max_area

                

                
                    

                        
