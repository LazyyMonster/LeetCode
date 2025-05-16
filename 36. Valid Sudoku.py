class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                box = ((r // 3) * 3 + (c // 3))
                if cell in rows[r] or cell in cols[c] or cell in boxes[box]:     
                    return False
                if cell != ".":
                    rows[r].add(cell)
                    cols[c].add(cell)
                    boxes[box].add(cell)

        return True