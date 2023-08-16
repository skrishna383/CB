class Solution:
    def reverseWords(self, s: str) -> str:
        ans=""
        words=s.split()
        for i in words[::-1]:
            ans=ans+i+" "
        return ans[:-1]    
