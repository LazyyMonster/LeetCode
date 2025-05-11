class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        rows = len(board)
        cols = len(board[0])

        def count_neighbours(row, col):
            live = 0
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if (r == row and c == col) or r >= rows or c >= cols or r < 0 or c < 0:
                        continue
                    live += board[r][c] % 10
            return live * 10 + board[row][col]


        for row in range(rows):
            for col in range(cols):
                board[row][col] = count_neighbours(row, col)  

        for row in range(rows):
            for col in range(cols):
                #ones represent original state, tens represent live neighbours 
                if board[row][col] in [21, 30, 31]:
                    board[row][col] = 1
                else:
                    board[row][col] = 0