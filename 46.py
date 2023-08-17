class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(res,nums,[])
        return res
    def dfs(self,res,nums,elt):
        if len(nums)==0:
            res.append(elt)
        for i in range(len(nums)):
            self.dfs(res,nums[:i]+nums[i+1:],elt+[nums[i]])