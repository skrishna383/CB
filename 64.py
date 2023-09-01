class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        @cache
        def dp(i,j):
            if i<0 or j<0:
                return maxsize
            if i==j==0:
                return grid[0][0]
            return grid[i][j]+min(dp(i-1,j),dp(i,j-1))
        return dp(len(grid)-1,len(grid[0])-1)
        
        
#m2
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        for i in range(1, n):
            grid[i][0] += grid[i - 1][0]

        for j in range(1, m):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[n - 1][m - 1]