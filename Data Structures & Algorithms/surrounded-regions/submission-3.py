class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. iterate through until encounter O's, run dfs and flip them
        # track path to not needlessly overlap

        # ["O","X","X","O","X"],
        # ["X","O","O","X","O"],
        # ["X","O","X","O","X"],
        # ["O","X","O","O","O"],
        # ["X","X","O","X","O"]]

        # ["O","X","X","O","X"],
        # ["X","X","X","X","O"],
        # ["X","X","X","O","X"],
        # ["O","X","O","O","O"],
        # ["X","X","O","X","O"]]


        # ["O","X","X","O","X"],
        # ["X","O","O","X","O"],
        # ["X","O","X","O","X"],
        # ["O","X","O","O","O"],
        # ["X","X","O","X","O"]]

        # ["O","X","X","O","X"],
        # ["X","X","O","X","O"],
        # ["X","O","X","O","X"],
        # ["O","X","O","X","O"],
        # ["X","X","O","X","O"]]

        # ["O","X","X","O","X"],
        # ["X","X","X","X","O"],
        # ["X","X","X","O","X"],
        # ["O","X","O","O","O"],
        # ["X","X","O","X","O"]
        ROWS,COLS=len(board),len(board[0])
        seen=set()
        q=deque()
        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def border_check(r,c):
            if r>=ROWS or r<0 or c>=COLS or c<0 or\
                board[r][c]=='X' or (r,c) in seen:
                return
            # print(f"yesth for {r},{c}->{board[r][c]}")
            q.append((r,c))
            seen.add((r,c))
        def check(r,c):
            if r>=ROWS-1 or r<1 or c>=COLS-1 or c<1 or\
                board[r][c]=='X' or (r,c) in seen:
                # print(f"nope for {r},{c}->{board[r][c]}")
                # print(f"ROWS-1:{ROWS-1}, COLS-1:{COLS-1}, seen:{seen}")
                return
            # print(f"yep for {r},{c}->{board[r][c]}")
            q.append((r,c))
            seen.add((r,c))

        def bfs(x,y,border=False):
            q.append((x,y))
            seen.add((x,y))
            # print(f"appended: {x},{y}")
            while q:
                r,c=q.popleft()
                # print(f"popped {r},{c}")
                if not border: board[r][c]='X'
                for dr,dc in directions:
                    if not border: 
                        check(r+dr,c+dc)
                    else:
                        border_check(r+dr,c+dc)
            
        for y in range(COLS):
            if board[0][y]=='O' and (0,y) not in seen: # 1st row
                bfs(0,y,True)
                # print(f"found at {0},{y}")
            if board[ROWS-1][y]=='O' and (ROWS-1,y) not in seen: # last row 
                bfs(ROWS-1,y,True)
                # print(f"found at {ROWS-1},{y}")
        for x in range(ROWS):
            if board[x][0]=='O' and (x,0) not in seen: # first col
                bfs(x,0,True)
                # print(f"found at {x},{0}")
            if board[x][COLS-1]=='O' and (x,COLS-1) not in seen: # last col
                bfs(x,COLS-1,True)
                # print(f"found at {x},{COLS-1}")
        # print(board)
        for x in range(ROWS):
            for y in range(COLS):
                if x>=ROWS-1 or x<1 or y>=COLS-1 or y<1 or\
                    board[x][y]=='X' or (x,y) in seen:
                    # print("ehh")
                    continue
                # print(f"yehh {x},{y}->{board[x][y]}")
                bfs(x,y,False)
            