class Solution:
    def addDigits(self, num: int) -> int:
        if num//10 ==0 :
            return num 
        else:
            res=0
            while num:
                res=res+num%10
                num=num//10
            return self.addDigits(res)
            
