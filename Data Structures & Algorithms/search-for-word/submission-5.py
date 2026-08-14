class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Goal: verify a chain of successive letters == word letters
        # State: track current path, track current character we're on
        # Base Case: when we've successfully traversed all letters
        # -> i >= word length
        # Constraints/Failures: word doesn't match, if letter is already visited

        ROW, COL = len(board), len(board[0])
        w = len(word)
        path = set()

        def dfs(r,c,i) -> bool:
            if i >= w:
                return True

            if (r<0 or r>=ROW or c<0 or c>=COL or
                board[r][c] != word[i] or (r,c) in path):
                return False

            path.add((r,c))
            
            result = (dfs(r+1,c,i+1) or
            dfs(r-1,c,i+1) or
            dfs(r,c+1,i+1) or
            dfs(r,c-1,i+1))

            path.remove((r,c))
            return result
        
        for row in range(ROW):
            for col in range(COL):
                if board[row][col] == word[0]:
                    res = dfs(row, col, 0)
                    if res:
                        return True
        return False


        
        
        

        