class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dungeon[-1][-1]=max(1,1-dungeon[-1][-1])
        @cache
        def dp(i,j):
            if i<0 or j<0:
                return maxsize
            if i==j==0:
                return max(-dungeon[0][0],1)
            return max(min(dp(i-1,j),dp(i,j-1))-dungeon[i][j],1)
        return dp(len(dungeon)-1,len(dungeon[0])-1)