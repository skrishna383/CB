class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserter=0
        for i in range(len(intervals)):
            if intervals[i][0]>newInterval[0]:
                intervals.insert(i,newInterval)
                inserter=1
                break
        if inserter==0:
            intervals.append(newInterval)

        ans=[intervals[0]]
        for i in intervals:
            if ans[-1][1]>=i[0]:
                ans[-1][1]=max(ans[-1][1],i[1])
            else:
                ans.append(i)
        return ans






#m2
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans=[]
        for i in range(len(intervals)):
            if newInterval[1]<intervals[i][0]:
                ans.append(newInterval)
                return ans+intervals[i:]
            elif newInterval[0]>intervals[i][1]:
                ans.append(intervals[i])
            else:
                newInterval=([min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])])
        ans.append(newInterval)
        return ans
        