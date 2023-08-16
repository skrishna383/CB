class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num=list(num)
        copy=num.copy()
        for _ in range(k):
            for i in reversed(range(len(num)-1)): 
                if num[i]<num[i+1]:
                    ii=i+1
                    while ii < len(num) and num[i] < num[ii]: ii += 1
                    num[i],num[ii-1]=num[ii-1],num[i]
                    l,h=i+1,len(num)-1
                    while l<h:
                        num[l],num[h]=num[h],num[l]
                        l=l+1
                        h=h-1
                    break
        ans=0
        for i in range(len(num)):
            ii=i
            while copy[i]!=num[i]:
                ans=ans+1
                ii=ii+1
                num[i],num[ii]=num[ii],num[i]
        return ans