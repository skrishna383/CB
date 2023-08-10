class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        ans=0
        arr.sort()
        count=[0]*101
        for no in arr:
            count[no]+=1
        for l in range(0,101):
            for r in range (l,101):
                t=target-l-r
                if t>100 or t<0 :
                    continue
                elif l==r and r==t:
                    ans += (count[l] * (count[l]-1) * (count[l]-2) )/6
                    
                elif l ==r and l != t:
                     ans += (count[l] * (count[l]-1) ) /2 * count[t]
                        
                elif l < r and r<t :
                    ans += count[l] *count[r] * count[t]
        return int(ans%(10**9+7))