class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        levels = (len(matrix) + 1) // 2
        a = len(matrix) - 1

        for level in range(levels):
            for col in range(level, a - level):
                temp = matrix[level][col]

                matrix[level][col] = matrix[a - col][level]
                matrix[a - col][level] = matrix[a - level][a - col]
                matrix[a - level][a - col] = matrix[col][a - level]
                matrix[col][a - level] = temp