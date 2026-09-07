class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS=len(board),len(board[0])
        q=deque()
        def check(r,c):
            if r>=ROWS or r<0 or c>=COLS or c<0 or\
                board[r][c]!='O':
                return
            q.append((r,c))

        def bfs(x,y):
            q.append((x,y))
            while q:
                r,c=q.popleft()
                board[r][c]='#'
                check(r+1,c)
                check(r,c+1)
                check(r-1,c)
                check(r,c-1)
            
        for y in range(COLS):
            if board[0][y]=='O': # 1st row
                bfs(0,y)
            if board[ROWS-1][y]=='O': # last row 
                bfs(ROWS-1,y)
        for x in range(ROWS):
            if board[x][0]=='O': # first col
                bfs(x,0)
            if board[x][COLS-1]=='O': # last col
                bfs(x,COLS-1)

        for x in range(ROWS):
            for y in range(COLS):
                if board[x][y]=='#': board[x][y]='O'
                elif board[x][y]=='O': board[x][y]='X'
                
            