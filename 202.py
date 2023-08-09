class Solution:
    def isHappy(self, n: int) -> bool:
        print(n)
        ans=0
        while n:
            d=n%10
            n=n//10
            ans=ans+d*d
        if ans==1 or ans==7:
            return True
        elif ans<10:
            return False
        else:
            return self.isHappy(ans)
