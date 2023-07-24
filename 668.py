class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def iskthsmallestelt(mi):
            count=0
            for i in range(1,m+1):
                a=min(mi//i,n)
                if a==0:
                    break
                count=count+a
            return count>=k
        l,r=1,m*n
        while l<r:
            mi=l+(r-l)//2
            if iskthsmallestelt(mi):
                r=mi
            else:
                l=mi+1
        return l
    