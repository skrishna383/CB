class Solution:
    def characterReplacement(self, s: str, k: int)-> int:
        l=0
        chf={}
        ans=0
        for r in range(len(s)):
            if not s[r] in chf:
                chf[s[r]]=0
            chf[s[r]]=chf[s[r]]+1
            cc=r-l+1
            if cc- max(chf.values()) <=k:
                ans=max(ans,cc)
            else:
                chf[s[l]]=chf[s[l]]-1
                l=l+1
        return ans
