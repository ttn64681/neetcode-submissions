class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area=0
        seen=set()
        ROWS,COLS = len(grid),len(grid[0])
        
        def dfs(x,y) -> int:
            if x<ROWS and y<COLS and x>=0 and y>=0 and\
                grid[x][y]==1 and (x,y) not in seen:
                seen.add((x,y))
                return (1 + dfs(1+x,y) + dfs(x,1+y)\
                        + dfs(x-1,y) + dfs(x,y-1))
            return 0

        for x in range(ROWS):
            for y in range(COLS):
                c=grid[x][y]
                if c==1 and (x,y) not in seen:
                    max_area=max(max_area, dfs(x,y))
        return max_area

                

                
                    

                        
