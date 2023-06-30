class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 for i in range(m)] for j in range(n)]
        for j in range(m-2,-1,-1):
            for i in range(n-2,-1,-1):
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
        return dp[0][0]
        
