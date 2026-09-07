class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        def dfs(r,c):
            if r>=ROWS or r<0 or c>=COLS or c<0 or\
                board[r][c]!='O':
                return
            board[r][c]='#'
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r-1,c)
            dfs(r,c-1)
        for y in range(COLS):
            dfs(0,y)
            dfs(ROWS-1,y)
        for x in range(ROWS):
            dfs(x,0)
            dfs(x,COLS-1)
        for x in range(ROWS):
            for y in range(COLS):
                if board[x][y]=='#': board[x][y]='O'
                elif board[x][y]=='O': board[x][y]='X'
                
            