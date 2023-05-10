class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask =0xffffffff
        sign =0
        if a<0 and b<0:
            sign=1
            a=-a
            b=-b
        while b!=0:
            temp=(a&b)
            a=(a^b)&mask 
            b=(temp<<1)&mask
        if a > 2000:
            return ~(a ^ mask)
        if sign:
            return -a
        else:
            return a
        