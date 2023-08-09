class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l=0
        r=int(sqrt(c))
        while l<=r:
            ss=l*l+r*r
            print(ss)
            if ss>c:
                r=r-1
            elif ss<c:
                l=l+1
            else:
                return True
        return False