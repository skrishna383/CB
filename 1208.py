class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        l=0
        c=0
        ans=0
        for r in range(len(s)):
            c=c+abs(ord(s[r])-ord(t[r]))
            while c>maxCost:
                c=c-abs(ord(s[l])-ord(t[l]))
                l=l+1
            ans=max(ans,r-l+1)
        return ans
