class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canmakeallbouquet(mi):
            bloomedflowers=["0"]*len(bloomDay)
            for i in range(len(bloomDay)):
                if bloomDay[i]<=mi :
                    bloomedflowers[i]="1"
            bloomedflowers="".join(bloomedflowers)
            return bloomedflowers.count("".join(["1"]*k))>=m

        if len(bloomDay)<m*k:
            return -1
        l,r=min(bloomDay),max(bloomDay)
        while l<r:
            mi=l+(r-l)//2
            if canmakeallbouquet(mi):
                r=mi
            else:
                l=mi+1
        return l
        
        
        
#M2

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canmakeallbouquet(days):
            bonquets, flowers = 0, 0
            for bloom in bloomDay:
                if bloom > days:
                    flowers = 0
                else:
                    bonquets += (flowers + 1) // k
                    flowers = (flowers + 1) % k
            return bonquets >= m

        if len(bloomDay)<m*k:
            return -1
        l,r=min(bloomDay),max(bloomDay)
        while l<r:
            mi=l+(r-l)//2
            if canmakeallbouquet(mi):
                r=mi
            else:
                l=mi+1
        return l