class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # OLD: DFS on every cell
        # iterate through cells, do dfs(), return True if path reaches pacific and atlantic, otherwise, add to sets if part of:
        # pacific -> (touches (0,0-0:C-1),(0,0:R-1,0)
        # atlantic-> (touches (R-1,0:R-1,C-1),(0,C-1:R-1,C-1)) 
        # if encounter (R-1,0) or (C-1,0) -> instant match

        # NEW: Multi-Source BFS, checking for increasing path from the sea
        # idea: if you find a decreasing path/cell, then that cell will never reach sea
        # w/ each increasing/equal cell, add to set based on which sea you started from
        # at end, iterate through entire grid; if cell in both sets, add to result arr
        ROWS,COLS=len(heights),len(heights[0])
        pacific,atlantic=set(),set()
        res=[]
        def dfs(r,c,prev_h,s):
            if r>=ROWS or r<0 or c>=COLS or c<0 or \
                heights[r][c]<prev_h or (r,c) in s:
                # print(f"skipped/invalid [{r},{c}]")
                return
            s.add((r,c)) # if valid/increasing, add to set
            
            h=heights[r][c]
            # down, right, up, left
            # print(f"path:{path}")
            res=dfs(r+1,c,h,s) or dfs(r,c+1,h,s) or \
                dfs(r-1,c,h,s) or dfs(r,c-1,h,s)
            # print(f"for [{r},{c}] h={h}: {res}")
            # known[(r,c)]=res
        
        for c in range(COLS):
            dfs(0,c,heights[0][c],pacific) # check first row
        for c in range(COLS):
            dfs(ROWS-1,c,heights[ROWS-1][c],atlantic) # check last row
        for r in range(ROWS):
            dfs(r,0,heights[r][0],pacific) # check first col
        for r in range(ROWS):
            dfs(r,COLS-1,heights[r][COLS-1],atlantic) # check last col

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        # print(pacific)
        # print(atlantic)
        return res



