class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        zr=[1]*n
        zc=[1]*m
        for i in range(0,m):
            for j in range(0,n):
                if matrix[i][j]==0:
                    zc[i]=0
                    zr[j]=0
        for i in range(0,m):
            if zc[i]==0:
                for j in range(0,n):
                    matrix[i][j]=0
            
        for i in range(0,n):
            if zr[i]==0:
                for j in range(0,m):
                    matrix[j][i]=0
                    


            
