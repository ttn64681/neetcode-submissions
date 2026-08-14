class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n=len(board)
        row_seen=set() # existence O(1)
        col_seen=set()
        grid=defaultdict(set) # [0:(0,1,2,4,9,8), 1:(3,5), 2:(3)]
        # check cols and rows
        for r in range(n):
            for c in range(n):
                rC=board[r][c]
                cR=board[c][r]
                sq_idx = (r//3)*3+(c//3) # grid/square index
                print(f"\nc: {c}, r: {r}, rC: {rC}, cR: {cR}")
                if rC in row_seen or rC in grid[sq_idx]\
                or cR in col_seen:
                    # print(f"\n{'='*20}")
                    # print(f"False at [{r},{c}] or [{c},{r}]\n")
                    # print(f"grid_set: {grid[sq_idx]}")
                    # print(f"row: {row_seen}")
                    # print(f"col: {col_seen}")
                    # print(f"\n{'='*20}")
                    return False
                if rC != ".":
                    # print("added to row")
                    row_seen.add(rC)
                    # print(f"row: {row_seen}")
                    grid[sq_idx].add(rC)
                if cR != ".":
                    # print("added to col")
                    col_seen.add(cR)
                    # print(f"col: {col_seen}")
            row_seen=set()
            col_seen=set()
        return True
