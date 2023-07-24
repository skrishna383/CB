class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def isugly(num):
            return (num//a + num//b + num//c - num//ab - num//ac - num//bc + num//abc)>=n
        ab =math.lcm(a, b)
        ac = math.lcm(a, c)
        bc =math.lcm(b, c)
        abc =math.lcm(a, bc)    
        l=1
        r=n*max(a,b,c)
        while l<r:
            mi=l+(r-l)//2
            if isugly(mi):
                r=mi
            else:
                l=mi+1
        return l