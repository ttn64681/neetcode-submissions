class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        n = len(word)

        def isInBounds(r,c):
            if (r<0 or r>=ROW or c<0 or c>=COL):
                return False

        def dfs(r, c, i):
            if (i == n): # finished finding all chars in word
                print("Complete (i==n)!")
                return True

            # If char not found, return False
            if (isInBounds(r,c) == False or
                board[r][c] == "#"): # if letter already read
                print("Not Found... indexOutOfBounds")
                return False
            elif (board[r][c] != word[i]):
                print("Not Found... ", board[r][c])
                return False
            
            # Else if char is found, mark it and continue
            temp = board[r][c]
            board[r][c] = "#" # mark as read ("#")
            print("Found! ", temp)

            paths = dfs(r+1,c,i+1) or\
                    dfs(r-1,c,i+1) or\
                    dfs(r,c+1,i+1) or\
                    dfs(r,c-1,i+1)
            
            board[r][c] = temp # unmark to original letter
            return paths

        
        for r in range(ROW):
            for c in range(COL):
                # whenever first letter of word found, do dfs
                if board[r][c] == word[0]:
                    res = dfs(r,c,0)
                    if res: return True
        return False
