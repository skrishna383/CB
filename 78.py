class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.dfs(res,[],0,sorted(nums))
        return res
    def dfs(self,res,elt,ind,nums):
        res.append(elt)
        for i in range(ind,len(nums)):
            self.dfs(res,elt+[nums[i]],i+1,nums)

