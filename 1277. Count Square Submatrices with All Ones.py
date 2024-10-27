class Solution:
    def checkSquare(self, matrix: List[List[int]], side: int, endr: int, endc: int, m: int, n: int):
        r = endr + 1
        c = endc + 1
        if r <= m - 1 and c <= n - 1:
            for row in range(side):
                if not matrix[endr - row][c]:
                    return
            for col in range(-1, side):
                if not matrix[r][endc - col]:
                    return
            self.res += 1
            self.checkSquare(matrix, side + 1, endr + 1, endc + 1, m, n)


    def countSquares(self, matrix: List[List[int]]) -> int:
        self.res = 0
        m = len(matrix)
        n = len(matrix[0])
        for row in range(m):
            for col in range(n):
                if matrix[row][col]:
                    self.res += 1
                    self.checkSquare(matrix, 1, row, col, m, n)
        return self.res