class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols=len(grid),len(grid[0])
        nislands=0
        islands=[]
        def addisland(r,c):
            if (r,c) in islands:
                return
            if r>=0 and c>=0 and r<rows and c<cols and grid[r][c]=="1":
                islands.append((r,c))
                grid[r][c]="2"
                addisland(r+1,c)
                addisland(r-1,c)
                addisland(r,c+1)
                addisland(r,c-1)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=="1":
                    addisland(i,j)
                    nislands+=1
                    islands.clear()
        return nislands