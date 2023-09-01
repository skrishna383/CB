class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans=[]
        self.dfs(ans,s,[],0,len(s))
        return ans
    def dfs(self,ans,s,elt,l,r):
        if l==r:
            ans.append(elt)
        for  i in range(l,r):
            if s[l:i+1]==s[l:i+1][::-1]:
                self.dfs(ans,s,elt+[s[l:i+1]],i+1,r)

        