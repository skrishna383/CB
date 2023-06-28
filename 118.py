class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[]
        r=[1]
        ans.append(r)
        pr=r
        for i in range(2,numRows+1):
            r=[]
            r.append(1)
            for j in range(2,i):
                r.append(pr[j-1]+pr[j-2])
            r.append(1)
            pr=r
            ans.append(r)
        return ans
