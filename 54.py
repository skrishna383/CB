class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        col=range(0,len(matrix[0])-1)
        row=range(0,len(matrix)-1)
        startr=0
        endr=len(matrix[0])
        startc=0
        endc=len(matrix)
        di=['r','d','l','u']
        cd=0
        m,n=0,0
        ans=[]
        while startc<=endc and startr<=endr:
            while m in range(startr,endr) and n in range(startc,endc):
                ans.append(matrix[n][m])
                if di[cd%4]=='r':
                    m=m+1
                elif di[cd%4]=='d':
                    n=n+1
                elif di[cd%4]=='l':
                    m=m-1
                else:
                    n=n-1  
            if di[cd%4]=='r':
                startc=startc+1
                m=m-1
                n=n+1
            elif di[cd%4]=='d':
                endr=endr-1
                n=n-1
                m=m-1
            elif di[cd%4]=='l':
                endc=endc-1
                m=m+1
                n=n-1
            else:
                startr=startr+1
                n=n+1
                m=m+1
            cd=cd+1
        return ans
            