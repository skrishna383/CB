class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canshipindays(c):
            l=0
            d=1
            for i in weights:
                l=l+i
                if l>c:
                    l=i
                    d=d+1
                    if d>days:
                        return False
            return True
        l,r=max(weights),sum(weights)
        while l<r:
            m=l+(r-l)//2
            if canshipindays(m):
                r=m
            else:
                l=m+1
        return l