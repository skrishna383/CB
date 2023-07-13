class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        anslen=0

        for i in range(len(s)):
            l=r=i
            while l>=0and r<len(s)and s[l]==s[r]:
                if anslen<r-l+1:
                    anslen= r-l+1
                    ans=s[l:r+1]
                l=l-1
                r=r+1
            l,r=i,i+1
            while l>=0and r<len(s)and s[l]==s[r]:
                if anslen<r-l+1:
                    anslen= r-l+1
                    ans=s[l:r+1]
                l=l-1
                r=r+1
            
        return ans