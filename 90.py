class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        self.dfs(ans,[],0,sorted(nums))
        return ans
    def dfs(self,ans,elt,ind,nums):
        ans.append(elt)
        for i in range(ind,len(nums)):
            if i!=ind and nums[i]==nums[i-1]:
                continue
            else:
                self.dfs(ans,elt+[nums[i]],i+1,nums)
