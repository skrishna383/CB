class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.dfs(ans,'',n,n)
        return ans
    def dfs(self,ans,elt,l,r):
        if l==0 and r==0:
            ans.append(elt)
        if l>0:
            self.dfs(ans,elt+"(",l-1,r)
        if r>0 and l<r:
            self.dfs(ans,elt+")",l,r-1)