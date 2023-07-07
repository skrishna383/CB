class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set()
        ans=0
        l=0
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                ans=max(ans,r-l+1)
            else:
                while s[r] in charSet:    
                    charSet.remove(s[l])
                    l=l+1
            charSet.add(s[r])
        return ans

