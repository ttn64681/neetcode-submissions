class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res=0
        x,y=0,0
        max_r=len(grid)
        max_c=len(grid[0])
        grid_seen=[['O' for c in r] for r in grid]
        # print(f"initial grid_seen:\n{grid_seen}")
        def recurse(x,y) -> bool:
            if grid_seen[x][y]=='X': # prevent circular loop
                return False
            grid_seen[x][y]='X'
            c=grid[x][y]
            if c=="1":
                if x+1<max_r: # traverse rows downward
                    recurse(x+1,y)
                if y+1<max_c: # traverse cols rightward
                    recurse(x,y+1)
                if 0<=x-1: # traverse rows upward
                    recurse(x-1,y)
                if 0<=y-1: # traverse cols leftward
                    recurse(x,y-1)
                return True
            return False # else if c=="0"
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid_seen[r][c]=='O':
                    if recurse(r,c)==True:
                        res+=1
                        # print(f"Island found at [{r},{c}]")
        # print(f"final grid_seen:\n{grid_seen}")
        return res

