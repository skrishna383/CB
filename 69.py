class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=x
        if x==0 or x==1:
            return x
        while left<right:
            mid=(left+right)//2
            if mid*mid>x:
                right=mid
            else:
                left=mid+1
        return left-1
            