class Solution:
    def makeMove(self, grid: List[List[int]], m: int, n: int) -> int:
        
        if n == len(grid[0]) - 1:
            return n

        if self.visited[m][n]:
            return self.visited[m][n]

        actualCell = grid[m][n]
        maxReach = n

        if m > 0 and grid[m - 1][n + 1] > actualCell:
            maxReach = max(maxReach, self.makeMove(grid, m - 1, n + 1))
        
        if grid[m][n + 1] > actualCell:
            maxReach = max(maxReach, self.makeMove(grid, m, n + 1))

        if m < len(grid) - 1 and grid[m + 1][n + 1] > actualCell:
            maxReach = max(maxReach, self.makeMove(grid, m + 1, n + 1))

        self.visited[m][n] = maxReach 
        return maxReach


    def maxMoves(self, grid: List[List[int]]) -> int:
        
        gridLen = len(grid)
        self.visited = [[0] * len(grid[0]) for _ in range(gridLen)]
        res = 0
        for r in range(gridLen):
            res = max(res, self.makeMove(grid, r, 0)) 

        return res