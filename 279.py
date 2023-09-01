class Solution:
    def numSquares(self, n: int) -> int:
        da=[n+1]*(n+1)
        da[0]=0
        s=[]
        for i in range(1,1+int(sqrt(n))):
            s.append(i*i)
        for a in range(1,n+1):
            for c in s: 
                if a-c>=0:
                    da[a]=min(da[a],1+da[a-c])
        return da[n]