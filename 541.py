class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans=""
        r=len(s)//(2*k)+1
        p=0
        for i in range(r):
            ans=ans+s[(2*i)*k:(2*i+1)*k][::-1] 
            ans=ans+s[(2*i+1)*k:(2*i+2)*k]
        print (ans)
        return ans