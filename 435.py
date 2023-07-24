class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda i:i[1])
        ans=0
        end=-100000
        for i in intervals:
            if i[0]>=end :
                end=i[1]
            else :
                ans+=1
        return ans