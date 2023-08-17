class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        self.dfs(res,sorted(candidates),target,[],0)
        return res
    def dfs(self,res,nums,target,elt,index):
        if target<0:
            return
        elif 0==target:
            res.append(elt)
            return
        for i in range(index,len(nums)):
            self.dfs(res,nums,target-nums[i],elt+[nums[i]],i)