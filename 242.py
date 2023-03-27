class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        atoz=string.ascii_lowercase
        d=dict.fromkeys(atoz,0)
        d1=dict.fromkeys(atoz,0)
        for ch in s:
            d[ch]=d[ch]+1
        for ch in t:
            d1[ch]=d1[ch]+1
        if d==d1:
            return True
        else :
            return False
        
