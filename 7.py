class Solution:
    def reverse(self, x: int) -> int:        
        ans=0
        if x<0:
            x=-x
            sign=False
        else:
            sign=True
        while x:
            ans=ans*10+x%10
            x=x//10
        if ans>(2**31 -1):
            return 0
        if ans<-(2**31) :
            return 0
        if sign :
            return ans
        else:
            return -ans

