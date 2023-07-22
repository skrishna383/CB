class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canfinishbananas(k):
            time=0
            for i in piles:
                time=time+(i-1)//k+1
                if time>h:
                    return False
            return True
        l,r=1,max(piles)
        while l<r:
            m=l+(r-l)//2
            if canfinishbananas(m):
                r=m
            else:
                l=m+1
        return l