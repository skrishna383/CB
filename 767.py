class Solution:
    def reorganizeString(self, s: str) -> str:
        counter=Counter(s)
        max_heap=[]
        for ch, i in counter.items():
            heapq.heappush(max_heap,(-i,ch))
        res=""
        heapq.heapify(max_heap)
        while max_heap:
            if len(max_heap)>1:
                co1,ch1=heapq.heappop(max_heap)
                res=res+ch1
                co2,ch2=heapq.heappop(max_heap)
                res=res+ch2
                co1,co2=co1+1,co2+1
                if co1<0:
                    heapq.heappush(max_heap,(co1,ch1))
                if co2<0:
                    heapq.heappush(max_heap,(co2,ch2))
            else:
                co,ch=heapq.heappop(max_heap)
                if co==-1:
                    res=res+ch
                else:
                    return ""
        return res