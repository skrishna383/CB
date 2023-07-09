class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="" : return ""
        countT,window={},{}
        for c in t :
            countT[c]=countT.get(c,0)+1
        have,need=0,len(countT)
        res,reslen=[-1,-1],float("infinity")
        l=0
        for r in range(len(s)):
            c=s[r]
            window[c]=window.get(c,0)+1
            if c in countT and window[c]==countT[c]:
                have=1+have
            while have==need:
                if (r-l+1)<=reslen:
                    res=[l,r]
                    reslen=r-l+1
                window[s[l]]=window[s[l]]-1
                if s[l]in countT and window[s[l]]<countT[s[l]]:
                    have=have-1
                l=l+1
        if reslen!=float("infinity"):
            return s[res[0]:res[1]+1]
        else:
            return ""

#M2
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(t)
        m=len(s)
        l,r=0,n
        ans=""
        al=[]
        for r in range(n-1,m):
            ans=s[l:r+1]
            count=0
            an=ans
            for ch in t :
                if ch in an:
                    an=an.replace(ch,"",1)
                    count=count+1
            if count==n:
                #print("---",ans,an,n)
                for l in range(0,len(ans)):
                sa=ans[l:]
                count=0
                an=sa
                for ch in t :
                    if ch in an:
                        an=an.replace(ch,"",1)
                        count=count+1
                if count==n:
                    if ch in sa:
                        al.append()
        ans=""
        for a in al :
            ans=a
        print(al)
        for a in al:
            for l in range(0,len(a)):
                sa=a[l:]
                count=0
                an=sa
                for ch in t :
                    if ch in an:
                        an=an.replace(ch,"",1)
                        count=count+1
                if count==n:
                    if ch in sa:
                        if ans!="" and len(ans)>len(sa):
                            ans=sa
        return ans
