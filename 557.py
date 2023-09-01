class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        words=s.split()
        for i in words:
            ans=ans+i[::-1]+" "
        return ans[:-1]    
