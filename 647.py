class Solution:
    def countSubstrings(self, s: str) -> int:
        ssl=[]
        ans=0
        for i in range(len(s)+1):
            for j in range(i+1,len(s)+1):
                if s[i:j] == s[i:j][::-1]:
                    ans=ans+1
        return ans
		
#m2

class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            l=r=i
            while l>=0and r<len(s)and s[l]==s[r]:
                ans=ans+1
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0and r<len(s)and s[l]==s[r]:
                ans=ans+1
                l=l-1
                r=r+1
            
        return ans