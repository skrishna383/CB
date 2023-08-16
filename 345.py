class Solution:
    def reverseVowels(self, s: str) -> str:
        o=[]
        for ch in s:
            if ch in  "aeiouAEIOU":
                o.append(ch)
        ans=""
        for i in range(len(s)):
            if s[i] in  "aeiouAEIOU":
                ans=ans+o.pop()
            else:
                ans=ans+s[i]
        return ans