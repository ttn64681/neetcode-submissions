class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        size = len(board)

        for r in range(size):
            seen = set() # reset after whole row checked
            for c in range(size):
                elem = board[r][c]
                if elem != ".":
                    if elem in seen:
                        return False
                    seen.add(elem)
            print(seen)

        for c in range(size):
            seen = set() # reset after each col checked
            for r in range(size):
                elem = board[r][c]
                if elem != ".":
                    if elem in seen:
                        return False
                    seen.add(elem)
            print(seen)
        
        for s in range(size):
            seen = set()
            for r in range(3):
                for c in range(3):
                    row = s//3*3 + r # s=0:row=0,1,2; s=1:row=0,1,2
                    col = s%3*3 + c # s=0:0,col=1,2; s=1:col=3,4,5
                    elem = board[row][col]
                    if elem != ".":
                        if elem in seen:
                            return False
                        seen.add(elem)
            print(seen)
        
        return True

"""
board=
[
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]
]
"""



        

        




