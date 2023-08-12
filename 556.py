class Solution:
    def nextGreaterElement(self, n: int) -> int:
        m=list(str(n))
        for i in range(len(m)):
            m[i]=int(m[i])

        
        index=-1
        l=len(m)
        for i in range(l-2,-1,-1):
            if m[i]<m[i+1]:
                index=i
                break
        if index==-1:
            m[:]=m[::-1]
            return -1
        for i in range(l-1,index-1,-1):
            if m[index]<m[i]:
                m[index],m[i]=m[i],m[index]
                break
        m[::]=m[:index+1]+sorted(m[index+1:])
        ans=0
        for i in m:
            ans=ans*10+i
        if ans<2**31:
            return ans
        else: return -1