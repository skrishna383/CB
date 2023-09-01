class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        v=[False]*len(nums)
        self.dfs(res,sorted(nums),[],v)
        return res
    def dfs(self,res,nums,elt,v):
        if len(nums)==len(elt):
            res.append(elt)
        for i in range(len(nums)):
            if not v[i]:
                if i>0 and not v[i-1] and nums[i] == nums[i-1]:
                    continue
                v[i] = True
                self.dfs(res, nums, elt+[nums[i]],v )
                v[i] = False