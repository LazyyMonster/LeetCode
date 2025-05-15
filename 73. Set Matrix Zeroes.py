class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        change_rows = [1] * rows
        change_cols = set()

        for ir, row in enumerate(matrix):
            for ic, el in enumerate(row):
                if el == 0:
                    change_rows[ir] = 0
                    change_cols.add(ic)

        for ir, row in enumerate(change_rows):
            if not row:
                matrix[ir] = [0] * cols
            else:
                for ic in change_cols:
                    matrix[ir][ic] = 0